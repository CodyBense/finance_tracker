import methods

def main():
    # total_bank_one = methods.get_bank_one_spending('june')
    # total_bank_two = methods.get_bank_two_spending('june')
    # total = methods.get_combine_spending(total_bank_one, total_bank_two)
    # bank_one_categories = methods.get_bank_one_category_spending('june')
    # print(f"Bank one monthly total: {total_bank_one:.2f}")
    # print(f"Bank two monthly total: {total_bank_two:.2f}")
    # print(f"Monthly total: {total:.2f}")
    # print(f"Bank one transaction amount per category\n{bank_one_categories}")
    category_amount_dict = methods.get_categories_amount('june')
    print(category_amount_dict)

if __name__ == "__main__":
    main()
