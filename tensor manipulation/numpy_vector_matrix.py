# 넘파이로 텐서 만들기
import numpy as np

t = np.array([0., 1., 2., 3., 4., 5., 6.])
# 파이썬으로 설명하면 List를 생성해서 np.array로 1차원 array로 변환함.
print(t)


print(t.ndim)  # ndim은 몇 차원인지 출력한다
print(t.shape)  # shape는 크기를 출력한다.
# (7,)는 (1, 7)을 의미한다 -> (1 X 7)

print(t[0], t[1], t[-1])  # 인덱스를 통해 원소접근
print(t[2:5], t[4:-1])
print(t[:2], t[3:])
print(t[::2])

# numpy 2차원 배열
t = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(t)

print(t.ndim)
print(t.shape)
