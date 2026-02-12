from itertools import chain, combinations

with open("input_small.txt") as f:
    lines = f.read().splitlines() 

print(lines)
n = int(lines[0])

line2 = [int(i) for i in lines[1].split()]
T = line2[0]
B = line2[1]

print("T: " , T , " ," , "B: " , B )

Activities = {}
for i in lines[3:]: 
    temp = i.split(" ")
    Activities[temp[0]] = [int(j) for j in temp[1:]]

print(Activities)


Best_solution = ((),-1)
# keep track of the best solution
# activities + total enjoyment (set to -1 as enjoyment will always be positive)


# defining the limit
limit = T
# sets the limit as time
# treat as hard limit
limitind = 0
#index in the dictionary


def powerset(activities):
    #"Subsequences of the iterable from shortest to longest."
    # powerset([1,2,3]) → () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3
    return chain.from_iterable(combinations(activities, r) for r in range(len(activities)+1))

#https://docs.python.org/3/library/itertools.html#itertools-recipes
#generates the powerset of a given input

powers = list(powerset(Activities))
print(powers)
for x in powers[1:]:
    totalenj = 0
    totallim = 0
    for y in x:
        totalenj += Activities[y][-1]
        totallim += Activities[y][limitind]
    if totallim > limit:
        continue
    # enforcing limit 
    if totalenj > Best_solution[1]:
        Best_solution = (x,totalenj)

print(Best_solution)


def bruteforce(filename:str):

    with open("input_small.txt") as f:
        lines = f.read().splitlines() 

    print(lines)
    n = int(lines[0])

    line2 = [int(i) for i in lines[1].split()]
    T = line2[0]
    B = line2[1]

    print("T: " , T , " ," , "B: " , B )

    Activities = {}
    for i in lines[3:]: 
        temp = i.split(" ")
        Activities[temp[0]] = [int(j) for j in temp[1:]]



    Best_solution = ((),-1)

    limit = T
    limitind = 0

    powers = list(powerset(Activities))
    print(powers)
    for x in powers[1:]:
        totalenj = 0
        totallim = 0
        for y in x:
            totalenj += Activities[y][-1]
            totallim += Activities[y][limitind]
        if totallim > limit:
            continue
        # enforcing limit 
        if totalenj > Best_solution[1]:
            Best_solution = (x,totalenj)


    return Best_solution