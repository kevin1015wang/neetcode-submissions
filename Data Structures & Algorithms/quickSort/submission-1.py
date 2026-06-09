# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSortHelper(self, pairs, start, end):
        if end - start + 1 <= 1:
            return pairs
        
        left = start
        pivot = pairs[end]

        for i in range(start, end):
            if pairs[i].key < pivot.key:
                temp = pairs[left]
                pairs[left] = pairs[i]
                pairs[i] = temp
                left += 1

        temp = pairs[left]
        pairs[left] = pairs[end]
        pairs[end] = temp

        self.quickSortHelper(pairs, start, left - 1)
        self.quickSortHelper(pairs, left + 1, end)

        return pairs

    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.quickSortHelper(pairs, 0, len(pairs) - 1)
        