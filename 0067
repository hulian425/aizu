# 岛屿问题，求图中有几块岛屿
# 方法：dfs搜索

dx=[1,0,-1,0]
dy=[0,1,0,-1]
def dfs(i,j,m):
    m[i][j] = 0
    for k in range(4):
        x = i + dx[k]
        y = j + dy[k]
        if (x < 12 and x >= 0 and y < 12 and y >= 0 and m[x][y] == 1):
            dfs(x,y,m)
    return
while True:
    try:
        m = []
        sum = 0
        for i in range(12):
            m.append(list(map(int, input())))
        for i in range(12):
            for j in range(12):
                if (m[i][j] == 1):
                    dfs(i,j,m)
                    sum += 1
        print(sum)
        input()
    except:
        break
