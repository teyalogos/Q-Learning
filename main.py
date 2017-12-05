import level as env
import matplotlib.pyplot as plt
import numpy as np
from random import randint
import time

#Initialize Environment
game = env.environment()

#Initialize Q-Table
Q = np.zeros([game.board_size**2,4])

#Learning Parameters
lr = 0.9 #learning rate
y = 0.9 #discount
e = 0.01 #epsilon/randomness
epochs = 50 #number of epochs

rList = [] #list of rewards for plotting

for i in range(epochs):
    s = game.reset()
    rAll = 0

    j = 0
    while j < 99:
        j+=1
        #Choose our action based on the Q-Table
        a = np.argmax(Q[s,:] + np.random.randn(1,4)*(1./(i+1)))
        #Little bit of randomness
        if np.random.rand(1) < e:
            a = randint(0, 3)
        #Get reward and state from doing that action
        s1,r, = game.step(a)
        #Add to our knowledge
        Q[s,a] = Q[s,a] + lr*(r + y*np.max(Q[s1,:]) - Q[s,a])
        s = s1

        rAll += r

        print '\n' * 100
        game.draw()
        time.sleep(0.01)

    rList.append(rAll)

    print "REWARD: %d" % (rAll)
    print "OF EPOCH %d/%d" % (i+1, epochs)
    time.sleep(0.3)


print "Q-TABLE"
print Q
print "PLOTTING..."
plt.plot(rList)
plt.show()