""" Given a list of positive and negative numbers, arrange them such that all negative integers appear before all the positive integers in the array. The order of appearance should be maintained.

Input format :
The input consists of a single line containing a list of integers enclosed in square brackets separated by commas.

Output format :
The output displays "List =" followed by an arranged list of integers as required, separated by commas and enclosed in square brackets.

Input:
[12, 11, -13, -5, 6, -7, 5, -3, -6]

Output:
List = [-13, -5, -7, -3, -6, 12, 11, 6, 5]       """

lst = list(map(int, input().strip("[]").split(", "))) 

neg = [x for x in lst if x<0]
pos = [y for y in lst if y>=0]
    
final = neg + pos

print("List=", final)