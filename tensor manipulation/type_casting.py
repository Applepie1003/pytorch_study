import torch

lt = torch.LongTensor([1, 2, 3, 4])
print(lt)
print(lt.long()) # 텐서에 .float를 붙이면 float타입으로 변환됨

bt = torch.ByteTensor([True, False, False, True])
print(bt)
print(bt.long()) # .long을 붙이면 long타입으로 변환된다
print(bt.float())  # .float을 붙이면 float타입으로 변환된다
