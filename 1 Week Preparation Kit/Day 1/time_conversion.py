"""
Given a time in -hour AM/PM format, convert it to military (24-hour) time.

Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.
"""


def time_conversion(s):
    # * Remove "AM or PM" for given input
    remove_am_pm = s[0:8]

    # * Split string with ":" symbol
    split_string = remove_am_pm.split(":")
    hour = split_string[0]
    minute = split_string[1]
    second = split_string[2]

    if s.endswith("PM") and hour != "12":
        final_time = f"{int(hour)+12}:{minute}:{second}"
    elif s.endswith("AM") and hour == "12":
        final_time = f"00:{minute}:{second}"
    else:
        final_time = remove_am_pm

    return final_time


if __name__ == "__main__":
    s = input()

    result = time_conversion(s)
