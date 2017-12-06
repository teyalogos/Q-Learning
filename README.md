# Q-Learning-1
First Q-Learning implementation I've ever done.

# The Game
Here, the AI is represented as a 1 and the goal is represented as a 2.
The goal of the game is to get to the goal as many times in 100 steps.
Here, the AI has reached the goal 12 times in a 100 steps in epoch 24.
```
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 1 0
0 0 0 0 2
REWARD: 12
OF EPOCH 24/50
```

# Options
Changing the environment parameters
```python
'Sets the environment size to a 20x20 square grid and the number of goals to 100'
game = env.environment(board_size=20, goal_num=(20**2)/4)
'Sets the environment size to a 20x20 square grid and the number of goals to 100 and also sets the player at the coordinates'
'x:10 y:10. The default value is 0'
game = env.environment(board_size=20, goal_num=(20**2)/4, player_x=10, player_y=10)
'Sets the environment size to a 10x20 square grid with one goal at the coordinates x:9 y:9'
game = env.environment(board_size=10, goal_x=[9], goal_y=[9])
```
