import random

__all__ = ['birthday', 'monty_hall']

def birthday(iteration, people_counter = 23 ):

    count = 0

    for i in range(iteration):
        age_list = []
        for j in range(people_counter):
            age = random.randint(1, 365)
            if age in age_list:
                count += 1
                break
        age_list.append(age)
    return "Вероятность совпадения ДР: " + str(count/(iteration/100)) + " %"


def open_door(win_door: int, choice: int) -> int:
    for i in range(1, 4):
        if i != win_door and i != choice:
            return i


def switch(choice: int, doors: list[int]) -> int:
    doors.remove(choice)
    return doors[0]


def monty_hall(iterations):

    win_with_change = 0
    win_without_change = 0

    for _ in range(iterations):
        doors = [1, 2, 3]
        win_door = random.randint(1, 3)
        choice = random.randint(1, 3)
        opened_door = open_door(win_door, choice)
        doors.remove(opened_door)
        if win_door == choice:
            win_without_change += 1
        else:
            choice = switch(choice, doors)
            if choice == win_door:
                win_with_change += 1
    return f"""Всего дверей открыто:{iterations}
    Шанс победы не меняя выбор: {win_without_change / iterations * 100}%
    Выбор менялся: {win_with_change / iterations * 100}%"""


if __name__ == "__main__":
    print(paradox.birthday(100000))
    print(paradox.monty_hall(100000))