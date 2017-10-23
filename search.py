# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util
import searchAgents as sa


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"

    # util.raiseNotDefined()
    #print "Enter depthFirstSearch..."
    #print "Start:", problem.getStartState()
    #print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    #print "Start's successors:", problem.getSuccessors(problem.getStartState())
    #print problem

    stack = util.Stack()
    # parent_node = problem.getStartState()
    #node = problem.getStartState()
    visited_node = []
    stack.push((problem.getStartState(), [], 0))
    while not stack.isEmpty():
        node, actions, costs = stack.pop()
        visited_node.append(node)
        if problem.isGoalState(node):
            break
        childNodes = problem.getSuccessors(node)
        for Next_node, action, cost in childNodes:
            if Next_node not in visited_node:
                stack.push((Next_node, actions + [action], costs + cost))

    print "here are the visited node", visited_node
    return actions


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    # util.raiseNotDefined()

    # print "Enter breadthFirstSearch..."
    # print "Start:", problem.getStartState()
    # print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    # print "Start's successors:", problem.getSuccessors(problem.getStartState())

    queue = util.Queue()
    # parent_node = problem.getStartState()
    # node = problem.getStartState()
    visited_node = [problem.getStartState()]
    queue.push((problem.getStartState(), [], 0))
    while not queue.isEmpty():
        node, actions, costs = queue.pop()

        if problem.isGoalState(node):
            return actions
        childNodes = problem.getSuccessors(node)
        for Next_node, action, cost in childNodes:
            if Next_node not in visited_node and Next_node not in node:
                queue.push((Next_node, actions + [action], costs + cost))
                visited_node.append(Next_node)
    print "here are the visited node", visited_node
    return actions




def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    # util.raiseNotDefined()

    # print "Enter Uniform Cost Search..."
    # print "Start:", problem.getStartState()
    # print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    # print "Start's successors:", problem.getSuccessors(problem.getStartState())

    pq = util.PriorityQueue()
    parent_node = problem.getStartState()
    pq.push((parent_node, [], 0), 0)
    visited_node = list()
    while not pq.isEmpty():
        node, actions, costs = pq.pop()
        # print "here is the popped item", ": ", node, "and its cost is ", costs
        if problem.isGoalState(node):
            break
        if node not in visited_node:
            visited_node.append(node)
            childNodes = problem.getSuccessors(node)
            for Next_node, action, cost in childNodes:
                #total_cost = costs + cost
                if Next_node not in (visited_node or pq):
                    total_cost = problem.getCostOfActions(actions + [action])
                    pq.push((Next_node, actions + [action], total_cost), total_cost)
                    #visited_node.append(Next_node)
                    # print "____Added Node_____", Next_node, " and its cost is: ", total_cost

    return actions


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    # print "A* Search..."
    # print "Start:", problem.getStartState()
    # print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    # print "Start's successors:", problem.getSuccessors(problem.getStartState())

    pq = util.PriorityQueue()
    parent_node = problem.getStartState()
    pq.push((parent_node, [], 0), 0)
    visited_node = list()
    while not pq.isEmpty():
        node, actions, costs = pq.pop()
        # print "here is the popped item", ": ", node, "and its cost is ", costs
        if problem.isGoalState(node):
            break
        if node not in visited_node:
            visited_node.append(node)
            childNodes = problem.getSuccessors(node)
            for Next_node, action, cost in childNodes:
                # total_cost = costs + cost
                if Next_node not in (visited_node or pq):
                    total_cost = problem.getCostOfActions(actions + [action])
                    pq.push((Next_node, actions + [action], total_cost), total_cost + heuristic(Next_node, problem))
                    # visited_node.append(Next_node)
                    # print "____Added Node_____", Next_node, " and its cost is: ", total_cost

    return actions


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
