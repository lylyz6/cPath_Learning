import torch
import torch.nn as nn
import torch.optim as optim
def forward():
    y_v = w * x + b
    return y_v
    
x = torch.randn(4, 4)
y_t = 2 * x + 1
w = torch.tensor([1.], requires_grad= True)
b = torch.tensor([0.], requires_grad= True)
nn.Linear(1,1)
lr = 0.5
for epoch in range(500):
    if epoch != 0:
        w.grad.zero_()
        b.grad.zero_()
    y_v = forward()
    loss = ((y_v - y_t)**2).sum()/32
    loss.backward()
    with torch.no_grad():
        w -= w.grad * lr
        b -= b.grad * lr
print(f'w: {w.detach().item(): .4f}\nb: {b.detach().item(): .4f}')



