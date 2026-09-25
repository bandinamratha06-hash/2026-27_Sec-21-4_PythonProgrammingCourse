#check valid triangle or not
a=int(input("enter the angle1"))
b=int(input("enter the angle2"))
c=int(input("enter the angle3"))
if a>0 and b>0 and c>0 and a+b+c==180:
    print(f"valid triangle(angle={a},{b},{c})")
else:
    print(f"not valid triangle(angle={a},{b},{c})")
