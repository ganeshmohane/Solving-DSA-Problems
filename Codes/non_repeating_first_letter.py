# Find the First Non-Repeating Character
# Test Case : Input: "swiss" => Output: "w"

def non_repeating_char(s):
    char_count = {}
    
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    
    for char in s:
        if char_count[char] == 1:
            return char
    return None

s = str(input("Enter the string : \n"))
print(non_repeating_char(s))