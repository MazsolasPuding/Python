import torch
import torch.nn as nn
import numpy as np
from torch.utils.data import TensorDataset
from torch.utils.data import DataLoader
import torch.nn.functional as F

######################################
#            Tutorial                #
######################################

class Grad:
    def __init__(self):
        # self.inputs, self.targets = self.training_data()
        # self.w, self.b = self.weights_and_biases()
        # self.linear_regression()
        pass

    def training_data(self):
        # Input (temp, rainfall, humidity)
        inputs = np.array([[73, 67, 43],
                           [91, 88, 64],
                           [87, 134, 58],
                           [102, 43, 37],
                           [69, 96, 70]], dtype='float32')
        # Targets (apples, oranges)
        targets = np.array([[56, 70],
                            [81, 101],
                            [119, 133],
                            [22, 37],
                            [103, 119]], dtype='float32')

        inputs = torch.from_numpy(inputs)
        targets = torch.from_numpy(targets)
        print('inputs:\n', inputs, '\ntargets:\n', targets, '\n')
        return inputs, targets

    @staticmethod
    def weights_and_biases():
        w = torch.randn(2, 3, requires_grad=True)
        b = torch.randn(2, requires_grad=True)
        print('w:', w, '\nb:', b, '\n')
        return w, b

    def model(self, x):
        return x @ self.w.t() + self.b

    @staticmethod
    def mean_sqr_error(pred, target):
        diff = pred - target
        return torch.sum(diff * diff) / diff.numel()

    def linear_regression(self):
        predictions = self.model(self.inputs)
        print(f'predictions:\n{predictions}\n')
        loss = self.mean_sqr_error(predictions, self.targets)
        print(f'Initial loss: {loss}\n')
        # print(loss.type())

        # Compute gradients
        loss.backward()
        # Gradients for weights
        print(f'w:\n{self.w}\n')
        print(f'w.grad:\n{self.w.grad}\n')

        with torch.no_grad():
            self.w -= self.w.grad * 1e-5  # Hyperparameter
            self.b -= self.b.grad * 1e-5  # Hyperparameter
            self.w.grad.zero_()
            self.b.grad.zero_()

        predictions = self.model(self.inputs)
        loss = self.mean_sqr_error(predictions, self.targets)
        print(f'loss:{loss}\n')

    def gradient_descent(self):
        for i in range(1000000):
            predictions = self.model(self.inputs)
            loss = self.mean_sqr_error(predictions, self.targets)
            loss.backward()
            with torch.no_grad():
                self.w -= self.w.grad * 1e-5  # Hyperparameter
                self.b -= self.b.grad * 1e-5  # Hyperparameter
                self.w.grad.zero_()
                self.b.grad.zero_()
            # print(loss)
        return loss, predictions

    def inbuilt_linear_regression(self):
        # Input (temp, rainfall, humidity)
        inputs = np.array([[73, 67, 43],
                           [91, 88, 64],
                           [87, 134, 58],
                           [102, 43, 37],
                           [69, 96, 70],
                           [74, 66, 43],
                           [91, 87, 65],
                           [88, 134, 59],
                           [101, 44, 37],
                           [68, 96, 71],
                           [73, 66, 44],
                           [92, 87, 64],
                           [87, 135, 57],
                           [103, 43, 36],
                           [68, 97, 70]],
                          dtype='float32')

        # Targets (apples, oranges)
        targets = np.array([[56, 70],
                            [81, 101],
                            [119, 133],
                            [22, 37],
                            [103, 119],
                            [57, 69],
                            [80, 102],
                            [118, 132],
                            [21, 38],
                            [104, 118],
                            [57, 69],
                            [82, 100],
                            [118, 134],
                            [20, 38],
                            [102, 120]],
                           dtype='float32')

        inputs = torch.from_numpy(inputs)
        targets = torch.from_numpy(targets)

        # Define dataset
        train_ds = TensorDataset(inputs, targets)
        print(train_ds[0:3])

        # Define data loader
        batch_size = 5
        train_dl = DataLoader(train_ds, batch_size, shuffle=True)

        # Define model
        model = nn.Linear(3, 2)
        print(model)
        print(model.weight)
        print(model.bias, '\n')

        # Parameters
        print(list(model.parameters()))

        # Generate predictions
        predictions = model(inputs)

        # Define Loss function
        loss_fn = F.mse_loss
        loss = loss_fn(model(inputs), targets)
        print(loss)

        # Define optimizer
        opt = torch.optim.SGD(model.parameters(), lr=1e-5)  # Stochastic gradient descent
        self.fit(1000, model, loss_fn, opt, train_dl)

    @staticmethod
    def fit(num_epochs, model, loss_fn, opt, train_dl):
        for epoch in range(num_epochs):
            for xb, yb in train_dl:
                prediction = model(xb)          # 1. Generate Predictions
                loss = loss_fn(prediction, yb)  # 2. Calculate loss
                loss.backward()                 # 3. Compute gradients
                opt.step()                      # 4. Update parameters using gradients
                opt.zero_grad()                 # 5. Reset the gradients to zero

            if (epoch + 1) % 10 == 0:
                # print('Epoch [{}/{}], Loss: {:.4f}'.format(epoch + 1, num_epochs, loss.item()))
                print(f"Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item()}")


if __name__ == '__main__':
    train = Grad()
    # loss, predictions = train.gradient_descent()
    # print('\nloss:', loss, '\nw:', train.w, '\nb:', train.b)
    # print('targets:\n', train.targets, '\npredictions:\n', predictions, '\n')
    train.inbuilt_linear_regression()
