class Tic_Tac_Toe:

    def __init__(self):
        self.grid = [['11','12','13'],
                    ['21','22','23'],
                    ['31','32','33']]

        self.rows = columns = len(self.grid)
        self.cells = self.rows * columns
        self.is_end = False

    def print_grid(self, round):
        print('{} {}{} {}'.format(''.ljust(7,'-'), 'ROUND NO.', str(round), ''.rjust(7,'-')))
        print('')
        print(''.ljust(5) + self.grid[0][0].center(3) + ' | ' + self.grid[0][1].center(3) + ' | ' + self.grid[0][2].center(3))
        print(''.ljust(5) + ''.ljust(16,'-'))
        print(''.ljust(5) + self.grid[1][0].center(3) + ' | ' + self.grid[1][1].center(3) + ' | ' + self.grid[1][2].center(3))           
        print(''.ljust(5) + ''.ljust(16,'-'))
        print(''.ljust(5) + self.grid[2][0].center(3) + ' | ' + self.grid[2][1].center(3) + ' | ' + self.grid[2][2].center(3))
        print('')
        print(''.ljust(26,'-'))

    def game_loop(self):
        counter = 0
        while self.is_end != True :
                self.print_grid(counter)
                while True:
                    print(''.ljust(40,'-'))
                    cell_number = input('Write the number of cell you picked : ')  
                    if cell_number in ['11','12','13','21','22','23','31','32','33']:
                        r = int(cell_number[0]) - 1
                        c = int(cell_number[1]) - 1
                        break                  
                if counter % 2 == 0:
                    self.grid[r][c] = 'x' 
                else:
                    self.grid[r][c] = 'o'
                for cell in range(0,3):
                    # Checks rows :
                    if self.grid[cell][0] == 'x' and self.grid[cell][1] == 'x' and self.grid[cell][2] == 'x':
                        winner = 'x'
                        self.is_end = True
                        break
                    elif self.grid[cell][0] == 'o' and self.grid[cell][1] == 'o' and self.grid[cell][2] == 'o':
                        winner = 'o'
                        self.is_end = True
                        break
                    # Checks columns:
                    elif self.grid[0][cell] == 'x' and self.grid[1][cell] == 'x' and self.grid[2][cell] == 'x':
                        winner = 'x'
                        self.is_end = True
                        break
                    elif self.grid[0][cell] == 'o' and self.grid[1][cell] == 'o' and self.grid[2][cell] == 'o':
                        winner = 'o'
                        self.is_end = True
                        break
                    elif  self.grid[0][0] == 'x' and self.grid[1][1] == 'x' and self.grid[2][2] == 'x':
                        winner = 'x'
                        self.is_end = True
                        break
                if  self.grid[0][0] == 'o' and self.grid[1][1] == 'o' and self.grid[2][2] == 'o':
                    winner = 'o'
                    self.is_end = True
                    break
                elif  self.grid[0][2] == 'x' and self.grid[1][1] == 'x' and self.grid[2][0] == 'x':
                    winner = 'x'
                    self.is_end = True
                    break
                elif self.grid[0][2] == 'o' and self.grid[1][1] == 'o' and self.grid[2][0] == 'o':
                    winner = 'o'
                    self.is_end = True
                    break
                if self.is_end == True:
                    self.print_grid(counter)
                    print('Congratulations !')
                    print('The winner is', winner.capitalize(), '!')
                    print(''.ljust(26,'-'))
                    break
                counter += 1

game = Tic_Tac_Toe()
game.game_loop()
print('Hope You Enjoyed Playing Tic-Tac-Toe')
