def heapsort(arr):
    heap_of_items = Heap()
    for x in arr:
        heap_of_items.insert(x)
    returning = []
    
    while len(heap_of_items.storage) > 0:
        returning.append(heap_of_items.delete())
        
    
    returning.reverse()
    print(returning)
    #pretty dumb to have a heap max  return a sorted array
    # from lowest to biggest. 
    return returning
 

class Heap:
  def __init__(self):
    self.storage = []
    self.size = 0 
    
  def insert(self, value):
    self.storage.append(value)
    self._bubble_up(len(self.storage) - 1)
    self.size += 1 

  def delete(self):
    retval = self.storage[0]
    self.storage[0] = self.storage[len(self.storage) - 1]
    self.storage.pop()
    self._sift_down(0)
    self.size -= 1 
    return retval 

  def get_max(self):
    return self.storage[0]

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index):
    while (index - 1) // 2 >= 0:
      if self.storage[(index - 1) // 2] < self.storage[index]:
        self.storage[index], self.storage[(index - 1) // 2] = self.storage[(index - 1) // 2], self.storage[index]
      index = (index - 1) // 2

  def _sift_down(self, index):
    while index * 2 + 1 <= len(self.storage) - 1:
      mc = self._max_child(index)
      if self.storage[index] < self.storage[mc]:
        self.storage[index], self.storage[mc] = self.storage[mc], self.storage[index]
      index = mc

  def _max_child(self, index):
    if index * 2 + 2 > len(self.storage) - 1:
      return index * 2 + 1
    else:
      return index * 2 + 1 if self.storage[index * 2 + 1] > self.storage[index * 2 + 2] else index * 2 + 2