from problem import Problem
import search

def main():
    print("Welcome to 862173656 8 puzzle solver")
    puzzle_type = input("Type \"1\" to use a default puzzle, or \"2\" to enter your own puzzle :")
    if puzzle_type == "1":
        #use default
        r1 = ["0", "1", "2"]
        r2 = ["4", "5", "3"]
        r3 = ["7", "8", "6"]
        initial_state = [r1,r2,r3]
    elif puzzle_type == "2":
        # use custom
        print("\nEnter your puzzle, use a zero to represent the blank")
        x,y,z = input("Enter the first row, use spaces between numbers\n").split()
        r1 =[x,y,z]
        x,y,z = input("Enter the second row, use spaces between numbers\n").split()
        r2 = [x,y,z]
        x,y,z = input("Enter the third row, use spaces between numbers\n").split()
        r3 = [x,y,z]
        initial_state = [r1,r2,r3]
    else:
        print("Invalid input")
    
    print("Enter your choice of algorithm")
    print("1 - Uniform Cost Search")
    print("2 - A* with the Misplaced Tile Heuristic")
    algorithm_type = input("3 - A* with the Euclidean distance heuristic\n")

    if algorithm_type == "1":
        search.uniform_cost_search(Problem(initial_state,False))
    elif algorithm_type == "2":
        search.misplaced_tile_search(Problem(initial_state, False))
    elif algorithm_type == "3":
        print("Would you like the algorithm with a trace of the solution or without:")
        print("1 - Without Trace")
        trace_type = input("2 - With Trace\n")
        if trace_type == "1":
            search.euclidean_distance_search(Problem(initial_state,False))
        elif trace_type == "2":
            search.euclidean_distance_search(Problem(initial_state, True))
    
if __name__ == "__main__": main()
