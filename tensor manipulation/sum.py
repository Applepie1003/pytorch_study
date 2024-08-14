import torch

# 덧셈
# 덧셈(sum)은 연산방법이나 인자가 평균(mean)과 같다

t = torch.FloatTensor([[1, 2], [3, 4]])
print(t)

print(t.sum()) # 단순히 원소 전체의 덧셈을 수행
print(t.sum(dim=0)) # 행을 제거
print(t.sum(dim=1)) # 열을 제거
print(t.sum(dim=-1)) # 열을 제거





