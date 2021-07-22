import os
import torch

dirname = os.path.dirname(os.path.realpath(__file__))
model_filename = os.path.join(dirname, "model.pt")

model = torch.load(model_filename)
print("Successfully load models")

