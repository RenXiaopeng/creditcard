#!/usr/bin/python
# -*- coding: UTF-8 -*-

import argparse
import creditcard

def start():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(title='子功能',
                                       description='功能分级',
                                       help='addtional help',
                                       dest='子功能名称')
    parser_addcreditcard = subparsers.add_parser('addcreditcard', help='add a new credit card.')
    parser_addcreditcard.set_defaults(func=addcreditcard)

    all= parser.parse_args()
    all.func(all)

def addcreditcard(args):
    print('start to add a new card...')
    newcard = creditcard.CreditCard()
    newcard.number = input('Input your credit card number: ')
    print(newcard.number)
    print(type(newcard.number))
    newcard.holder_name = input('Input the card holder\'s name: ')
    print(newcard.holder_name)

start()