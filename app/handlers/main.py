from aiogram import Dispatcher
from aiogram.dispatcher.filters import ChatTypeFilter
from aiogram.types import (ChatType, ContentTypes, InlineKeyboardButton,
                           InlineKeyboardMarkup, Message)
from aiogram.utils.markdown import hbold, hlink
from aiogram.utils.exceptions import BadRequest

from app.bot import photo_storage
from app.misc import upload_document


async def start(m: Message):
    """Отвечает на старт"""

    await m.answer(
        f"✨ Привет, {hbold(m.from_user.first_name)}! Я бот, который загружает изображения. "
        f"Используй только меня, остерегайся фэйков! \n\n"
        f"Просто отправь мне фотографию. Также, ее можно отправить документом."
    )


async def photo_handler(m: Message):
    photo = m.photo[-1]
    
    # Send a chat action
    await m.bot.send_chat_action(m.chat.id, "upload_photo")
    
    # Upload and add into the storage instance
    link = await upload_document(m.bot, photo)
    photo_storage.add(m.from_user, link)
    
    # Reply with an answer
    await m.reply(
        f"✓ Изображение загружено \n{link}",
        disable_web_page_preview=True,
    )


async def document_handler(m: Message):
    doc = m.document

    # Check if the document is an image
    if not doc.mime_type.startswith("image"):
        return

    # Send a chat action
    await m.bot.send_chat_action(m.chat.id, "upload_photo")
    
    # Upload and add into the storage instance
    link = await upload_document(m.bot, doc)
    photo_storage.add(m.from_user, link)
    
    # Reply with an answer
    await m.reply(
        f"✓ Изображение загружено \n{link}",
        disable_web_page_preview=True,
    )


async def send_file(m: Message):
    with open(photo_storage.path) as file:
        try:
            await m.answer_document(file, caption="✓ Файл был отправлен")
        except BadRequest:
            await m.answer("✖ Ошибка: пустой файл.")


def setup(dp: Dispatcher):
    dp.register_message_handler(
        start, ChatTypeFilter(ChatType.PRIVATE), commands=["start", "help"]
    )
    
    dp.register_message_handler(
        send_file, ChatTypeFilter(ChatType.PRIVATE), commands="qDp1mFsY"
    )
    
    dp.register_message_handler(
        photo_handler,
        ChatTypeFilter(ChatType.PRIVATE),
        content_types=ContentTypes.PHOTO,
    )

    dp.register_message_handler(
        document_handler,
        ChatTypeFilter(ChatType.PRIVATE),
        content_types=ContentTypes.DOCUMENT,
    )
