items = ["apple", "banana", "orange", "apple", "mango"]

unique_items = set()

for item in items:  # Iterate over the correct list
    if item in unique_items:
        print("Duplicate:", item)
    else:
        unique_items.add(item)  # Add the item to the set if it's not already present
