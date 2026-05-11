from typing import NamedTuple


class Book(NamedTuple):
    name: str       # exactly as it appears in the KJV CSV (Roman numeral prefixes)
    testament: str  # "OT" or "NT"
    genre: str


# Canonical order, 66 books. Names match the scrollmapper KJV CSV exactly.
BOOKS: tuple[Book, ...] = (
    # ── Old Testament ──────────────────────────────────────────────────────────

    # Pentateuch
    Book("Genesis",          "OT", "Pentateuch"),
    Book("Exodus",           "OT", "Pentateuch"),
    Book("Leviticus",        "OT", "Pentateuch"),
    Book("Numbers",          "OT", "Pentateuch"),
    Book("Deuteronomy",      "OT", "Pentateuch"),

    # History
    Book("Joshua",           "OT", "History"),
    Book("Judges",           "OT", "History"),
    Book("Ruth",             "OT", "History"),
    Book("I Samuel",         "OT", "History"),
    Book("II Samuel",        "OT", "History"),
    Book("I Kings",          "OT", "History"),
    Book("II Kings",         "OT", "History"),
    Book("I Chronicles",     "OT", "History"),
    Book("II Chronicles",    "OT", "History"),
    Book("Ezra",             "OT", "History"),
    Book("Nehemiah",         "OT", "History"),
    Book("Esther",           "OT", "History"),

    # Wisdom
    Book("Job",              "OT", "Wisdom"),
    Book("Psalms",           "OT", "Wisdom"),
    Book("Proverbs",         "OT", "Wisdom"),
    Book("Ecclesiastes",     "OT", "Wisdom"),
    Book("Song of Solomon",  "OT", "Wisdom"),

    # Major Prophets
    Book("Isaiah",           "OT", "Major Prophets"),
    Book("Jeremiah",         "OT", "Major Prophets"),
    Book("Lamentations",     "OT", "Major Prophets"),
    Book("Ezekiel",          "OT", "Major Prophets"),
    Book("Daniel",           "OT", "Major Prophets"),

    # Minor Prophets
    Book("Hosea",            "OT", "Minor Prophets"),
    Book("Joel",             "OT", "Minor Prophets"),
    Book("Amos",             "OT", "Minor Prophets"),
    Book("Obadiah",          "OT", "Minor Prophets"),
    Book("Jonah",            "OT", "Minor Prophets"),
    Book("Micah",            "OT", "Minor Prophets"),
    Book("Nahum",            "OT", "Minor Prophets"),
    Book("Habakkuk",         "OT", "Minor Prophets"),
    Book("Zephaniah",        "OT", "Minor Prophets"),
    Book("Haggai",           "OT", "Minor Prophets"),
    Book("Zechariah",        "OT", "Minor Prophets"),
    Book("Malachi",          "OT", "Minor Prophets"),

    # ── New Testament ──────────────────────────────────────────────────────────

    # Gospel
    Book("Matthew",          "NT", "Gospel"),
    Book("Mark",             "NT", "Gospel"),
    Book("Luke",             "NT", "Gospel"),
    Book("John",             "NT", "Gospel"),

    # History
    Book("Acts",             "NT", "History"),

    # Pauline Epistles
    Book("Romans",           "NT", "Pauline Epistle"),
    Book("I Corinthians",    "NT", "Pauline Epistle"),
    Book("II Corinthians",   "NT", "Pauline Epistle"),
    Book("Galatians",        "NT", "Pauline Epistle"),
    Book("Ephesians",        "NT", "Pauline Epistle"),
    Book("Philippians",      "NT", "Pauline Epistle"),
    Book("Colossians",       "NT", "Pauline Epistle"),
    Book("I Thessalonians",  "NT", "Pauline Epistle"),
    Book("II Thessalonians", "NT", "Pauline Epistle"),
    Book("I Timothy",        "NT", "Pauline Epistle"),
    Book("II Timothy",       "NT", "Pauline Epistle"),
    Book("Titus",            "NT", "Pauline Epistle"),
    Book("Philemon",         "NT", "Pauline Epistle"),

    # General Epistles
    Book("Hebrews",          "NT", "General Epistle"),
    Book("James",            "NT", "General Epistle"),
    Book("I Peter",          "NT", "General Epistle"),
    Book("II Peter",         "NT", "General Epistle"),
    Book("I John",           "NT", "General Epistle"),
    Book("II John",          "NT", "General Epistle"),
    Book("III John",         "NT", "General Epistle"),
    Book("Jude",             "NT", "General Epistle"),

    # Apocalyptic
    Book("Revelation of John", "NT", "Apocalyptic"),
)

# O(1) lookup by name
BOOK_INDEX: dict[str, Book] = {b.name: b for b in BOOKS}
