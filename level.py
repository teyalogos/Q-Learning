import numpy as np


class environment(object):
    #Map Properties
    board_size = 5
    board = np.zeros((board_size,board_size))
    #Player Coordinates
    player_x = 0
    player_y = 0
    #Goal Coordinates
    goal_x = board_size-1
    goal_y = board_size-1


    def __init__(self):
        'Initialize Object'
        self.reset()


    def reset(self):
        'Resets the Board'
        self.board = np.zeros((self.board_size,self.board_size))
        self.board[self.goal_x][self.goal_y] = 2

        #Reset Player
        self.player_y = 0
        self.player_x = 0
        self.board[self.player_x][self.player_y] = 1

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
        'Get reward'
        if [self.player_x, self.player_y] == [self.goal_x, self.goal_y]:
            self.reset()
            return 1
        return 0
