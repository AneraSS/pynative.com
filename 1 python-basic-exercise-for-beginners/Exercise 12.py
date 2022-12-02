# Calculate income tax for the given income by adhering to the below rules

def taxable_income(paycheck):
    if (paycheck-20_000) > 0: # ili: paycheck > 20000
        tax_income= (paycheck-20_000)*0.2+(10_000*0.1)
        return tax_income
    elif (paycheck-10_000) > 0:
        tax_income = (paycheck-10_000)*0.1
        return tax_income
    else:
        tax_income = 0
        return tax_income


print(taxable_income(45000))
print(taxable_income(15000))
print(taxable_income(10000))
print(taxable_income(9000))
print(taxable_income(4500))
