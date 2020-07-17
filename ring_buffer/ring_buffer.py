class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.insert_index = 0
        self.storage = []

    def append(self, item):
        if len(self.storage) == self.capacity:
            self.storage[self.insert_index] = item
            if self.insert_index + 1 == self.capacity:
                self.insert_index = 0
            else:
                self.insert_index += 1
        else:
            self.storage.append(item)

    def get(self):
        return self.storage
