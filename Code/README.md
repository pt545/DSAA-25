# DSAA-25
Coursework for Data Structures and Algorithmns. Group 25



### File Structure

This program is divided into three files: BruteForce.py, Dynamic.py and event_planner.py. 

The file event_planner.py is the main file of interest as it implements the functionalities of the other two.

The program is stored in a folder named 'Code' per the coursework specifications. 
The input files are stored in a parallel folder named 'Input_Files'.

### Running the program

To run the program one must run the event_planner.py file in 'Code' (ensuring that BruteForce.py and Dynamic.py are also present), the program will then prompt the user to input a file name (which must be present in 'Input_files'). The program will then generate calculate the optimal solution for a given constraint (in this case defined as time) using both algorithms. The optimal solution will then be outputted to the console.


### Dependencies and Libraries

This program makes use of two external libraries:

- event_planner.py uses the 'time' library to measure the execution time for either algorithm.
- BruteForce.py uses the 'itertools' library. In specific it uses the chain and combinations methods in order to generate the powerset for all possible combinations of events.

Additionally event_planner.py makes use of the methods in BruteForce.py and Dynamic.py.

