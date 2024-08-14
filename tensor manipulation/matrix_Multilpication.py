import torch
# 행렬 곱셈과 곱셈의 차이

# 행렬 곱셈(.matmul)
m1 = torch.FloatTensor([[1, 2], [3, 4]])
m2 = torch.FloatTensor([[1], [2]])
print(m1.shape)  # 2 x 2
print(m2.shape)  # 2 x 1
print(m1.matmul(m2))

# 원소별 곱셈(.mul)
print(m1 * m2)
print(m1.mul(m2))
