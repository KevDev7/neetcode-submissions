class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # turn list of pairs to dict adjacency list
        course_prerequisites = {}

        # fill dict key values with empty list
        for c in range(numCourses):
            course_prerequisites[c] = []

        # fill in all prerequisites to list value in dict
        for course, prerequisite in prerequisites:
            course_prerequisites[course].append(prerequisite)

        # set used to store seen nodes in current dfs path, will be reset
        current_path = set()

        def dfs(course):
            # recursion

            # Base Case: current node already seen, cycle found
            if course in current_path:
                return False
            
            # Base Case: current node has no prerequisites, no cycle found by end of dfs path
            if course_prerequisites[course] == []:
                return True

            # Current Node Check: add current course to dfs path
            current_path.add(course)

            # Recursive Step: recursively check each of node's prerequisites to find cycle
            for prerequisite_course in course_prerequisites[course]:
                if dfs(prerequisite_course) == False:
                    return False

            # no cycle found after finishing checking this course, remove from active DFS path
            current_path.remove(course)

            # mark course as proven safe (by pretending it has no prerequisites)
            course_prerequisites[course] = []

            return True


        # Loop thru each course, find its depth, if cycle found, exit dfs() and return false
        for course in range(numCourses):
            if dfs(course) == False:
                return False
        
        # Found no cycle after checking every node
        return True

