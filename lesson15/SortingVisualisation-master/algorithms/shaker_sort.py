# shaker Sort or Cocktail Sort Algorithm

"""
    Repeatedly steps through the list, compares adjacent
    elements and swaps them if they are in the wrong order.

    The pass through the list is repeated until the list is sorted.

    The algorithm, which is a comparison sort, is named for
    the way smaller or larger elements "shaker" to the top of the list.
"""

from random import sample


class ShakerSort:

    def __init__(self, unsorted, n):
        self.shaker(unsorted, n)

    @staticmethod
    def shaker(unsorted, n):
        """ shaker sort algorithm """
        for i in range(0, n - 1):
            swapped = False
            for j in range(i, n - 1 - i):
                if unsorted[j] > unsorted[j + 1]:
                    val = unsorted[j]
                    swap = unsorted[j + 1]
                    unsorted[j] = swap
                    unsorted[j + 1] = val
                    swapped = True
            for j in range(n - 1 - i, i, -1):
                if unsorted[j] < unsorted[j - 1]:
                    val = unsorted[j]
                    swap = unsorted[j - 1]
                    unsorted[j] = swap
                    unsorted[j - 1] = val
                    swapped = True
            if not swapped:
                break


if __name__ == '__main__':
    a = sample(range(1000), 1000)
    n = len(a)
    solver = ShakerSort(a, n)
    print(a)
