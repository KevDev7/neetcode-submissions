class Solution:
    def canFinish(self, numCourses, prerequisites):
        # Build a map where: preMap[course] = list of courses that must be completed first
        preMap = {course: [] for course in range(numCourses)}
        for course, prerequisite in prerequisites:
            preMap[course].append(prerequisite)

        # Stores only the courses in the CURRENT DFS path.
        # It is used to detect whether the path loops back to a course
        # we are already trying to complete.
        current_path = set()

        def dfs(course):
            # If this course is already in the current path, the prerequisite chain has formed a cycle.
            # EX: 0 requires 1, 1 requires 2, and 2 requires 0
            if course in current_path:
                return False

            # An empty prerequisite list means either: The course never had prerequisites, or we already checked this course before and proved it is safe.
            if preMap[course] == []:
                return True

            # Add this course to the current path before checking all of the courses it depends on.
            current_path.add(course)

            # Recursively check every prerequisite for this course.
            for prerequisite in preMap[course]:
                # If any prerequisite leads to a cycle, this course cannot be completed either.
                if not dfs(prerequisite):
                    return False

            # We finished checking this course without finding a cycle, so remove it from the current path.
            current_path.remove(course)

            # Mark this course as already proven safe. Future DFS calls can immediately return True for it.
            preMap[course] = []

            return True

        # Start DFS from every course because the graph may contain separate, disconnected groups of courses.
        for course in range(numCourses):
            if not dfs(course):
                return False

        # Every course was checked without finding a cycle.
        return True