import methods

statement = methods.get_bank_one_month('june')
print('Printing statement:\n')
print(statement)

category_spending = methods.get_categories_amount_two(statement)
print('Printing category spedning:\n')
print(category_spending)
