"""  Nora is building a simple data-analysis tool that works with lists of integers. 
Given a list of N integers, she needs to find the largest divisor for each element in the list, other than the number itself.
The divisor should be from the list. If there is no such divisor, print -1.
Help Nora implement this logic.

Input format :
The first line contains an integer n, representing the number of elements in the list.
The second line contains n integers separated by a comma and a space, representing the elements of the list.

Output format :
The output should print a list of n integers, where the ith integer represents the largest divisor of the ith element 
in the input list (excluding the element itself) separated by comma as a list. 

Input 1 :
6
5, 16, 4, 8, 9, 10
Output 1 :
[-1, 8, -1, 4, -1, 5] """

n = int(input())

nums = list(map(int, input().split(", ")))
count=0

div=[]

newnums = []

for i in range(len(nums)):
    div = []
    
    for j in range(len(nums)):
        if j!=i and nums[i]%nums[j]==0:
            div.append(nums[j])
        
    if div:
        newnums.append(max(div))
    else:
        newnums.append(-1)

print(newnums)