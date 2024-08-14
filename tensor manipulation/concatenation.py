import torch

x = torch.FloatTensor([[1, 2], [3, 4]])
y = torch.FloatTensor([[5, 6], [7, 8]])

# 어느 차원을 늘릴것 인지를 인자로 줄 수 있다
print(torch.cat((x, y), dim=0))  # (2 x 2) -> (4 x 2)
print(torch.cat((x, y), dim=1))  # (2 x 2) -> (2 x 4)