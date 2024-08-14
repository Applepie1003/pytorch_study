import torch

# 행렬의 덧셈, 뺄셈을 할려면 행렬의 크기가 같아야 한다
# 형렬의 곱셈을 할려면 행렬의 차원이 같아야 합니다.
# 다른 차원끼리 사칙연산을 하면 크기와 차원을 자동으로 맞추어 주어 연산해주는 것이 브로드캐스팅입니다

m1 = torch.FloatTensor([[3, 3]])
m2 = torch.FloatTensor([[2, 2]])
print(m1 + m2)

# Vector + scalar
m1 = torch.FloatTensor([[1, 2]])
m2 = torch.FloatTensor([3]) # [3] -> [3, 3]
print(m1 + m2)

# 2 x 1 Vector + 1 x 2 Vector
m1 = torch.FloatTensor([[1, 2]])
m2 = torch.FloatTensor([[3], [4]])
print(m1 + m2)

'''
# 브로드캐스팅 과정에서 실제로 두 텐서가 어떻게 변경되는지 보겠습니다.
[1, 2]
==> [[1, 2],
     [1, 2]]
[3]
[4]
==> [[3, 3],
     [4, 4]]
'''
# 브로드캐스팅은 자동으로 실행되는 기능이기 때문에 주의 하면서 사용해야 합니다
