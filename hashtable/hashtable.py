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
        self.entry_count = 0

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

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.fnv1(key) % self.capacity

    def load_factor(self):
        return self.entry_count / self.capacity

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
        # If node exists, set prev to None
        if node is not None:
            prev = None
        # While Node is true, check that node's key and compare to key we're looking for, if they match, overwrite the current value with new value
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
            self.entry_count += 1
            # After we add item, we need to check the load count and resize depending on result
            if self.load_factor() > 0.7:
                self.resize()
        # If Node does not exist, generate a new LL node and insert into the hashtable
        else:
            self.storage[index] = new_node
        self.entry_count += 1
        # After we add item, we need to check the load count and resize depending on result
        if self.load_factor() > 0.7:
            self.resize()

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)
        node = self.storage[index]
        prev = None
        load_factor = self.entry_count / len(self.storage)
        # While node exists and keys do not match, step through the LL
        while node is not None and node.key != key:
            prev = node
            node = node.next
        # If node does not exist, let them know that key was not found
        if node is None:
            print('Warning, key not found!')
        # Otherwise, if node exists with no other conditions required...
        else:
            if prev is None:
                self.storage[index] = node.next
            else:
                prev.next = node.next
        self.entry_count -= 1

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



    def resize(self, new_capacity):
        """
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Implement this.
        """
        # Need logic here to double the size of the hashtable and rehash the elements to the new table
        # Get old hashtable
        old_hash_table = self.storage
        # Define new hashtable capacity
        # self.capacity = self.capacity * 2
        # Generate a new hashtable with the updated capacity
        new_hash_table = [None] * new_capacity
        # Assign that new hashtable to storage
        self.storage = new_hash_table
        # Loop over the old hash table checking for values, if they exist....rehash and add them back in.
        for v in old_hash_table:
            if v is not None:
                while v:
                    self.put(v.key, v.value)
                    v = v.next

if __name__ == "__main__":
    ht = HashTable(2)

    ht.put("line_1", "Tiny hash table")
    print(ht.capacity)
    ht.put("line_2", "Filled beyond capacity")
    print(ht.capacity)
    ht.put("line_3", "Linked list saves the day!")
    print(ht.capacity)

    print("")

    # Test storing beyond capacity
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    print(old_capacity)
    ht.resize()
    new_capacity = len(ht.storage)
    print(new_capacity)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    print("")

