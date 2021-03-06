# 6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие
# лекционных, практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
#
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

# Чтение данных из файла
try:
    with open("text_6.txt") as file:
        data = file.readlines()

except FileNotFoundError:
    print('Файл не найден')

# Создание базы для работы на основе списка
lessons = []
for i in range(len(data)):
    lessons.append(data[i].split())

# Обработка и вывод
summary = {}
for lesson in lessons:
    key = lesson[0][:-1]  # убрать двоеточие
    value = 0
    for item in lesson:

        # Вынимаем только числа, проверяя символы на цифры
        num = ''
        for symbol in item:
            if symbol.isdigit():
                num += symbol

        # Приводим числовые строки к числам и суммируем
        num_int = 0
        if num:
            value += int(num)

    summary.update({key: value})
print(summary)
