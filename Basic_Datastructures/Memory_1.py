import pandas as pd

def main():
    print("Inside main")
    a=10
    b=10
    
    print("Address")
    print(id(a)," ",id(b))

    print("Division")
    print(5/2)
    print(5//2)
    print(int(5/2))

    print("Increment")
    a=a+5
    print(a)
    a+=5
    print(a)
    a+=1
    print(a)

    print("Condition")
    print(5>2)
    print(2==2)
    print(5>=2)
    print(3<=1)

    print("Logical Operator")
    print(5 and 2) # Logical and
    print(5 & 2)  # Bitwise and operator


    print("Membership operator")
    a = [1,2,3,4,5]
    b = 3
    print(b in a)

    c=99
    print(c not in a)

    str1 = "Hello World"
    print("H" in str1)

    print("Identity operator")
    a=5
    b=5
    c=5
    print(a is b)
    print(c is not b)

    print("Loop")
    a = [1,2,3,4,5]
    b = 3
    for b in a:
        print(b)
if __name__=="__main__":
    main()