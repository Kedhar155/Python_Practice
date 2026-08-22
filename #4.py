"""  Dhoni is organizing his tasks for the day and wants to create a simple to-do list using Python. 
He plans to input his tasks one by one and then remove them as he completes them.
He wants to create a program that allows him to add tasks, mark them as completed by removing first and last elements from the list, and visualize his progress.

Input format :
The first line of input consists of the number of elements in the list N.
The next N lines of input consist of integers representing the elements in the list.

Output format :
The first line displays "List after appending elements: " followed by the list after appending elements to it.
The second line displays "List after popping last element: " followed by the list after popping the last element.
The third line displays "Popped element: " followed by the popped last element.
The fourth line displays "List after popping first element: " followed by the list after popping the first element.
The fifth line displays "Popped element: " followed by the popped first element.

Input 1 :
5
10
20
30
40
50
Output 1 :
List after appending elements: [10, 20, 30, 40, 50]
List after popping last element: [10, 20, 30, 40]
Popped element: 50
List after popping first element: [20, 30, 40]
Popped element: 10  """

N=int(input())
lst = []

for i in range(N):
    p = int(input())
    lst.append(p)

print("List after appending elements:", lst)

print("List after popping last element:", lst[0:(len(lst)-1)] )

print("Popped element:", lst.pop())

print("List after popping first element:", lst[1:])

print("Popped element:", lst.pop(0))