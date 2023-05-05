from problem import Problem
import search

def main():
    print("Welcome to ...")
    puzzle_type = input("Type \"1\" to use a default puzzle... :")
    if puzzle_type == "1":
        print("yo")# use default puzzle
    elif puzzle_type == "2":
        print("\nEnter your puzzle, use a zero to represent the blank")
        x,y,z = input("Enter the first row, use spaces between numbers\n").split()
        r1 =[x,y,z]
        x,y,z = input("Enter the second row, use spaces between numbers\n").split()
        r2 = [x,y,z]
        x,y,z = input("Enter the third row, use spaces between numbers\n").split()
        r3 = [x,y,z]
        initial_state = [r1,r2,r3]
        # use custom
    else:
        print("Invalid input")
    
    algorithm_type = input("Enter your choice of algorithm\n")
    if algorithm_type == "1":
        search.uniform_cost_search(Problem(initial_state))
    
if __name__ == "__main__": main()
