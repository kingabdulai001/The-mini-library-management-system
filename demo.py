"""
Demo script showing Mini Library Management System usage
"""
import operations


def demo_library_system():
    print("🚀 Mini Library Management System Demo")
    print("=" * 50)

    # Add some books
    print("\n1. Adding Books:")
    books_to_add = [
        ("9780134853987", "Clean Code", "Robert Martin", "Non-Fiction", 3),
        ("9780201633610", "Design Patterns", "Gamma et al.", "Non-Fiction", 2),
        ("9780451524935", "1984", "George Orwell", "Fiction", 4),
        ("9780441013593", "Dune", "Frank Herbert", "Sci-Fi", 3)
    ]

    for isbn, title, author, genre, copies in books_to_add:
        success, message = operations.add_book(isbn, title, author, genre, copies)
        print(f"   Adding '{title}': {message}")

    # Add some members
    print("\n2. Adding Members:")
    members_to_add = [
        ("MEM001", "Alice Johnson", "alice@email.com"),
        ("MEM002", "Bob Smith", "bob@email.com"),
        ("MEM003", "Carol Davis", "carol@email.com")
    ]

    for member_id, name, email in members_to_add:
        success, message = operations.add_member(member_id, name, email)
        print(f"   Adding {name}: {message}")

    # Search for books
    print("\n3. Searching Books:")
    print("   Searching for 'code':")
    results = operations.search_books('title', 'code')
    for isbn, book in results:
        print(f"     - {book['title']} by {book['author']}")

    print("   Searching for author 'Orwell':")
    results = operations.search_books('author', 'orwell')
    for isbn, book in results:
        print(f"     - {book['title']} by {book['author']}")

    # Borrow books
    print("\n4. Borrowing Books:")
    borrow_operations = [
        ("MEM001", "9780134853987"),
        ("MEM001", "9780201633610"),
        ("MEM002", "9780451524935"),
        ("MEM001", "9780441013593")  # Third book for MEM001
    ]

    for member_id, isbn in borrow_operations:
        success, message = operations.borrow_book(member_id, isbn)
        book_title = operations.books[isbn]['title'] if isbn in operations.books else "Unknown"
        print(f"   {member_id} borrowing '{book_title}': {message}")

    # Try to borrow beyond limit
    print("\n5. Testing Borrow Limit:")
    success, message = operations.borrow_book("MEM001", "9780451524935")
    print(f"   MEM001 trying to borrow fourth book: {message}")

    # Return a book
    print("\n6. Returning a Book:")
    success, message = operations.return_book("MEM001", "9780134853987")
    book_title = operations.books["9780134853987"]['title']
    print(f"   MEM001 returning '{book_title}': {message}")

    # Update book information
    print("\n7. Updating Book:")
    success, message = operations.update_book("9780134853987", total_copies=5)
    print(f"   Updating 'Clean Code' copies to 5: {message}")

    # Show current status
    print("\n8. Current Library Status:")
    print(f"   Total books: {len(operations.books)}")
    print(f"   Total members: {len(operations.members)}")

    print("\n   Books in library:")
    for isbn, book in operations.books.items():
        print(f"     - {book['title']}: {book['available_copies']}/{book['total_copies']} available")

    print("\n   Member borrowing status:")
    for member in operations.members:
        print(f"     - {member['name']}: {len(member['borrowed_books'])} books borrowed")

    # Delete operations (when no borrowed items)
    print("\n9. Cleanup Operations:")
    # Return all books first
    for member in operations.members:
        for isbn in member['borrowed_books'][:]:
            operations.return_book(member['member_id'], isbn)

    # Now delete
    success, message = operations.delete_book("9780134853987")
    print(f"   Deleting 'Clean Code': {message}")

    success, message = operations.delete_member("MEM003")
    print(f"   Deleting member Carol Davis: {message}")

    print("\n" + "=" * 50)
    print("✅ Demo completed successfully!")


if __name__ == "__main__":
    demo_library_system()