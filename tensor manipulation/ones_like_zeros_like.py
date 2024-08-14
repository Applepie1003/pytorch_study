import torch
x = torch.FloatTensor([[0, 1, 2], [2, 1, 0]])
print(x)

# 동일한 크기(shape)지만 1만으로 채워진 텐서 생성
print(torch.ones_like(x))

# 동일한 크기(shape)지만 0만으로 채워진 텐서 생성
print(torch.zeros_like(x))