import torch

x = torch.FloatTensor([[1, 2], [3, 4]])

print(x.mul(2.))  # 곱하기 2를 수행한값
print(x)  # 기존값 출력

# 위에 결과 처럼 원래있던 값을 변하지 않는다
# 값을 초기화 하고 싶다면 아래 코드처럼 하면된다
print(x.mul_(2.))  # 곱하기 2를 수행한 결과를 변수 x에 값을 저장하면서 결과를 출력
print(x) # 기존의 값 출력


