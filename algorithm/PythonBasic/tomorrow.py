def read_date():
    year, month, day = tuple(map(int, input().split()))
    return year, month, day

def print_date(date):
    year, month, day = date
    print("%02d/%02d/%04d" % (month, day, year))

def advance_day(date):
    year,month,day = date
    
    # 마지막 달이면 true
    end_of_month = (month, day) in [(1, 31), (2, 28), (3, 31), (4, 30), (5, 31), (6, 30), (7, 31), (8, 31), (9, 30), (10, 31), (11, 30), (12, 31)]
    
    # 마지막 해이면 true
    end_of_year = month == 12 and day == 31
    
    if end_of_month:
        if end_of_year:
            year += 1
            month = 1
            day = 1
        else:
            month += 1
            day = 1
    else:
        day += 1    
    return year, month, day

if __name__ == "__main__":
    today = read_date()
    print_date(today)
    tomorrow = advance_day(today)
    print_date(tomorrow)    