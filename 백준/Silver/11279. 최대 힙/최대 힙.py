import sys
import heapq

input = sys.stdin.read
data = list(map(int, input().split()))

N = data[0]
operations = data[1:]

heap = []
output = []

for x in operations:
    if x == 0:
        if heap:
            output.append(-heapq.heappop(heap))
        else:
            output.append(0)
    else:
        heapq.heappush(heap, -x)

print('\n'.join(map(str, output)))