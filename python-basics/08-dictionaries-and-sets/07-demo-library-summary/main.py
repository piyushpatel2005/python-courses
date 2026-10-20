loans = [{"member": "Maya", "book": "Gardening"}, {"member": "Maya", "book": "Cooking"}, {"member": "Luis", "book": "Gardening"}]
members = []
book_counts = {}
for loan in loans:
    members.append(loan["member"])
    book = loan["book"]
    book_counts[book] = book_counts.get(book, 0) + 1
borrowers = len(members)
print(f"{borrowers} members; {book_counts}")
