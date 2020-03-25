from doubly_linked_list import DoublyLinkedList
import sys
sys.path.append('./doubly_linked_list.py')

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.limit = limit
        self.order = DoublyLinkedList()
        self.storage_dict = dict()
        self.size = 0

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        if key in self.storage_dict:
            node = self.storage_dict[key]
            self.order.move_to_end(node)
            return node.value[1]
        else:
            return None

    def get_guided(self, key):
        # key is not in cache - return none
        if key not in self.storage_dict:
            return None
        # key is in cache
        else:
            # move it to most recently used
            node = self.storage_dict[key]
            self.order.move_to_end(node)
            # return value 
            return node.value[1]

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        # if key is already in cache
        if key in self.storage_dict:
            node = self.storage_dict[key]
            node.value = (key, value)
            self.order.move_to_end(node)
            return 
        # size is at limit
        if self.size == self.limit:
            del self.storage_dict[self.order.head.value[0]]
            self.order.remove_from_head()
            self.size -= 1
        # size is not at limit
        self.order.add_to_tail((key, value))
        self.storage_dict[key] = self.order.tail
        self.size += 1


    def set_guided(self, key, value):
        # if key/item already exists
        if key in self.storage_dict:
            # overwrite the value
            # where is the value stored
            node = self.storage_dict[key]
            node.value = (key, value)
            # move to the tail (most recently used)
            self.order.move_to_end(node)
            return
        # if size is at limit
        if len(self.order) == self.limit:
            # delete the oldest one 
            # remove from list and storage_dict
            del self.storage_dict[self.order.head.value[0]]
            self.order.remove_from_head()
            # add new one to the end

        # size is not at limit
        # add to order
        self.order.add_to_tail((key, value))
        # add it to storage
        self.storage_dict[key] = self.order.tail




