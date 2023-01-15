from datetime import date
import re
import inflect


def main():
    p = inflect.engine()
    try:
        y, m, d = validate(input('Date of birth: '))
    except:
        raise ValueError('Enter valid birthday')

    compute_change = date.today() - date(int(y), int(m), int(d))
    mins = compute_change.days * 24 * 60
    otpt = p.number_to_words(mins, andword='')
    final_cap = otpt.capitalize()

    print(final_cap + " minutes")




def validate(b):
    bday = re.search(r'[0-9]{4}-[0-9]{2}-[0-9]{2}', b)

    if not bday:
        pass
    else:
        y, m, d = b.split('-')
        return y, m, d


if __name__ == "__main__":
    main()