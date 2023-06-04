# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 16:33:35 2022

@author: sethy
"""
def BF(s1,s2):
     """ BF algorithm """
     i = 0
     j = 0
     while(i < len(s1) and j < len(s2)):
         if(s1[i] ==  s2[j]):
             i += 1
             j += 1
         else:
             i = i - j + 1
             j = 0
     if(j >= len(s2)):
         return i - len(s2)
     else:
         return 0
  

a1=str(input("enter a string: "))
a2=str(input('enter a string: '))
b=BF(a1,a2)
print(b)
     # s1 = "ababcabcacbab"
     # s2 = "abcac"
     # print(BF(s1,s2))