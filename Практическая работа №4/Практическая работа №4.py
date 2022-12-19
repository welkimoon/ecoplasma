def read_file (filename: str):
    words = set()
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            [words.add(word.lower()) for word in line.split()]
    return words
def save_file (filename: str, words) -> None:
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"Всего уникальных слов: {len(words)}\n")
        f.write("\n".join(words))


words = read_file("DS.txt")
save_file("DS.txt", sorted(words))