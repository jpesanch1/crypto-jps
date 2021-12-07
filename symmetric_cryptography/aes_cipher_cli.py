#!/usr/bin/env python
from symmetric_cryptography import des_cipher
import argparse


def build_parser():
    my_parser = argparse.ArgumentParser(description="Cipher AES calculator")
    subparsers = my_parser.add_subparsers()

    parse_commands(subparsers)

    return my_parser


def parse_commands(subparsers):
    encryption_commands(subparsers)
    decryption_commands(subparsers)


def encryption_commands(encrypt_subparsers):
    encrypt_parser = encrypt_subparsers.add_parser("encrypt", help="encrypt data with DES algorithm")
    # encrypt_parser.add_argument('encrypt', help="encrypt data with DES algorithm")
    encrypt_parser.add_argument('--message',
                                type=str,
                                required=True,
                                help='message in hexadecimal string to encrypt')
    encrypt_parser.add_argument('--key',
                                type=str,
                                required=True,
                                help='key in hexadecimal string to encrypt')
    encrypt_parser.add_argument('--iv',
                                type=str,
                                required=True,
                                help='initialization vector in hexadecimal string')
    encrypt_parser.set_defaults(func=encryption)


def decryption_commands(decrypt_subparsers):
    decrypt_parser = decrypt_subparsers.add_parser("decrypt", help="encrypt data with DES algorithm")
    decrypt_parser.add_argument('--message',
                                type=str,
                                required=True,
                                help='message in hexadecimal string to decrypt')
    decrypt_parser.add_argument('--key',
                                type=str,
                                required=True,
                                help='key in hexadecimal string to decrypt')
    decrypt_parser.add_argument('--iv',
                                type=str,
                                required=True,
                                help='initialization vector in hexadecimal string')
    decrypt_parser.set_defaults(func=decryption)


def encryption(args):
    print(des_cipher.encrypt(args.message, args.key, args.iv))


def decryption(args):
    print(des_cipher.decrypt(args.message, args.key, args.iv))







