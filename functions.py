import pandas as pd
import numpy as np
import os
from dotenv import load_dotenv


load_dotenv()
BANK_ONE = os.getenv('BANK_ONE')
BANK_TWO = os.getenv('BANK_TWO')


## Bank One

def get_bank_one_month(month: str):
    savings = get_bank_one_saving(month)
    credit = get_bank_one_saving(month)
    checking = get_bank_one_checking(month)
    file = pd.concat([savings, credit, checking])
    return file


def get_bank_one_saving(month: str) -> pd.DataFrame:
    try:
        savings:pd.DataFrame = pd.read_csv(
            f"statements/{BANK_ONE}/savings/{BANK_ONE}_savings_{month}.csv",
            usecols=["Date", "Description", "Category", "Amount"],
            dtype={"Date":str, "Description": str, "Category":str, "Amount": float}
        )
        savings["Category"] = savings["Category"].fillna("Payment")
        return savings
    except:
        print(f"Bank one savings file for {month} doesn't exist")
    return None


def get_bank_one_credit(month: str) -> pd.DataFrame:
    try:
        credit:pd.DataFrame = pd.read_csv(
            f"statements/{BANK_ONE}/credit/{BANK_ONE}_credit_{month}.csv",
            usecols=["Date", "Description", "Category", "Amount"],
            dtype={"Date":str, "Description": str, "Category":str, "Amount": float}
        )
        credit["Category"] = credit["Category"].fillna("Payment")
        return credit
    except:
        print(f"Bank one credit file for {month} doesn't exist")
    return None



def get_bank_one_checking(month: str) -> pd.DataFrame:
    try:
        checking:pd.DataFrame = pd.read_csv(
            f"statements/{BANK_ONE}/checking/{BANK_ONE}_checking_{month}.csv",
            usecols=["Date", "Description", "Category", "Amount"],
            dtype={"Date":str, "Description": str, "Category":str, "Amount": float}
        )
        checking["Category"] = checking["Category"].fillna("Payment")
        return checking
    except:
        print(f"Bank one checking file for {month} doesn't exist")
    return None


def get_bank_one_spending(month: str) -> float:
    savings = get_bank_one_saving(month)
    checking = get_bank_one_checking(month)
    credit = get_bank_one_credit(month)

    savings_total = get_spent_negative(savings)
    checking_total = get_spent_negative(checking)
    credit_total = get_spent_positive(credit)

    return savings_total + checking_total + credit_total


def get_bank_one_category_spending(month: str):
    statement = get_bank_one_month(month)

    categories_amount_dict = get_categories_amount(statement)

    return categories_amount_dict


## Bank Two
def get_bank_two_month(month: str) -> pd.DataFrame:
    credit = get_bank_two_credit(month)
    return credit


def get_bank_two_credit(month: str) -> pd.DataFrame:
    try:
        statement = pd.read_csv(
            f"statements/{BANK_TWO}/{BANK_TWO}_{month}.CSV",
            usecols=["Transaction Date", "Description", "Category", "Amount"],
            dtype={"Transaction Date":str, "Description": str, "Category":str, "Amount": float}
        )
        return statement
    except:
        print(f"Bank two credit file for {month} doesn't exist")
    return None



def get_bank_two_spending(month: str) -> float:
    credit = get_bank_two_credit(month)

    credit_total = get_spent_negative(credit)

    return credit_total


## Helper functions
def get_spent_negative(file:pd.DataFrame) -> float:
    statement = file
    total = 0
    for transaction in statement["Amount"]:
        if transaction < 0:
            total -= transaction
    return total


def get_spent_positive(file:pd.DataFrame) -> float:
    statement = file
    total = 0
    for transaction in statement["Amount"]:
        if transaction > 0:
            total += transaction
    return total


def get_categories_amount(*files: pd.DataFrame) -> dict[str,float]:
    categories_amount_dict:dict[str,float] = dict()
    for file in files:
        categorized = categorize(file)
        categories_amount_dict.update(categorized)
    return categories_amount_dict


def categorize(file: pd.DataFrame) -> dict[str,float]:
    category_dict:ditct[stf,float] = dict()
    for x in range(len(file)):
        category = file["Category"][x]
        amount = file["Amount"][x]
        if amount < 0:
            amount = -(amount)
        if category not in category_dict.keys():
            category_dict.update({category:amount})
        else:
            category_dict[category] += amount
    return category_dict


def combine_categorized_spending(*categorized_spendings:dict[str,float]) -> dict[str,float]:
    combined_categorized_spending = dict()
    for dt in categorized_spendings:
        combined_categorized_spending.update(dt)
    
    return combined_categorized_spending


def print_catogorized_spending(categorized_spending:dict[str,float]):
    for key in categorized_spending.keys():
        print(f"{key}: {categorized_spending[key]:.2f}")
