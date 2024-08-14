import torch


x = torch.FloatTensor([1, 2])
y = torch.FloatTensor([3, 4])
z = torch.FloatTensor([5, 6])

print(torch.stack([x, y, z])) # (3 x 2)

# 스택킹은 많은 연산을 포함하고 있다
# 위에 코드를 풀어쓰면 아래와 같다
print(torch.cat([x.unsqueeze(0), y.unsqueeze(0), z.unsqueeze(0)]))


# 스택킹은 추가적으로 dim인자를 줄 수 있다
print(torch.stack([x, y, z], dim=1))  # (2 x 3)


