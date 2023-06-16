
class LinearSearch:
    def ___init__(self, arr, key):
        self.arr = arr
        self.key = key


    def search_elements(self, arr=None, key=None):

        if not arr:
            arr = self.arr
        
        if not key: 
            key=self.key
        
        index = -1
        
        for i  in range(0, len(arr)):
            elm = arr[i]
            if( key == elm):
                index = i 
                break
        
        return index