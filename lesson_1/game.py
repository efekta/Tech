# Задача: реализовать игру в загадки
# Требования:
# Программа должна выводить в консоль текст загадки и ждать ввода пользователя
# Программа после ввода пользователя ответа должна вывести в консоль результат:
# правильный ли ответ дал пользователь
# Загадок должно быть 10, тематика вопросов должна быть по первому занятию

# Дополнительные требования (со звездочкой или сложные, необязательно для выполнения):
# Программа должна в конце игры сказать, сколько ответов дал пользователь:
# сколько из них было верных
# Программа должна не учитывать регистр ответа:
# "Python" и "python" оба должны быть правильным ответом на вопрос "Какой язык мы учим?"

quiz = {
    "Какой язык мы учим?: ": "python",
    "Как преобразовать число в строку: ": "str()",
    "Как преобразовать строку в целое число: ": "int()",
    "Как число или строку в число с плавающей точкой: ": "float()",
    "Булевый тип данных (правда): ": "True",
    "Булевый тип данных (ложь): ": "False",
    "Итерирующий цикл: ": "for",
    "Цикл с предусловием: ": "while",
    "Логический оператор 'И': ": "and",
    "Логический оператор 'ИЛИ': ": "or"
}

answer_true = 0
qwestions = 0
for key in quiz:
    qwestion = input(key)
    qwestions += 1
    if qwestion.lower() == quiz[key].lower():
        answer_true += 1
        print("Ответ верный")
    elif not qwestion.lower():
        print("Вопрос пропущен")
    elif qwestion.lower() != quiz[key].lower():
        print("Ответ неверный")

print("Задано вопросов: {}".format(qwestions))
print("Правильных ответов: {}".format(answer_true))