from collections import namedtuple
n,arrangement = int(input()),input()
Student = namedtuple('Student',arrangement)
print(sum( [int(Student._make(input().split()).MARKS) for _ in range(n)])/n)
