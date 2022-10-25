import numpy as np
from itertools import combinations
import random

def sigmoid(x):
    return 1/(1 + np.exp(-x))

def sigmoid_derivate(x):
    return sigmoid(x) * (1 - sigmoid(x))

def binl(number, n):
    '''4 -> [1 0 0]'''
    _temp = bin(number)[2:]
    return [0] * (n - len(_temp)) + [int(i) for i in _temp]

class Layer:

    def __init__(self, i, j):
        np.random.seed(1)
        self.weights = 2 * np.random.random((i, j)) - 1

    def feed_forward(self, x):
        return sigmoid(np.dot(x, self.weights))

    def back_prop(self, x, y):
        output = self.feed_forward(x)
        error = y - output
        self.weights += np.dot(x.T, error * sigmoid_derivate(output))
        return output

    def train(self, x, y, time):
        for _ in range(time):
            self.back_prop(x, y)

class ANN:
    def __init__(self):
        self.input_layer = Layer(4, 8)
        self.hidden_layer1 = Layer(8, 8)
        self.hidden_layer2 = Layer(8, 4)

    def feed_forward(self, x):
        return self.hidden_layer2.feed_forward(self.hidden_layer1.feed_forward(self.input_layer.feed_forward(x)))

    def back_prop(self, x, y):
        self.x2 = self.input_layer.back_prop(x, self.x2)
        self.x3 = self.hidden_layer1.back_prop(self.x2, self.x3)
        self.hidden_layer2.back_prop(self.x3, y)

    def train(self, x, y, time):
        self.x2 = self.input_layer.feed_forward(x)
        self.x3 = self.hidden_layer1.feed_forward(self.x2)
        for _ in range(time):
            self.back_prop(x, y)

temp = [0, 1, 2, 3]
x = list(combinations(temp, 2))  # x <- [[0 1] [0 2] ...]
'''for i in list(combinations(temp, 2)):
    if bool(random.getrandbits(1)) and len(x) > 10:
        x.remove(i)
'''
y = [sum(i) for i in x] # y <- [0+1 0+2 ...]

print('Training data: ')
for i in range(len(y)):
    print(f'{x[i][0]} + {x[i][1]} = {y[i]}')

# Convert x, y to binary array
x = np.array([binl(i, 2) + binl(j, 2) for i,j in x])
y = np.array([binl(i, 4) for i in y])

an = ANN()
an.train(x, y, 30000)

print('\nAfter training:\n3 + 1 = ', end='')
test_answer = an.feed_forward(binl(3, 2) + binl(1, 2))
rounded_answer = ''.join(str(round(i)) for i in test_answer)
print(int(rounded_answer, 2))



