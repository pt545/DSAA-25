from itertools import chain, combinations

def Information(filename:str,limittype:str):

    with open(filename) as f:
        lines = f.read().splitlines() 

    #print(lines)
    n = int(lines[0])

    Activities = {}
    # Activities are divided into a dictionary
    # The name is used as a key and the limits and enjoyment are kept in a list 

    #print(n)
    for i in lines[2:]:
        #print(i)
        parts = i.split(' ')
        Activities[parts[0]] = [int(parts[1]) , int(parts[2]),int(parts[3])]
    #print(Activities)

    limits = [int(i) for i in lines[1].split()]
    if limittype == "Time":        
        limitind = 0
    elif limittype == "Budget":
        limitind = 1
    # The limit can be set to either Time or Budget
    # The code will decide which one based on the index set here 
    # The indexes are consistent so this works thought the program.

    #print(limits)
    #print(limitind)

    return [Activities,limits,limitind]
    # Return the relevant information to a central program

def bruteforce(Activities,limits,limitind):
    
    iterations = list(powerset(Activities))[1:]
    # powerset is converted into a list (with the first item - which is empty- removed)
    #print(iterations)

    Best_solution = ((),(-1,1000,1000))
    # The best solution stores the current optimal set of activities
    # Stores the name and then (enjoyment, total time, total money spent)
    # Default values almost guaranteed to be replaced

    for x in iterations:
        # iterates though the possibilities

        #print(Best_solution)
        totaltime = 0
        totalbdg = 0
        # This keeps track of the total time and budget of this iteration

        totalenj = 0
        totallim = 0
        # Keeps track of the enjoyment 
        # Keeps track of the limiting factor 
        for y in x:
            totalenj += Activities[y][2]
            totallim += Activities[y][limitind]

            totaltime += Activities[y][0]
            totalbdg += Activities[y][1]

        #print(totalenj,totallim)
        if totallim > limits[limitind]:
            # If this iteration surpasses the limit it is not considered 
            continue
        elif totalenj > Best_solution[1][0]:
            # else it is compared with the best solution 
            # if it has a greater total enjoyment it becomes the best solution
            Best_solution = (x,(totalenj,totaltime,totalbdg))
        
    # After the program finishes iterating though the possibilities the best solution found is returned
    return Best_solution



def powerset(activities):
    # This function generates the powerset (ie: every possible combination) of the activities
    return chain.from_iterable(combinations(activities, r) for r in range(len(activities)+1))

#https://docs.python.org/3/library/itertools.html#itertools-recipes