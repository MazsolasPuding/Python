import torch
import torchvision
from torchvision.datasets import MNIST
import matplotlib.pyplot as plt
import torchvision.transforms as transforms
from torch.utils.data import DataLoader
import numpy as np
import os


class ImageClassification:
    def __init__(self):
        self.dataset = MNIST(root='resources/', download=True)
        self.test_dataset = MNIST(root='resources/', train=False)
        self.printing_initialized_dataset()
        self.show_images()

    def printing_initialized_dataset(self):
        print(len(self.dataset))
        print(len(self.test_dataset))
        print(self.dataset[0])

    def show_images(self):
        image_1, label_1 = self.dataset[0]
        plt.imshow(image_1, cmap='gray')
        print('Label_1: ', label_1)
        plt.show()

        image_2, label_2 = self.dataset[10]
        plt.imshow(image_2, cmap='gray')
        print('Label_2: ', label_2)
        plt.show()

    def split_indices(self, n, val_pct):
        """Split dataset into training set and validation set."""
        n_val = int(val_pct * n)
        idxs = np.random.permutation(n)
        return idxs[n_val:], idxs[:n_val]


if __name__ == '__main__':
    ic = ImageClassification()

