class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [ -c for c in count.values()]
        heapq.heapify(maxHeap)
        queue = deque()
        time = 0
        while maxHeap or queue:
            time += 1
            if maxHeap:
                node = 1 + heapq.heappop(maxHeap)
                if node:
                    queue.append([node, time + n])
            if queue:
                if queue[0][1] == time:
                    node, t = queue.popleft()
                    heapq.heappush(maxHeap, node)
        return time