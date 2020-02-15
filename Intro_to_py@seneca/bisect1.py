import bisect
a=[2,5,7,1,0,9,4,8]
a.sort()
x=6
i = bisect.bisect(a, x)
if i:
  print (a[i-1])