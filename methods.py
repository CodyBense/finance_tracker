import pandas as pd
import numpy as np
import os
from dotenv import load_dotenv

load_dotenv()
BANK_ONE = os.getenv('BANK_ONE')
BANK_TWO = os.getenv('BANK_TWO')


## Bank One

# Get the relavent data from the statement form bank one
def get_bank_one_month(month):
    savings = get_bank_one_month_savings(month)
    credit = get_bank_one_month_credit(month)
    checking = get_bank_one_month_checking(month)
    file = pd.concat([savings, credit, checking])
    return file


# Get the relavent data from savings account
def get_bank_one_month_savings(month):
    savings = pd.read_csv(f"statements/{BANK_ONE}/savings/{BANK_ONE}_savings_{month}.csv", usecols=["Date", "Description", "Category", "Amount"])
    return savings


# Get the relavent data from credit account
def get_bank_one_month_credit(month):
    credit = pd.read_csv(f"statements/{BANK_ONE}/credit/{BANK_ONE}_credit_{month}.csv", usecols=["Date", "Description", "Category", "Amount"])
    return credit


# Get the relavent data from checking account
def get_bank_one_month_checking(month):
    checking = pd.read_csv(f"statements/{BANK_ONE}/checking/{BANK_ONE}_checking_{month}.csv", usecols=["Date", "Description", "Category", "Amount"])
    return checking


# Get the relavent data from the non savings accounts from bank one
def get_bank_one_spending_statement(month):
    credit = pd.read_csv(f"statements/{BANK_ONE}/credit/{BANK_ONE}_credit_{month}.csv", usecols=["Date", "Description", "Category", "Amount"])
    checking = pd.read_csv(f"statements/{BANK_ONE}/checking/{BANK_ONE}_checking_{month}.csv", usecols=["Date", "Description", "Category", "Amount"])
    file = pd.concat([credit, checking])
    return file


# Get the spending data from bank one
def get_bank_one_spending(month):
    savings = get_bank_one_month_savings(month)
    checking = get_bank_one_month_checking(month)
    credit = get_bank_one_month_credit(month)

    savings_total = get_spent_negative_total(savings)
    checking_total = get_spent_negative_total(checking)
    credit_total = get_spent_positive_total(credit)

    return savings_total + checking_total + credit_total


# Get spending data per category
def get_bank_one_category_spending(month):
    statement = get_bank_one_month(month)

    categories_amount_dict = get_categories_amount(statement)

    return categories_amount_dict


## Bank Two

# Get that relavent data from the statement from bank two
def get_bank_two_month(month):
    file = pd.read_csv(f"statements/{BANK_TWO}/{BANK_TWO}_{month}.CSV", usecols=["Transaction Date", "Description", "Category", "Amount"])
    file.rename(columns={'Transaction Date': 'Date'}, inplace=True)
    return file


# Get the spending data from bank two
def get_bank_two_spending(month):
    bank_two_statement = get_bank_two_month(month)

    return get_spent_negative_total(bank_two_statement)


## Both Banks

# Get the total spending from both banks
def get_combine_spending(bank_one_spending, bank_two_spending):
    return bank_one_spending + bank_two_spending


# Combine the data from all statements from both banks
def get_combine_statements(statement_one, statement_two):
    file = pd.concat([statement_one, statement_two])
    return file


## Helper functions

# Use if the amount spend is represented by a positive number
def get_spent_positive_total(file):
    total = 0
    for transaction in file["Amount"]:
        if transaction > 0:
            total += transaction
    return total


# Use if the amount spent is represented by a negative number
def get_spent_negative_total(file):
    total = 0
    for transaction in file["Amount"]:
        if transaction < 0:
            total -= transaction
    return total


def get_categories_amount(month):
    file = get_bank_two_month(month)
    categories_amount_dict = dict()
    for x in range(len(file)):
        category = file["Category"][x]
        amount = float(file["Amount"][x])
        print(category)
        print(amount)
        if category not in categories_amount_dict.keys():
            categories_amount_dict.update({category:amount})
        else:
            categories_amount_dict[category] += amount
    return categories_amount_dict


def test(month):
    statement = get_bank_two_month(month)
    # for transaction in statement["Date"]:
    #     print()
    len_statement = len(statement)
    print(len_statement)
    for x in range(len_statement):
        print(statement["Amount"][x])
