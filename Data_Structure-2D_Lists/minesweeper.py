import copy
#the function takes in no of rows for the minsweeper game
#also takes in input ('-' and '#') and converts to a list
# D function then returns a grid, replacing each dash with the no of adj mine
def mine_sweep_game(mine_sweeper):
    try:

            # makes a deep copy of the input list
            copy_minesweeper = copy.deepcopy(mine_sweeper)
            #each tuple represents a relative position to the current cell in the board
            offset = [[-1,-1],[-1,0],[-1,1],[0,1],[0,-1],[1,-1],[1,0],[1,1]]

            #loops thru board rows
            for index, value in enumerate(mine_sweeper):
                for index_, value_ in enumerate(value):# loops thru board columns
                    if value_ == "-": #checks if the cell has value = "-"
                        mine_count = 0 # if yes starts a count 
                        for r,c in offset: #loops thru the offset to find other adj. "#"
                            ir,ic = index+r, index_+c #gets the relative position on the board
                            #ensuring only indexes in range 
                            if ir in range(len(mine_sweeper)) and ic in range(len(value)):
                                mine_count += mine_sweeper[ir][ic] == "#" 

                        copy_minesweeper[index][index_] = str(mine_count)
            print("\nThis is the modified grid, each dash is now replaced with the no of adj mine\n")
            [print(i, end='\n') for i in copy_minesweeper]
            return copy_minesweeper
    except ValueError:
            print("Incorrect input: input a valid number")
    except IndexError:
                print("Error: number of elements entered in each row must be the same")

mine_sweeper = []
for row in range(int(input("Build your minesweeper game \ninsert number of rows: "))):
    list_input= list(input(f'input objects in row no {row + 1},E.g #---# : '))
    for i in list_input:
        if i not in ("-",'#'):
            raise ValueError('Invalid Input: Enter only "#"and"-"\'s')
    mine_sweeper.append(list_input)
    
     
mine_sweep_game(mine_sweeper)




   