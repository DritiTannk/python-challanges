"""
Your task is to implement the function strstr. The function takes two strings as arguments (s,x) and  locates the occurrence of the string x in the string s. The function returns and integer denoting the first occurrence of the string x in s.

Example:
Input
2
GeeksForGeeks Fr
GeeksForGeeks For
Output
-1
5
"""

if __name__ == '__main__':
    usr_input1 = input("Enter The Sentence: ").lower()
    usr_input2 = input("Enter The Word To Be Found: ").lower()

    if usr_input1 == '' or usr_input2 == '':  # If empty values are entered
        print("\n *** You Have Entered the Empty Value. ***")
    else:
        find_operation = lambda s1, s2: s1.find(s2)  # Lambda function for searh operation.
        pos = find_operation(usr_input1, usr_input2)
        if pos == -1:
            print(f'Word \'{usr_input2}\' NOT Found.')
        else:
            print("Position Of \'{0}\' Word Is: {1} ".format(usr_input2, pos))
