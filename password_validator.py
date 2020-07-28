#!/usr/bin/env python3

import sys

weak_password_list_filename = sys.argv[1]
weak_password_set = set(line.strip() for line in open(weak_password_list_filename))


def replace_non_printable(text, replacement):
    return ''.join([i if ord(i) < 128 else replacement for i in text])


def print_validation_message(pw, message):
    print(replace_non_printable(pw, '*') + " -> Error: " + message)


def validate_length(pw_length):
    if len(pw_length) < 8:
        print_validation_message(pw_length, "Too Short")
    if len(pw_length) > 64:
        print_validation_message(pw_length, "Too Long")


def validate_ascii_chars(pw_ascii):
    if not pw_ascii.isascii():
        print_validation_message(pw_ascii, "Invalid Characters")


def check_if_a_weak_pwd(pw_weak):
    if pw_weak in weak_password_set:
        print_validation_message(pw_weak, "Too Common")


for line in sys.stdin:
    password = line.rstrip()
    validate_length(password)
    validate_ascii_chars(password)
    check_if_a_weak_pwd(password)
