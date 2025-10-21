"""
Unit tests for Mini Library Management System
"""
import operations


def test_add_book():
    """Test adding books"""
    # Reset data
    operations.books.clear()

    # Test valid book addition
    success, message = operations.add_book("1234567890", "Python Programming", "John Doe", "Non-Fiction", 5)
    assert success == True
    assert message == "Book added successfully"
    assert "1234567890" in operations.books

    # Test duplicate ISBN
    success, message = operations.add_book("1234567890", "Another Book", "Jane Doe", "Fiction", 3)
    assert success == False
    assert "already exists" in message

    # Test invalid genre
    success, message = operations.add_book("0987654321", "Invalid Book", "Author", "InvalidGenre", 2)
    assert success == False
    assert "Invalid genre" in message

    print("✓ All add_book tests passed!")


def test_add_member():
    """Test adding members"""
    # Reset data
    operations.members.clear()

    # Test valid member addition
    success, message = operations.add_member("M001", "Alice Smith", "alice@email.com")
    assert success == True
    assert message == "Member added successfully"
    assert len(operations.members) == 1

    # Test duplicate member ID
    success, message = operations.add_member("M001", "Bob Brown", "bob@email.com")
    assert success == False
    assert "already exists" in message

    print("✓ All add_member tests passed!")


def test_borrow_return_book():
    """Test borrowing and returning books"""
    # Reset data
    operations.books.clear()
    operations.members.clear()

    # Setup test data
    operations.add_book("1111111111", "Test Book", "Test Author", "Fiction", 2)
    operations.add_member("M001", "Test Member", "test@email.com")

    # Test successful borrow
    success, message = operations.borrow_book("M001", "1111111111")
    assert success == True
    assert "borrowed successfully" in message

    # Test borrowing same book again
    success, message = operations.borrow_book("M001", "1111111111")
    assert success == False
    assert "already borrowed" in message

    # Test successful return
    success, message = operations.return_book("M001", "1111111111")
    assert success == True
    assert "returned successfully" in message

    print("✓ All borrow/return tests passed!")


def test_borrow_limit():
    """Test borrowing limit of 3 books per member"""
    # Reset data
    operations.books.clear()
    operations.members.clear()

    # Setup test data
    operations.add_member("M001", "Test Member", "test@email.com")
    operations.add_book("1111111111", "Book 1", "Author 1", "Fiction", 1)
    operations.add_book("2222222222", "Book 2", "Author 2", "Non-Fiction", 1)
    operations.add_book("3333333333", "Book 3", "Author 3", "Sci-Fi", 1)
    operations.add_book("4444444444", "Book 4", "Author 4", "Mystery", 1)

    # Borrow 3 books
    operations.borrow_book("M001", "1111111111")
    operations.borrow_book("M001", "2222222222")
    operations.borrow_book("M001", "3333333333")

    # Try to borrow fourth book
    success, message = operations.borrow_book("M001", "4444444444")
    assert success == False
    assert "borrow limit" in message

    print("✓ All borrow limit tests passed!")


def test_delete_with_borrowed_items():
    """Test deletion when items are borrowed"""
    # Reset data
    operations.books.clear()
    operations.members.clear()

    # Setup test data
    operations.add_book("1111111111", "Test Book", "Test Author", "Fiction", 1)
    operations.add_member("M001", "Test Member", "test@email.com")
    operations.borrow_book("M001", "1111111111")

    # Try to delete book with borrowed copies
    success, message = operations.delete_book("1111111111")
    assert success == False
    assert "copies are currently borrowed" in message

    # Try to delete member with borrowed books
    success, message = operations.delete_member("M001")
    assert success == False
    assert "borrowed books" in message

    print("✓ All deletion constraint tests passed!")


if __name__ == "__main__":
    test_add_book()
    test_add_member()
    test_borrow_return_book()
    test_borrow_limit()
    test_delete_with_borrowed_items()
    print("\n🎉 All tests passed!")