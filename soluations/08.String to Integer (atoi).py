
#  ------- I earn from here ---------->

#1. strip() method used for remove whitespace from start and end


# 02
#  Convert String to Number Methods
# We have explained the methods to convert a string into a integer datatype. Here is the list of the functions:

# Using int() function
# Using eval() function
# Using ast.literal_eval
# Using str.isdigit() function

# -03-------- What is the ord() function in Python? ord() function in Python is used to convert a single Unicode character into its integer representation,



class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()

        if not s :
            return 0;

        sign = -1 if s[0] == '-' else 1
        if s[0] in {'-', '+'} :
            s = s[1:]

        num = 0

        for c in s:
            if not c.isdigit():
                break


            num = num * 10 + ord(c) - ord("0")
            print("num: ", num)

            if sign * num <= -2**31 :
                return -2**31
            if sign * num >= 2**31 - 1 :
                return 2**31 - 1
            
        return sign*num
    
instance = Solution()
string = " -45 "
res = instance.myAtoi(string)

print("res",res)



#----------------------------

# Here's a step-by-step explanation of the code:

# s = s.strip(): Removes leading and trailing whitespaces from the input string.

# if not s:: Checks if the string is empty after stripping whitespaces. If it is, the function returns 0.

# sign = -1 if s[0] == '-' else 1: Determines the sign of the integer. If the first character is '-', the sign is set to -1; otherwise, it is set to 1.

# if s[0] in {'-', '+'}: s = s[1:]: If the first character of the string is '-' or '+', it is removed from the string.

# num = 0: Initializes a variable num to store the resulting integer.

# for c in s:: Iterates through each character in the modified string.

# if not c.isdigit(): break: If the current character is not a digit, the loop breaks. This is because the string should only contain digits for a valid conversion.

# num = num * 10 + ord(c) - ord('0'): Converts the character to its corresponding digit value and updates the result by multiplying the existing result by 10 and adding the new digit.

# if sign * num <= -2**31: return -2**31: Checks if the result exceeds the minimum 32-bit signed integer value. If it does, the function returns the minimum integer value.

# if sign * num >= 2**31 - 1: return 2**31 - 1: Checks if the result exceeds the maximum 32-bit signed integer value. If it does, the function returns the maximum integer value.

# return sign * num: Returns the final result, taking into account the sign determined earlier.



#------------------------------------