# Enter your code here. Read input from STDIN. Print output to STDOUT
for _ in range(int(input())):
    n=int(input())
    s=input()
    ans=1
    for i in range(n):
        p1,p2=i,i
        while p1>-1 and p2<n and s[p1]==s[p2]:
            p1-=1
            p2+=1
        ans=max(ans,p2-p1-1)
        p1,p2=i-1,i
        while p1>-1 and p2<n and s[p1]==s[p2]:
            p1-=1
            p2+=1
        ans=max(ans,p2-p1-1)
    print(ans)