from itertools import chain, combinations
def powerset(activities):
    #"Subsequences of the iterable from shortest to longest."
    # powerset([1,2,3]) → () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3
    return chain.from_iterable(combinations(activities, r) for r in range(len(activities)+1))


def Information(filename:str,limittype:str):

    with open(filename) as f:
        lines = f.read().splitlines() 

    #print(lines)
    n = int(lines[0])

    Activities = {}
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
    
    #print(limits)
    #print(limitind)

    return [Activities,limits,limitind]

def bruteforce(Activities,limits,limitind):
    
    iterations = list(powerset(Activities))[1:]
    #print(iterations)

    Best_solution = ((),(-1,1000,1000))

    for x in iterations:
        #print(Best_solution)
        totaltime = 0
        totalbdg = 0

        totalenj = 0
        totallim = 0
        for y in x:
            totalenj += Activities[y][2]
            totallim += Activities[y][limitind]

            totaltime += Activities[y][0]
            totalbdg += Activities[y][1]

        #print(totalenj,totallim)
        if totallim > limits[limitind]:
            continue
        elif totalenj > Best_solution[1][0]:
            Best_solution = (x,(totalenj,totaltime,totalbdg))
        

    return Best_solution



def powerset(activities):
    #"Subsequences of the iterable from shortest to longest."
    # powerset([1,2,3]) → () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3
    return chain.from_iterable(combinations(activities, r) for r in range(len(activities)+1))

#https://docs.python.org/3/library/itertools.html#itertools-recipes