import copy
from queue import PriorityQueue

#creates puzzle where color 1 is represented 1, and color 2 by 2, with 0 being a blank space
start_state = [1,1,1,0,2,2,2] #0 = blank space, 1 = Red, 2 =
all_states =[]
all_states.append(start_state)
state_depth = [0]


#create a best-first search with the cost equal to the num of tiles the blank moves
#want all of '2' color on left and '1' color on right

v = 100
graph = [[] for i in range(v)]

states_PQ = PriorityQueue()

def best_first_search(current_state):
    visited = []
    states_PQ.put((0, current_state))


    #print (current_state)
    while states_PQ.empty() == False:
        current_state = states_PQ.get()[1]  #grabs the highest priority off the PQ (lowest cost)
        # Displaying the path having lowest cost
        #print(current_state)
        counter = 0
        done = False   #flag set to break while loop
        printRG(current_state)
        print("State Number: ", all_states.index(current_state))
        if current_state in visited:
            continue
        visited.append(current_state)
        for index, value in enumerate(current_state):
            if value == 1 and index <= 3: #if there is a 1 in the 1st 3 indecies, then cant be goal state
                break
            elif value == 2 and index <= 3:
                #print("If statement 1 has been hit AND counter value is", counter, "| current index:", index)
                counter += 1

            if counter == 3:
                #print("If statement 2 has been hit AND counter value is", counter, "| current index:", index)
                done = True
                break
        print("State Depth: ", state_depth[all_states.index(current_state)])
        print("Total Number of States:", len(all_states))

        print("_______________________")
        if done:
            break
            #print(current_state)


        generateStates(current_state, visited)

    print("The goal state:", end="")
    printRG(visited[-1])
    print("Goal State Number: ", all_states.index(current_state))
    print("Goal State Depth: ", state_depth[all_states.index(current_state)])
    print("Total Number of States:", len(all_states))

def printRG(printstate):
    print("[", end="")
    for index, value in enumerate(printstate):
        if value == 0:
            print(" ", end="")
        if value == 1:
            print("R", end="")
        if value == 2:
            print("G", end="")
        if index != len(printstate)-1:
            print(", ", end="")

    print("]")

def swapTiles(jump,current_state1,index,visited):

    #print(index)
    global total_states
    temp = current_state1[index + jump]    #temp = value at the place we want to trade the blank for
    temp_state = copy.copy(current_state1) #temp_state gets set to the current_state state
    temp_state[index + jump] = 0           #set the value where we want to put blank to blank (currently 2 blanks)
    #another debug line


    #print(current_state1, "debug")
    temp_state[index] = temp               #set value at index of current blank to value of the index we are trading (should be successfully swapped here)
    if temp_state not in all_states:
        all_states.append(temp_state)
        state_depth.append(state_depth[all_states.index(current_state1)]+1)
        #print(visited[-1], "test")
        cost = 0
        if abs(jump) == 1:
            cost = 1
        elif abs(jump) == 2:
            cost = 1
        elif abs(jump) == 3:
            cost = 2
        states_PQ.put((cost, temp_state)) #put into the PQ the new state with swapped places with the Priority value set to the cost of the spaces needed to move
        #More debug lines

        #print(current_state1, "current_state showing not affected by changes")

def generateStates(current_state, visited):
    index = current_state.index(0)
    if index == 0:
        swapTiles(1,current_state,index,visited)
        swapTiles(2,current_state,index,visited)
        swapTiles(3,current_state,index,visited)

    if index == 1:
        swapTiles(-1,current_state,index,visited)
        swapTiles(1,current_state,index,visited)
        swapTiles(2,current_state,index,visited)
        swapTiles(3,current_state,index,visited)

    if index == 2:
        swapTiles(-2,current_state,index,visited)
        swapTiles(-1,current_state,index,visited)
        swapTiles(1,current_state,index,visited)
        swapTiles(2,current_state,index,visited)
        swapTiles(3,current_state,index,visited)

    if index == 3:
        swapTiles(-3,current_state,index,visited)
        swapTiles(-2,current_state,index,visited)
        swapTiles(-1,current_state,index,visited)
        swapTiles(1,current_state,index,visited)
        swapTiles(2,current_state,index,visited)
        swapTiles(3,current_state,index,visited)

    if index == 4:
        swapTiles(-3,current_state,index,visited)
        swapTiles(-2,current_state,index,visited)
        swapTiles(-1,current_state,index,visited)
        swapTiles(1,current_state,index,visited)
        swapTiles(2,current_state,index,visited)

    if index == 5:
        swapTiles(-3,current_state,index,visited)
        swapTiles(-2,current_state,index,visited)
        swapTiles(-1,current_state,index,visited)
        swapTiles(1,current_state,index,visited)

    if index == 6:
        swapTiles(-3,current_state,index,visited)
        swapTiles(-2,current_state,index,visited)
        swapTiles(-1,current_state,index,visited)
#print()

best_first_search(start_state)
