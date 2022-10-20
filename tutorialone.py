# Marvish Chandra

import numpy as np
from random import randint
from sklearn.utils import shuffle
from sklearn.preprocessing import MinMaxScaler

train_labels = []
train_samples = []

# given scientific study of people

# the ~5% of younger individuals who did experience side effects
for i in range(50):
    random_younger = randint(13,64)
    train_samples.append(random_younger)
    train_labels.append(1)

# the ~5% of older individuals who didn't experience side effects
random_older = randint(65,100)
train_samples.append(random_younger)
train_labels.append(0)

for i in range(1000):
    # 95% of younger individuals who didn't experience side effects
    random_younger = randint(13,64)
    train_samples.append(random_younger)
    train_labels.append(0)

    # the 95% old who experienced side effects

    random_older = randint(65,100)
    train_samples.append(random_younger)
    train_labels.append(1)

    for i in train_samples:
        print(i)

    for i in train_labels:
        print(i)

    # use the numpy library to as first interpret data
    train_labels = np.array(train_labels)
    train_samples = np.array(train_samples)
    train_labels, train_samples = shuffle(train_labels, train_samples)

    scaler = MinMaxScaler(feature_range=(0,1))
    scaled_train_samples = scaler.fit_transform(train_samples.reshape(-1,1)) 

    for i in scaled_train_samples:
        print(i)



