import streamlit as st
import json   # Stores and loads the library data in a file
import os     # Helps in checking whether the file exists

st.set_page_config(page_title="Personal Library Manager", page_icon="📘", layout="wide")

st.title("📚 Personal Library Manager")
st.subheader("By YOhAli Azam")

# File to store book data 
LIBRARY_FILE = "yoha_books.json"

# function to load library data
# LIBRARY_FILE is a string variable that stores the filename "yoha_books.json"
def load_library():
    if os.path.exists(LIBRARY_FILE):
        with open(LIBRARY_FILE, "r") as file:
            return json.load(file)
    return []   
 
# Function to save library data
def save_library(library):
    with open(LIBRARY_FILE, "w") as file:
# Save data permanently data remains available even after restarting the app 
        json.dump(library, file, indent=4)

# keep exixting books by empty list
library = load_library()

# side bar
# .radio() is best for short lists few options.
# st.selectbox() is better when you have many choices 10+ options.
menu = st.sidebar.radio("📖 Library Menu", ["📥 Add Book", "📥 Remove Book", "🔍 Search Book", "📚 View Library", "📊 Library Stats"])

# Add a Book
if menu == "📥 Add Book":
    st.header("➕ Add a Book")
    title = st.text_input("📖 Book Title")
    author = st.text_input("✍️ Author")
    year = st.number_input("📅 Publication Year", min_value=1000, max_value=2025, step=1)
    genre = st.text_input("🏷 Genre")
    read_status = st.radio("📘 Read Status", ["Read", "Unread"])

    if st.button("➕ Add a Book"):
        new_book = {
            "title": title,
            "author": author,
            "year": year,
            "genre": genre,
            "read_status": read_status
        }
        library.append(new_book) # append
        save_library(library)    # save
        st.success(f"📚 {title} Added to your Library!")

# Remove a Book
elif menu == "📥 Remove Book":
    st.header("🗑 Remove a Book")
    if not library:
        st.warning("No books found in the library.")
    else:
        #  Creates a new list with only the book titles
        book_titles = [book["title"] for book in library] 
        book_remove = st.selectbox("Select a book to remove", book_titles)
        if st.button("❌ Remove a Book"):
            library = [book for book in library if book["title"] != book_remove]
            save_library(library)
            st.success(f"📚 {book_remove} has been removed.")

# Search for a Book
elif menu == "🔍 Search Book":
    st.header("🔎 Search for a Book")
    search_by = st.radio("🔍 Search by", ["Title", "Author"])
    search_term = st.text_input(f"Enter {search_by}")

    if st.button("🔍 Search"):
        results = [book for book in library if search_term.lower() in book[search_by.lower()].lower()]
        if results:
            st.write("### 📚 Search Results:")
            st.table(results)
    # Displays results as a table using st.table(results), making it easy to read
        else:
            st.warning(f"No books found matching '{search_term}'.")

# View all Books
elif menu == "📚 View Library":
    st.header("📚 Your Book Collection")
    if library:
        st.table(library)
    else:
        st.warning("No books in the library.")

# Library Stats
elif menu == "📊 Library Stats":
    st.header("📊 Library Stats")
    total_books = len(library)
    read_books = sum(1 for book in library if book["read_status"] == "Read")
    percent_read = (read_books / total_books * 100) if total_books else 0

    st.write(f"📚 **Total Books:** {total_books}")
    st.write(f"✅ **Books Read:** {read_books} ({percent_read:.2f}%)")
