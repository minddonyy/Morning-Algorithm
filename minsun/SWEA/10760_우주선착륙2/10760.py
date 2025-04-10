import sys
sys.stdin = open('input.txt', 'r')
########################################

dxy = [[-1, 0], [1, 0], [0, -1], [0, 1], [-1, 1], [1, -1], [1, 1], [-1, -1]]

T = int(input())     # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    N, M = map(int, input().split())
    space_map = [list(map(int, input().split())) for _ in range(N)]
    result = 0


    for i in range(N):
        for j in range(M):
            cur_xy = space_map[i][j]
            cnt = 0

            for dx,dy in dxy:
                nx = dx + i
                ny = dy + j

                if 0 <= nx < N and 0 <= ny < M:
                    if space_map[nx][ny] < cur_xy:
                        cnt += 1
            if cnt >= 4:
                result += 1

    print(f"#{tc}", result)