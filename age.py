import datetime


def age(input_string):
    now = datetime.datetime.now()  # Current date

    day, month, year = input_string.split("-")  # Convert birthday to d/m/y
    birthday = datetime.datetime(
        day=int(day), month=int(month), year=int(year))

    # Find difference
    difference = now - birthday
    return difference.days // 365  # find integer division


if __name__ == "__main__":
    print(age("18-12-2002"))
