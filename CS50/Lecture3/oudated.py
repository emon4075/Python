Months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]

while True:
    Date = input("Date: ")
    try:
        Month, Day, Year = map(int, Date.split("/"))
        if (Month >= 1 and Month <= 12) and (Day >= 1 and Day <= 31):
            break
    except:
        try:
            Old_Month, Old_Day, Year = Date.split(" ")
            if Old_Month in Months:
                Month = Months.index(Old_Month) + 1
            if not Old_Day.endswith(","):
                continue
            Day = int(Old_Day.replace(",", ""))
            if (Month >= 1 and Month <= 12) and (Day >= 1 and Day <= 31):
                break
        except:
            pass

print(f"{Year}-{int(Month):02}-{int(Day):02}", end="")
