# mlp.py

# import packages
from collections import OrderedDict
import torch.nn as nn


def get_training_model(in_features=4, hidden_dim=8, n_classes=3):
    # construct a shallow NN
    mlp_model = nn.Sequential(OrderedDict([
        ('hidden_layer_1', nn.Linear(in_features, hidden_dim)),
        ('activation_1', nn.ReLU()),
        ('output_layer', nn.Linear(hidden_dim, n_classes))
    ]))

    return mlp_model
