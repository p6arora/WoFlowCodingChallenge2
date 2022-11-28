#!/usr/bin/env python3
"""
Module Docstring
"""

__author__ = "Paarth Arora"


import requests
import collections

def main():
    """ Main entry point of the app """

    # keep track of all nodes visited
    visited = {}
    queue = collections.deque()

    starting_node = "089ef556-dfff-4ff2-9733-654645be56fe"

    starting_url = "https://nodes-on-nodes-challenge.herokuapp.com/nodes/"

    #url = starting_url + starting_node

    queue.append(starting_node)

    while len(queue) != 0:

        n = queue.popleft()

        url = starting_url + n

        r = requests.get(url)

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
        if v > max_hits:
            max_hits = v
            most_common_node = k

    print("Most Common Node: " + most_common_node)
    print("Number of Unique keys: " +  str(len(visited)))    


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()