def minmax(list):
    pmin = list[0]
    pmax = list[0]

    for number in list:
        if number < pmin:
            pmin = number
        elif number > pmax:
            pmax = number
        continue

    return [pmin, pmax]


if __name__ == "__main__":
    print(minmax([0, -1, 5, 23, 4]))
