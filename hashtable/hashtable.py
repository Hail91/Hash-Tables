class HashTableEntry:
    """
    Hash Table entry, as a linked list node.
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity

    def fnv1(self, key):
        """
        FNV-1 64-bit hash function

        Implement this, and/or DJB2.
        """
        # offset_basis
        hash_value = 14695981039346656037
        # Each octet of data to be hashed
        for x in key:
            hash_value = hash_value * 1099511628211 # FNV prime
            hash_value = hash_value ^ ord(x)
        return hash_value


    # def djb2(self, key):
        """
        DJB2 32-bit hash function

        Implement this, and/or FNV-1.
        """

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.fnv1(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # value_location = self.hash_index(key)
        # self.storage[value_location] = value

        # Get index of hashtable to store LL node
        index = self.hash_index(key)
        # Get current index of our hashtable and create a spot for a LL node
        node = self.storage[index]
        # Create a new LL node and assign to new_node variable
        new_node = HashTableEntry(key, value)
        # 0 ---> (key, value) --> (key1, value1)
        # If node does not exist, then create one
        if node is not None:
            prev = None
        # While There is a next node and the keys are not the same
            while node is not None:
                if node.key == key:
                    node.value = value
                    return
                # Assign current node to prev
                prev = node
                # Assign next node to current node
                node = node.next
                # ^ This is just stepping through the linked list nodes
            prev.next = new_node
        else:
            self.storage[index] = new_node

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)
        node = self.storage[index]

        prev = None
        while node is not None and node.key != key:
            prev = node
            node = node.next
        if node is None:
            print('Warning, key not found!')
        else:
            if prev is None:
                self.storage[index] = node.next
            else:
                prev.next = node.next

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)
        node = self.storage[index]

        while node is not None:
            if node.key == key:
                return node.value
            else:
                node = node.next
        return None



    def resize(self):
        """
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Implement this.
        """

if __name__ == "__main__":
    ht = HashTable(2)

    ht.put("line_1", "Tiny hash table")
    ht.put("line_2", "Filled beyond capacity")
    ht.put("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    print("")

