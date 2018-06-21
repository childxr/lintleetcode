import Queue

class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: true if can finish all courses or false
    """
    def canFinish(self, numCourses, prerequisites):
        # write your code here
        if numCourses <= 0 or not prerequisites:
            return True
        
        graph = [[] for j in xrange(numCourses)]
        degrees = [0 for i in xrange(numCourses)]
        
        for prerequisite in prerequisites:
            pre_course = prerequisite[-1]
            cur_course = prerequisite[0]
            graph[pre_course].append(cur_course)
            degrees[cur_course] += 1

        queue = Queue.Queue()
        for i in xrange(numCourses):
            if degrees[i] == 0:
                queue.put(i)
        cnt = 0
        while not queue.empty():
            cur = queue.get()
            cnt += 1
            for course in graph[cur]:
                degrees[course] -= 1
                if degrees[course] == 0:
                    queue.put(course)

        return cnt == numCourses
                
        
                

