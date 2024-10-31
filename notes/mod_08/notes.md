### 10/28/2024
* Keys --Hash Function--> idx of bucket in hash table
* Hash table: array of m locations (called buckets)
* Mapping ADT:
    * put(key, value): add key, value pair
    * get(key): return value, raise KeyError if key is not present
* Mod hash value to fit in size of hash table: hash(x) % len(hash_table)
* Hash collision: when hash(x) % len(hash_table) is the same for different values
    * h(x1) = H(x2), and x1 != x2
* Open addressing (closed hashing): look for next available bucket
    * Linear probing: looking linearly for next bucket
    * Quadratic probing: skipping more buckets to find next available
    * Double hashing: using 2 hash functions to avoid collisions
* Separate chaining
    * Store all colliding keys in same bucket (points to list of entries)
    * Then do linear time search on list of entries in bucket
    * On average, constant time (assumes small # of entries in each bucket)
    * O(n) if all items in the same bucket, have to check if key is in bucket linked list, then append
    * Store as linked list
* Reshashing: support O(1) regardless of n
    * bucket_idx = hash(key) % m
    * rehash when n gets too big/small
    * Create list with p buckets, rehash every key
    * O(n) cost of rehashing, still O(1) average cost
    * Lazy rehashing: only rehash when threshold reached 
    * load factor = # elements / # buckets, 75%
