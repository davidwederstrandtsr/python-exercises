my_books = [{'author': 'Stephen King', 'title': 'The Dark Tower I: The Gunslinger', 'genre': 'Horror'}, 
	{'author': 'Francois Chollet', 'title': 'Deep Learning with Python', 'genre': 'Data Science'}, 
	{'author': 'Ervin Varga', 'title': 'Practical Data Science with Python 3', 'genre': 'Data Science'},
	{'author': 'Eric Matthes', 'title': 'Python Crash Course 2nd Edition', 'genre': 'Data Science'},
	{'author': 'Stephen King', 'title': 'The Dark Tower I: The Drawing of the Three', 'genre': 'Horror'},
	{'author': 'Stephen King', 'title': 'The Dark Tower I: The Waste Lands', 'genre': 'Horror'}]

genre_list = ["Horror", "Data Science"]

for book in my_books:
    print(f"'{book['title']}' by {book['author']} is about {book['genre']}")

print()
print("Your library currently has the following genres:")
print()
print("\tHorror\n\tData Science")
print()

genre_search = input("Enter a genre: ")
genre_search = genre_search.title()

while genre_search not in genre_list:
    print("You entered an invalid genre")
    print("Your library currently have the following genres:")
    print("Horror\nData Science")
    genre_search = input("Enter a genre: ")

for book in my_books:
    if book["genre"] == genre_search:
        print("{:<25}{}".format(book["title"],book["author"]))

