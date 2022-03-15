class MyHashMap:
    ## Using a straight list of size 10 ^ 6
    ## Very expensive on space as many spaces will be bank
    ## get: O(1)
    ## put: O(1)
    ## delete: O(1)

    def __init__(self):
        self.giant_list = [None for _ in range(1000001)]

    def put(self, key, value):
        self.giant_list[key] = value
      
    def get(self, key):
        return self.giant_list[key] if self.giant_list[key]!= None else -1

    def remove(self, key):
        if self.giant_list[key]:
            self.giant_list[key] = None 
