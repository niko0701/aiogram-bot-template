from aiogram.types import InlineKeyboardMarkup, Message, CallbackQuery
from aiogram.exceptions import TelegramRetryAfter


async def try_edit(
    message_or_callback: Message | CallbackQuery,
    text: str,
    reply_markup: InlineKeyboardMarkup | None = None,
    only_answer: bool = False,
) -> int | None:
    message: Message = (
        message_or_callback
        if isinstance(message_or_callback, Message)
        else message_or_callback.message
    )
    if isinstance(message_or_callback, Message) or only_answer:
        if not text:
            return
        return (await message.answer(text=text, reply_markup=reply_markup)).message_id
    try:
        await message.edit_text(text=text, reply_markup=reply_markup)
        return message.message_id
    except TelegramRetryAfter:
        await message.delete()
        return (await message.answer(text=text, reply_markup=reply_markup)).message_id
