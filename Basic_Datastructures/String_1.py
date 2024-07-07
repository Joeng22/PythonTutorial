#How to replace a character in a string python
'''
Answer
In Python, strings are immutable, which means that once a string is created, it cannot be modified. 
However, you can create a new string by replacing certain characters in the original string. 
One way to do this is by using the replace() method. But this will create new object for the string.
'''

def Replace_1(InputStr,char1,char2):
    print("Repace_1 Before:",id(InputStr))
    InputStr = InputStr.replace(char1,char2)
    print("Repace_1 After:",id(InputStr))

    return InputStr

def Conventional_1(InputStr,char1,char2):
    OutputStr = ""
    for each in InputStr:
        if each == char1:
            OutputStr = OutputStr + char2
        else:
            OutputStr = OutputStr + each

    return OutputStr

def main():
    Input_str = "America"
    charInString = "e"
    newChar = "a"

    print("*************** Method 1 ********************")
    print("Input:",id(Input_str))
    Output_str = Replace_1(Input_str,charInString,newChar)
    print(Output_str)
    print("Output:",id(Output_str))


    print("*************** Method 2 ********************")
    print("Input:",id(Input_str))
    Output_str = Conventional_1(Input_str,charInString,newChar)
    print(Output_str)
    print("Output:",id(Output_str))



if __name__=="__main__":
    main()