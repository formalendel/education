# Импорт библиотек
from math import sqrt, pi
import pathlib
import json

print("Hello")
a = 1

if a < 0:
    print("Negative")
elif a == 0:
    print("Zero")
else:
    print("Positive")

# for i=1,5 do
for i in range(5):
    print(i)

# {1,2,3,4,5}
arr = [1, 2, 3, 4, 5]

dictionary = {"one": 1, "two": 2, "three": 3}

a = json.load(dictionary)
# a = 5
# b = 10 if a > 5 else 15

# local length = #arr
length = len(arr)


# a = "Привет"
# for i in a:
#   print(i)
# a[0] -- П

# a = "1;2;3, 4, 5, 6"
# arr = a.split(";")

# for i=1,#arr do
for i in range(length):
    print(arr[i])
    break # он выходит из цикла
    continue # он пропускает оставшуюся часть и переходит к следующей итерации

# ВАЖНO: В python индексация с 0, а в Lua с 1

# for key, value in pairs(arr) do
for key, value in dictionary.items():
    print(key, value)

# for key in dictionary.keys():
# for value in dictionary.values():
# for index, value in enumerate(arr):


"""
    Пример:
    arr = [1, 2, 3]
    arr = [i*2 for i in arr]

    a = list(map(lambda x: x*2, arr))
"""

"""
function example(arr):
    return x * x
"""
def example(x: list[int | str | bool]) -> dict[str, int]:
    return x * x

example([1, 2, 3])

@app.get("/", response_class=HTMLResponse)
async def read_root():
    # Ваш HTML с закрепленным хедером
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Закрепленный хедер</title>
        <link rel="stylesheet" href="/static/style.css">
        <style>
            body { margin: 0; font-family: sans-serif; }
            header {
                background-color: #333;
                color: white;
                padding: 10px 0;
                text-align: center;
                width: 100%;
                position: fixed; /* Закрепление */
                top: 0;
                left: 0;
                z-index: 1000; /* Чтобы был поверх всего */
                box-shadow: 0 2px 5px rgba(0,0,0,0.2);
            }
            nav a {
                color: white;
                margin: 0 15px;
                text-decoration: none;
            }
            .content {
                padding-top: 80px; /* Отступ, чтобы контент не перекрывался хедером */
                padding-left: 20px;
                padding-right: 20px;
                text-align: center;
            }
            /* Пример стилей для длинного контента */
            .long-content {
                height: 200vh; /* Создаем скролл */
                background-color: #f4f4f4;
            }
        </style>
    </head>
    <body>
        <header>
            <h1>Мой Сайт</h1>
            <nav>
                <a href="/">Главная</a>
                <a href="/preview">Предпросмотр</a>
                <a href="/form">Форма</a>
                <a href="/preview/debet?sort_by=Ф.И.О.">Дебеторы</a>
            </nav>
        </header>
        <div class="router-content">
            <h2>Добро пожаловать!</h2>
            <p>Это основной контент страницы.</p>
            <div class="long-content">
                {<p>Этот блок большой, чтобы показать эффект закрепленного хедера при скролле.</p>
                <p>Скролльте вниз...</p>}
            </div>
        </div>
    </body>
    </html>
    """