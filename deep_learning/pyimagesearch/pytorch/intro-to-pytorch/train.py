# train.py
import torch

from models import mlp
from torch.optim import SGD
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_blobs
import torch.nn as nn


# define generator for batches
def next_batch(inputs, targets, batch_size):
    # loop over the dataset
    for i in range(0, inputs.shape[0], batch_size):
        # yield a tuple of the current batched data and labels
        yield inputs[i: i + batch_size], targets[i: i + batch_size]


# batch_size, epochs and learning rate
BATCH_SIZE = 64
EPOCHS = 10
LR = 1e-2

# determine the device we will be using for training
DEVICE = 'cuda' if torch.cuda.is_available() else 'cpu'
print(f'[INFO] Training using {DEVICE}')


# generate a 3-class classification problem with 10000 data points,
# where each data point is a 4D feature vector
print("[INFO] preparing data...")
X, y = make_blobs(n_samples=1000, n_features=4, centers=3, cluster_std=2.5, random_state=95)

# create training and testing splits, and convert them to PyTorch tensors
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.15, random_state=95)

X_train = torch.from_numpy(X_train).float()
X_test = torch.from_numpy(X_test).float()
y_train = torch.from_numpy(y_train).float()
y_test = torch.from_numpy(y_test).float()

# initialize model and display its architecture
mlp = mlp.get_training_model().to(DEVICE)
print(mlp)

# initialize optimizer and loss function
opt = SGD(mlp.parameters(), lr=LR)
loss_func = nn.CrossEntropyLoss()

# implement the training loop
for epoch in range(1, EPOCHS+1):
    # initialize tracker variables and set model to trainable
    print(f'[INFO] epoch: {epoch}...')
    train_loss = 0
    train_acc = 0
    samples = 0
    mlp.train()

    # loop over the current batch of data
    for batch_x, batch_y in next_batch(X_train, y_train, BATCH_SIZE):
        # flash data to device
        batch_x, batch_y = batch_x.to(DEVICE), batch_y.to(DEVICE)
        # make predictions
        predictions = mlp(batch_x)
        # calculate loss
        loss = loss_func(predictions, batch_y.long())

        # flush gradients
        opt.zero_grad()
        # backpropagation
        loss.backward()
        # update weights
        opt.step()

        # update training loss, accuracy and number of samples visited
        train_loss += loss.item() * batch_y.size(0)
        train_acc += (predictions.max(1)[1] == batch_y).sum().item()
        samples += batch_y.size(0)

    print(f'epoch: {epoch}  train_loss: {train_loss/samples:.3f}   train_acc: {train_acc/samples:.3f}')


