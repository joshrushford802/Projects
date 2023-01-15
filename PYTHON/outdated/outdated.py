month = [
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
    "December"
]

while True:
    dte = input("Date: ")
    try:
        mnth, dy, yr = dte.split("/")
        if (int(mnth) > 0 and int(mnth) < 13) and (int(dy) > 0 and int(dy) < 32):
            break
    except:
        try:
            spc_mnth, spc_dy, spc_yr = dte.split(" ")

            for n in range(len(month)):
                if spc_mnth == month[1]:
                    mnth = n + 1

            dy = spc_dy.replace(",", "")

            if (int(mnth) > 0 and int(mnth) < 13) and (int(dy) > 0 and int(dy) < 32):
                break

        except:
            print()
            pass

print(f"{yr}-{int(mnth):02}-{int(dy):02}")