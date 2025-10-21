"""
Mini Library Management System
Operations module containing all core functions
"""

# Data Structures
books = {}  # Dictionary: ISBN -> book details
members = []  # List of dictionaries for members
valid_genres = ('Fiction', 'Non-Fiction', 'Sci-Fi', 'Mystery', 'Biography', 'History')  # Tuple


# Book Management Functions
def add_book(isbn, title, author, genre, total_copies):
    """
    Add a book if ISBN is unique and genre is valid
    """
    if isbn in books:
        return False, "Book with this ISBN already exists"

    if genre not in valid_genres:
        return False, f"Invalid genre. Must be one of: {valid_genres}"

    books[isbn] = {
        'title': title,
        'author': author,
        'genre': genre,
        'total_copies': total_copies,
        'available_copies': total_copies,
        'borrowed_by': []  # List of member IDs who borrowed this book
    }
    return True, "Book added successfully"


def search_books(search_by, keyword):
    """
    Search books by title or author
    """
    results = []
    keyword = keyword.lower()

    for isbn, book in books.items():
        if search_by == 'title' and keyword in book['title'].lower():
            results.append((isbn, book))
        elif search_by == 'author' and keyword in book['author'].lower():
            results.append((isbn, book))

    return results


def update_book(isbn, **kwargs):
    """
    Update book details
    """
    if isbn not in books:
        return False, "Book not found"

    book = books[isbn]
    allowed_fields = ['title', 'author', 'genre', 'total_copies']

    for field, value in kwargs.items():
        if field in allowed_fields:
            if field == 'genre' and value not in valid_genres:
                return False, f"Invalid genre. Must be one of: {valid_genres}"
            book[field] = value

    return True, "Book updated successfully"


def delete_book(isbn):
    """
    Delete book only if no copies are borrowed
    """
    if isbn not in books:
        return False, "Book not found"

    book = books[isbn]
    if len(book['borrowed_by']) > 0:
        return False, "Cannot delete book - copies are currently borrowed"

    del books[isbn]
    return True, "Book deleted successfully"


# Member Management Functions
def add_member(member_id, name, email):
    """
    Add a member if ID is unique
    """
    for member in members:
        if member['member_id'] == member_id:
            return False, "Member ID already exists"

    members.append({
        'member_id': member_id,
        'name': name,
        'email': email,
        'borrowed_books': []  # List of ISBNs borrowed by this member
    })
    return True, "Member added successfully"


def update_member(member_id, **kwargs):
    """
    Update member details
    """
    member = None
    for m in members:
        if m['member_id'] == member_id:
            member = m
            break

    if not member:
        return False, "Member not found"

    allowed_fields = ['name', 'email']
    for field, value in kwargs.items():
        if field in allowed_fields:
            member[field] = value

    return True, "Member updated successfully"


def delete_member(member_id):
    """
    Delete member only if they have no borrowed books
    """
    member = None
    for m in members:
        if m['member_id'] == member_id:
            member = m
            break

    if not member:
        return False, "Member not found"

    if len(member['borrowed_books']) > 0:
        return False, "Cannot delete member - they have borrowed books"

    members.remove(member)
    return True, "Member deleted successfully"


# Borrow/Return Functions
def borrow_book(member_id, isbn):
    """
    Member can borrow up to 3 books if available
    """
    # Find member
    member = None
    for m in members:
        if m['member_id'] == member_id:
            member = m
            break

    if not member:
        return False, "Member not found"

    # Check if book exists
    if isbn not in books:
        return False, "Book not found"

    book = books[isbn]
    # Check member's borrow limit
    if len(member['borrowed_books']) >= 3:
        return False, "Member has reached borrow limit (3 books)"

    # Check book availability
    if book['available_copies'] <= 0:
        return False, "No copies available for borrowing"

    # Check if member already borrowed this book
    if isbn in member['borrowed_books']:
        return False, "Member already borrowed this book"

    # Process borrowing
    member['borrowed_books'].append(isbn)
    book['borrowed_by'].append(member_id)
    book['available_copies'] -= 1

    return True, "Book borrowed successfully"


def return_book(member_id, isbn):
    """
    Return borrowed book
    """
    # Find member
    member = None
    for m in members:
        if m['member_id'] == member_id:
            member = m
            break

    if not member:
        return False, "Member not found"

    # Check if book exists
    if isbn not in books:
        return False, "Book not found"

    book = books[isbn]

    # Check if member borrowed this book
    if isbn not in member['borrowed_books']:
        return False, "Member hasn't borrowed this book"

    # Process return
    member['borrowed_books'].remove(isbn)
    book['borrowed_by'].remove(member_id)
    book['available_copies'] += 1

    return True, "Book returned successfully"


# Utility Functions
def get_all_books():
    """Return all books"""
    return books


def get_all_members():
    """Return all members"""
    return members


def get_valid_genres():
    """Return valid genres tuple"""
    return valid_genres


def get_member_borrowed_books(member_id):
    """Get books borrowed by a member"""
    for member in members:
        if member['member_id'] == member_id:
            return member['borrowed_books']
    return []
