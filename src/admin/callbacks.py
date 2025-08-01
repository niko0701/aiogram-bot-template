from aiogram.filters.callback_data import CallbackData

class AdminCallback(CallbackData, prefix="ad"):
    data: str
