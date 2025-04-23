import pytest
from src.library_manager import Book, LibraryManager

@pytest.fixture
def empty_library():
    return LibraryManager()

@pytest.fixture
def sample_books():
    return [
        Book(1, "The Hobbit", "J.R.R. Tolkien", 1937, "Fantasy"),
        Book(2, "Pride and Prejudice", "Jane Austen", 1813, "Romance"),
        Book(3, "1984", "George Orwell", 1949, "Dystopian"),
        Book(4, "To Kill a Mockingbird", "Harper Lee", 1960, "Fiction"),
        Book(5, "The Great Gatsby", "F. Scott Fitzgerald", 1925, "Fiction")
    ]

@pytest.fixture
def library_with_books(empty_library, sample_books):
    library = empty_library
    for book in sample_books:
        library.add_book(book)
    return library

class TestBookAddition:
    def test_add_book(self, empty_library, sample_books):
        result = empty_library.add_book(sample_books[0])
        assert result is True
        assert len(empty_library.books) == 1
        assert empty_library.get_book(1) == sample_books[0]

    def test_add_duplicate_book(self, library_with_books, sample_books):
        result = library_with_books.add_book(sample_books[0])

        assert result is False
        assert len(library_with_books.books) == 5

    def test_add_invalid_book(self, empty_library):
        with pytest.raises(TypeError, match="Must be a book"):
            empty_library.add_book("not a book")


class TestBookRetrieval:
    def test_get_existing_book(self, library_with_books, sample_books):
        book = library_with_books.get_book(1)

        assert book == sample_books[0]

    def test_get_nonexistent_book(self, library_with_books):
        book = library_with_books.get_book(999)

        assert book is None


class TestBookRemoval:
    def test_remove_book(self, library_with_books):
        result = library_with_books.remove_book(1)

        assert result is True
        assert len(library_with_books.books) == 4
        assert library_with_books.get_book(1) is None

    def test_remove_nonexistent_book(self, library_with_books):
        result = library_with_books.remove_book(999)

        assert result is False
        assert len(library_with_books.books) == 5

    def test_remove_borrowed_book(self, library_with_books):
        library_with_books.borrow_book(1, "user1")

        with pytest.raises(ValueError, match="Cannot remove a borrowed book"):
            library_with_books.remove_book(1)


class TestBookBorrowing:
    def test_borrow_book(self, library_with_books):
        result = library_with_books.borrow_book(1, "user1")

        assert result is True
        assert library_with_books.books[1].is_borrowed is True
        assert library_with_books.books[1].borrow_count == 1
        assert "user1" in library_with_books.borrowed_books
        assert 1 in library_with_books.borrowed_books["user1"]

    def test_borrow_already_borrowed_book(self, library_with_books):
        library_with_books.borrow_book(1, "user1")
        result = library_with_books.borrow_book(1, "user2")

        assert result is False
        assert "user2" not in library_with_books.borrowed_books

    def test_borrow_nonexistent_book(self, library_with_books):
        with pytest.raises(ValueError, match="Book not found in library"):
            library_with_books.borrow_book(999, "user1")


class TestBookReturning:
    def test_return_book(self, library_with_books):
        library_with_books.borrow_book(1, "user1")
        result = library_with_books.return_book(1, "user1")

        assert result is True
        assert library_with_books.books[1].is_borrowed is False
        assert "user1" not in library_with_books.borrowed_books

    def test_return_not_borrowed_book(self, library_with_books):
        result = library_with_books.return_book(1, "user1")

        assert result is False

    def test_return_book_wrong_borrower(self, library_with_books):
        library_with_books.borrow_book(1, "user1")

        with pytest.raises(ValueError, match="Book was not borrowed by this borrower"):
            library_with_books.return_book(1, "user2")

    def test_return_nonexistent_book(self, library_with_books):
        with pytest.raises(ValueError, match="Book not found in library"):
            library_with_books.return_book(999, "user1")


class TestBookSearch:
    @pytest.mark.parametrize("criteria, expected_count", [
        ({"title": "The"}, 2),
        ({"author": "J.R.R. Tolkien"}, 1),
        ({"year_from": 1930, "year_to": 1960}, 3),
        ({"genre": "Fiction"}, 2),
        ({"title": "The", "genre": "Fantasy"}, 1),
        ({"available_only": True}, 5),
    ])
    def test_search_books(self, library_with_books, criteria, expected_count):
        results = library_with_books.search_books(criteria)

        assert len(results) == expected_count

    def test_search_with_borrowed_books(self, library_with_books):
        library_with_books.borrow_book(1, "user1")

        results = library_with_books.search_books({"available_only": True})
        assert len(results) == 4

        for book in results:
            assert book.is_borrowed is False


class TestLibraryStatistics:
    def test_statistics_empty_library(self, empty_library):
        stats = empty_library.get_statistics()

        assert stats["total_books"] == 0
        assert stats["available_books"] == 0
        assert stats["borrowed_books"] == 0
        assert stats["borrowers_count"] == 0
        assert stats["genres"] == {}
        assert stats["popular_books"] == []

    def test_statistics_with_books(self, library_with_books):
        stats = library_with_books.get_statistics()

        assert stats["total_books"] == 5
        assert stats["available_books"] == 5
        assert stats["borrowed_books"] == 0
        assert stats["borrowers_count"] == 0
        assert len(stats["genres"]) == 4
        assert stats["genres"]["Fiction"] == 2
        assert len(stats["popular_books"]) == 5

    def test_statistics_with_borrowed_books(self, library_with_books):
        library_with_books.borrow_book(1, "user1")
        library_with_books.borrow_book(2, "user1")
        library_with_books.borrow_book(3, "user2")

        library_with_books.borrow_book(4, "user3")
        library_with_books.return_book(4, "user3")
        library_with_books.borrow_book(4, "user3")
        library_with_books.return_book(4, "user3")

        stats = library_with_books.get_statistics()

        assert stats["total_books"] == 5
        assert stats["available_books"] == 2
        assert stats["borrowed_books"] == 3
        assert stats["borrowers_count"] == 3

        assert stats["popular_books"][0].book_id == 4
        assert stats["popular_books"][0].borrow_count == 2