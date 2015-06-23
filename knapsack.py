import pdb
import numpy as np
#https://en.wikipedia.org/wiki/Knapsack_problem

#This is for unbounded knapsack
def knapsack_dp(items, maxweight):
  m = [0]*maxweight
  m_set = [[]]*maxweight
  for w in range(maxweight):
    if w == 0:
      m[0] = 0
    else:
      max_w = 0
      max_i = -1 #If this is not changed, no need to delete
      for i, item in enumerate(items):
        if item[0] <= w:
          prev_w = item[1]  + m[w-item[0]]
          if prev_w > max_w:
            max_w = prev_w
            max_i = i
        else:
          continue
      m[w] = max_w
          
      #pdb.set_trace()
      #if max_i != -1:
      #  del items[max_i]
  return m

#http://www.es.ele.tue.nl/education/5MC10/Solutions/knapsack.pdf
def knapsack_0_1(items,maxweight):
  # Input:
  # Values (stored in array v)
  # Weights (stored in array w)
  # Number of distinct items (n)
  # Knapsack capacity (W)
  n = len(items)
  m = np.zeros((n+1,maxweight+1))
  #keep = np.zeros((n+1,maxweight+1))
  #for j in range(maxweight):
  #  m[0, j] = 0
  pdb.set_trace()
  for i in range(1,n+1):
    for j in range(maxweight+1):
      if items[i-1][0] <= j:
        m[i, j] = max(m[i-1, j], m[i-1, j-items[i-1][0]] + items[i-1][1])
      else:
        m[i, j] = m[i-1, j]
  return m
  
#weight then value
stuff = [(4,20),(1,1)]

print knapsack_dp(stuff, 10)
print knapsack_0_1(stuff, 10)