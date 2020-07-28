#!/usr/bin/env python3

import sys


def replace_non_printable(text, replacement):
    return ''.join([i if ord(i) < 128 else replacement for i in text])


def print_error_message(pw, message):
    print(replace_non_printable(pw, '*') + " -> Error: " + message)
    return True


def check_valid_length(pw_length):
    if len(pw_length) < 8:
        print_error_message(pw_length, "Too Short")
        return False
    if len(pw_length) > 64:
        print_error_message(pw_length, "Too Long")
        return False
    return True


def check_valid_ascii_chars(pw_ascii):
    if not pw_ascii.isascii():
        print_error_message(pw_ascii, "Invalid Characters")
        return False
    return True


def check_if_not_a_weak_pw(pw_common, weak_password_set):
    if pw_common in weak_password_set:
        print_error_message(pw_common, "Too Common")
        return False
    return True


def main():
    weak_password_list_filename = sys.argv[1]
    weak_password_set = set(line.strip() for line in open(weak_password_list_filename))

    for line in sys.stdin:
        password = line.rstrip()
        check_valid_length(password)
        check_valid_ascii_chars(password)
        check_if_not_a_weak_pw(password, weak_password_set)


if __name__ == "__main__":
    main()
