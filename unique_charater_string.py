def firstUniqChar(s):
    char_count = {}

    # Populating the hashmap with character counts
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    # Checking the count of each character in the hashmap
    for i in range(len(s)):
        if char_count[s[i]] == 1:
            return i

    return -1

# Example usage:
s = "leetcode"
print(firstUniqChar(s))
t = "loveleetcode"
print(firstUniqChar(t))
u = "aabb"
print(firstUniqChar(u))
