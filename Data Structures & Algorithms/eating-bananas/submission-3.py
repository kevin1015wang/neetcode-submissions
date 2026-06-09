class Solution:
    def numHoursToEat(self, piles: List[int], speed: int) -> int:
        numHours = 0

        for bananas in piles:
            remainder = bananas % speed

            if remainder > 0:
                numHours += (bananas // speed) + 1
            else:
                numHours += bananas / speed
        
        return numHours

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)

        while low < high:
            mid = (low + high) // 2

            if self.numHoursToEat(piles, mid) <= h:
                high = mid
            else:
                low = mid + 1
        
        return low
