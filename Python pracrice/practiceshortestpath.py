#        python D:\Pythonpractice\practice.py


import heapq as hp
import math

graph = {
	"A": {"B": 5, "C": 1},
	"B": {"A": 5, "C": 2, "D": 1},
	"C": {"A": 1, "B": 2, "D": 4, "E": 8},
	"D": {"B": 1, "C": 4, "E": 3, "F": 6},
	"E": {"C": 8, "D": 3},
	"F": {"D": 6}
}


def init_distance(graph ,start):
	distance = {start: 0}
	for vertex in graph:
		if vertex != start:
			distance[vertex] = math.inf
	return distance



def dijkstra(graph, start):
	#initialization
	pqueue = []
	parents = {start: 'none'}
	distance = init_distance(graph, start) 
	hp.heappush(pqueue, (0, start))
	seen = []
	seen.append(start)
	# poping the first step from the priority queue
	while len(pqueue) != 0:
		nextstepvalues = hp.heappop(pqueue)
		stepdistance = nextstepvalues[0]
		step = nextstepvalues[1]
		seen.append(step)
		potentialsteps = graph[step].keys()
		for vertex in potentialsteps:
			if vertex not in seen:
				shortdistance = distance[step] + graph[step][vertex]
				hp.heappush(pqueue, (shortdistance, vertex))
				if shortdistance < distance[vertex]:
					distance [vertex] = shortdistance
					parents[vertex] = step
	return parents, distance



def dijkstrahelper(graph, start, end):
	parent, distance = dijkstra(graph, start)
	path = []
	path.append(end)
	nextstep = parent[end]
	while nextstep != start:
		path.append(nextstep)
		nextstep = parent[nextstep]
	path.append(start)
	path = path[::-1]
	final = distance[end]
	return path, final


path, final = dijkstrahelper(graph, "A", "F")
parents, distance = dijkstra(graph, "A")
print(parents)
print(distance)
print(path)
print(final)





