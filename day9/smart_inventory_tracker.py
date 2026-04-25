import copy

from script5 import analyze_data


def create_inventory():
    return [
        {
            "item": "Laptop",
            "details": {"price": 50000, "stock": 10, "supplier": {"rating": 4.5}}
        },
        {
            "item": "Phone",
            "details": {"price": 20000, "stock": 25, "supplier": {"rating": 4.2}}
        }
    ]

def apply_discount(data, roll):
    index = roll % len(data)

    for i in range(len(data)):
        if i == index:
            data[i]["details"]["price"] = int(data[i]["details"]["price"] * 0.9)
            data[i]["details"]["stock"] -= 2

def compare_data(org, modified):
    changed = 0
    same = 0

    for i in range(len(org)):
        if org[i] == modified[i]:
            same += 1
        else:
            changed += 1

    return changed, same

def analyze_changes(original, shallow_copy, deep_copy):
    print("\nAnalysis:")

    if original == shallow_copy:
        print("Shallow Copy affected original data.")
        print("Reason: Nested dictionaries are shared (same reference).")

    else:
        print("Shallow Copy did NOT affect original.")

    if original != deep_copy:
        print("Deep Copy remained independent.")
        print("Reason: Deep copy creates a separate copy of all nested data.")
    else:
        print("Deep Copy affected original (unexpected).")

    print("\nExample:")
    print("If price is changed in shallow copy → original price also changes.")
    print("If price is changed in deep copy → original remains unchanged.")

roll_number = 601
original = create_inventory()
shallow_copy = copy.copy(original)
deep_copy = copy.deepcopy(original)

apply_discount(shallow_copy, roll_number)
apply_discount(deep_copy, roll_number)

print("Original Data:")
print(original)

print("\nShallow Copy:")
print(shallow_copy)

print("\nDeep Copy:")
print(deep_copy)

print("\nDifferences Observed:")
print("Shallow Result (change,same):", compare_data(original, shallow_copy))
print("Deep Result: (change,same)", compare_data(original, deep_copy))

analyze_changes(original, shallow_copy,deep_copy)
#Tuple summary
shallow_result= compare_data(original, shallow_copy)
deep_result= compare_data(original, deep_copy)

print("\nTuple summary:")
print("Shallow Result (changed_items_count, unchanged_items_count):", shallow_result)
print("Deep Result (changed_items_count, unchanged_items_count):", deep_result)

print(original)
