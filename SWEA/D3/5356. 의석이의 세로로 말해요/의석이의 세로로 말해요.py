T = int(input())
for tc in range(1, T+1):
    print(f'#{tc}', end=' ')
    arr = [list(input()) for _ in range(5)]
    for j in range(15):
        for i in range(5):
            try:
                print(arr[i][j], end='')
            except:
                continue
    print()