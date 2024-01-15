![FastAPI for Data Science](docs/images/fastapi-banner-1.png)

# Тьюториал: Основы FastAPI для Data Science

## 👀 Описание

🎓 **Что это такое?** Тьюториал "Основы FastAPI для Data Science" это целое путешествие в мир создания веб-сервисов на FastAPI, специально для Data Scientists и ML Engineers. Этот тьюториал покажет вам, как легко и быстро можно использовать FastAPI для сервинга ML моделей.

👩🏻‍💻 **Кому это подойдет?** Если вы Data Scientist или начинающий ML инженер, этот тьюториал будет вашим лучшим другом. Здесь вы найдете всё, что нужно для начала работы с FastAPI.

🎯 **Что вы узнаете?**

- Почему FastAPI - ваш выбор для Data Science (плюсы и минусы).
- Основные методы работы с FastAPI, включая GET и POST запросы.
- Как интегрировать обученные ML модели в ваш веб-сервис.
- Локальное тестирование функциональности разработанного веб-сервиса.
- Запуск веб-сервиса FastAPI в Docker контейнере.

🔍 **Как это устроено?** Вам не придется долго искать нужную информацию. Тьюториал содержит исчерпывающие примеры кода и пошаговые инструкции в формате Markdown.

⏱️ **Сколько времени займет?** Всего 30 минут - и вы будете готовы создавать свои веб-сервисы на FastAPI.

---

