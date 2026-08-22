""" Charlie is organizing a charity event and has recorded donation amounts from attendees. He wants to calculate the percentage of donations that are greater than the median donation amount. Implement a solution to find the median after sorting the recorded donations, count how many donations exceed this median, and compute the percentage of such donations relative to the total number of donations.
The median is the middle value in a sorted list if the number of elements is odd, or the average of the two middle values if the number of elements is even.
Help Charlie by Implementing a solution using list comprehension to solve this problem.

Input format :
The first line of input consists of an integer n, representing the number of donations.
The second line contains n space-separated integers, each representing a donation amount.

Output format :
The output displays a float rounded to two decimal places, representing the percentage of donations that exceed the median donation amount.  

Input 1 :
5
32 42 45 95 67
Output 1 :
40.00    """

n = int(input())
mid=0
med=0
count=0
perc=0

donations = list(map(int, input().split()))

donations.sort()

if n%2!=0:
    mid = (n+1)//2
    med = donations[(mid-1)]
else:
    mid = n//2
    med = ( donations[mid-1] + donations[mid] ) / 2
    