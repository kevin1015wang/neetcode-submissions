# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        self.mergeSortHelper(pairs, 0, len(pairs))
        return pairs
        
    def mergeSortHelper(self, pairs, start, end):
        if end - start + 1 <= 1:
            return pairs
        
        middle = (start + end) // 2

        self.mergeSortHelper(pairs, start, middle)

        self.mergeSortHelper(pairs, middle + 1, end)

        self.merge(pairs, start, middle, end)

        return pairs

    def merge(self, pairs, start, middle, end):
        leftPairs = pairs[start: middle + 1]
        rightPairs = pairs[middle + 1: end + 1]

        leftIndex = 0
        rightIndex = 0
        pairsIndex = start

        while leftIndex < len(leftPairs) and rightIndex < len(rightPairs):
            if leftPairs[leftIndex].key <= rightPairs[rightIndex].key:
                pairs[pairsIndex] = leftPairs[leftIndex]
                leftIndex += 1
            else:
                pairs[pairsIndex] = rightPairs[rightIndex]
                rightIndex += 1
            pairsIndex += 1
        
        while leftIndex < len(leftPairs):
            pairs[pairsIndex] = leftPairs[leftIndex]
            leftIndex += 1
            pairsIndex += 1
        while rightIndex < len(rightPairs):
            pairs[pairsIndex] = rightPairs[rightIndex]
            rightIndex += 1
            pairsIndex += 1