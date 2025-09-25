import array

# Sample Data
ledger = [
    {'id': 1, 'name': 'Groceries', 'value': 150},
    {'id': 2, 'name': 'Utilities', 'value': 120},
    {'id': 3, 'name': 'Rent', 'value': 1000},
    {'id': 4, 'name': 'Internet', 'value': 60},
    {'id': 5, 'name': 'Entertainment', 'value': 200},
]

# -------- Integers: Compute total, average, min, and max --------
values = [item['value'] for item in ledger]
total = sum(values)
average = total / len(values)
minimum = min(values)
maximum = max(values)

# -------- Strings: Formatted output --------
report = (
    f"Total Household Expenses: ${total}\n"
    f"Average Expense: ${average:.2f}\n"
    f"Minimum Expense: ${minimum}\n"
    f"Maximum Expense: ${maximum}\n"
)
print("===== Formatted Report =====")
print(report)

# -------- Booleans: Threshold check --------
threshold = 300
if average > threshold and maximum > 2 * threshold:
    print("Status: Significantly Above Standard")
elif average > threshold:
    print("Status: Above Standard")
else:
    print("Status: Below Standard")

# -------- Lists: Add, remove, sort --------
ledger.append({'id': 6, 'name': 'Subscriptions', 'value': 80})  # Add new
ledger = [item for item in ledger if item['value'] > 50]        # Remove items under $50
ledger.sort(key=lambda x: x['value'])                           # Sort by value

print("\n===== Sorted Ledger (After Add/Remove) =====")
for item in ledger:
    print(item)

# -------- Arrays: Using array module --------
value_array = array.array('i', values)
array_sum = sum(value_array)
print(f"\nSum from array: {array_sum} (Compare with list sum: {total})")

# -------- Dictionaries: Update, delete, compute total --------
# Update
ledger[0]['value'] = 160  # Update the first record's value

# Delete
del ledger[1]  # Remove the second item

# Total after modifications
new_total = sum(item['value'] for item in ledger)

print(f"\nUpdated Total After Modifications: ${new_total}")
