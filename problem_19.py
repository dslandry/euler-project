# dow = day of week
class Constants:
    days_to_add_leap_year = [3, 1, 3, 2, 3, 2, 3, 3, 2, 3, 2, 3]
    days_to_add_normal_year = [3, 0, 3, 2, 3, 2, 3, 3, 2, 3, 2, 3]


def is_leap_year(value):
    if value % 100 == 0:
        if value % 400 == 0:
            return True
        else:
            return False
    else:
        if value % 4 == 0:
            return True


def get_sundays_on_first_of_month_for_year(year, dow):
    year_values = Constants.days_to_add_leap_year if (
        is_leap_year(year)) else Constants.days_to_add_normal_year
    sundays_count = 0
    next_dow = dow
    for value in year_values:
        if next_dow == 6:
            sundays_count += 1
        next_dow = (next_dow + value) % 7

    return sundays_count, next_dow


if __name__ == "__main__":
    start_year = 1901
    end_year = 2000
    dow = 1
    total_sundays_count = 0

    for year in range(start_year, end_year+1):
        sundays_count, dow = get_sundays_on_first_of_month_for_year(year, dow)
        total_sundays_count += sundays_count

    print(total_sundays_count)
