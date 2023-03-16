"""
Exercise 2: ⬤
Lexicographical order is often known as alphabetical order when dealing with strings. A string is greater than another
string if it comes later in a lexicographically sorted list.
Given a word, create a new word by swapping some or all of its characters. This new word must meet two criteria:
●       It must be greater than the original word
●       It must be the smallest word that meets the first condition
Example w = abcd
The next largest word is abdc.
Create the function bigger_Is_greater and return the new string meeting the criteria. If it is not possible, return no answer.
Function Description
Function has the following parameter(s):
    	●	string w: a word
Returns
    	- 	string: the smallest lexicographically higher string possible or no answer
Input Format
The first line of input contains T, the number of test cases. Each of the next T lines contains w.
Constraints
●   	1 ≤ T ≤ 105
●   	1 ≤ length of w ≤ 100
●   	w will contain only letters in the range ascii[a...z]
Sample Input:
5 ab bb hefg dhck dkhc
Sample Output ba no answer
hegf dhkc hcdk
Explanation Test case 1: ba is the only string which can be made by rearranging ab. It is greater.
Test case 2:
It is not possible to rearrange bb and get a greater string.
Test case 3: hegf is the next string greater than hefg.
Test case 4: dhkc is the next string greater than dhck. Test case 5: hcdk is the next string greater than dkhc.
Sample Input: 6 lmno dcba dcbb abdc abcd fedcbabcd
Sample Output lmon no answer no answer acbd abdc Fedcbabdc


"""

def bigger_is_greater(w):
    # Convert the word to a list of characters
    w = list(w)

    i = len(w) - 1

    while i > 0 and w[i - 1] >= w[i]:
        i -= 1

    if i <= 0:
        return 'no answer'

    j = len(w) - 1
    while w[j] <= w[i - 1]:
        j -= 1

    # Swap the characters
    w[i - 1], w[j] = w[j], w[i - 1]

    # Reverse
    w[i:] = w[len(w) - 1:i - 1:-1]

    # Convert the list of characters back to a string
    return ''.join(w)


# number of test cases
n = int(input("Input number: "))

for i in range(n):
    print(bigger_is_greater(input("Input word: ")))





# second option
"""
def bigger_is_greater(w):
    best = ''
    for i in range(len(w)):
        idx = -i - 1
        c = w[idx]
        if c >= best:
            best = c
        else:
            l = sorted(w[idx:])
            for j, ch in enumerate(l):
                if ch > c:
                    return w[:idx] + ch + ''.join(l[:j] + l[j + 1:])
    return 'no answer'


n = int(input("Input number: "))
for i in range(n):
    print(bigger_is_greater(input("Input word: ")))
"""