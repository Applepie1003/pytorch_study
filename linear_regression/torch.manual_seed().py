# torch.manual_seed()를 사용한 프로그램의 결과는 다른 컴퓨터에서 실행시켜도 동일한 결과를 얻을 수 있다
# 다른 컴퓨터에서 실행 시켜도 동일한 결과를 얻을수 있는 이유는 torch.manual_seed()는 난수 밝생 순서와 값을 동일하게 보당해준다는 특징때문이다
# 랜덤 시드가 3이면 두번 난수를 발생 시킨다

import torch
torch.manual_seed(3)
print('랜덤 시드가 3일 때')
for i in range(1,3):
  print(torch.rand(1))

torch.manual_seed(5)
print('랜덤 시드가 5일 때')
for i in range(1,3):
  print(torch.rand(1))

torch.manual_seed(3)
print('랜덤 시드가 3일 때')
for i in range(1,3):
  print(torch.rand(1))

# 랜덤 시드를 3으로 실행 했다가 5로 실행하고 3으로 실행하면 처음부터 실행한것 처럼 난수 발생 순서가 초기화 된다
#

