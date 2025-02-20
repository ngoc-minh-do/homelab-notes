# Nvidia GPU acceleration in PyTorch

## Setting Up PyTorch for GPU Acceleration
Check for GPU availability in PyTorch
```
import torch
if torch.cuda.is_available():
	print(f"GPU: {torch.cuda.get_device_name(0)} is available.")
else:
	print("No GPU available. Training will run on CPU.")
```
Set the device configuration to GPU using the torch.device class in PyTorch
```
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(device) # cuda
```
## Moving Tensors to GPU
```
tensor = torch.randn((3, 3))
tensor = tensor.to('cuda')
```
After moving a tensor to the GPU, the operations can be carried out just like they would with CPU tensors. PyTorch automatically utilizes the GPU for these operations, leading to quicker computation times.

## Parallel Processing with PyTorch
Parallel processing with PyTorch for GPU acceleration involves distributing computation tasks across multiple GPUs or parallelizing computations within a single GPU. This means that instead of executing tasks sequentially, which is common in CPUs, GPUs can handle multiple tasks simultaneously.

PyTorch's torch.nn.DataParallel module simplifies parallel processing across multiple GPUs.

This module replicates model on multiple GPUs, splits input data among the GPUs, computes forward and backward passes independently, and then averages the gradients across all GPUs. Wrap your model with DataParallel to distribute mini-batches across available GPUs. Below is the example of how DataParallel can be implemented:
```
import torch
import torch.nn as nn

model = nn.Conv2d(3, 64, 3, 1, 1) # Create a model

model = nn.DataParallel(model) # Wrap the model with DataParallel

model = model.to('cuda') # Move the model to the GPU
# Perform forward pass on the model
input_data = torch.randn(20, 3, 32, 32).to('cuda')
output = model(input_data)
```

## Neural Network Training with GPU Acceleration
Here is a simple neural network code demonstrating the model and data transfer to GPU.
```
class Generate(nn.Module):
	def __init__(self):
		super(Generate, self).__init__()
		self.gen = nn.Sequential(
			nn.Linear(5,1),
			nn.Sigmoid()
		)

	def forward(self, x):
		return self.gen(x)

model = Generate() # Initialize the model
model.to('cuda') # Move the model to the GPU

# Create input data inside GPU
input_data = torch.randn(16, 5, device=device)
output = model(input_data) # Forward pass on theGP
output
```
## GPU Memory Management for Deep Learning Tasks in PyTorch

- Memory Clearance: PyTorch supplies the `torch.cuda.empty_cache()` function, which aids in releasing GPU memory that is no longer in use. Employing this function strategically, such as after completing a task or encountering out-of-memory errors, proves beneficial for freeing up GPU memory.
- Monitoring Memory Usage: PyTorch provides tools like `torch.cuda.max_memory_allocated()` and `torch.cuda.max_memory_reserved()` to monitor the highest levels of memory allocation and caching on the GPU. Utilizing these functions allows for the tracking of memory usage throughout training, facilitating the identification of potential memory leaks or inefficiencies.

## Ref
- https://www.geeksforgeeks.org/how-to-use-gpu-acceleration-in-pytorch/