# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSortHelper(self, pairs, s, e):
        if e - s + 1 <= 1:
            return
        
        m = (s + e) // 2

        self.mergeSortHelper(pairs, s, m)
        self.mergeSortHelper(pairs, m + 1, e)

        self.merge(pairs, s, m, e)

        return pairs

    def merge(self, arr, l, m, r):
        left = arr[l: m + 1]
        right = arr[m + 1: r + 1]

        i = 0
        j = 0
        k = l

        while i < len(left) and j < len(right):
            if left[i].key <= right[j].key:
                arr[k] = left[i]
                i += 1
                k += 1
            else:
                arr[k] = right[j]
                j += 1
                k += 1
        
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

        return

    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        if len(pairs) == 0:
            return []
        
        if len(pairs) == 1:
            return [pairs[0]]
        
        return self.mergeSortHelper(pairs, 0, len(pairs) - 1)
