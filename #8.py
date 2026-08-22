""" Ravi is learning Python and got an assignment to practice list operations. He is required to take N integers as input, store them in a list, and then transform the list based on specific index-based rules.

Sort the list in ascending order.
Replace the element at index 0 with 0.
For elements at even indices (excluding index 0), replace them with their cube.
For elements at odd indices, replace them with their square.
Finally, display both the original sorted list and the transformed list.


Help Ravi write a program to accomplish this task.

Input format :
The first line of input contains an integer N, representing the size of the list.
The next N lines contain one integer each, representing the elements of the list.

Output format :
The first line of output prints: "Original List: " followed by the sorted list.
The second line of output prints: "Replaced List: " followed by the transformed list. 

Input 1 :
5
5
1
2
3
4
Output 1 :
Original List: [1, 2, 3, 4, 5]
Replaced List: [0, 4, 27, 16, 125] """

N=int(input())
lst=[]

for i in range(N):
    a = int(input())
    lst.append(a)
    
lst.sort()
print("Original List:",lst)


lst[0]=0

for j in range(len(lst)):
    if j%2==0:
        lst[j]=lst[j]**3
    else:
        lst[j]=lst[j]**2

print("replaced List:",lst)

    