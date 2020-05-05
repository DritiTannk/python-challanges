"""
Given two strings a and b consisting of lowercase characters. The task is to check whether two given strings are anagram of each other or not. An anagram of a string is another string that contains same characters, only the order of characters can be different. For example, “act” and “tac” are anagram of each other.

Example:
Input:
2
geeksforgeeks forgeeksgeeks
allergy allergic

Output:
YES
NO

Explanation:
Testcase 1: Both the string have same characters with same frequency. So, both are anagrams.
Testcase 2: Characters in both the strings are not same, so they are not anagrams.

"""

from itertools import permutations


def anagram_check(word1, word2):
    """ Checks whether the strings are anagram or not. """

    if len(word1) == len(word2):  # Comparing the len of each word.
        w1_per = permutations(word1)  # Finding permutation strings of user first word.
        for item in w1_per:  # iterating and comparing the each word for finding match.
            format_word = ''.join(item)  # Reformatting the each word from permutation list.
            if format_word == word2:
                answer = "The Given Words:\'{}\' and \'{}\' are Anagram.".format(word1, word2)
    else:
        answer = "The Given Words: \'{}\' and \'{}\' are NOT Anagram.".format(word1, word2)

    return answer


if __name__ == '__main__':
    usr_input1 = input("Enter The 1st Word: ").lower()
    usr_input2 = input("Enter The 2nd Word: ").lower()

    if usr_input1 == '' or usr_input2 == '':
        print("\n *** You Have Entered the Empty Value. ***")  # If both or either of the values are empty.
    else:
        result = anagram_check(usr_input1,usr_input2)
        print(result)

