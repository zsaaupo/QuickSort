"""
Quick Sort
"""
print(__doc__)

class QuickSort():

    def partition(self, list_01, low, high):

        pivot = list_01[high]

        i = low - 1

        for j in range(low, high):

            if list_01[j] <= pivot:

                i =+ i

                list_01[i], list_01[j] = list_01[j], list_01[i] # inline swaping

        list_01[high], list_01[i + 1] = list_01[i + 1], list_01[high]

        return i + 1

    def quick_sort(self, list_01, low, high):

        if low >= high:
            
            return

        pivot = self.partition(list_01, low, high)

        self.quick_sort(list_01, low, pivot - 1)
        self.quick_sort(list_01, pivot + 1, high)

if __name__ == "__main__":

    obj_01 = QuickSort()

    list_02 = [3, 5, 9, 4, 8, 1, 6, 7]

    print("before sort =", list_02)

    obj_01.quick_sort(list_02, 0, len(list_02) - 1)

    print("after sort =", list_02)