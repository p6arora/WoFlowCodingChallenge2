#!/usr/bin/env python3
"""
Challenge for WoFlow

This function takes in a starting node, makes a tally of which node-id it has seen, and then looks at the child node. 
It then takes a GET request for the child node and adds their children to the visited list as well. We keep iterating 
until we have looked at all the nodes
"""

__author__ = "Paarth Arora"


import requests
import collections

def main():
    """ Main entry point of the app """

    # keep track of all nodes visited
    visited = {}

    # we import a queue to take into account which child nodes we have to iterate for
    queue = collections.deque()

    # Starting node given in assignment
    starting_node = "089ef556-dfff-4ff2-9733-654645be56fe"

    # starting url given in assignment
    starting_url = "https://nodes-on-nodes-challenge.herokuapp.com/nodes/"

    # append to queue the initial starting node
    queue.append(starting_node)

    # keep executing until the queue is empty
    while len(queue) != 0:

        # remove the first element from the start of the queue
        n = queue.popleft()

        # create the final URL 
        url = starting_url + n

        # does the GET request
        r = requests.get(url)

        # stores the results in JSON
        data = r.json()

        # get name of id 
        id = data[0]["id"]

        # increment our visited counter
        if id not in visited:
            visited[id] = 1
        else:
            visited[id] += 1

        # get child ids
        child_ids = data[0]["child_node_ids"]

        # iterate over each child node and add to queue
        for c in child_ids:
            queue.append(c)


    # iterate over visited dictionary and see what was max
    most_common_node = ""
    max_hits = 0

    for i, (k, v) in enumerate(visited.items()):
        # check for each key what node had the most counts
        if v > max_hits:
            max_hits = v
            most_common_node = k

    # print out results
    print("Most Common Node: " + most_common_node)
    print("Number of Unique keys: " +  str(len(visited)))    


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()