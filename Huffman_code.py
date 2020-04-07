'''f:0
c:100
d:101
a:1100
b:1101
e:111'''


from heapq import heappush,heappop
class HuffmanItem:
    def __init__(self, frequency, letter, left_son, right_son):
        self.freq = frequency
        self.alpha = letter
        self.left = left_son
        self.right = right_son
    def __lt__(self, other):
        return self.freq < other.freq
def print_codes(tree, str_collector):
    if tree is None:
        return
    if tree.alpha != '$':
        print("{}:{}".format(tree.alpha,str_collector))
    print_codes(tree.left, str_collector + '0')
    print_codes(tree.right, str_collector + '1')
if __name__ == '__main__':
    t = 1
    for _ in range(t):
        alpha = ['a','b','c','d','e','f']
        freq = [5,9,12,13,16,45]
        pq = []  
        for i in range(len(alpha)):
            heappush(pq, HuffmanItem(freq[i], alpha[i], None, None))
        while len(pq) != 1:
            left = heappop(pq)
            right = heappop(pq)
            top = HuffmanItem(left.freq + right.freq, '$', left, right)
            heappush(pq, top)
        print_codes(heappop(pq), "")
        print()