## 📖 Содержание
- [Тьюториал: Основы FastAPI для Data Science](#тьюториал-основы-fastapi-для-data-science)
  - [👀 Описание](#описание)
  - [📖 Содержание](#-содержание)
  - [👩‍💻 1 - Установка](#-1-установка)
  - [🤔 2 - Почему FastAPI?](#-2-почему-fastapi)
  - [⭐ 2 - Основные методы работы с FastAPI (10 минут)](#-2-основные-методы-работы-с-fastapi-10-минут)
    - [Шаг 1 - Создание простого API с GET Запросом](#шаг-1-создание-простого-api-с-get-запросом)
    - [Шаг 2 - Запуск FastAPI сервиса](#шаг-2-запуск-fastapi-сервиса)
    - [Шаг 3 - Тестирование сервиса](#шаг-3-тестирование-сервиса)
    - [Шаг 4 - Создание API с POST запросом](#шаг-4-создание-api-с-post-запросом)
    - [Шаг 4 - Тестирование POST запроса](#шаг-4-тестирование-post-запроса)
    - [Шаг 5 - Автоматическая документация API](#шаг-5-автоматическая-документация-api)
  - [🛠️ 3 - Интеграция ML модели в FastAPI (10 минут)](#️-3-интеграция-ml-модели-в-fastapi-10-минут)
    - [Шаг 1 - Сохранение модели](#шаг-1-сохранение-модели)
    - [Шаг 2 - Загрузка модели в FastAPI](#шаг-2-загрузка-модели-в-fastapi)
    - [Шаг 3 - Создание эндпоинта для прогнозов модели](#шаг-3-создание-эндпоинта-для-прогнозов-модели)
    - [Шаг 4 - Запуск приложения](#шаг-4-запуск-приложения)
    - [Шаг 5 - Тестирование эндпоинта](#шаг-5-тестирование-эндпоинта)
  - [🚀 4 - Запуск веб-сервиса FastAPI в Docker контейнере](#-4-запуск-веб-сервиса-fastapi-в-docker-контейнере)
    - [Шаг 1 - Проверка Структуры Проекта](#шаг-1-проверка-структуры-проекта)
    - [Шаг 2 - Подготовка Dockerfile](#шаг-2-подготовка-dockerfile)
    - [Шаг 3 - Сборка Docker-образа](#шаг-3-сборка-docker-образа)
    - [Шаг 4 - Запуск Docker-контейнера](#шаг-4-запуск-docker-контейнера)
  - [🔗 Дополнительные ресурсы](#-дополнительные-ресурсы)



## 👩‍💻 1 - Установка

Сначала установите готовый пример. Для получения более подробной технической информации и примечаний обратитесь к оригинальному файлу README.

**1. Сделайте форк / Клонируйте этот репозиторий**

Клонируйте репозиторий с примером кода. Этот репозиторий предоставляет необходимые файлы и скрипты для тьюториала.

```bash
git clone https://gitlab.com/risomaschool/tutorials-raif/fastapi-1-for-ml.git 
cd fastapi-1-for-ml
```

**2. Создайте виртуальное окружение** 

Для запуска примеров тьюториала нужен Python 3.9 или выше.

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## 🤔 2 - Почему FastAPI? 

FastAPI — это современный, быстрый (высокопроизводительный) веб-фреймворк для создания API используя Python 3.8+, в основе которого лежит стандартная аннотация типов Python.

Некоторые особенности:

- **Скорость**: Очень высокая производительность. [Один из самых быстрых фреймворков Python](https://fastapi.tiangolo.com/ru/#_10).
- **Быстрота разработки**: Увеличьте скорость разработки примерно на 200–300%.
- **Интуитивно понятный**: Отличная поддержка редактора.  везде. Меньше времени на отладку.
- **Надежность**: Получите готовый к работе код. С автоматической интерактивной документацией.
- **На основе стандартов**: Основан на открытых стандартах API и полностью совместим с ними: [OpenAPI](https://github.com/OAI/OpenAPI-Specification) (ранее известном как Swagger) и [JSON Schema](https://json-schema.org/).

## ⭐ 2 - Основные методы работы с FastAPI (10 минут)

В этом разделе вы научитесь создавать базовый веб-сервис с использованием GET и POST запросов в FastAPI и поймете основные декораторы и функции фреймворка.

### Шаг 1 - Создание простого API с GET Запросом

Создайте файл `main.py` со следующим содержимым:

```bash
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}
```

Этот код создает базовый веб-сервис, который отвечает на GET запрос к корневому URL (`"/"`) фразой "Hello World".

### Шаг 2 - Запуск FastAPI сервиса

Теперь, откройте терминал, перейдите в директорию, в которой находит файл `main.py` и запустите сервер с помощью команды:

```bash
uvicorn main:app --reload
```

Разберем из чего состоит эта команда: 

- `main`: файл `main.py` (модуль Python)
- `app`: объект, созданный внутри `main.py` с помощью строки `app = FastAPI()`
- `--reload`: аргумент для перезапуска сервера после изменения кода (удобно во время разработки)

### Шаг 3 - Тестирование сервиса

Откройте браузер и перейдите по адресу `http://localhost:8000/`. Вы должны увидеть ответ `{"Hello": "World"}`.

![Untitled](docs/images/Untitled.png){width=800}

### Шаг 4 - Создание API с POST запросом

Теперь добавим функционал для обработки POST запросов.

Обновите `main.py`, добавив следующий код

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/items/")
def create_item(item: Item):
    return item
```

Здесь мы создаем класс `Item`, который будет использоваться для валидации данных, отправляемых в POST запросе.

> ⚠️ Обратите внимение на основные декораторы и функций FastAPI:
>
> - `@app.get("/")` и `@app.post("/")`: Это декораторы, которые определяют функции для обработки GET и POST запросов соответственно.
> - `def read_root()` и `def create_item(item: Item)`: Это функции, которые выполняются при получении соответствующего HTTP запроса.
> - `class Item(BaseModel)`: Pydantic модель данных, которая используются для валидации и документирования тела запроса.

### Шаг 4 - Тестирование POST запроса

Вы можете использовать инструменты, такие как Postman или curl, для отправки POST запроса:

```bash
curl -X 'POST' \
  'http://localhost:8000/items/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
    "name": "Sample Item",
    "description": "This is a sample item",
    "price": 15.99,
    "tax": 1.5
    }'

```

### Шаг 5 - Автоматическая документация API

Одна из классных фичей FastAPI - автоматическая документация по API! 

Перейдите на [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs). Вы увидите автоматическую интерактивную документацию API (предоставленную [Swagger UI](https://github.com/swagger-api/swagger-ui)):

![Untitled](docs/images/Untitled%201.png){width=800}

А теперь перейдите на [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc). Вы увидите альтернативную автоматическую документацию (предоставленную [ReDoc](https://github.com/Rebilly/ReDoc)):

![Untitled](docs/images/Untitled%202.png){width=800}

## 🛠️ 3 - Интеграция ML модели в FastAPI (10 минут)

> 💡 В этом разделе вы будете использовать код из приложения  `app/gift_predictor.py`

Сейчас мы переходим к одному из самых захватывающих этапов: интеграции обученной ML модели в веб-сервис FastAPI. Этот процесс не только удивительно прост, но и крайне важен для того, чтобы твои ML-разработки были доступны миру. Давай приступим! 

### Шаг 1 - Сохранение модели

Первый шаг - сохранение твоей ML модели в формате, который можно будет легко загрузить в FastAPI. Для примера в тьюториале будем использовали JSON для хранения данных о подарках и интересах. Это удобный способ хранения статических данных, который легко интегрируется в Python-приложения. Для простоты будем использовать модель сохраненную в JSON.

Путь к модели: `models/model.json`

### Шаг 2 - Загрузка модели в FastAPI

Теперь, когда у нас есть модель, мы можем загрузить ее непосредственно в FastAPI приложение:

```python
with open('models/model.json', 'r') as json_file:
    model = json.load(json_file)
```

Этот код загружает данные из JSON-файла в переменную `model`, которую мы будем использовать для получения прогнозов.

### Шаг 3 - Создание эндпоинта для прогнозов модели

Эндпоинт – это место в API, куда пользователи могут обращаться за рекомендациями. В нашем случае это POST-запрос, который принимает возраст и интересы:

```python
@app.post("/predict/")
def predict_birthday_gift(input_data: PredictionInput):
    ...
```

Код внутри этой функции обрабатывает входные данные, запрашивает модель и возвращает рекомендуемый подарок.

Итоговый код приложения с эндпоинтом `/predict`, который принимает JSON с данными и возвращает прогноз:

```python
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import json
from pydantic import BaseModel
import random

app = FastAPI()

# Load the model from the JSON file
with open('models/model.json', 'r') as json_file:
    model = json.load(json_file)

class PredictionInput(BaseModel):
    """
    Represents the input data for predicting a birthday gift.
    """
    age: int
    interest: str

@app.get("/", response_class=HTMLResponse)
def get_interests():
    """
    Returns the available interests for selecting a birthday gift.
    """
    interests = list(model["interests"].keys())
    interests_str = '</li>\n  <li>'.join(interests)

    return f"""
        <html>
            <head>
                <title>Birthday Gift Predictor</title>
            </head>
            <body>
                <h1>Birthday Gift Predictor</h1>
                <h2>Wanna cool gift for the next birthday?</h2>
                <p>Just let me know your <b>Age</b> and one of the <b>Interests</b>.</p>
                
                <p>Available interests are:</p>
                <ul>
                    <li>{interests_str}</li>
                </ul>
            </body>
        </html>
    """

@app.post("/predict/")
def predict_birthday_gift(input_data: PredictionInput):
    """
    Predicts a birthday gift based on the input data.
    """
    age = input_data.age
    interest = input_data.interest.lower()

    primary_gift = model["gifts_by_age"].get(str(age), "Special Surprise Gift")
    specif_gift = model['interests'].get(interest, '')
    prob = random.randint(50, 100)
    gift = f"{primary_gift} and {specif_gift}" if specif_gift else primary_gift

    return f"predicted_gift: {gift} with probability {prob}%"

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

### Шаг 4 - Запуск приложения

Запустим приложение стандартным способом: 

```bash
uvicorn app.gift_predictor:app --reload
```

![Untitled](docs/images/Untitled%203.png){width=800}

### Шаг 5 - Тестирование эндпоинта

После создания эндпоинта его необходимо протестировать. Запустии FastAPI приложение, и отправим POST-запрос на `/predict/` с JSON-данными. Это поможет убедиться, что эндпоинт корректно обрабатывает запросы и возвращает правильные прогнозы.

```bash
curl -X 'POST' \
  'http://localhost:8000/predict/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
    "age": 25,
    "interest": "data"
    }'
```

То же самое можно сделать через web интерфейс!

- Откройте  [`http://127.0.0.1:8000/docs`](http://127.0.0.1:8000/docs)

![Untitled](docs/images/Untitled%204.png){width=800}

- Укажите `age`  и `interest`

![Untitled](docs/images/Untitled%205.png){width=800}

- Получите прогноз и добавьте в свой Список желаний! 🎁

![Untitled](docs/images/Untitled%206.png){width=800}

Интересно какой будет результат? Запустите сервис и узнайте! 😎

## 🚀 4 - Запуск веб-сервиса FastAPI в Docker контейнере

Чтобы запустить приложение FastAPI в Docker, необходимо собрать Docker Image (образ) и использовать его для запуска Docker-контейнера с приложением. 

Для сборки Docker образа обычно используют конфигурационнный файл - `Dockerfile`. 
Давайте создадим его!

### Шаг 1 - Проверка Структуры Проекта

Убедитесь, что структура проекта выглядит примерно так:

```yaml
fastapi-1-for-ml/
│
├── app/
│   └── git_predictor.py  # FastAPI приложение
│
├── models/
│   └── model.json        # Файл модели
│
├── Dockerfile
└── requirements.txt

```

### Шаг 2 - Подготовка Dockerfile

Создайте файл с именем `Dockerfile` в корневой директории проекта со следующим содержанием:

```docker
# Используем официальный образ Python как базовый
FROM python:alpine3.18

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Копируем файлы зависимостей и устанавливаем их
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем остальные файлы проекта в контейнер
COPY . .

# Задаем команду для запуска приложения
CMD ["uvicorn", "app.gift_predictor:app", "--host", "0.0.0.0", "--port", "8000"]

```

Этот `Dockerfile` начинается с базового образа Python, устанавливает зависимости из `requirements.txt`, копирует файлы проекта в контейнер и запускает сервер Uvicorn при старте контейнера.

### Шаг 3 - Сборка Docker-образа

Соберем Docker контейнер для нашего приложения FastAPI. Это позволит развернуть приложение в изолированной среде, что упростит его запуск и развертывание.

Откройте терминал и перейдите в директорию, где находится `Dockerfile`. Затем выполните следующую команду для сборки Docker-образа:

```bash
docker build -t birthday-gift-predictor .

```

### Шаг 4 - Запуск Docker-контейнера

После успешной сборки образа запусти контейнер, используя следующую команду:

```bash
docker run --name mygiftapp -p 8000:8000 birthday-gift-predictor
```

Удалите старый контейнер, если он существует:

```bash
docker rm -f mygiftapp
```

Эта команда запустит контейнер в фоновом режиме (`-d`), присвоит ему имя `mygiftapp` и пробросит порт 8000 для доступа к приложению.

Теперь приложение доступно по адресу `http://localhost:8000/`.

Для тестирования сервиса, можно использовать те же способы и примеры запросов из предыдущего раздела тьюториала.

```bash
curl -X 'POST' \
  'http://localhost:8000/predict/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
    "age": 25,
    "interest": "data"
    }'
```

Этот простой пример покзывает как лего можно запустить FastAPI приложение Docker контейнере.

## 🧪 5 - Основы Pydantic для FastAPI и не только

### Аннотации типов в Python

Python славится своей динамической типизацией, что означает, что вы не обязаны явно указывать типы переменных. В отличие от статически типизированных языков, таких как Java или C++, Python позволяет вам работать с переменными, не определяя их типы заранее. Эта динамичность делает Python дружелюбным к новичкам и гибким. Однако такое динамическое поведение иногда может вызвать трудноуловимые ошибки, особенно в сложных кодовых базах или обработке данных, где поток данных может быть неочевидным.  

Давайте разберемся на простом примере, что это такое и зачем нужно! Возьмем для примера словарь `input_data` и функцию `iamgroot` ниже. Есть идеи, как их использовать вместе? (не подглядывая ниже) 

```python
input_data = {
    "key1": ["I", "am", "Groot!"],
    "key2": "I am Groot!",
    "key3": True
}

def iamgroot(i, am, groot): 
   pass
```

Этот код может вызвать путаницу и вопросы у других разработчиков или даже у автора кода в будущем! Из из сигнатуры функции нельзя определить, какие типы данных ожидаются для аргументов `i`, `am`, и `groot` и ****что она возвращает.

Теперь посмотрим на модифицированный вариант 

```python
from typing import Text, List

def iamgroot(i: Text, am: str | List[str], groot: bool) -> Text: 
   pass
```

В этом обновлении мы все еще не знаем, что делает функция, но мы знаем типы входных аргументов и возвращаемого значения! В этом обновлении:

- Аргумент `i` ожидается как `Text`, что является аналогом типа `str` в Python. Это указывает на то, что `i` должен быть строкой
- Аргумент `am` может быть либо строкой (`str`), либо списком строк (`List[str]`).
- Аргумент `groot` ожидает логическое значение (`bool`). Это означает, что он должен быть либо `True`, либо `False`.
- Более того, мы знаем, что возвращаемое значение  - просто строка!

Можно предположить, что корректным будем вызов функции в таком виде: 

```python
result = iamgroot(
    input_data["key2"],  # "I am Groot!"
    input_data["key1"],  # ["I", "am", "Groot!"]
    input_data["key3"],  # True
)
print(result)  # Выведет, конечно же: "I am Groot!" )))
```

**Почему это важно использовать Type Annotation в Python?** 

1. Аннотации типов делают код более понятным и легким для чтения, помогая другим разработчикам и вам самим быстрее понять структуру и назначение кода.
2. Проще предотвратить ошибки и легче их обнаружить.
3. Аннотации типов позволяют использовать инструменты для строгой проверки типов, такие как `mypy`, что повышает надежность и безопасность кода.
4. Улучшается работа с IDE и инструментами разработки: (автодополнение, подсказки…)

### Основы Pydantic в FastAPI приложениях

Pydantic - это библиотека Python, используемая для валидации данных и управления настройками на основе аннотаций типов Python. Она обеспечивает простой способ создания и использования моделей данных, которые автоматически проверяются на соответствие заданным типам и форматам.

В FastAPI Pydantic используется для определения структуры данных и валидации входных данных.  Чтобы использовать Pydantic, вы сначала определяете модель данных, используя классы Python.  

В пример FastAPI приложения выше вы уже использовали Pydantic для определения модели входных данных `PredictionInput`

```python
from pydantic import BaseModel

class PredictionInput(BaseModel):
    """
    Represents the input data for predicting a birthday gift.
    """
    age: int 
    interest: str

```

В этом примере определена модель `PredictionInput`, содержащая два поля:  `age`

и `interest`. Каждое поле имеет тип данных, указанный через аннотации типов.

### Валидация и создание экземпляров модели

Создание экземпляра модели Pydantic автоматически приводит к валидации данных:

```python
input = PredictionInput(age=30, interest="gaming")

# Pydantic автоматически проверит, что 'age' - это целое число, а 'interest' - строка.
```

Если данные не соответствуют определенному типу или условиям, Pydantic вызовет исключение.

### Расширенные возможности валидации c Fields

Pydantic также позволяет использовать более сложные валидации, включая использование регулярных выражений, проверку диапазонов значений и многое другое. Для этого можно использовать `Fields` .

```python
from pydantic import BaseModel, Field

class PredictionInput(BaseModel):
    age: int = Field(gt=0, le=100)
    interest: str

```

### Использование Field Validators

Для более сложной проверки Pydantic позволяет вам определить свои собственные собственные валидаторы полей с помощью `@field_validator`

```python
class PredictionInput(BaseModel):
    """
    Represents the input data for predicting a birthday gift.
    """
    age: int = Field(gt=0, le=100)
    interest: str

    @field_validator('age', 'interest')
    @classmethod
    def check_alphanumeric(cls, v: str, info: ValidationInfo) -> str:
        if not v.replace(' ', '').isalnum():
            raise ValueError(f'Field: {info.field_name} must be alphanumeric')
        return v
```

### Добавим Annotated Validators

```python
InterestType = Annotated[
        str, 
        Field(description="Interest should be one of predefined categories"),
    ]

class PredictionInput(BaseModel):
    """
    Represents the input data for predicting a birthday gift.
    """
    age: int = Field(gt=0, le=100)
    interest: InterestType
    ...
```

### Добавим AfterValidator

AfterValidator позволяют добавить дополнительные валидации после того, как Pydantic проверил ве внутренни валидации модели.

```python
from pydantic import BaseModel, Field, constr, validator
from typing import Annotated
from pydantic.functional_validators import AfterValidator

# Функция валидации для интереса
def validate_interest(value: str) -> str:
    valid_interests = [
        "painting", 
        "reading",
        "gardening",
        "gaming",
        "yoga",
        "fashion",
        "data",
        "ml",
        "programming",
        "it",
        "no"
    ]
    if value not in valid_interests:
        raise ValueError(f"Interest must be one of {valid_interests}")
    return value

InterestType = Annotated[
        str, 
        Field(description="Interest should be one of predefined categories"),
        AfterValidator(validate_interest)
    ]

class PredictionInput(BaseModel):
    """
    Represents the input data for predicting a birthday gift.
    """
    age: int = Field(gt=0, le=100)
    interest: InterestType
    ...

```

В этом примере:

- Мы определяем словарь **`valid_interests`**, содержащий допустимые интересы.
- Функция **`validate_interest`** проверяет, соответствует ли значение **`interest`** одному из ключей в словаре **`valid_interests`**.
- В случае, если значение **`interest`** не соответствует ожиданиям, генерируется исключение **`ValueError`**.

В этом обновленном примере кода для FastAPI используются лучшие практики Pydantic для валидации входных данных. Модель `PredictionInput` теперь проверяет, что введенный возраст и интерес соответствуют данным, загруженным из `model.json`. В случае ошибок валидации или чтения файла модели генерируются соответствующие исключения HTTPException.

Теперь можно запустить обновленное FastAPI приложение, и протестировать его. 

```bash
uvicorn app.gift_predictor_update:app --reload
```

Для тестирования воспользуйтесь утилитой командой строки `curl` , или откройте Swagger документацию http://127.0.0.1:8000/docs 

```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/predict/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
        "age": -1,
        "interest": "books"
    }'
```

![Untitled](docs/images/pydantic-1-test.png){width=800}

Оба варианта вернут сообщение об ошибках, с указанием какое поле и почему не прошло валидацию.

![Untitled](docs/images/pydantic-2-error.png){width=800}

Поздравляю с завершением тьюториала! 🥳 Вы только что интегрировали свою ML модель в FastAPI, создав функциональный эндпоинт для прогнозов. Это не просто крутой способ демонстрации твоих навыков, но и шаг к созданию реальных продуктов на основе машинного обучения. Приятного кодинга! 🚀👩‍💻👨‍💻

> Если рекомендованный подарок 🎁 вам по душе - добавьте его в список желаний, или сразу купите! Вы этого заслуживаете! 🤗

## 🔗 Дополнительные ресурсы

- [Документация FastAPI](https://fastapi.tiangolo.com/ru/#_5)
- [4 Tips for Building a Production-Ready FastAPI Backend](https://www.youtube.com/watch?v=XlnmN4BfCxw)
- [FastAPI Best Practices](https://betterprogramming.pub/fastapi-best-practices-1f0deeba4fce)
- [12 Beginner Concepts About Type Hints To Improve Your Python Code](https://towardsdatascience.com/12-beginner-concepts-about-type-hints-to-improve-your-python-code-90f1ba0ac49#)
- [Type Hinting in Python](https://dagster.io/blog/python-type-hinting)
- [Pydantic](https://docs.pydantic.dev/latest/)


![FastAPI for Data Science](docs/images/fastapi-notes-1.png)

[⬆️ Содержание](#-содержание)