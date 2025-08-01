import asyncio
from aiogram import types
from aiogram.enums import ContentType
from aiogram.exceptions import TelegramRetryAfter
from aiogram.types import InputMediaPhoto


async def edit_or_answer_func(
    message: types.message.Message | types.callback_query.CallbackQuery,
    text: str | None = None,
    reply_markup: types.InlineKeyboardMarkup | types.ReplyKeyboardMarkup | None = None,
    only_answer: bool = False,
    photo: str | None = None,
) -> None | int:
    type_of_update = type(message)
    message_id = None
    if type_of_update == types.message.Message:
        message: types.message.Message
        if not photo:
            message_id = await message.answer(text=text, reply_markup=reply_markup)
        else:
            message_id = await message.answer_photo(
                photo=photo, caption=text, reply_markup=reply_markup
            )
    elif type_of_update == types.callback_query.CallbackQuery:
        callback: types.callback_query.CallbackQuery = message
        message_id = callback.message
        if not only_answer:
            if callback.message.content_type == ContentType.TEXT:
                if not photo:
                    await callback.message.edit_text(
                        text=text, reply_markup=reply_markup
                    )
                else:
                    await callback.message.delete()
                    message_id = await callback.message.answer_photo(
                        photo=photo, reply_markup=reply_markup, caption=text
                    )
            elif callback.message.content_type == ContentType.PHOTO:
                if not photo:
                    await callback.message.delete()
                    message_id = await callback.message.answer(
                        text=text, reply_markup=reply_markup
                    )
                else:
                    try:
                        await callback.message.edit_media(
                            media=InputMediaPhoto(media=photo, caption=text),
                            reply_markup=reply_markup,
                        )
                    except TelegramRetryAfter:
                        await callback.message.delete()
                        message_id = await callback.message.answer_photo(
                            photo=photo, caption=text, reply_markup=reply_markup
                        )
            else:
                await callback.message.delete()
                if not photo:
                    message_id = await callback.message.answer(
                        text=text, reply_markup=reply_markup
                    )
                else:
                    message_id = await callback.message.answer_photo(
                        photo=photo, reply_markup=reply_markup, caption=text
                    )
        else:
            if not photo:
                message_id = await callback.message.answer(
                    text=text, reply_markup=reply_markup
                )
            else:
                message_id = await callback.message.answer_photo(
                    photo=photo, reply_markup=reply_markup, caption=text
                )
    if message_id:
        return message_id.message_id


async def try_edit(
    message: types.message.Message | types.callback_query.CallbackQuery,
    text: str | None = None,
    reply_markup: types.InlineKeyboardMarkup | types.ReplyKeyboardMarkup | None = None,
    only_answer: bool = False,
    photo: str | None = None,
    continue_on_exception: bool = True,
    wait: int | float | None = None,
) -> None | int:
    """
    Try to edit message, if it fails, try to answer, usefull for handlers which works with both message and callback

    params:
        message: Message or CallbackQuery
        text: can be None only if you send photo
        reply_markup: InlineKeyboardMarkup or ReplyKeyboardMarkup
        only_answer: If True, answers anyway
        continue_on_exception: If True, continue on exception related to too many requests error, waiting until sending will be allowed
        wait:
    return:
        message_id - Id of sent message, you can you use it later
    """
    type_of_update = type(message)
    message_id = None
    if wait:
        await asyncio.sleep(wait)
    try:
        message_id = await edit_or_answer_func(
            message=message,
            text=text,
            reply_markup=reply_markup,
            only_answer=only_answer,
            photo=photo,
        )
    except TelegramRetryAfter as e:
        if continue_on_exception:
            sleep_seconds = int(e.message.split(" ")[-1])
            await asyncio.sleep(sleep_seconds)
            if type_of_update == types.callback_query.CallbackQuery:
                await message.answer(
                    f"Please wait {sleep_seconds} seconds, too many requests"
                )
            message_id = await edit_or_answer_func(
                message=message,
                text=text,
                reply_markup=reply_markup,
                only_answer=only_answer,
                photo=photo,
            )

    return message_id
