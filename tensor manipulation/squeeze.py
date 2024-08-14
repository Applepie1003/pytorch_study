import torch

# 스퀴즈는 차원이 1인 경우에는 해당 차원을 제거합니다
t = torch.FloatTensor([[1], [2], [3]])
print(t)
print(t.shape)

print(t.squeeze())  # (3 x 1) -> (3,)
print(t.squeeze().shape)
