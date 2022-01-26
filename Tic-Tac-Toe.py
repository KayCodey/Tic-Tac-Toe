grid = [['11','12','13'],['21','22','23'],['31','32','33']]

rows = len(grid)
columns = len(grid[0])

rule = rows * columns
end = False
'''print(str(rule))
print(str(rows))
print(str(columns))'''

def print_grid(round):
    print("       __ " + "ROUND NO. " + str(x) + " __")
    print(" ")
    print("          " + grid[0][0] + " | " + grid[0][1] + " | " + grid[0][2] + " ")
    print("        ----------------")
    print("          " + grid[1][0] + " | " + grid[1][1] + " | " + grid[1][2] + " ")           
    print("        ----------------") 
    print("          " + grid[2][0] + " | " + grid[2][1] + " | " + grid[2][2] + " ")
    print(" ")
    print("________________")
    
for x in range(0,rule):
    print_grid(x)
    number = input("Write the number of cell you picked : ")
    r = int(number[0]) - 1
    c = int(number[1]) - 1
    user = input("Are you X or O : ")
    grid[r][c] = user 
    for i in range(0,len(grid[0])):
        # Checks rows :
        if grid[i][0] == "x" and grid[i][1] == "x" and grid[i][2] == "x":
            print("The winner is X")
            end = True
            break
        elif grid[i][0] == "o" and grid[i][1] == "o" and grid[i][2] == "o":
            print("The winner is O")
            end = True
            break
        # Checks columns:
        elif grid[0][i] == "x" and grid[1][i] == "x" and grid[2][i] == "x":
            print("The winner is X")
            end = True
            break
        elif grid[0][i] == "o" and grid[1][i] == "o" and grid[2][i] == "o":
            print("The winner is O")
            end = True
            break
        elif  grid[0][0] == "x" and grid[1][1] == "x" and grid[2][2] == "x":
            print("The winner is X")
            end = True
            break
        elif  grid[0][0] == "o" and grid[1][1] == "o" and grid[2][2] == "o":
            print("The winner is O")
            end = True
            break
        elif  grid[0][2] == "x" and grid[1][1] == "x" and grid[2][0] == "x":
            print("The winner is X")
            end = True
            break
        elif  grid[0][2] == "o" and grid[1][1] == "o" and grid[2][0] == "o":
            print("The winner is O")
            end = True
            break
    if end == True:
        print_grid(x)
        break
print("Hope You Enjoyed Playing Tic-Tac-Toe")
