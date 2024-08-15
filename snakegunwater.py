from random import randint
print("""for 'snake' :- 0
for 'gun' :- 1
for 'water' :- 2 """)
x=int(input('enter :-  '))
y=randint(0,2)
if x>2 or x<0:
    print('wrong entry')
elif x==y:
    print('Draw')
elif (x==0 and y==2) or (x==1 and y==0) or (x==2 and y==1):
    print('you win')
else :
    print('you lose')