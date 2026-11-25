"""One-Line Laugh-Off — entry for make.fun.

Writes one line to /output/entry.txt.
"""
import os

# The joke: my calendar is so packed it needs a meeting about being packed.
TEXT = "My calendar is so full it just scheduled a meeting to discuss how full my calendar is."

def write_entry():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")

def main():
    write_entry()

if __name__ == "__main__":
    main()
