import collections


class Employee:
    def __init__(self, id: int, importance: int, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates


class Solution:
    def getImportance(self, employees, id: int) -> int:
        m = dict()
        for employee in employees:
            m[employee.id] = employee
        num = 0
        queue = collections.deque()
        employee = m[id]
        for s in employee.subordinates:
            queue.append(s)
        num += employee.importance
        while len(queue) > 0:
            employee = m[queue.popleft()]
            for s in employee.subordinates:
                queue.append(s)
            num += employee.importance
        return num


class Solution2(object):
    def getImportance(self, employees, query_id):
        emap = {e.id: e for e in employees}

        def dfs(eid):
            employee = emap[eid]
            return (employee.importance +
                    sum(dfs(eid) for eid in employee.subordinates))

        return dfs(query_id)
