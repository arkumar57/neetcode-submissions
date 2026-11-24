class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l = 1

        r = max(piles)

        result = float('inf')

        while l <= r:

            mid = (l + r) // 2

            count = 0
            for i in range(len(piles)):
                
                if piles[i] % mid == 0:
                    count += piles[i] // mid
                else:
                    count += piles[i] // mid
                    count += 1
                # while piles[i] > 0:
                    
                #     print(piles[i])
                #     count += 1
                #     piles[i] -= mid

            if count > h:

                l = mid + 1

            else:

                r = mid - 1
                result = min(result, mid)
        
        return result

