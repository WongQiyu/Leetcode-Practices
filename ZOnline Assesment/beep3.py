def shortestSubstring(givenString):
    char_set = set(givenString)
    char_count = {}
    start = 0
    min_length = float('inf')
    min_start = 0
    unique_count = 0

    for end in range(len(givenString)):
        if givenString[end] not in char_count or char_count[givenString[end]] == 0:
            unique_count += 1
        char_count[givenString[end]] = char_count.get(givenString[end], 0) + 1

        while unique_count == len(char_set):
            if end - start + 1 < min_length:
                min_length = end - start + 1
                min_start = start

            char_count[givenString[start]] -= 1
            if char_count[givenString[start]] == 0:
                unique_count -= 1
            start += 1

    return givenString[min_start:min_start + min_length] if min_length != float('inf') else ""

# Example usage
s = "dabbcabcd"
result = shortestSubstring(s)
print(f"Shortest substring: {result}")
print(f"Length: {len(result)}")