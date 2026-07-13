"""
Convert every time expression in text to 24-hour HH:MM format.
Handles: "4:00 PM", "nineteen hundred", "four o'clock", "19:00", "1900 hours".
"""
import re

# Word -> number lookup for spelled-out hours
WORDS = {
    "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6,
    "seven": 7, "eight": 8, "nine": 9, "ten": 10, "eleven": 11, "twelve": 12,
    "thirteen": 13, "fourteen": 14, "fifteen": 15, "sixteen": 16,
    "seventeen": 17, "eighteen": 18, "nineteen": 19, "twenty": 20,
    "twenty-one": 21, "twenty-two": 22, "twenty-three": 23,
}
WORD_PATTERN = "|".join(sorted(WORDS, key=len, reverse=True))


def normalize_times(text):
    if not isinstance(text, str):
        return text

    # "4:00 PM" or "4:00pm" -> "16:00"
    def fix_meridiem(m):
        hour, minute, ampm = int(m.group(1)), int(m.group(2)), m.group(3).lower()
        if ampm.startswith("p") and hour != 12:
            hour += 12
        elif ampm.startswith("a") and hour == 12:
            hour = 0
        return f"{hour:02d}:{minute:02d}"
    text = re.sub(r"\b(1[0-2]|0?[1-9]):([0-5]\d)\s*([ap]\.?m\.?)\b",
                  fix_meridiem, text, flags=re.IGNORECASE)

    # "nineteen hundred" -> "19:00"
    def fix_word_military(m):
        return f"{WORDS[m.group(1).lower()]:02d}:00"
    text = re.sub(rf"\b({WORD_PATTERN})\s+hundred\b(?:\s+hours?)?",
                  fix_word_military, text, flags=re.IGNORECASE)

    # "1900 hours" -> "19:00"
    def fix_num_military(m):
        return f"{int(m.group(1)):02d}:{int(m.group(2)):02d}"
    text = re.sub(r"\b([01]\d|2[0-3])([0-5]\d)\s*hours?\b",
                  fix_num_military, text, flags=re.IGNORECASE)

    # "seven o'clock PM" -> "19:00", "four o'clock" -> "04:00"
    def fix_oclock(m):
        hour = WORDS[m.group(1).lower()]
        ampm = m.group(2)
        if ampm and ampm.lower().startswith("p") and hour != 12:
            hour += 12
        return f"{hour:02d}:00"
    text = re.sub(rf"\b({WORD_PATTERN})\s+o[\u2018\u2019\u0027`]?clock\b(?:\s*([ap]\.?m\.?))?",
                  fix_oclock, text, flags=re.IGNORECASE)

    # Already-formatted "19:00" or "4:00" -> zero-pad to "19:00" / "04:00"
    def fix_existing(m):
        return f"{int(m.group(1)):02d}:{int(m.group(2)):02d}"
    text = re.sub(r"\b(\d{1,2}):([0-5]\d)\b", fix_existing, text)

    return text
