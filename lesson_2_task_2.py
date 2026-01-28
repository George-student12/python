
def is_year_leap(year):
    if year % 4 == 0:
        return True
    else:
        return False


test_years = [2020, 2021, 2022, 2023, 2024]

for year in test_years:
    result = is_year_leap(year)
    print(f"Год {year}: {result}")
