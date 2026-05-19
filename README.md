# Expense Tracker

A simple CLI-based Expense Tracker built with Python.

This project was created as a **1-Day Programming Challenge** to practice core Python fundamentals through building a complete small-scale application instead of isolated exercises.

---

## 📅 Challenge Information

**Challenge Date:** May 19, 2026
**Challenge Type:** One-Day Project Challenge
**Status:** Completed Successfully ✅

---

## 🎯 Project Goal

The purpose of this project was to strengthen practical Python programming skills by building a small real-world style application using only foundational Python concepts.

The focus was on:

* program flow
* data organization
* file handling
* validation
* reusable functions
* CLI interaction

without relying on advanced libraries or frameworks.

---

## 🧠 Concepts Practiced

This project heavily uses:

* Functions
* Lists
* Dictionaries
* Loops
* Conditional Statements
* File Handling
* String Formatting
* Exception Handling
* Data Persistence
* Basic State Management

---

## ⚙️ Features

### ✅ Add Expense

Allows the user to enter:

* Expense Name
* Category
* Amount

The expense is stored inside a list using dictionaries.

---

### ✅ View Expenses

Displays all saved expenses in a clean formatted structure.

Example:

```text
Food           | Burger         | 25.5
Transport      | Taxi           | 12
```

---

### ✅ Save To File

Saves all expenses into a text file using custom formatting.

---

### ✅ Load From File

Loads saved expenses from the file back into the program.

---

### ✅ Input Validation

Handles invalid numeric input using exception handling.

---

## 📂 Project Structure

```text
expense_tracker/
│
├── main.py
├── expenses.txt
└── README.md
```

---

## 🗂️ Data Structure

Each expense is stored as a dictionary:

```python
{
    "Name": "Burger",
    "Category": "Food",
    "Amount": 25.5
}
```

All expenses are stored inside a list during runtime.

---

## 🚀 What This Project Helped Practice

This project was designed to transition from:

* small isolated exercises

to:

* building complete interactive programs

It helped practice:

* organizing logic across functions
* handling user input continuously
* saving/loading application state
* managing structured data
* building a simple CLI application flow

---

## 📌 Notes

This project intentionally avoids:

* databases
* JSON
* external libraries
* GUI frameworks

to focus completely on strengthening core Python fundamentals first.

---

## 🔮 Possible Future Improvements

Potential future upgrades include:

* Search System
* Expense Statistics
* Sorting Expenses
* Delete Expense Feature
* Category Analytics
* CSV Export
* Multi-file Refactoring

---

## 🏁 Final Result

The challenge was successfully completed within one day and achieved its main goal:

> building a fully functional small-scale Python application using core programming fundamentals.
