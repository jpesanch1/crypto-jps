#!/usr/bin/env python
import argparse


def build_parser():
    my_parser = argparse.ArgumentParser(description="Hash calculator")
    subparsers = my_parser.add_subparsers()

    parse_commands(subparsers)

    return my_parser


def parse_commands(subparsers):
    calculate_commands(subparsers)
    verify_commands(subparsers)


def calculate_commands(subparsers):
    parser = subparsers.add_parser("calculate", help="calculate hash for message")
    parser.add_argument('--algorithm',
                        type=str,
                        required=True,
                        help='hash algorithm')
    parser.add_argument('--message',
                        type=str,
                        required=True,
                        help='message in hexadecimal string')
    parser.set_defaults(func=calculate)


def verify_commands(subparsers):
    parser = subparsers.add_parser("verify", help="verify hash for a message")
    parser.add_argument('--algorithm',
                        type=str,
                        required=True,
                        help='hash algorithm')
    parser.add_argument('--message',
                        type=str,
                        required=True,
                        help='message in hexadecimal string')
    parser.add_argument('--hash',
                        type=str,
                        required=True,
                        help='hash to verify')
    parser.set_defaults(func=verify)


def calculate(args):
    print("Hash calculate")


def verify(args):
    print("Hash verify")
