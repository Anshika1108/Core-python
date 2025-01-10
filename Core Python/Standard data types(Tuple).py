#Tuple
t0 = (1,2,'a','b')

print(t0)
print(t0[0])
print(t0[2])
print('lenght of tuple =', len(t0))

t1 = ('Anshika',21,14.55,'A')
t2 = (1,2,3,'A','B')

t = t1+t2
print(t)

Mul_t = t1*2
print(Mul_t)

t3 = t2[2:3]
t4 = t2[1:3]

print(t3)
print(t4)

t5 = [2, 3, 5, 7, 9, 3, 5, 3, 3]
print('max value of t5 =',max(t5))
print('min value of t5 =',min(t5))

t6 = ['anshi', 'ansh', 'anshika', 'shrivansh']
print('max value of t6 =',max(t6))
print('min value of t6 =',min(t6))

list = [11,14,17,20,25]
print(tuple(list)) #tuple() method converts list into tuple
