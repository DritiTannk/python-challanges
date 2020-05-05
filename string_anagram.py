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


def anagram_check( word1, word2):
    """ Checks whether the strings are anagram or not. """

    if (sorted(word1) == sorted(word2)):  # It sorts the strings and compares each element.
        result = "The Given Words:\'{}\' and \'{}\' are Anagram.".format(word1, word2)
    else:
        result = "The Given Words:\'{}\' and \'{}\' are not Anagram.".format(word1, word2)
    return result


if __name__ == '__main__':
    usr_input1 = input("Enter The 1st Word: ").lower()
    usr_input2 = input("Enter The 2nd Word: ").lower()

    if usr_input1 == '' or usr_input2 == '':
        print("\n *** You Have Entered the Empty Value. ***")
    else:
        result = anagram_check(usr_input1, usr_input2)
        print(result)
