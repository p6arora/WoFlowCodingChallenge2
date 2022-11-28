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

    # make sure we don't go over the same node as it runs the same results
    seen = set()

    # we import a queue to take into account which child nodes we have to iterate for
    queue = collections.deque()

    # Starting node given in assignment
    starting_node = "089ef556-dfff-4ff2-9733-654645be56fe"

    # starting url given in assignment
    starting_url = "https://nodes-on-nodes-challenge.herokuapp.com/nodes/"

    # append to queue the initial starting node
    queue.append(starting_node)


    visited[starting_node] = 1

    # use a set to keep track of nodes already visited
    seen.add(starting_node)

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

        # get child ids
        child_ids = data[0]["child_node_ids"]

        # iterate over each child node and add to queue
        for c in child_ids:

            # if child has not been before - add to seen list so we don't add to queue again
            if c not in seen:
                queue.append(c)
                visited[c] = 1
                seen.add(c)
                
            # if child has been seen before - no need to execute that API call again - add to seen 
            else:
                visited[c] += 1

            




    # iterate over visited dictionary and see what was max
    most_common_node = max(visited, key=visited.get)


    # print out results
    print("Most Common Node: " + most_common_node)
    print("Number of Unique keys: " +  str(len(visited)))    


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()