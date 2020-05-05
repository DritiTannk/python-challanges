"""Given a string S. The task is to print all permutations of a given string.

Example:
Input:
ABC

Output:
ABC ACB BAC BCA CAB CBA 
"""

from itertools import permutations


def string_permutation(word):
    """ This Function returns the permutated list of the user string """
    words_list = []

    permutations_list = permutations(word)  # This function will generate all the strings and return a list.

    for item in permutations_list:
        format_word = ''.join(item)
        words_list.append(format_word)
    return words_list


if __name__ == '__main__':
    usr_string = input("Enter The Word: ")

    if (usr_string == ''):
        print("\n *** Permutation of Empty Word cannot be found !!! *** ")
    else:
        result = string_permutation(usr_string)
        print('The Permutation List of the given \'{}\' Word are as follows:'.format(usr_string))
        for i in range(1, len(result)):
            print(" Word {0}: {1}".format(i, result[i]))


