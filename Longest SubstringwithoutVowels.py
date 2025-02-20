# Enter your code here. Read input from STDIN. Print output to STDOUT
for _ in range(int(input())):
    s=input()
    i=0
    c=0
    n=len(s)
    ans=0
    a=set(['a','e','i','o','u'])
    while i<n:
        if s[i] not in a:
            c+=1
        else:
            ans=max(ans,c)
            c=0
        i+=1
    ans=max(ans,c)
    print(ans)
        