"""
Given a String of length S, reverse the whole string without reversing the individual words in it. Words are separated by dots.

Example:
Input:

i.like.this.program.very.much
pqr.mno

Output:
much.very.program.this.like.i
mno.pqr

** For More Input/Output Examples Use 'Expected Output' option **

"""


def string_reverse(sentence):

    """     This function will reverse the string that user enters.  """

    sentence_list = sentence.split(sep='.')  # string will be seperated by '.' and will be stored as list.
    reversed_list = sentence_list[::-1]  # reversed string will be stored
    custom_sep = '.'  # defining the custom_sep for new string.
    result= custom_sep.join(reversed_list)  # reversed string will be appended with custom_sep.
    return result


if __name__ == '__main__':
    usr_string = input("Enter The Sentence: ")

    if (usr_string == ''):
        print("\n *** Empty Sentence Can't be Reversed !!! *** ")
    else:
        result = string_reverse(usr_string)
        print(f"Reversed String is : {result}")
