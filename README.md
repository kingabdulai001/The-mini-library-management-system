# 📚 The Mini Library Management System
A lightweight Python library management system for handling books, members, and borrowing operations with robust validation rules.

# ✨ Features
📖 Book Management - Add, search, update, and delete books

👥 Member System - Register and manage library members

🔄 Loan Tracking - Borrow/return books with automatic inventory

# ⚡ Validation Rules - Enforce borrowing limits and data integrity

🔍 Search Function - Find books by title or author

# 🧪 Comprehensive Testing - Full test coverage for all operations

# 🚀 Quick Start
# Installation
bash
git clone <your-repo-url>
cd library_management
No dependencies required! Just Python 3.6+.

# Run Demo
bash
python demo.py
Run Tests
bash
python test.py

# 🛠️ Usage
python
import operations

# Add a book
operations.add_book("9780134853987", "Clean Code", "Robert Martin", "Non-Fiction", 3)

# Register a member  
operations.add_member("MEM001", "Alice Johnson", "alice@email.com")

# Borrow a book
operations.borrow_book("MEM001", "9780134853987")

# Search books
results = operations.search_books('title', 'clean code')
# 📁 Project Structure
File	Purpose
operations.py	Core library logic & data structures
demo.py	Live demonstration of all features
test.py	Comprehensive test suite

# 🏗️ Core Modules
operations.py - The engine of the system:

Data structures for books and members

All CRUD operations with validation

Borrowing/returning logic with limits

Search and utility functions

demo.py - See it in action:

Preloads sample books and members

Demonstrates every feature

Shows real-time status updates

Cleanup and deletion examples

test.py - Quality assurance:

Tests all edge cases

Validates business rules

Ensures data integrity

Prevents regression bugs

# 📊 Supported Genres
Fiction • Non-Fiction • Sci-Fi • Mystery • Biography • History

# 🛡️ Business Rules
Rule	Enforcement
Unique ISBN	No duplicate book IDs
Valid Genres	Predefined categories only
3-Book Limit	Members can't exceed limit
Availability	Only borrow available copies
No Duplicates	Can't borrow same book twice
Safe Deletion	Can't delete borrowed items

# 🧪 Testing
The test suite validates:

✅ Book and member creation

✅ Borrowing/returning workflows

✅ 3-book limit enforcement

✅ Deletion constraints

✅ Error handling

✅ Edge cases

# 🔮 Example Output
text

# ✔ Mini Library Management System Demo

1. Adding Books:
   Adding 'Clean Code': Book added successfully
   Adding 'Design Patterns': Book added successfully

2. Adding Members:
   Adding Alice Johnson: Member added successfully

3. Searching Books:
   Searching for 'code':
   - Clean Code: 3/3 available
     
# 🤝 Contributing
Fork the repository

Create your feature branch (git checkout -b feature/amazing-feature)

Commit your changes (git commit -m 'Add amazing feature')

Push to the branch (git push origin feature/amazing-feature)

Open a Pull Request

# 📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

