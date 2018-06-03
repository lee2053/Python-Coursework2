#jlee_A6_indiv
#Jangwon Lee
#group 8
import xml.etree.ElementTree as ET

# 1.(40 points) Write a function called display_book that prints the title,
#     author, and price of the book with a certain id (passed as a parameter).
#     Example call: display_book(“bk107”)
def display_book(item):
    root = ET.parse(source = "library.xml")
    books = root.iter("book")
    for book in books:
        book_id = book.attrib["id"]
        if book_id == item:
            print("The title:" , book.find("title").text,", Author:", book.find("author").text, ", Price:", "$"+book.find("price").text,", Book id:" ,item,"\n")
        
        
#main
display_book("bk107")

# 2.(30 points) Display the title, author, and price of each Computer book released in December.
def computerbook_Dec():
    root = ET.parse(source = "library.xml")
    books = root.iter("book")
    print("Computer books released in December:")

    for book in books:
        
        date = book.find("publish_date").text
        if "12" in date:
            print("The title:" , book.find("title").text,", Author:", book.find("author").text, ", Price:", "$"+book.find("price").text, ", the date published:", book.find("publish_date").text,"\n")

computerbook_Dec()

# 3.(30 points) Print all the genres in the file.
def genres():
    root = ET.parse(source = "library.xml")
    genres = root.iter("book")
    print("All the genres in the file:")
    genre_list = []
    for genre in genres :
        genre = genre.find("genre").text
        genre_list.append(genre)
    genre_list = sorted(set(genre_list))
    for genre in genre_list:
        print (genre)
    
genres()
