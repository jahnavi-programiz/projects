'''Write a python program to solve a classic ancient Chinese puzzle.
We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how many chickens do we have?
Sample Input            Expected Output
heads-150 legs-400          100 50
heads-3 legs-11             No solution
heads-3 legs-12              0 3
heads-5 legs-10              5 0'''

#lex_auth_012693810762121216155

def solve(heads,legs):
    error_msg="No solution"
    chicken_count=0
    rabbit_count=0
     # Check if the solution is possible
    if legs % 2 != 0 or heads > legs // 2 or heads * 4 < legs:
        print(error_msg)
        return

    # Calculate the number of rabbits and chickens
    rabbit_count = (legs - 2 * heads) // 2
    chicken_count = heads - rabbit_count

    # Print the results
    if rabbit_count < 0 or chicken_count < 0:
        print(error_msg)
    else:
        print(chicken_count, rabbit_count)

    #Start writing your code here
    #Populate the variables: chicken_count and rabbit_count



    # Use the below given print statements to display the output
    # Also, do not modify them for verification to work

    #print(chicken_count,rabbit_count)
    #print(error_msg)

#Provide different values for heads and legs and test your program
solve(38,131)