num=int(input("enter N:"))
origi_num=num
work=num
total=0
while work>0:
    digit=work%10
    total=total+digit
    work=work//10
print(f"sum of digit of {origi_num} is {total}")
    
