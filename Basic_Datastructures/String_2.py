
def main():
    a = int(input("Enter the value:"))
    print(a,type(a))


def range_func():
    r1 = range(10)
    r2 = range(3,10)
    r3 = range(1,10,2)

    print(r1,type(r1))
    for r in r1:
        print(r)
    print(r2,type(r2))
    for r in r2:
        print(r)
    print(r3,type(r3))
    for r in r3:
        print(r)


def string_func():
    str1 = "Hello world"

    list1 = list(str1)
    print(str1, type(str1))
    for e1 in str1:
        print(e1)

    print(list1,type(list1))


    print(str1[0])
    print(str1[:-2])
    print(str1[1:3])


    str2 = str1[-1::-1]

    print(str2)

def CharacterToUpper(str1,ch):

    str6 = ""
    for each in str1:
        if(each == ch):
            str6 = str6 + each.upper()
        else:
            str6 = str6 + each

    return str6

def case_func():
    str1 = "Hello world"
    str2 = str1.upper()
    str3 = str1.lower()

    str4 = str2.title()
    str5 = str2.capitalize()

    print(str1)
    print(str2)
    print(str3)    
    print(str4)
    print(str5)

    print(CharacterToUpper(str3,"o"))

if __name__=="__main__":
    #main()
    #range_func()
    #string_func()
    case_func()