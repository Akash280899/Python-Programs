#avg of marks
from collections import namedtuple
n, item = int(input()), input().split().index("MARKS")
print ("{0:.2f}".format(sum([int(input().split()[item]) for i in range(n)]) / n))
