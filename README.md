# Python Practice

A collection of projects and exercises completed while learning Python through Harvard's CS50P.

This repository documents my progress as I develop my Python programming skills, with a focus on applying what I learn to a business tracker.

## CS50P Projects

### Lecture 0 - Functions, Variables

**Project: Monthly Business Analyzer**

A program that accepts a business name, revenue, and expenses, then calculates profit and profit margin.

**Features:**

- Accepts user input.
- Calculates business profit.
- Calculates profit margin.
- Identifies profit, loss, or break-even status.
- Handles zero revenue to prevent division errors.

**Concepts practiced:**

- Variables and data types
- Functions and return values
- User input
- Arithmetic operations
- Conditional statements
- Formatted strings

[View Monthly Business Analyzer](./practice5.py)

### Lecture 1 - Conditionals

**Project: Business Transaction Classifier**

A program that accepts a transaction description, amount, and type, then classifies the transaction based on its size and validates its type.

**Features:**

- Accepts a transaction description, amount, and type.
- Classifies transactions as small, medium, or large.
- Validates transaction types (income or expense).
- Rejects invalid transaction types.
- Displays formatted transaction information.

**Concepts practiced:**

- Conditional statements
- Comparison operators
- Boolean expressions
- Logical operators
- Functions and return values
- Input validation
- String methods
- Formatted strings

[View Business Transaction Classifier](./lecture%201)

### Lecture 2 - Loops

**Project: Business Expense Analyzer**

A program that collects multiple business expenses, then calculates the total and average expenses.

**Features:**

- Collects multiple expense entries.
- Stops collecting expenses when the user enters 0.
- Calculates total expenses.
- Counts the number of expenses entered.
- Calculates the average expense.
- Handles cases where no expenses are entered.

**Concepts practiced:**

- Loops (`while` and `for`)
- Lists and `range()`
- `break` and `continue`
- Nested loops
- Augmented assignment operators (`+=`)
- Conditional statements
- Running totals and counters

[View Business Expense Analyzer](https://github.com/dantonj/python-practice/blob/main/lecture%202)

### Lecture 3 - Exceptions

**Project: Transaction Recorder**

A program that collects business transaction information, validates user input, and records multiple transactions while handling invalid entries.

**Features:**

- Accepts a business name.
- Collects transaction descriptions, amounts, and types.
- Validates user input.
- Handles invalid numerical input using exception handling.
- Allows users to record multiple transactions.
- Tracks the total number of transactions recorded.

**Concepts practiced:**

- Exception handling
- `try` and `except`
- `ValueError`
- `while` loops
- Conditional statements
- Functions and return values
- Input validation
- Global variables
- Formatted strings

[View Transaction Recorder](./lecture%203)

### Lecture 4 - Libraries

**Project: Financial Data Integration & Analyzer**

A command-line currency converter that retrieves exchange-rate data from the Frankfurter API and calculates conversions based on user-provided currencies and amounts.

**Features:**

- Accepts source currency, target currency, and amount through command-line arguments.
- Retrieves exchange-rate data from an external API.
- Parses JSON responses and extracts exchange rates.
- Calculates converted currency amounts.
- Validates command-line arguments and numerical input.
- Handles request failures, invalid responses, and missing exchange rates.
- Displays a formatted currency conversion report.

**Concepts practiced:**

- External libraries (`requests` and `sys`)
- API requests using `requests.get()`
- Query parameters
- JSON parsing
- Dictionaries and nested data access
- Command-line arguments (`sys.argv`)
- HTTP status codes and `raise_for_status()`
- Exception handling
- Functions and return values
- Program organization using `main()`
- Python entry-point convention (`if __name__ == "__main__"`)

[View Financial Data Integration & Analyzer](./lecture%204)

## Learning Goals

- Develop a strong foundation in Python.
- Learn to work with financial and business datasets.
- Practice writing reusable and organized code.
- Apply programming concepts to real-world analytics projects.

## Progress

- [x] Lecture 0 – Functions, Variables
- [x] Lecture 1 – Conditionals
- [x] Lecture 2 – Loops
- [x] Lecture 3 – Exceptions
- [x] Lecture 4 – Libraries
- [ ] Lecture 5 – Unit Tests
- [ ] Lecture 6 – File I/O
- [ ] Lecture 7 – Regular Expressions
- [ ] Lecture 8 – Object-Oriented Programming
- [ ] Lecture 9 – Et Cetera
