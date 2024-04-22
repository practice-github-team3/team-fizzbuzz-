for i in range(1, 30+1):
    if i % 5 == 0:
        print('='*20)
        for j in range(1, 9+1):
            print(f'{i} X {j} = {i*j}')
