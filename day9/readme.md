# Smart Inventory Mutation Tracker

## Overview

This project shows how inventory data changes when we copy and modify it.
The data is stored as a list of dictionaries with nested details like price, stock, and supplier rating.

---

## Shallow Copy (Simple Idea)

A shallow copy creates a new list, but the inner data is still shared.

So if we change values inside the copied data,
the same change also appears in the original.

**Example:**
Changing price in shallow copy → original price also changes

---

## Deep Copy (Simple Idea)

A deep copy creates a fully separate copy of the data.

 So changes in copied data do not affect the original.

**Example:**
Changing price in deep copy → original stays the same

---

## Personalization Rule

We use the roll number to decide which item to modify.

```python
index = roll_number % len(inventory)
```

Only that index is updated.

**Example:**
Roll number: 601
Inventory size: 2

601 % 2 = 1 → only second item is modified

---

## What the Program Does

* Creates inventory data
* Makes shallow and deep copies
* Modifies copied data
* Compares results
* Shows which copy affected the original

---

## Final Result

* Shallow copy → affects original
* Deep copy → works independently

---

## Conclusion

Shallow copy is not safe for nested data.
Deep copy is better when we want separate and safe changes.
