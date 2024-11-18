def split_and_join(line):
    # write your code here

    return "-".join(str(item) for item in line.split(" "))


if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)