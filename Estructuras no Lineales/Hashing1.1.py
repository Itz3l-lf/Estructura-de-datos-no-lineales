from collections import Counter
a = ['apple', 'banana', 'apple', 'orange', 'banana', 'banana']
freq = Counter(a)
print(dict(freq))