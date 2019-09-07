import re

S = input() #string
k = input() #pattern

'''
re.compile(pattern, repl, string):

We can combine a regular expression pattern into pattern objects, which can be used for pattern matching. It also helps to search a pattern again without rewriting it.

'''
pattern = re.compile(k)
r = pattern.search(S)
#print(r)
if not r: 
    print("(-1, -1)")
while r:
    print("({0}, {1})".format(r.start(), r.end() - 1))
    r = pattern.search(S,r.start() + 1)



