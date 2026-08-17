# 作者:lixy
# 2026年08月17日20时52分11秒
# 2695016411@qq.com
class solution:
    def convert(self,s,numRows):
        n,r=len(s),numRows
        if r==1 or r>=n:
            return s

        t=2*r-2
        c=(n+t-1)/t*(r-1)

        mat=[['']*c for _ in range(r)]
        x,y=0,0
        for i,ch in enumerate(s):
            mat[x][y]=ch
            if i%t<r-1:
                x+=1
            else:
                x-=1
                y+=1
        return ''.join(ch for row in mat for ch in row)