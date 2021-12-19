# SliderPuzzle

 ---------------------------------------------------------------------------------
 * Program takes in a 1D array representing the starting state of a slider puzzle
   with 2 colors (represented by int values 1 and 2) and a blank space (represented
   by an int value 0) and finds a "goal state" using Best-First-Search.
 
 * - "Goal State" - A state in which all '2' colors are on left of all '1' colors
 
 * Author: @Jason Chambliss, @Dakota Jackson
----------------------------------------------------------------------------------

This program utilizes a best-first informed search AI algorithm.

-There are 7 possible goal states. 

- Because there are multiple goal states, there are varying heights to reach it. 
  Our program located a goal state with a depth of 23, but we were able to locate
   a goal state with a depth of 12.

- The number of the goal state found by the program is 129.

- The worst case time complexity of Best first search is O(nlog(n))
