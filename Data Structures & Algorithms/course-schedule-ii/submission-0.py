class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        in_degree = [0] * numCourses

        for course, prereq in prerequisites:
            graph[prereq].append(course)
            in_degree[course] += 1

        queue = deque([c for c in range(numCourses) if in_degree[c] == 0])

        sched = []
        while queue:
            curr = queue.popleft()
            sched.append(curr)
            for next_course in graph[curr]:
                in_degree[next_course] -= 1
                if in_degree[next_course] == 0:
                    queue.append(next_course)
        print(sched)
        return sched if len(sched) == numCourses else []