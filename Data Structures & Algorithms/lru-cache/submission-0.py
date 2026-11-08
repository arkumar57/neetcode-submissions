class LRUCache:

    def __init__(self, capacity: int):


        self.capacity = capacity
        self.mycache = OrderedDict()
        

    def get(self, key: int) -> int:

        if key in self.mycache:

            self.mycache.move_to_end(key)
            return self.mycache[key]
        
        else:

            return -1


        

    def put(self, key: int, value: int) -> None:

        if key in self.mycache:
            
            self.mycache.move_to_end(key)

        self.mycache[key] = value

        if len(self.mycache) > self.capacity:

            self.mycache.popitem(last = False)


        
        
