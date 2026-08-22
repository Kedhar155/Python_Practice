""" An environmental monitoring system collects Air Quality Index (AQI) readings. The system identifies "natural pattern" readings that belong to the Fibonacci sequence.
Stations with Fibonacci AQI values are considered "naturally balanced" and should be prioritized for reporting.
Rearrange the AQI readings so that all Fibonacci numbers appear first, followed by non-Fibonacci numbers, while maintaining the original order within each category.
Note: The Fibonacci sequence considered: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377. (Since AQI ≤ 500) 

Input format :
The input contains a single line of space-separated integers representing AQI readings.

Output format :
The output should be printed as a single line of space-separated numbers, 
where all Fibonacci AQI values appear first followed by all non-Fibonacci AQI values, while preserving the original order within each group.

Input 1 :
0 5 8 13 20 34 50 89
Output 1 :
0 5 8 13 34 89 20 50 """

fibo = [0,1,1,2,3,5,8,13,21,34,55,89,144,233,377]

aqi = list(map(int, input().split()))

a = [x for x in aqi if x in fibo]
b = [y for y in aqi if y not in fibo]

p = a+b

print(*p)
    