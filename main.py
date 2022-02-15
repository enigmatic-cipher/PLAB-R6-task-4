"""
Given a list of numbers as input. Print numbers that are divisible by 3 and 4 but not by 12. Also these numbers should lie in the range of 3 and 99 [inclusive].
Input-> [1,5,15,20,27,72,75,150,400]
Output-> 5 15 20 27 72 75
"""

list_1 = [1,5,15,20,27,72,75,150,400]
lenght_1 = len(list_1)
for i in range(1,lenght_1):
  e = list_1[i]
  if (e%3==0 or e%4==0 or e%12!=0) and (3<=e<=99):
    print(e)
  