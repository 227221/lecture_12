import csv
import os
import random


cwd_path = os.getcwd()


def read_row(file_name):
    """
    Reads one row for a CSV file and returns numeric data.
    :param file_name: (str), name of CSV file
    :return: (list, int),
    """
    digits = []
    with open(file_name, "r") as file:
        group = csv.reader(file, delimiter="\t")
        group = list(group)
        numbers = group[0]
        for number in numbers:
            number = int(number)
            digits.append(number)
        return digits


def read_rows(file_name, row_number):
    """
    Reads selected row for a CSV file and returns selected numeric data.
    :param file_name: (str), name of CSV file
    :param row_number: (int), number of selected row
    :return: (list, int),
    """
    pass


def selection_sort(number_array, direction="ascending"):
    """
        Sorts and returns selected numeric data with Selection Sort.
        :param number_array: (list,int), list with numeric array
        :return: (list, int), sorted numeric array
    """
    sorted_numbers = []
    for count in range(0, len(number_array)):
        position = 0
        value = number_array[0]
        for index, number in enumerate(number_array):
            if direction == "ascending":
                if number < value:
                    value = number
                    position = index
                else:
                    continue
            else:
                if number > value:
                    value = number
                    position = index
                else:
                    continue
        sorted_numbers.append(number_array.pop(position))
    return sorted_numbers


def bubble_sort(number_array):
    """
       Sorts and returns selected numeric data with Bubble Sort.
       :param number_array: (list,int), list with numeric array
       :return: (list, int), sorted numeric array
    """
    pass


def main():
    numbers = read_row("numbers_one.csv")
    print(numbers)

    # Ukol: Selection Sort
    sorted_numbers = selection_sort(numbers)
    print(sorted_numbers)

    # Ukol: Selection Sort - se smerem razeni
    numbers = read_row("numbers_one.csv")
    sorted_numbers = selection_sort(numbers, "descending")
    print(sorted_numbers)

    # Ukol: Bubble Sort


    # příklad výpisu hodnot seřazené řady
    # print ("Seřazená řada čísel je:")
    # for i in range(len(number_array)):
    #	print ("%d" %number_array[i]),


if __name__ == '__main__':
    main()
