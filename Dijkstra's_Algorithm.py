# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 21:11:59 2020

@author: Rui Sun
Reference: Grokking Algorithms: An illustrated guide for programmers and other curious people
Aditya Bhargava

Plus, I strongly recommend you to read this book!
"""

# find_lowest_cost_node
def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

# Create a graph by Using Hash Table
graph = {}
# Create more Hash Tables to describe the graph
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2

graph["a"] = {}
graph["a"]["fin"] = 1

graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5

graph["fin"] = {}
# Define Infinity
infinity = float("inf")

# Create Cost Table in start node by Using Hash Table
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity
# Create Parent Table in start node by Using Hash Table
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None
# Put Processed Nodes into it
processed = []

# Implement Dijkstra's Algorithm
node = find_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)
        
print(costs["fin"])   

# In summary, we need to create three hash tables to store graph infor
# including graph structure, costs or weights and parent nodes.