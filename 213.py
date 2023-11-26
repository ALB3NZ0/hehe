import asyncio
import random




async def download_file(url):
    print(f"Загрузка файла: {url}")
    await asyncio.sleep(random.randint(1, 5))  # имитация загрузки файла
    print(f"Файл {url} загружен")


async def process_data(file):
    print(f"Обработка данных: {file}")
    await asyncio.sleep(random.randint(1, 5))  # имитация обработки данных
    print(f"Данные из файла {file} обработаны")


async def upload_data(data):
    print(f"Загрузка данных: {data}")
    await asyncio.sleep(random.randint(1, 5))  # имитация загрузки данных
    print(f"Данные {data} загружены")




async def main():
    while True:
        print("Выберите действие: ")
        print("1 - Загрузка файлов")
        print("2 - Обработка файлов")
        print("3 - Загрузка данных")
        print("4 - Выход из программы")

        hehe = int(input("Введите номер действия: "))

        if hehe == 1:
            url = input("Введите URL файла: ")
            await download_file(url)
        elif hehe == 2:
            file = input("Введите имя файла для обработки: ")
            await process_data(file)
        elif hehe == 3:
            data = input("Введите данные для загрузки: ")
            await upload_data(data)
        elif hehe == 4:
            print("Всего хорошего")
            break


asyncio.run(main())

