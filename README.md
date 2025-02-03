# Telegram Chat Bot

## Описание
Этот бот для Telegram способен отвечать на текстовые сообщения и генерировать изображения на основе пользовательского запроса. 

### Функциональность
- Ответы на текстовые сообщения с использованием языковой модели.
- Генерация изображений по текстовому описанию.

## Настройка и установка
### 1. Установка необходимых компонентов
Перед запуском убедитесь, что у вас установлены все необходимые компоненты. Для macOS установите их через **Homebrew**:
```sh
brew install python3
brew install pipx
pipx ensurepath
```

### 2. Установка зависимостей
Используйте **pip** для установки необходимых библиотек:
```sh
pip install python-telegram-bot huggingface_hub pillow
```

### 3. Настройка `config.txt`
Для корректной работы бота необходимо создать(при отстуствии) файл **config.txt** в корневой директории проекта и заполнить его следующими данными (подробные инструкция и примеры указаны в **config.txt**):

- **bot_token** – токен бота, полученный в BotFather.
- **allowed_ID_Chats** – список ID чатов, в которых бот может работать, через запятую.
- **api_key** – API-ключ, полученный на сайте Hugging Face.
- **prompt_message** – промт для ответа модели, использует сообщение пользователя.

## Запуск бота
После настройки запустите бота с помощью команды:
```sh
python Tg_bot.py
```

## Используемые модели
Бот использует несколько моделей `Hugging Face API` для своей работы:
- **Image_generator** – модуль генерации изображений с помощью `Hugging Face API`.
- **Text_generator** – модуль текстовой генерации ответов с помощью `Hugging Face API`.
