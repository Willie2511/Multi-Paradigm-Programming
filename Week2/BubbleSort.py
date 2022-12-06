

def bubble_sort(list1):
    """
                    Given a list of numbers as input this function will return a sorted list.

                    :param list: the list of numbers given as input
                    :return: a sorted list.
                """
    for i in range(len(list1)):
        for j in range(0, len(list1) - i -1):
            if(list1[j] > list1[j+1]):
                temp = list1[j]
                list1[j] = list1[j+1]
                list1[j+1] = temp
    return list1
