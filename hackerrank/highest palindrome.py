def highestValuePalindrome(s, n, k):
    i = 0
    j = n- 1
    s = list(s)
    changed = [0 for _ in range(n)]
    while i <= j and k > 0:
        if int(s[i]) > int(s[j]):
            s[j] = s[i]
            k -= 1
            changed[i] = 1
        if int(s[j]) > int(s[i]):
            s[i] = s[j]
            k -= 1
            changed[i] = 1
        i += 1
        j -= 1

    if s != s[::-1]:
        return '-1'

    i = 0
    j = n - 1
    while i <= j and k > 0:
        if s[i] != '9':
            if changed[i] == 1:
                k -= 1
                s[i] = s[j] = '9'
            elif k > 1:
                k -= 2
                s[i] = s[j] = '9'
            elif i == j:
                s[i] = s[j] = '9'



        i += 1
        j -= 1

    return "".join(s)

#edge case: k-=2 if we didnt change both left and right
#edge case: middle number or single number not changed



if __name__ == '__main__':
    print(highestValuePalindrome('5', 1, 1))
    print(highestValuePalindrome('3943',4,1))
    print(highestValuePalindrome('092282', 6, 3))
    print(highestValuePalindrome('0011', 4, 1))
    print(highestValuePalindrome('932239', 6, 2))
    # #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    #
    # first_multiple_input = input().rstrip().split()
    #
    # n = int(first_multiple_input[0])
    #
    # k = int(first_multiple_input[1])
    #
    # s = input()
    #
    # result = highestValuePalindrome(s, n, k)

    #fptr.write(result + '\n')

    #fptr.close()