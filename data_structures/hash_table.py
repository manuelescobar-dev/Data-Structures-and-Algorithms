class HashTable:
    def __init__(self, size):
        self.data = [None] * size

    def _hash(self, key):
        hash = 0
        for i in range(len(key)):
            hash = (hash + ord(key[i]) * i) % len(self.data)
        return hash

    def set(self, key, value):
        bucket = [key, value]
        hash = self._hash(key)
        if self.data[hash] is None:
            self.data[hash] = []
        self.data[hash].append(bucket)
        return hash

    def get(self, key):
        hash = self._hash(key)
        result = self.data[hash]
        if result is None:
            return "Not Found"
        else:
            # If no collision -> O(1)
            for i in result:
                if i[0] == key:
                    return i

    def keys(self):
        k = []
        for i in self.data:
            # If no collision -> O(1)
            if i is not None:
                for j in i:
                    k.append(j[0])
        return k
