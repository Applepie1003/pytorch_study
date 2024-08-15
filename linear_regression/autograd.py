import torch

# requires_grad=True 자동미분을 활성화 한다는 의미
w = torch.tensor(2.0, requires_grad=True)
y = w**2
z = 2*y + 5
# 해당 수식을 w에 미분해야 한다

z.backward()
print('수식을 w로 미분한 값 : {}'.format(w.grad))


