# "This time, instead of returning a boolean, I need to return all valid root-to-leaf paths.
# So I use DFS with backtracking. I keep track of the current path and the remaining sum.
# When I reach a leaf node and the remaining sum matches the node value, I add a copy of the current path to the result.
# After exploring each branch, I backtrack by removing the current node from the path."

