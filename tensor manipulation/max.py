import torch

# 최대(Max)와 아그맥스(ArgMax)

t = torch.FloatTensor([[1, 2], [3, 4]])

print(t.max())  # 모든 원소중 최대값
print(t.max(dim=0))  # (dim=0) 첫번째 차원을 제거한다는 의미
'''
실행 결과 : (tensor([3., 4.]), tensor([1, 1]))

[1, 1]가 무슨 의미인지 봅시다. 기존 행렬을 다시 상기해봅시다.
[[1, 2],
 [3, 4]]
첫번째 열에서 0번 인덱스는 1, 1번 인덱스는 3입니다.
두번째 열에서 0번 인덱스는 2, 1번 인덱스는 4입니다.
다시 말해 3과 4의 인덱스는 [1, 1]입니다.
'''
print('Max :',t.max(dim=0)[0])  # 0번 인덱스만 사용하면 max값만
print('ArgMax :',t.max(dim=0)[1])  # 1번 인덱스만 사용하면 argmax값만
