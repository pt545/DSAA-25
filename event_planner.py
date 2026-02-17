import BruteForce
import Dynamic
import time

print("Please enter file path")
filePath = input()

print("========================================")
print("EVENT PLANNER - RESULTS")
print("========================================\n")

BruteData = BruteForce.Information(filePath,"Time")
brute_starttime = time.perf_counter()
BruteSol = BruteForce.bruteforce(BruteData[0],BruteData[1],BruteData[2])
brute_endtime = time.perf_counter()
brute_time = brute_endtime - brute_starttime 

print("Available Time: ",BruteData[1][0]," Hours")
print("Available Budget: £",BruteData[1][1])
print()

BruteForce.printSol(BruteSol[0],BruteSol[1][0],BruteSol[1][1],BruteSol[1][2],brute_time)
# Activities, total enjoyment, total time, total cost, execution time


DynamicData = Dynamic.read_input(filePath)
dynamic_starttime = time.perf_counter()
DynamicSol = Dynamic.maximise_enjoyment(DynamicData[3],DynamicData[1])
dynamic_endtime = time.perf_counter()
dynamic_time = dynamic_endtime - dynamic_starttime

Dynamic.print_results(dynamic_time,DynamicSol[1],DynamicSol[0])