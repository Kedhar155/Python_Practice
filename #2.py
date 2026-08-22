"""  Meenu is a diligent programmer who loves to work on tasks related to list manipulation. Today, she's tasked with a problem that involves determining whether a given list contains unique elements or if there are duplicates present. 
Meenu needs to develop a program that checks whether all elements in a given list are unique or if there are duplicates present.

Input format :
The input consists of a single line containing space-separated integers, representing the elements of the list.

Output format :
The first line prints "List: " followed by the input list in square brackets, separated by commas.
The second line contains the result message:
If all elements in the input list are unique, the message is "All elements are unique".
If the input list contains duplicate elements, the message is "List contains duplicate elements".  

Input 1 :
1 2 3 4
Output 1 :
List: [1, 2, 3, 4]
All elements are unique  """

lst = list(map(int, input().split()))
count=0

for i in range(len(lst)):
    for j in range(i+1, len(lst)):
        if lst[i]==lst[j]:
            count+=1
        

print("List: ",lst)

if count==0:
    print("All elements are unique")
else:
    print("List contains duplicate elements")