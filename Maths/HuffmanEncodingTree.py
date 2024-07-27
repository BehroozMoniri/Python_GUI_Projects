from heapq import heapify, heappop, heappush
## Huffman tried to build the tree from the bottom up rather top-down as Shannon-Fano coding 
class Node:
    def __init__(self, ch, freq, left=None, right=None):
        self.ch, self.freq = ch, freq
        self.left , self.right = left, right
        def __lt__(self, other):
            return self.freq < other.freq
        
    def getHuffmanTree(self, text):
        if len(text) ==0:
            return
        freq = {ch: text.count(ch) for ch in set(text)}
        pq = [Node(k,v) for k,v in freq.items()]
        heapify(pq)
        while len(pq) > 1:
            left, right = heappop(pq), heappop(pq)
            newFreq = left.freq + right.freq
            heappush(pq, Node(None, newFreq, left, right))
        root = pq[0]
        return root