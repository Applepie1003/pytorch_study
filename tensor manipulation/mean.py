import torch

# 평균(Mean)

t = torch.FloatTensor([1, 2])
print(t.mean())

t = torch.FloatTensor([[1, 2], [3, 4]])
print('원소 전체의 평균 :',t.mean())

print('차원을 인자로 준 경우 :',t.mean(dim=0))
# 입력에서 첫번쩨 차원을 제거 한다. 즉 행 차원을 제거 한다
# 1과 3의 평균을 구하고 2와 4의 평균을 구한다

print('인자로 dim=1을 준 경우 :', t.mean(dim=1))
# 입력에서 두분째 차원을 제거 한다. 즉 열 차원을 제거 한다