a = [1, 3, [10, 20], 'python', [40, 50]]
b=a[:]
c=a.copy()

print('a: ',a)
print('b: ',b)
print('c: ',c)

a[0]=[100,200]
a[2][1]=300
a[3]='java'
a[4]=90
c[4][1]='c++'

print('a: ',a)
print('b: ',b)
print('c: ',c)
