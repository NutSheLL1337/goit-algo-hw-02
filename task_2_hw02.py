from collections import deque
# Завдання 2

# Необхідно розробити функцію, яка приймає рядок як вхідний параметр, 
# додає всі його символи до двосторонньої черги (deque з модуля collections в Python), 
# а потім порівнює символи з обох кінців черги, щоб визначити, чи є рядок паліндромом. 
# Програма повинна правильно враховувати як рядки з парною, так і з непарною кількістю символів, 
# а також бути нечутливою до регістру та пробілів.

def is_palindrome_queue(string: str) -> bool:
    word = string.replace(' ', '').lower()
    deq = deque(word)
    while len(deq) > 1:
        if deq.popleft() != deq.pop():
            return print(False)
    return print(True)


is_palindrome_queue("Madam")

    