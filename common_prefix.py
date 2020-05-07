"""
Given a array of N strings, find the longest common prefix among all strings present in the array.

Example:
Input:
geeksforgeeks geeks geek geezer
apple ape april

Output:
gee
ap
"""


def common_prefix(usr_string):
    """ This function finds the prefix from given words. """
    prefix_list = []  # Empty list for prefix letters.
    words_list = usr_string.split(',')  # Splitting the input by ',' seperator.
    words_list.sort()  # Sorting the list.
    first_word = words_list.pop(0)  # Getting first word from the list.
    len_first_word = len(first_word)  # Finding length of first word of the list.

    for i in range(len(words_list)):
        for j in range(0, len_first_word):  # The highest length of the prefix can be of length first word.
            if words_list[i][j] == first_word[j]:  # Comparing the first letter of each list item with dirst word letter.

                if not words_list[i][j] in prefix_list:
                    prefix_list.append(words_list[i][j])  # Appending the non repeating letter to the list.

        prefix = "".join(prefix_list)  # Formatting the word.

    return prefix


if __name__ == '__main__':
    usr_input = input("Enter The List: ").lower()

    if usr_input != '':
        result = common_prefix(usr_input)

        if result == '':
            print("\n *** There Is NO Common Prefix In The Given Input. ***")
        else:
            print("The Longest Common Prefix IS: ", result)

    else:
        print("\n *** You Have Entered the Empty Values. ***")

