from typing import Union, List, Optional
from aiogram.enums import ChatType
from aiogram.filters import Filter
from aiogram.types import CallbackQuery, Message, TelegramObject


class ChatTypeFilter(Filter):
    """
    Filter for checking chat type.

    This filter allows messages only from specified chat types.
    Supports both Message and CallbackQuery objects.

    Args:
        allowed_types: List of allowed ChatType enums or single ChatType

    Example:
        ```python
        # Single chat type
        @router.message(ChatTypeFilter(ChatType.PRIVATE))
        async def private_handler(message: Message):
            pass

        # Multiple chat types
        @router.message(ChatTypeFilter([ChatType.GROUP, ChatType.SUPERGROUP]))
        async def group_handler(message: Message):
            pass
        ```
    """

    def __init__(self, allowed_types: Union[ChatType, List[ChatType]]) -> None:
        # Normalize input to list for consistent handling
        if isinstance(allowed_types, ChatType):
            self.allowed_types = [allowed_types]
        else:
            self.allowed_types = allowed_types

    def _extract_chat_type(
        self, obj: Union[Message, CallbackQuery]
    ) -> Optional[ChatType]:
        """Extract chat type from Message or CallbackQuery object."""
        if isinstance(obj, Message):
            return obj.chat.type
        elif isinstance(obj, CallbackQuery) and obj.message:
            return obj.message.chat.type
        return None

    async def __call__(self, obj: TelegramObject) -> bool:
        """
        Check if the update's chat type is in allowed types.

        Args:
            obj: Telegram update object (Message or CallbackQuery)

        Returns:
            True if chat type is allowed, False otherwise
        """
        if not isinstance(obj, (Message, CallbackQuery)):
            return False

        chat_type = self._extract_chat_type(obj)
        return chat_type in self.allowed_types if chat_type else False


class ChatIdFilter(Filter):
    """
    Filter for checking specific chat IDs.

    This filter allows messages only from specified chat IDs.
    Supports both positive and negative chat IDs.

    Args:
        chat_ids: List of allowed chat IDs or single chat ID

    Example:
        ```python
        # Single chat ID
        @router.message(ChatIdFilter(123456789))
        async def specific_chat_handler(message: Message):
            pass

        # Multiple chat IDs
        @router.message(ChatIdFilter([123456789, -987654321]))
        async def multiple_chats_handler(message: Message):
            pass
        ```
    """

    def __init__(self, chat_ids: Union[int, List[int]]) -> None:
        # Normalize input to list for consistent handling
        if isinstance(chat_ids, int):
            self.chat_ids = [chat_ids]
        else:
            self.chat_ids = chat_ids

    def _extract_chat_id(self, obj: Union[Message, CallbackQuery]) -> Optional[int]:
        """Extract chat ID from Message or CallbackQuery object."""
        if isinstance(obj, Message):
            return obj.chat.id
        elif isinstance(obj, CallbackQuery) and obj.message:
            return obj.message.chat.id
        return None

    async def __call__(self, obj: TelegramObject) -> bool:
        """
        Check if the update's chat ID is in allowed IDs.

        Args:
            obj: Telegram update object (Message or CallbackQuery)

        Returns:
            True if chat ID is allowed, False otherwise
        """
        if not isinstance(obj, (Message, CallbackQuery)):
            return False

        chat_id = self._extract_chat_id(obj)
        return chat_id in self.chat_ids if chat_id is not None else False
