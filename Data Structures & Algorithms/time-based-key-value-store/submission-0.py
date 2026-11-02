class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:

        if key in self.store:
            self.store[key].append([timestamp, value])
        else:
            self.store[key] = [[timestamp, value]]
        

    def get(self, key: str, timestamp: int) -> str:

        if key not in self.store:
            return ""
        
        need = self.store[key]

        l = 0
        r = len(need) - 1

        res = ""
        while l <= r:

            mid = (l+r) // 2

            if need[mid][0] == timestamp:

                return need[mid][1]

            elif need[mid][0] < timestamp:
                
                res = need[mid][1]
                l = mid + 1
            else:
                r = mid - 1
        
        return res
            
            

            
        
