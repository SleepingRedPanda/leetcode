def checkInclusion(s1: str, s2: str) -> str:
    char_frequency = {}

    for char in s1:
        if char not in char_frequency:
            char_frequency[char] = 0
        char_frequency[char] += 1

    window_start = 0
    matched = 0

    for window_end in range(len(s2)):
        right_char = s2[window_end]

        if right_char in char_frequency:
            char_frequency[right_char] -= 1
            if char_frequency[right_char] == 0:
                matched += 1

        if window_end >= len(s1) - 1:
            left_char = s2[window_start]
            window_start += 1
            if left_char in char_frequency:
                if char_frequency[left_char] == 0:
                    matched -= 1
                char_frequency[left_char] += 1

        if matched == len(char_frequency):
            return True

    return False
s1 = "dc"
s2 = "odicf"

print(checkInclusion(s1, s2))
