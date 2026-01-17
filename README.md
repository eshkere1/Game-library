# RAWG Strategy Games Parser

Небольшой Python-скрипт для получения информации о стратегических многопользовательских играх с высоким рейтингом из API RAWG.

Скрипт получает список стратегических игр с Metacritic ≥ 80, выводит основную информацию об игре, ссылки на скриншоты и магазины, где игру можно купить.

## Функциональность

- Получение данных из RAWG API
- Фильтрация игр:
  - жанр: strategy
  - теги: multiplayer
  - рейтинг Metacritic: 80–100
- Вывод информации:
  - название игры
  - дата выхода
  - ссылка на страницу игры
  - скриншоты
  - магазины

## Используемые технологии

- Python 3
- requests
- python-dotenv
- RAWG Video Games Database API

## Установка

1. Клонируйте репозиторий:
   git clone https://github.com/your-username/your-repo-name.git  
   cd your-repo-name

2. Установите зависимости:
   pip install -r requirements.txt

Файл requirements.txt:
requests
python-dotenv

## Настройка API-ключа

1. Зарегистрируйтесь на https://rawg.io/apidocs
2. Создайте файл .env в корне проекта
3. Добавьте в него строку:
   API_KEY=ваш_api_ключ

## Запуск

python main.py

После запуска в консоль будет выведена информация о 10 играх.

## Пример вывода

Название игры: StarCraft II  
Дата выхода: 2010-07-27  
Ссылка на игру: https://rawg.io/games/starcraft-ii  

Скриншоты для игры:  
https://media.rawg.io/media/screenshots/...  

Где купить:  
https://store.steampowered.com/app/...

## Примечания

- Используется slug игры для получения скриншотов и магазинов
- RAWG API имеет ограничения на количество запросов
- Для работы необходим валидный API-ключ

## Лицензия

Проект создан в учебных целях. Используйте RAWG API согласно их правилам.
