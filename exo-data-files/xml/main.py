from bs4 import BeautifulSoup
import os


def get_file_directory(file_path):
    return os.path.dirname(os.path.abspath(file_path))
exec_dir = get_file_directory(__file__)


with open(f"{exec_dir}/data.xml","r") as input:
    xml = input.read()

soup = BeautifulSoup(xml, features="xml")
books = soup.find_all("book")

# Chercher celui qui a pour titre "1984"
for book in books:
    title = book.find("title").text
    if title == "1984":
        author = book.find("author").text
        year = book.find("year").text
        price = book.find("price").text
        genre = book.find("genre").text
        print(f"Titre: {title}")
        print(f"Auteur: {author}")
        print(f"Année: {year}")
        print(f"Prix: {price}")
        print(f"Genre: {genre}")
        break