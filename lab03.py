# -*- coding: utf-8 -*-
"""Lab03.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1usKl4Kcmkv8DybrSacipMtLnOtNapLIs
"""

import time
from util import Stack, Queue, PriorityQueue

class SearchProblem:
    def getStartState(self):
        util.raiseNotDefined()

    def isGoalState(self, state):
        util.raiseNotDefined()

    def getSuccessors(self, state):
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        util.raiseNotDefined()

# Timer wrapper function
def TimeAlgorithm(algorithm, problem):
    start_time = time.perf_counter_ns()
    result = algorithm(problem)
    end_time = time.perf_counter_ns()
    elapsed_time = (end_time - start_time) / 1e9
    print(f"Execution Time: {elapsed_time:.8f} seconds")
    return result

def DepthFirstSearch(problem):
    def dfs(problem):
        stack = Stack()
        stack.push((problem.getStartState(), []))
        visited = set()

        while not stack.isEmpty():
            state, path = stack.pop()
            if state in visited:
                continue
            visited.add(state)

            if problem.isGoalState(state):
                return path

            for successor, action, _ in problem.getSuccessors(state):
                if successor not in visited:
                    stack.push((successor, path + [action]))

        return []

    return TimeAlgorithm(dfs, problem)

def BreathFirstSearch(problem):
    def bfs(problem):
        queue = Queue()
        queue.push((problem.getStartState(), []))
        visited = set()

        while not queue.isEmpty():
            state, path = queue.pop()
            if state in visited:
                continue
            visited.add(state)

            if problem.isGoalState(state):
                return path

            for successor, action, _ in problem.getSuccessors(state):
                if successor not in visited:
                    queue.push((successor, path + [action]))

        return []

    return TimeAlgorithm(bfs, problem)

def UniformCostSearch(problem):
    def ucs(problem):
        pq = PriorityQueue()
        pq.push((problem.getStartState(), [], 0), 0)
        visited = {}

        while not pq.isEmpty():
            state, path, cost = pq.pop()
            if state in visited and visited[state] <= cost:
                continue
            visited[state] = cost

            if problem.isGoalState(state):
                return path

            for successor, action, step_cost in problem.getSuccessors(state):
                new_cost = cost + step_cost
                if successor not in visited or new_cost < visited.get(successor, float('inf')):
                    pq.push((successor, path + [action], new_cost), new_cost)

        return []

    return TimeAlgorithm(ucs, problem)