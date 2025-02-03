from telegram import Update, ChatMember
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackContext, filters
import logging
import time
import os
from Image_generator import getImagePath
from Text_generator import getTextResponse
from Config_handler import load_config

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

config = load_config('config.txt')
bot_token = config['bot_token']
allowed_ID_Chats = set(map(int, config['allowed_ID_Chats'].split(',')))

Image_action_keywords = {"создай", "сгенерируй", "нарисуй"}
Image_type_keywords = {"фото", "фотку", "изображение", "рисунок"}

lastUpdateTime = time.time()

async def handle_message(update: Update, context: CallbackContext) -> None:
    global lastUpdateTime
    global Image_action_keywords
    global Image_type_keywords
    chat_id = update.effective_chat.id

    if update.message.date.timestamp() < lastUpdateTime:
        return
    if chat_id in allowed_ID_Chats:
        member = await context.bot.get_chat_member(chat_id, context.bot.id)
        if member.status in ["kicked", "left"]:
            allowed_ID_Chats.remove(chat_id)
            return
        
        response = update.message.text.lower()
        if any(word in response for word in Image_type_keywords) and any(word in response for word in Image_action_keywords):
            image_path = getImagePath(response)
            if image_path:
                with open(image_path, "rb") as photo:
                    await context.bot.send_photo(chat_id=chat_id, photo=photo)
                os.remove(image_path)
            else:
                await context.bot.send_message(chat_id=chat_id, text="Не смог сгенерировать фото")
        else:
            response = getTextResponse(response)
            await context.bot.send_message(chat_id=chat_id, text=response)

    else:
        await context.bot.send_message(chat_id=chat_id, text="Извините, мне нельзя отвечать в вашем чате")
        await context.bot.leave_chat(chat_id=chat_id)

    lastUpdateTime = time.time()

def main():
    application = Application.builder().token(bot_token).build()

    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    application.run_polling()

if __name__ == '__main__':
    main()
