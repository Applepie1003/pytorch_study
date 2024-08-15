# 파이토치는 미분한 값을 누적 시키는 특징이 있다

import torch
w = torch.tensor(2.0, requires_grad=True)

nb_epochs = 20
for epoch in range(nb_epochs + 1):

  z = 2*w

  z.backward()
  print('수식을 w로 미분한 값 : {}'.format(w.grad))
# 위에 코드를 보면 미분한 값인 2가 누적되는 것을 볼 수 있다
# 그러기에 optimizer.zero_grad()를 통해 미분값을 계속 0으로 초기화 시켜줘야 한다
