import time
def read_input(filePath):
    with open(filePath, "r") as f: 
        fileLines = f.readlines()
    number_of_activities = int(fileLines[0].strip())
    second_line = fileLines[1].strip()
    parts = second_line.split()
    max_time = int(parts[0])
    max_budget = int(parts[1])
    activities = []
    for i in range(number_of_activities):
        parts = fileLines[i + 2].strip().split()

        name = parts[0]
        time = int(parts[1])
        cost = int(parts[2])
        enjoyment = int(parts[3])

        # add as a row in the 2D table
        activities.append([name, time, cost, enjoyment])
    return number_of_activities, max_time, max_budget ,activities


def maximise_enjoyment(activities, max_time):
    number_of_activities = len(activities)
    # dynamic programming table with  one row for each activity ( with one for 0 activities)
    #one column for each possible total time from 0 up to the max
    # table[i][capacity] = maximum enjoyment using first i activities with time limit capacity
    enjoyment_table = [[0] * (max_time + 1) for _ in range(number_of_activities + 1)]
    # filling the table
    for i in range(1, number_of_activities + 1):
            # get time and enjoyment of the current activity
            time = activities[i-1][1]
            enjoyment = activities[i-1][3]

             # loop through all capacities from 0 to max_time
            for capacity in range(max_time + 1):
                # option1 - do not take activity
                enjoyment_table[i][capacity] = enjoyment_table[i-1][capacity]

                # option 2 - if it fits take activity 
                if time <= capacity:
                    # enjoyment gained by taking activity and max enjoyment with remaining time
                    current_value = enjoyment + enjoyment_table[i-1][capacity - time]
                    # choose to skip or include based on enjoyment 
                    if current_value > enjoyment_table[i][capacity]:
                        enjoyment_table[i][capacity] = current_value
    # Backtrack to find which activities were chosen
    selected_activities = []
    capacity = max_time # Start from the full capacity
    i = number_of_activities #start from the last activity

    # go back through the table
    while i > 0:
        # if the value is different activity was selected
        if enjoyment_table[i][capacity] != enjoyment_table[i-1][capacity]:    # activity was chosen
            selected_activities.append(activities[i-1])# add activity to list
            capacity -= activities[i-1][1] # calculate remaining time
        i -= 1 # move to activity before

    selected_activities.reverse()  # show activties in the orginal order
    max_enjoyment =enjoyment_table[number_of_activities][max_time] # gets max enjoyment value
    # return maximum enjoyment and  activities chosen
    return max_enjoyment, selected_activities

def print_results( execution_time,selected_activities, max_enjoyment):

    total_time = sum(a[1] for a in selected_activities) # adds up time of each chosen activity  
    total_cost = sum(a[2] for a in selected_activities) # adds cost of each chosen activity 

    print(f"--- DYNAMIC PROGRAMMING ALGORITHM ---")
    print("Selected Activities:")
    for a in selected_activities:
        print(f" - {a[0]} ({a[1]} hours, £{a[2]}, enjoyment {a[3]})")
    print(f"Total Enjoyment: {max_enjoyment}")
    print(f"Total Time Used: {total_time} hours")
    print(f"Total Cost: £{total_cost}")
    print(f"Execution Time: {execution_time:.6f} seconds")
  

print("Please enter file path")
filePath = input()
# Start timer
start_time = time.perf_counter()
end_time = time.perf_counter()
execution_time = end_time - start_time
number_of_activities, max_time, max_budget, activities = read_input(filePath)
max_enjoyment, selected_activities = maximise_enjoyment(activities, max_time)
print_results(execution_time,selected_activities, max_enjoyment)
