import numpy as np
from random import randint


class environment(object):
    #Map Properties
    board_size = 10
    board = np.zeros((board_size,board_size))

    #Player Coordinates
    player_x = 0
    player_y = 0

    #Goal Settings
    #Setting goal coordinates to empty will automatically randomize
    goal_x = []
    goal_y = []
    goal_num = 0



    def __init__(self, board_size=5, goal_x=[4], goal_y=[4],
                 player_x=0, player_y=0, goal_num=1):
        'Initialize Object'

        self.board_size = board_size
        self.goal_x = goal_x
        self.goal_y = goal_y
        self.goal_num = len(self.goal_x)
        self.player_x = player_x
        self.player_y = player_y

        #Check if we should randomize the board,
        if not self.goal_x and not self.goal_y:
            self.goal_num = goal_num
            self.randomize_goals()

        #Reset environment
        self.reset()


    def reset(self):
        'Resets the environment'

        #Reset board to all zeros
        self.board = np.zeros((self.board_size,self.board_size))
        #Reset Player
        self.player_x = 0
        self.player_y = 0
        self.board[self.player_x][self.player_y] = 1
        #Reset Goals
        self.goalset()

        return self.board_size * self.player_y + self.player_x


    def draw(self):
        'Draw the Board'

        for y in range(self.board_size):
            for x in range(self.board_size):
                print int(self.board[y][x]),
            print


    def step(self, direction):
        'Move the player'
        self.board[self.player_y][self.player_x] = 0

        if direction == 0 and self.player_x > 0:
            self.player_x -= 1 #left
        if direction == 1 and self.player_x < self.board_size-1:
            self.player_x += 1 #right
        if direction == 2 and self.player_y > 0:
            self.player_y -= 1 #up
        if direction == 3 and self.player_y < self.board_size-1:
            self.player_y += 1 #down

        self.board[self.player_y][self.player_x] = 1
        return self.board_size * self.player_y + self.player_x, self.reward()


    def reward(self):
        'Calculate and return reward'

        #If any goals in board
        if sum(sum(self.board)) != 1:
            #Check number of goals
            ua, uind = np.unique(self.board, return_inverse=True)
            count = np.bincount(uind)

            #Return difference of total number of goals minus number of remaining goals
            return self.goal_num-count[2]

        #Otherwise, reset board and return total goal number
        self.reset()
        return self.goal_num


    def goalset(self):
        'Sets goal values to board'

        for x, y in zip(self.goal_x, self.goal_y):
            self.board[y][x] = 2


    def randomize_goals(self):
        'Sets goal coordinates randomly'

        for i in range(self.goal_num):
            self.goal_x.append(randint(0, self.board_size - 1))
            self.goal_y.append(randint(0, self.board_size - 1))
