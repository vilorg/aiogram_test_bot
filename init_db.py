import sqlite3


def main():
    con = sqlite3.connect("tutorial.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS word(word TEXT, is_ii INTEGER)")
    with open("words.txt", "r") as f:
        while True:
            line = f.readline()
            if line == "end":
                break
            if line == "\n":
                continue
            line = line.replace("\n", "")
            cur.execute("INSERT INTO word VALUES (?, ?)", (line, 0))
    with open("ii.txt", "r") as f:
        while True:
            line = f.readline()
            if line == "end":
                break
            if line == "\n":
                continue
            line = line.replace("\n", "")
            cur.execute("INSERT INTO word VALUES (?, ?)", (line, 1))
    cur.execute("CREATE TABLE IF NOT EXISTS person(user_id INTEGER, is_admin INTEGER)")
    con.commit()


if __name__ == "__main__":
    main()
