import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):

    if s.startswith("<iframe"):
        match = re.sub(r"(http)+(s)?(://)+(www.)?youtube.com/embed/", "https://youtu.be/", s)

        match_list = match.split('"')

        for _ in match_list:
            if _.startswith("https://youtu.be/"):
                return _
            else:
                pass
    else:
        return None


if __name__ == "__main__":
    main()