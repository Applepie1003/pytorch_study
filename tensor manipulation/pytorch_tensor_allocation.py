# 파이토치 텐서 전환
import torch

# 1차원 텐서(벡터) 만들기
t = torch.FloatTensor([0., 1., 2., 3., 4., 5., 6., 7., 8., 9.])
print(t)

print(t.dim())  # rank. 즉 차원
print(t.shape)  # shape
print(t.size())  # shape

# 인덱스로 텐서에 접근하는 것은 numpy와 같다
print(t[0], t[1], t[-1])  # 인덱스로 접근
print(t[2:5], t[4:-1])    # 슬라이싱
print(t[:2], t[3:])       # 슬라이싱


# 2차원 텐서
t = torch.FloatTensor([[1., 2., 3.,], [4., 5., 6.,], [7., 8., 9.], [10., 11., 12.]])
print(t)

print(t.dim())  # rank == 차원
print(t.size())  # shape

print(t[:, 1])  # 첫번째 차원을 전체 선택한 상황에서 두번째 차원의 첫번째 것만 가져온다
print(t[:, -1].size())  # 위에거 크기

print(t[:, :-1]) # 첫번째 차원을 전체 선택한 상황에서 두번째 차원에서는 맨 마지막에서 첫번째를 제외하고 다 가져온다.
'''
출력 결과
tensor([[ 1.,  2.],
        [ 4.,  5.],
        [ 7.,  8.],
        [10., 11.]])
'''


