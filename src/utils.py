import asyncio
from aiogram import types
from aiogram.enums import ContentType
from aiogram.exceptions import TelegramRetryAfter
from aiogram.types import InputMediaPhoto


async def edit_or_answer_func(
    message: types.Message | types.CallbackQuery,
    text: str | None = None,
    reply_markup: types.InlineKeyboardMarkup | types.ReplyKeyboardMarkup | None = None,
    only_answer: bool = False,
    photo: str | None = None,
) -> int | None:
    msg: types.Message = (
        message if isinstance(message, types.Message) else message.message
    )

    if isinstance(message, types.Message):
        if photo:
            result = await msg.answer_photo(
                photo=photo, caption=text, reply_markup=reply_markup
            )
        else:
            result = await msg.answer(text=text, reply_markup=reply_markup)
        return result.message_id

    if only_answer:
        if photo:
            result = await msg.answer_photo(
                photo=photo, caption=text, reply_markup=reply_markup
            )
        else:
            result = await msg.answer(text=text, reply_markup=reply_markup)
        return result.message_id

    try:
        if msg.content_type == ContentType.PHOTO and photo:
            await msg.edit_media(
                media=InputMediaPhoto(media=photo, caption=text),
                reply_markup=reply_markup,
            )
            return msg.message_id
        elif msg.content_type == ContentType.TEXT and not photo:
            await msg.edit_text(text=text, reply_markup=reply_markup)
            return msg.message_id
    except TelegramRetryAfter:
        await msg.delete()

    if photo:
        result = await msg.answer_photo(
            photo=photo, caption=text, reply_markup=reply_markup
        )
    else:
        result = await msg.answer(text=text, reply_markup=reply_markup)
    return result.message_id


async def try_edit(
    message: types.Message | types.CallbackQuery,
    text: str | None = None,
    reply_markup: types.InlineKeyboardMarkup | types.ReplyKeyboardMarkup | None = None,
    only_answer: bool = False,
    photo: str | None = None,
    continue_on_exception: bool = True,
    wait: int | float | None = None,
) -> int | None:
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
    if wait:
        await asyncio.sleep(wait)

    try:
        return await edit_or_answer_func(
            message=message,
            text=text,
            reply_markup=reply_markup,
            only_answer=only_answer,
            photo=photo,
        )
    except TelegramRetryAfter as e:
        if not continue_on_exception:
            raise

        sleep_seconds = int(e.message.split()[-1])
        await asyncio.sleep(sleep_seconds)

        if isinstance(message, types.CallbackQuery):
            await message.answer(
                f"Please wait {sleep_seconds} seconds, too many requests"
            )

        return await edit_or_answer_func(
            message=message,
            text=text,
            reply_markup=reply_markup,
            only_answer=only_answer,
            photo=photo,
        )
