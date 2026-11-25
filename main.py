import os

# Your Week in One Line — cap 100.
# The win, the fail and the chaos in one breath; the plant is the punchline.
ENTRY_TEXT = "Shipped 214 fixes, broke prod twice — the week's only green tick was the plant I finally watered."


def main():
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    entry_path = os.path.join(out_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT + "\n")


if __name__ == "__main__":
    main()
