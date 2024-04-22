
# 1~30의 숫자 중에서 15의 배수인 경우 15로 나누고, 그 외에는 숫자로 나타내라
for i in range(1, 30+1):
    # 15의 배수는 15로 나누기
    if i % 15 == 0:
        print(i/15)
    # 5의 배수 구구단 출력
    if i % 5 == 0:
        print('='*20)
        for j in range(1, 9+1):
            print(f'{i} X {j} = {i*j}')
    # 그 외에는 숫자로 나타내기        
    else:
        print(i)
