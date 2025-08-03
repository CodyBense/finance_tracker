import functions

def main():
    bank_one_credit = functions.get_bank_one_credit('june')
    bank_one_saving = functions.get_bank_one_saving('june')
    bank_one_checking = functions.get_bank_one_checking('june')
    bank_one_cateogry_spending = functions.get_categories_amount(
        bank_one_credit,
        bank_one_saving,
        bank_one_checking
    )
    print("Bank one")
    functions.print_catogorized_spending(bank_one_cateogry_spending)

    bank_two_credit = functions.get_bank_two_month('june')
    bank_two_category_spending = functions.get_categories_amount(bank_two_credit)
    print(f"\nBank two")
    functions.print_catogorized_spending(bank_two_category_spending)

    print(f"\nCombined")
    combined_category_spending = functions.combine_categorized_spending(bank_one_cateogry_spending, bank_two_category_spending)
    functions.print_catogorized_spending(combined_category_spending)

if __name__ == "__main__":
    main()
