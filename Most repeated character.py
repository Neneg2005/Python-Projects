
from pprint import pprint
sentence = "Find the most repeated character in this string"

char = {}
for ch in sentence:
    if ch in char:
        char[ch] += 1
    else:
        char[ch] = 1

#pprint(char, width=1)

#Dictionaries are unordered. We sort out these values by converting each key-value pair into tuples
#These tuples are put into lists and sorted 

char_sorted = sorted(char.items(), key=lambda kv:kv[1], reverse=True)
print(char_sorted[1])



