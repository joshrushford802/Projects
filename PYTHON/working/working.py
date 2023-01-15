import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    times = re.search(r"[1-9]{1}[1-2]?:?[0-5]?[0-9]? (AM|PM) to [1-9]{1}[1-2]?:?[0-5]?[0-9]? (AM|PM)", s)

    if times != None:
        times_list = s.split(" ")
    else:
        raise ValueError(1)

    if len(times_list[0]) <= 2 and len(times_list[3]) <= 2:
        if int(times_list[0]) > 12 or int(times_list[3]) > 12:
            raise ValueError(1)

    i = 0
    if times:
        for _ in times_list:

            if _ != "AM" and _ != "PM" and len(_) <= 4:
                # Add 0 to beginning of str
                times_list[i] = "0" + _

            if times_list[i] == "AM":
                times_list.remove(_)

            if times_list[i] == "PM":
                # This changes the first part of list item to an int so it can add to 12, then converts it back to a
                # string and concatinates it back to the rest of the list item
                if len(times_list[i - 1]) <= 2:
                    expand_li_item = times_list[i - 1]
                    tmp = int(expand_li_item)
                    add_them = tmp + 12
                    times_list[i - 1] = str(add_them)
                    times_list.remove(_)
                else:
                    expand_li_item = times_list[i - 1].split(":")
                    tmp = int(expand_li_item[0])
                    add_them = tmp + 12
                    concat_strs = str(add_them) + ":" + expand_li_item[1]
                    times_list[i - 1] = concat_strs
                    times_list.remove(_)

            i += 1

        if len(times_list[0]) == 2 and len(times_list[2]) == 2:
            times_list[0] = str(times_list[0]) + ":00"
            times_list[2] = str(times_list[2]) + ":00"
        return f"{times_list[0]} {times_list[1]} {times_list[2]}"


if __name__ == "__main__":
    main()