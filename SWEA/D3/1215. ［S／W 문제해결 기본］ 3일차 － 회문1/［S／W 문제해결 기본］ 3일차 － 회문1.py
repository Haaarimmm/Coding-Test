for tc in range(1, 11):
    n = int(input())
    b1 = [list(input()) for _ in range(8)]
    b2 = list(zip(*b1)) # 전치 행렬 리스트화
    cnt = 0
    for i in range(8):
        for j in range(9 - n):
            str1 = b1[i][j:j + n]
            str2 = b2[i][j:j + n]
            if str1 == str1[::-1]:
                cnt += 1
            if str2 == str2[::-1]:
                cnt += 1
    print(f'#{tc} {cnt}')