def is_leap(year):
    leap = False
    if year % 4:
        return leap
    if not year % 100 and year % 400:
        return leap

    # Write your logic here
    leap = True
    return leap


year = int(input())
print(is_leap(year))