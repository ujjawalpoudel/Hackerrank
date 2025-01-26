def find_longest_substring(s):
    last_occurance = {}
    start = 0
    max_length = 0

    for index, char in enumerate(s):
        if char in last_occurance:
            start = max(start, last_occurance[char] + 1)
        last_occurance[char] = index
        max_length = max(max_length, index - start + 1)

    return max_length


print(find_longest_substring("abcabcbb"))
