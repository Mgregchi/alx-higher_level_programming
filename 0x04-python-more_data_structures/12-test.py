#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string:
        return 0
    if not isinstance(roman_string, str):
        return 0
    if not roman_string.isupper():
        roman_string.upper()
    r_dict = {
        "I": 1,
        "IV": 4,
        "V": 5,
        "IX": 9,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    result = 0
    temp = list(roman_string)
    itemp = []
    if len(temp) > 1:
        idx = 0
        for i in temp:
            # If a bigger letter preceedes a smaller letter
            # the letters are added
            try:
                l = r_dict[temp[idx]]
                r = r_dict[temp[idx + 1]]

                if l > r:
                    itemp.append(l + r)

                    # When a smaller letter preceedes a bigger one,
                    # the letters are subtracted
                elif l < r:
                    itemp.append(l - r)

                    # When a letter is repeated 2 or 3 times,
                    # they get added together
                elif l == r and r_dict[temp[idx + 2]] != l:
                    itemp.append(l + r)

                    # The same letter cannot be used more than three times
                    # in a succession.
                elif 1 == r and r_dict[temp[idx + 2]] == r:
                    itemp.append(sum([l,r, r_dict[temp[idx + 2]]]))
                else:
                    pass

            except IndexError:
                pass
            idx += 1

