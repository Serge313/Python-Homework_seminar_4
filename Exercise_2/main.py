"""Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на
круглой грядке, причем кусты высажены только по окружности. Таким образом,
у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
выросло различное число ягод – на i-ом кусте выросло ai ягод.
В этом фермерском хозяйстве внедрена система автоматического сбора черники.
Эта система состоит из управляющего модуля и нескольких собирающих модулей.
Собирающий модуль за один заход, находясь непосредственно перед некоторым
кустом, собирает ягоды с этого куста и с двух соседних с ним.
Напишите программу для нахождения максимального числа ягод, которое может
собрать за один заход собирающий модуль, находясь перед некоторым кустом
заданной во входном файле грядки."""


import sys


def fill_list_of_bushes(list, n):
    """The method fills empty list"""
    count = 1
    while count <= n:
        try:
            number_of_berries = int(input(f"Enter the number of berries on the {count} bush: "))
        except ValueError as ex:
            print(f"Error: {ex}")
            sys.exit()
        list.append(number_of_berries)
        count += 1
    return list


def find_max_harvested_berried(list, maximum=0):
    """The method finds the maximum number of berries
    that the picking module can collect in one run"""
    for i in range(1, len(list) - 1):
        if maximum < list[i - 1] + list[i] + list[i + 1]:
            maximum = list[i - 1] + list[i] + list[i + 1]
    return maximum


def testing_find_max_harvested_berried(test_list=[1, 2, 3, 4]):
    """The method tests find_max_harvested_berried method"""
    print("Testing of the \"find_max_harvested_berried\" method has been launched...")
    expected = 9
    actual = find_max_harvested_berried(test_list)
    is_equal = expected == actual
    if is_equal:
        print("Test completed successfully!")
    else:
        print("Error! Need to fix the method!")


testing_find_max_harvested_berried()
print()


try:
    number_of_bushes = int(input("Enter the number of bushes: "))
except ValueError as e:
    print(f"Error: {e}")
    sys.exit()


print()
list_of_bushes = []
filled_list_of_bushes = fill_list_of_bushes(list_of_bushes, number_of_bushes)
RESULT = find_max_harvested_berried(filled_list_of_bushes)
print()
print(f"The entered number of berries on each bush: {filled_list_of_bushes}"
      f"\nThe maximum number of berries that the picking module can collect"
      f" in one run: {RESULT}")

