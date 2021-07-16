from linked_list import LinkedList

# hash & modulo to get bucket index
# each bucket is a linkedlist
# collisions - when too many size exceeds load factor occur we need to resize the hashtable
# when resizing, you are guarenteed a new bucket index and an even lower chance of further collisions (because amount of buckets changes)

class Dictionary:
    def __init__(self, init_size=8):
        self.buckets = [LinkedList() for i in range(init_size)]
        self.size = 0

    def __bool__(self):
        return self.size > 0

    # def __delete__(self, key):
    #     # self.delete(key)
    #     pass

    def __iter__(self):
        for key in self.keys():
            yield key
    
    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):
        return self.contains(key)
    
    def get_size(self):
        return self.size
    
    def items(self):
        all_items = []

        for bucket in self.buckets:
            items = bucket.items()
            all_items.extend(items)
        
        return all_items
    
    def bucket_index(self, key):
        return hash(key) % len(self.buckets)
    
    def load_factor(self):
        return (self.size / len(self.buckets))
    
    def keys(self):
        all_keys = []

        for bucket in self.buckets:
            for key, _ in bucket.items():
                all_keys.append(key)
        
        return all_keys
    
    def vals(self):
        all_vals = []

        for bucket in self.buckets:
            for _, val in bucket.items():
                all_vals.append(val)
        
        return all_vals
    
    def contains(self, key):
        index = self.bucket_index(key)
        bucket = self.buckets[index]

        entry = bucket.find(lambda key_val: key_val[0] == key)
        return entry is not None
    
    def get(self, key):
        index = self.bucket_index(key)
        bucket = self.buckets[index]

        entry = bucket.find(lambda key_val: key_val[0] == key)

        print(entry)

        return entry[1] if entry is not None else None
    
    def insert_or_update(self, key, val):
        index = self.bucket_index(key)
        bucket = self.buckets[index]
        entry = bucket.find(lambda key_val: key_val[0] == key)

        # if a key has a val, update
        if entry:
            bucket.delete(entry)
            self.size -= 1
        
        # add updated or new key, val pair
        bucket.append((key, val))
        self.size += 1

        # check for load factor
        if self.load_factor() > 0.75:
            self.resize()
    
    def delete(self, key):
        index = self.bucket_index(key)
        bucket = self.buckets[index]
        entry = bucket.find(lambda key_val: key_val[0] == key)

        if entry:
            bucket.delete(entry)
            self.size -= 1
    
    def resize(self, new_size=None):
        if new_size is None:
            new_size = len(self.buckets) * 2

        temp = self.items()

        self.__init__(new_size)

        for key, val in temp:
            self.insert_or_update(key, val)

def test_hash_table():
    ht = Dictionary(4)
    print('HashTable: ' + str(ht))

    print('Setting entries:')
    ht.insert_or_update('I', 1)
    print('insert_or_update(I, 1): ' + str(ht))
    ht.insert_or_update('V', 5)
    print('insert_or_update(V, 5): ' + str(ht))
    print('size: ' + str(ht.size))
    print('size: ' + str(ht.get_size()))
    print('buckets: ' + str(len(ht.buckets)))
    print('load_factor: ' + str(ht.load_factor()))
    ht.insert_or_update('X', 10)
    print('insert_or_update(X, 10): ' + str(ht))
    ht.insert_or_update('L', 50)  # Should trigger resize
    print('insert_or_update(L, 50): ' + str(ht))
    print('size: ' + str(ht.size))
    print('size: ' + str(ht.get_size()))
    print('buckets: ' + str(len(ht.buckets)))
    print('load_factor: ' + str(ht.load_factor()))

    print('Getting entries:')
    print('get(I): ' + str(ht.get('I')))
    print('get(V): ' + str(ht.get('V')))
    print('get(X): ' + str(ht.get('X')))
    print('get(L): ' + str(ht.get('L')))
    print('contains(X): ' + str(ht.contains('X')))

    print("TEST X", "X" in ht)
    print("TEST GET ITEMS DUNDER", ht["X"])
    print("TEST ITER", [i for i in ht])
    print("")

    print('Deleting entries:')
    ht.delete('I')
    print('delete(I): ' + str(ht))
    ht.delete('V')
    print('delete(V): ' + str(ht))
    # ht.delete('X')
    # print('delete(X): ' + str(ht))
    # ht.delete('L')
    print('TEST del X: ' + str(ht))
    del ht.size
    print(ht.size)

    print('delete(L): ' + str(ht))
    print('contains(X): ' + str(ht.contains('X')))
    print('size: ' + str(ht.size))
    print('size: ' + str(ht.get_size()))
    print('buckets: ' + str(len(ht.buckets)))
    print('load_factor: ' + str(ht.load_factor()))


if __name__ == '__main__':
    test_hash_table()

