#!/usr/bin/env python
import argparse

from symmetric_cryptography import des_cipher_cli, aes_cipher_cli, hash_cli


def build_parser():
    my_parser = argparse.ArgumentParser(description="Symmetric Cryptography")
    subparsers = my_parser.add_subparsers()

    parse_commands(subparsers)

    return my_parser


def parse_commands(subparsers):
    des_cipher_commands(subparsers)
    aes_cipher_commands(subparsers)
    hash_commands(subparsers)


def des_cipher_commands(subparsers):
    subparsers.add_parser("des", help="DES algorithm")
    des_cipher_cli.parse_commands(subparsers)


def aes_cipher_commands(subparsers):
    subparsers.add_parser("aes", help="AES algorithm")
    aes_cipher_cli.build_parser()


def hash_commands(subparsers):
    subparsers.add_parser("hash", help="Hash functions")
    hash_cli.build_parser()









