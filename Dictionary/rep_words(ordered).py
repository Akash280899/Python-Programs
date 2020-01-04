#repeated words and its occurences
from collections import OrderedDict
words = OrderedDict()
for _ in range(int(input())):
    word = input()
    words.setdefault(word, 0)+1
    #words[word] += 1
   
print(len(words))
print(*words.values())
