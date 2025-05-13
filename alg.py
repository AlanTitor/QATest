# Ввод чисел с клавиатуры через пробел. Возвращает список чисел(int) разделенный на подстроки функцией split
custom_input = list(map(int, input("Введите числа через запятую: ").split(',')))

# Возвращает только четные числа благодаря list comprehension
even_list = [x for x in custom_input if x % 2 == 0]

print(f"Список четных чисел: {even_list}")

# Использование built-in функций по нахождению максимального и минимального числа
print(f"Максимальное число: {max(custom_input)}.")
print(f"Минимальное число: {min(custom_input)}.")


# Простая сортировка листа пузырьком
def sort(list: list) -> None:
    for i in range(len(list)):
        for j in range(len(list) - 1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]

# Вызов нашей функции сортировки пузырьком
sort(custom_input)
print(custom_input)

# Альтернативный способ сортировки, не используя built-in функцию sorted
custom_input.sort()
print(custom_input)