def _is_leap(year: int) -> bool:
    return not year % 4 and year % 100 or not year % 400


def check_date(date: str) -> bool | str:
    separator = [sep for sep in date if not sep.isdigit()]
    if len(set(separator)) > 1:
        return 'Ошибка ввода данных'
    separator = separator[0]

    day, month, year = map(int, date.split(separator))

    months = {
        1: 32, 2: 29 if _is_leap(year) else 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }

    if 0 < year < 10000:
        if 0 < month < 13:
            if 0 < day <= months[month]:
                return True
    return False


print(check_date('20.06.1984'))
print(check_date('31/12/2000'))
print(check_date('32/12/2000'))
print(check_date('31/12-2000'))
print(check_date('31,13,1000'))

print(check_date(date=input('Please enter date to check: ')))
