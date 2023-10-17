# Author: Jorge Nader
# Date: 09/30/2023
# Description: This program creates an agent that uses the A* algorithm to find the exit from a maze.

# Import necessary classes from pyamaze and heapq
from pyamaze import maze, agent, textLabel
import heapq  # Import heapq for a more efficient priority queue

# Define a heuristic function to estimate the distance between two cells
def h(cell1, cell2):
    x1, y1 = cell1
    x2, y2 = cell2
    return abs(x1 - x2) + abs(y1 - y2)

# Define the A* algorithm
def aStar(m):
    start = (m.rows, m.cols)  # Set the start position
    
    # Initialize g_score and f_score for each cell with infinity
    g_score = {cell: float('inf') for cell in m.grid}
    g_score[start] = 0
    f_score = {cell: float('inf') for cell in m.grid}
    f_score[start] = h(start, (1, 1))
    
    open_list = []  # Use a list for heapq
    heapq.heappush(open_list, (f_score[start], h(start, (1, 1)), start))  # Use heappush to add elements
    
    aPath = {}
    
    # Main loop for A* algorithm
    while open_list:  # Updated condition
        currCell = heapq.heappop(open_list)[2]  # Use heappop to remove the smallest element
        if currCell == (1, 1):
            break
        for d in 'ESNW':  # Loop through possible directions
            if m.maze_map[currCell][d]:
                childCell = {
                    'E': (currCell[0], currCell[1] + 1),
                    'W': (currCell[0], currCell[1] - 1),
                    'N': (currCell[0] - 1, currCell[1]),
                    'S': (currCell[0] + 1, currCell[1])
                }[d]
                
                # Calculate g_score and f_score for the child cell
                temp_g_score = g_score[currCell] + 1
                temp_f_score = temp_g_score + h(childCell, (1, 1))
                
                # Update scores and path if the new path is shorter
                if temp_f_score < f_score[childCell]:
                    g_score[childCell] = temp_g_score
                    f_score[childCell] = temp_f_score
                    heapq.heappush(open_list, (temp_f_score, h(childCell, (1, 1)), childCell))  # Use heappush
                    aPath[childCell] = currCell
    
    # Reconstruct the forward path
    fwdPath = {}
    cell = (1, 1)
    while cell != start:
        fwdPath[aPath[cell]] = cell
        cell = aPath[cell]
    
    return fwdPath

# Main execution
if __name__ == '__main__':
    m = maze(140, 140)  # Create an nxn maze or any size you input 
    m.CreateMaze()  # Generate the maze
    path = aStar(m)  # Find the path using the A* algorithm
    
    # Create an agent to walk the path and show footprints
    a = agent(m, footprints=True, color='red')
    m.tracePath({a: path})  # Trace the path in the maze
    
    # Display the length of the path in the maze
    l = textLabel(m, 'A Star Path Length', len(path) + 1)
    m.run()  # Run the maze visualization
