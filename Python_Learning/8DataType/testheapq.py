__author__ = 'Raychang'
import heapq

import heapq
heap = []
heapq.heappush(heap, 1)
heapq.heappush(heap, 2)
print heap

l1 = [2,1,33,23,7,5,6,9]
heapq.heapify(l1)
print l1
print type(l1)
