# Импортируем(загружаем) модуль(библиотека базы данных SQLite) в программу
import sqlite3
import string  # Для операций с классом string и его методами

# Выводим на монитор выбор необходимых действий
print("1 - Добавить запись\n2 - Просмотр записей\n3 - Удалить запись\n4 - Удалить все записи")

# Блоком try/except задаём исключение(ошибку) ввода номера действия, если ввели букву
try:
    # Создаём переменную, для ввода числа выборанного действия и нажать ENTER
    choice = int(input("> "))
except ValueError:
    print("Ошибка ввода")
    choice = int(input("> "))

# Создаём переменную(объекта Connection), для соединения с модулем(базой данных SQLite)
# и созданием файла, где будут храниться данные
connect = sqlite3.connect('test.db')

# Оборачиваем код оператором менеджера контекста и это гарантия закрытия файла
# вне зависимости от того, как будет завершён вложенный код
with connect:
    # Создаём переменную(объекта Cursor), который позволит нам производить операции с SQL
    cursor = connect.cursor()

    # Вызываем метод execute(), для выполнения команд SQL, где создаём таблицу test с 4 рядами(row)
    cursor.execute("CREATE TABLE IF NOT EXISTS test (id INTEGER, name TEXT, surname TEXT, age INTEGER)")

    # Логика программы(условие), если ввели 1 и нажали ENTER, то предлогается выбор ввода данных
    if choice == 1:
        try:
            # Создаём переменные, которые указали при создании таблицы test
            id_number = int(input("Номер\n> "))  # Здесь сами задаём номер строки и нажать ENTER
        except ValueError:
            print("Ошибка ввода")
            id_number = int(input("Номер\n> "))

        # В цикле while, проверяем ввод строки(str), если ввели цифру
        while True:
            name = input("Имя\n> ")
            for s in name:
                if s in string.digits:
                    print("Ошибка ввода")
                    break
                continue
            else:
                break

        while True:
            surname = input("Фамилия\n> ")
            for s in surname:
                if s in string.digits:
                    print("Ошибка ввода")
                    break
                continue
            else:
                break

        try:
            age = int(input("Возраст\n> "))
        except ValueError:
            print("Ошибка ввода")
            age = int(input("Возраст\n> "))
        # Вызываем метод execute(), где добавляем данные в таблицу
        cursor.execute("INSERT INTO test VALUES (?, ?, ?, ?)", (id_number, name, surname, age))

    # Или же ввели 2
    elif choice == 2:
        # Вызываем метод execute(), где получаем все данные из таблицы
        cursor.execute("SELECT * FROM test")

        # Создаём переменную, где вызываем метод fetchall(), который записывает данные в переменную
        # и возвращает все записи
        rows = cursor.fetchall()

        # В цикле for перебираем все ряды и вставляем в переменную и выводим на монитор
        for row in rows:
            print(row[0], row[1], row[2], row[3])

    # Или же ввели 3
    elif choice == 3:
        print("Введите номер записи для удаления")
        try:
            # Вводим номер строки, для удаления
            choice = int(input("> "))  # Нажать ENTER
        except ValueError:
            print("Ошибка ввода")
            choice = int(input("> "))

        # Присваиваем существующему номеру строки номер, который ввели
        id_number = choice

        # Условие, если номера строк одинаковые
        if choice == id_number:
            # Вызываем метод execute(), где удаляем данные из таблицы по номеру строки
            cursor.execute("DELETE FROM test WHERE id = ?", (id_number,))
            print("Запись удалена")

    # Или же ввели 4
    elif choice == 4:
        # Вызываем метод execute(), где удаляем все данные в таблице
        cursor.execute("DELETE FROM test")
        print("Записи удалены")

    # Иначе
    else:
        print("Выберите нужное действие")

    connect.commit()  # Сохранить(зафиксировать) изменения
    cursor.close()  # Закрыть объект Cursor
    # Закрыть соединение объекта Connection
    # connect.close()
