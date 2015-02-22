def new(num_buckets=256):
	aMap = []
	for i in range(0, num_buckets):
	    aMap.append([])
	return aMap

def hash_key(aMap, key):
    return hash(key) % len(aMap)
