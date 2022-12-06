import csv
from BubbleSort import bubble_sort
import numpy as np


def get_maximum_value(list):
    """
                Given a list of numbers as input this function will return the maximum value in list.

                :param list: the list of numbers given as input
                :return: the maximum value of the list
            """
    maximum = list[0]
    for l in list:
        if maximum < l:
            maximum = l
    return maximum


def get_minimum_value(list):
    """
            Given a list of numbers as input this function will return the minimum value in list.

            :param list: the list of numbers given as input
            :return: the minimum value of the list
        """
    minimum = list[0]
    for l in list:
        if minimum > l:
            minimum = l
    return minimum


def get_average(list):
    """ 
        Given a list of numbers as input this function will return the numerical average.

        :param list: the list of numbers given as input
        :return: the numerical average of the list
    """
    total = 0
    for l in list:
        total += l

    average = total / len(list)
    return average


def get_median_value(list):
    """
                Given a list of numbers as input this function will return the median value in the list.

                :param list: the list of numbers given as input
                :return: the median value in the list
            """
    list1 = list.copy()
    bubble_sort(list1)
    median = list1[int(len(list1)/2)]
    return median

def read_scores_from_csv(filename):
    """
                    Given a filename as input this function will return the ist of "Score" from the file.

                    :param filename: the name of a file
                    :return: the list of integers in "Score" column of file
                """
    scores = []
    with open(filename, mode='r') as file:
        csvFile = csv.DictReader(file)

        for lines in csvFile:
            score = int(lines["Score"])
            scores.append(score)
    return scores


def read_student_number_from_csv(filename='example.csv'):
    """
                    Given a filename as input this function will return the ist of "Student Number" from the file.

                    :param filename: the name of a file
                    :return: the list of integers in "Student Number" column of file
                """
    student_number = []
    # Specified an encoding to remove /ufeff from the beginning of String
    # so that the column name could be correctly recognised
    with open(filename, mode='r', encoding='utf-8-sig') as file:
        csvFile = csv.DictReader(file)

        for lines in csvFile:
            student_num = int(lines["Student Number"])
            student_number.append(student_num)
    return student_number




def get_mode(list):
    """
                Given a list of numbers as input this function will return the mode of list.

                :param list: the list of numbers given as input
                :return: the mode value of the list (the value that appears most frequently).
            """
    highest_freq = 0
    mode = scores[0]
    for score in scores:
        frequency = 0
        for score2 in scores:
            if score == score2:
                frequency += 1
        if frequency > highest_freq:
            mode = score
            highest_freq = frequency
    return mode

def get_odd(list):
    """
                    Given a list of numbers as input this function will return a list of the odd numbers.

                    :param list: the list of numbers given as input
                    :return: list of odd numbers.
                """
    odd_nums = []
    for num in list:
        if num % 2 != 0:
            odd_nums.append(num)
    return odd_nums


def get_even(list):
    """
                        Given a list of numbers as input this function will return a list of the even numbers.

                        :param list: the list of numbers given as input
                        :return: list of even numbers.
                    """
    even_nums = []
    for num in list:
        if num % 2 == 0:
            even_nums.append(num)
    return even_nums


if __name__ == "__main__":

    scores = read_scores_from_csv(
        'example.csv')

    average = np.average(scores)
    minimum = min(scores)
    maximum = max(scores)
    median = np.median(scores)
    mode = get_mode(scores)
    odd_nums = get_odd(scores)

    sorted_list = bubble_sort(scores)
    print(f'Testing Bubble Sort algorithm: {sorted_list}')
    student_nums = read_student_number_from_csv()


    print(
        f'Average: {average} Median: {median} Smallest: {minimum} Largest: {maximum} mode: {mode} odd: {odd_nums}')
    print(f'Data in Student Number Column is : {student_nums}')