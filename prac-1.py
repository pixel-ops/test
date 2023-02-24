#function to convert string to number
def convert_string_to_num(n,num):
    my_str = n
    my_len = len(my_str)
    x = 0
    # checkes if the string is empty or not
    if x != my_len:
        # for every word in the given string it checks for the number and adds that number to the string
        if my_str[x:x+3] == "one":
            num = num +  "1"
            x = x+3
            return convert_string_to_num(my_str[x:],num)
        elif my_str[x:x+3] == "two":
            num = num +  "2"
            x = x+3
            return convert_string_to_num(my_str[x:],num)
        elif my_str[x:x+3] == "six":
            num = num +  "6"
            x = x+3
            return convert_string_to_num(my_str[x:],num)
        elif my_str[x:x+4] == "four":
            num = num +  "4"
            x=x+4
            return convert_string_to_num(my_str[x:],num)
        elif my_str[x:x+4] == "five":
            num = num +  "5"
            x=x+4
            return convert_string_to_num(my_str[x:],num)
        elif my_str[x:x+4] == "nine":
            num = num +  "9"
            x=x+4
            return convert_string_to_num(my_str[x:],num)
        elif my_str[x:x+4] == "zero":
            num = num +  "0"
            x=x+4
            return convert_string_to_num(my_str[x:],num)
        elif my_str[x:x+5] == "three":
            num = num +  "3"
            x=x+5
            return convert_string_to_num(my_str[x:],num)
        elif my_str[x:x+5] == "seven":
            num = num +  "7"
            x=x+5
            return convert_string_to_num(my_str[x:],num)
        elif my_str[x:x+5] == "eight":
            num = num +  "8"
            x=x+5
            return convert_string_to_num(my_str[x:],num)
        else:
            #if the string inputted is invalid
            print("Enter valid numbers")
    elif x == my_len:
        # when we reach the end of string 
        return num

#function to find gcd
def gcd(x,y):
    if y == 0:
        return x
    else:
        return gcd(y,x%y)

#function to convert number to string
def convert_num_to_string(my_gcd,ans):
    x=0
    my_len = len(my_gcd)
    #for checking end of string
    if x != my_len:
        # for every number in the given string it checks for the string and adds that string to the answer string
        if my_gcd[x] == "1":
            ans = ans +  "one"
            x = x+1
            return convert_num_to_string(my_gcd[x:],ans)
        elif my_gcd[x] == "2":
            ans = ans +  "two"
            x = x+1
            return convert_num_to_string(my_gcd[x:],ans)
        elif my_gcd[x] == "3":
            ans = ans +  "three"
            x = x+1
            return convert_num_to_string(my_gcd[x:],ans)
        elif my_gcd[x] == "4":
            ans = ans +  "four"
            x = x+1
            return convert_num_to_string(my_gcd[x:],ans)
        elif my_gcd[x] == "5":
            ans = ans +  "five"
            x = x+1
            return convert_num_to_string(my_gcd[x:],ans)
        elif my_gcd[x] == "6":
            ans = ans +  "six"
            x = x+1
            return convert_num_to_string(my_gcd[x:],ans)
        elif my_gcd[x] == "7":
            ans = ans +  "seven"
            x = x+1
            return convert_num_to_string(my_gcd[x:],ans)
        elif my_gcd[x] == "8":
            ans = ans +  "nine"
            x = x+1
            return convert_num_to_string(my_gcd[x:],ans)
        elif my_gcd[x] == "0":
            ans = ans +  "zero"
            x = x+1
            return convert_num_to_string(my_gcd[x:],ans)
        elif my_gcd[x] == "3":
            ans = ans +  "three"
            x = x+1
            return convert_num_to_string(my_gcd[x:],ans)
        else:
            # if the input is not correct
            print("Error in input")
    elif x == my_len:
        # when end of string return the answer value
        return ans

#number 1 to be inputted
num1 = int(convert_string_to_num(str(input("Enter your first number: ")),num=""))
#number 2 to be inputted
num2 = int(convert_string_to_num(str(input("Enter your second number: ")),num=""))
#gcd function call
mygcd = str(gcd(num1,num2))
#final output which convert number to string
print("Your output: ",convert_num_to_string(mygcd,ans=""))