sample_dict = {"name": "Chris", "city": "Seattle", "cake": "Chocolate"}

del sample_dict['cake']

print sample_dict

sample_dict['fruit'] = "Mango"

print sample_dict

print sample_dict.keys()
print sample_dict.values()

print 'cake' in sample_dict.keys()
print 'Mango' in sample_dict.values()

nums = list(range(0,15))
hexidecimal = [0,1,2,3,4,5,6,7,8,9,"A","B","C","D","E","F"]

print dict(zip(nums, hexidecimal))

for key in sample_dict.keys():
	value = sample_dict[key].count('t')
	sample_dict[key] = value
    
s2 = set([i for i in range(1,21) if i % 2 == 0])
s3 = set([i for i in range(1,21) if i % 3 == 0])
s4 = set([i for i in range(1,21) if i % 4 == 0])

print s3.issubset(s2)
print s4.issubset(s2)

python_set = set("Python")
python_set.add("i")

marathon_set = frozenset("marathon")
python_set.union(marathon_set)
python_set.intersection(marathon_set)
