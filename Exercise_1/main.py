"""Задача 22: Даны два неупорядоченных набора целых чисел
(может быть, с повторениями). Выдать без повторений в порядке
возрастания все те числа, которые встречаются в обоих наборах."""


import sys


def fill_list_of_numbers(list, n):
    """The method fills empty list"""
    count = 1
    while count <= n:
        try:
            number = int(input(f"Enter number at index {count - 1}:    "))
        except ValueError as ex:
            print(f"Error: {ex}")
            sys.exit()
        list.append(number)
        count += 1
    return list


def set_and_intersect(list_num_one, list_num_two):
    """The method converts lists to sets, finds
    the numbers in the intersection and returns
    them in ascending order"""
    first_set = set(list_num_one)
    second_set = set(list_num_two)
    set_of_intersection = sorted(first_set.intersection(second_set))
    return set_of_intersection


def testing_set_and_intersect(first_test_list=[2, 4, 6, 8, 10, 12, 10, 8, 6, 4, 2],
                              second_test_list=[3, 6, 9, 12, 15, 18]):
    """The method tests set_and_intersect method"""
    print("Testing of the \"set_and_intersect\" method has been launched...")
    expected = [6, 12]
    actual = set_and_intersect(first_test_list, second_test_list)
    is_equal = expected == actual
    if is_equal:
        print("Test completed successfully!")
    else:
        print("Error! Need to fix the method!")
        print(actual)


testing_set_and_intersect()
print()


try:
    number_of_elements_in_first_list = int(input("Enter number of elements of the first list: "))
except ValueError as e:
    print(f"Error: {e}")
    sys.exit()


print()


try:
    number_of_elements_in_second_list = int(input("Enter number of elements of the second list: "))
except ValueError as e:
    print(f"Error: {e}")
    sys.exit()


first_list = []
print()
print("Enter elements of the first list of numbers |"
      "\n\t\t\t\t\t\t\t|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯"
      "\n\t\t\t\t\t\t\tv")
first_list_of_numbers = fill_list_of_numbers(first_list, number_of_elements_in_first_list)

second_list = []
print()
print("Enter elements of the second list of numbers |"
      "\n\t\t\t\t\t\t\t|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯"
      "\n\t\t\t\t\t\t\tv")
second_list_of_numbers = fill_list_of_numbers(second_list, number_of_elements_in_second_list)

RESULT = set_and_intersect(first_list_of_numbers, second_list_of_numbers)
print()
print(f"Your fist list: {first_list_of_numbers}"
      f"\nYour second list: {second_list_of_numbers}"
      f"\nNumbers in the intersection in ascending order: {RESULT}")
