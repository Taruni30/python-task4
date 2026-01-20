#printing numbers from 0 to 100
for i in range(1,100):
    print(i, end=" ")

#countdown timer
count=10
while count>0:
    print(count)
    count-=1
    print("Countdown timer")
#continue and break statements
for i in range(1,11):
    if(i==5):
        print("continue the loop of 5")
        continue
    if(i==9):
        print("break the loop at 9")
        break
    print(i)
print()
#iterating string
string="Tarunika"
for str in string:
    print(str)
print()
#multiplication table of 3
num=3
for i in range(1,11):
    print(num, "x",i,"=", num*i)
#range with steps
for i in range(2,21,2):
    if(i%2==0):
        print(i, "is a even number")
    else:
        print(i, "is a odd number")
#Real world example
marks=(90,60,76,35,85)
for mark in marks:
    if (mark>=40):
        print("PASS", mark)
    else:
        print("FAIL", mark)


