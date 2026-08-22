""" An e-commerce platform analyzes product discounts. It calculates the maximum discount value, and considers any product with discount at least half of the maximum discount as premium deals.
Rearrange the list so that premium deals appear first, followed by regular deals, while maintaining order.

Input format :
A single line of space-separated integers representing discount percentages.

Output format :
Print the rearranged discounts such that values greater than or equal to half of the maximum discount appear first.

Input 1 :
100 50 25
Output 1 :
100 50 25     """

disc = list(map(int, input().split()))

maxx = max(disc)
thresh = maxx/2

prem = [i for i in disc if i>=thresh]
reg = [j for j in disc if j<thresh]

result = prem+reg

print(*result)