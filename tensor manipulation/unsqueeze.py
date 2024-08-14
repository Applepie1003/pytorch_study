import torch

t = torch.Tensor([0, 1, 2])
print(t)

print(t.unsqueeze(0))
print(t.unsqueeze(0).shape)

# view로도 구현 가능
print(t.view(1, -1))
print(t.view(1, -1).shape)

# 인자로 1을 넣으면 두번쨰 차원 1인 차원을 추가 하겠다는 의미입니다
print(t.unsqueeze(1))
print(t.unsqueeze(1).shape)
#맨 뒤에 1인 차원이 추가되면서 1차원 벡터가 (3, 1)의 크기를 가지는 2차원 텐서로 변경되었습니다


# view(), squeeze(), unsqueeze()는 텐서의 원소 수를 그대로 유지하면서 모양과 차원을 조절합니다.

