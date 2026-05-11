import requests
import csv

def fetch_books():
    base_url = "https://gutendex.com/books/?languages=hu"
    all_books = []
    page = 1
    max_pages = 4

    while base_url and page <= max_pages:
        response = requests.get(base_url)
        if response.status_code != 200:
            print(f"Hiba az API hívásnál: {response.status_code}")
            break

        data = response.json()
        results = data.get("results", [])

        for book in results:
            title = book.get("title", "")
            authors = ", ".join([author.get("name", "") for author in book.get("authors", [])])
            summaries = "\n".join(book.get("summaries", []))
            all_books.append({
                "title": title,
                "authors": authors,
                "summaries": summaries,
                "page": page
            })

        base_url = data.get("next")  # Következő oldal URL-je
        page += 1

    return all_books


def save_to_csv(books, filename="talalatok.csv"):
    if not books:
        print("Nincs adat a mentéshez.")
        return

    with open(filename, mode="w", newline="", encoding="utf-8-sig") as file:  # UTF-8 BOM-mal
        writer = csv.DictWriter(file, fieldnames=["title", "authors", "summaries", "page"])
        writer.writeheader()
        writer.writerows(books)

    print(f"Adatok mentve: {filename}")

# Futtatás
books = fetch_books()
save_to_csv(books)