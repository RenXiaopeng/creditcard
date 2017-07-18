#!/usr/bin/python
# -*- coding: UTF-8 -*-

class CreditCard:

    def __int__(self, number, bank, card_property, last_four_number, validity, three_number, holder_name, accountant_bill_date, due_date, fixed_account, available_account):
        self.number = number
        self.bank = bank
        self.card_property = card_property
        self.last_four_number = last_four_number
        self.validity = validity
        self.three_number = three_number
        self.holder_name = holder_name
        self.accountant_bill_date = accountant_bill_date
        self.due_date = due_date
        self.fixed_account = fixed_account
        self.available_account = available_account

    def displayCardBasicInfo(self):
        print("卡号：", self.number, "\n")
        print("所属银行：", self.bank, "\n")
        print("卡片类型：", self.card_property, "\n")
        print("持卡人：", self.holder_name, "\n")
        print("账单日：", self.accountant_bill_date, "\n")
        print("还款日：", self.due_date, "\n")
        print("固定额度：", self.fixed_account, "\n")
        print("可用额度：", self.available_account, "\n")

