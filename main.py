import methods

def main():
    total_bank_one = methods.get_bank_one_spending('june')
    total_bank_two = methods.get_bank_two_spending('june')
    total = methods.get_combine_spending(total_bank_one, total_bank_two)
    print(f"Bank one monthly total: {total_bank_one:.2f}")
    print(f"Bank two monthly total: {total_bank_two:.2f}")
    print(f"Monthly total: {total:.2f}")

if __name__ == "__main__":
    main()
