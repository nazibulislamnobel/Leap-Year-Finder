start_year = 2001
end_year = 2100

leap_year_count = 0

for year in range(start_year, end_year + 1):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(year, end=' ')
        leap_year_count += 1

    if leap_year_count == 10:
        print()
        leap_year_count = 0

if leap_year_count != 0:
    print()