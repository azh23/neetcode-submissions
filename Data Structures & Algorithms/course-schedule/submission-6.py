class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True
        empty = []
        bToA = dict()
        aToB = dict()

        for pr in prerequisites:
            if pr[1] not in bToA:
                bToA[pr[1]] = set()
            bToA[pr[1]].add(pr[0])

            if pr[0] not in aToB:
                aToB[pr[0]] = set()
            aToB[pr[0]].add(pr[1])


        for a in aToB.keys():
            if a not in bToA:
                empty.append(a)

        print(empty, aToB, bToA)

        if len(empty) == 0:
            return False

        while empty:
            curr_course = empty.pop()

            if curr_course not in aToB:
                continue
            for next_course in aToB[curr_course]:
                bToA[next_course].remove(curr_course)
                if not bToA[next_course]:
                    bToA.pop(next_course, None)
                    empty.append(next_course)
            
        return len(bToA) == 0

"""
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)   # prereq -> courses that need it
        in_degree = [0] * numCourses

        for course, prereq in prerequisites:
            graph[prereq].append(course)
            in_degree[course] += 1

        queue = deque([c for c in range(numCourses) if in_degree[c] == 0])
        visited = 0

        while queue:
            curr = queue.popleft()
            visited += 1
            for next_course in graph[curr]:
                in_degree[next_course] -= 1
                if in_degree[next_course] == 0:
                    queue.append(next_course)

        return visited == numCourses
"""

        
