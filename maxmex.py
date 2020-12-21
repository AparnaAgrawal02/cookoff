"""Max Mex Problem Code: MAXMEXSolvedSubmit

 
Read problems statements in Hindi, Mandarin Chinese, Russian, Vietnamese, and Bengali as well.
Chef has a sequence of positive integers A1,A2,…,AN. He wants to choose some elements of this sequence (possibly none or all of them) and compute their MEX, i.e. the smallest positive integer which does not occur among the chosen elements. For example, the MEX of [1,2,4] is 3.

Help Chef find the largest number of elements of the sequence A which he can choose such that their MEX is equal to M, or determine that it is impossible.

Input
The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
The first line of each test case contains two space-separated integers N and M.
The second line contains N space-separated integers A1,A2,…,AN.
Output
For each test case, print a single line containing one integer ― the maximum number of elements Chef can choose, or −1 if he cannot choose elements in such a way that their MEX is M.

Constraints
1≤T≤100
2≤M≤N≤105
1≤Ai≤109 for each valid i
the sum of N over all test cases does not exceed 106
Example Input
1
3 3
1 2 4
Example Output
3
Explanation
Example case 1: The MEX of whole array is 3. Hence, we can choose all the elements."""


# cook your dish here
def f():
    return list(map(int,input().split()))
def ii():
    return map(int,input().split())
"""-----------------------------------------"""
t=int(input())
for _ in range(t):
    n,m=ii()
    arr=sorted(f())
    arr1=arr[::]
    arr=list(set(arr))
    
    
    a=0
    d=[]
    for i in range(0,len(arr)):
        if a+1 != arr[i]:
            d+=[a+1]
            break
        a=arr[i]
    if d==[]:
        d.append(arr[-1]+1)
    if m in arr:
        if d==[]:
            print(n-arr1.count(m))

        elif d[0]>m :
            print(n-arr1.count(m))
        else:
            print(-1)

    else:
        if d[0]>m:
            print(n)
        elif d[0]==m:
            print(n)
        else:
            print(-1)


