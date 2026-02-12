import BruteForcemk2
import time
print("========================================")
print("EVENT PLANNER - RESULTS")
print("========================================\n")

filename = "input_100.txt"
limittype = "Time"
print("Input File: " + filename)

Data = BruteForcemk2.Information(filename,limittype)

#print(Data)
# 0 Activities
# 1 limits
# index of working limit 
print("Available Time: ",Data[1][0]," Hours")
print("Available Budget: £",Data[1][1])
print()

print("--- BRUTE FORCE ALGORITHM ---")
startime = time.time()
BruteSol = BruteForcemk2.bruteforce(Data[0],Data[1],Data[2])
endtime = time.time()
#print(BruteSol)
print("Selected Activities:")
for i in BruteSol[0]:
    print("-" + i + " (" + str(Data[0][i][0]) + " hours, £" + str(Data[0][i][1]) + ", enjoyement " + str(Data[0][i][2]) + ")")
print("Total Enjoyment:", BruteSol[1][0])
print("Total Time Used:" , BruteSol[1][1])
print("Total Cost:", BruteSol[1][2])

print()

print("Execution Time:",(endtime-startime))