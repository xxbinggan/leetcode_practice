# 作者:lixy
# 2026年10月22日16时01分38秒
# 2695016411@qq.com
import sys
input=sys.stdin.read

def main():
    data=input().split()
    idx=0
    n=int(data[idx])
    idx+=1
    m=int(data[idx])
    idx+=1
    sum=0
    vec=[]
    for i in range(n):
        row=[]
        for j in range(m):
            num=int(data[idx])
            idx+=1
            row.append(num)
            sum+=num
        vec.append(row)

    horizontal=[0]*n
    for i in range(n):
        for j in range(m):
            horizontal[i]+=vec[i][j]

    vertical=[0]*m
    for j in range(m):
        for i in range(n):
            vertical[j]+=vec[i][j]

    result=float('inf')
    horizontalCut=0
    for i in range(n):
        horizontalCut+=horizontal[i]
        result=min(result,abs(sum-horizontalCut*2))

    verticalCut=0
    for j in range(m):
        verticalCut+=vertical[j]
        result=min(result,abs(sum-verticalCut*2))

    print(result)

if __name__ == '__main__':
    main()