class Solution:
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        deadset = set(deadends)
        if '0000' in deadset:
            return -1
        import queue
        setps = 0
        q = queue.Queue()
        q.put('0000')
        visited = {'0000'}

        while not q.empty():
            setps += 1
            length = q.qsize()
            for _ in range(length):

                node = q.get()

                for i in range(4):
                    for j in (-1, 1):
                        slst = list(node)
                        slst[i] = str((int(slst[i]) + j) % 10)
                        tem = ''.join(slst)
                        if tem == target:
                            return setps
                        if tem not in visited and tem not in deadset:
                            q.put(tem)
                        visited.add(tem)

        return -1


deadends = ["0000"]
target = "8888"
s = Solution()

print(s.openLock(deadends, target))
