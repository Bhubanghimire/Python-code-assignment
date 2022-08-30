def ryerson_letter_grade(pct):
    if 0 <= pct <= 49:
        return "F"

    elif 50 <= pct <= 52:
        return "D-"

    elif 53 <= pct <= 56:
        return "D"

    elif 57 <= pct <= 59:
        return "D+"

    elif 60 <= pct <= 62:
        return "C-"

    elif 63 <= pct <= 66:
        return "C"

    elif 67 <= pct <= 69:
        return "C+"

    elif 70 <= pct <= 72:
        return "B-"

    elif 73 <= pct <= 76:
        return "B"

    elif 77 <= pct <= 79:
        return "B+"

    elif 80 <= pct <= 84:
        return "A-"

    elif 85 <= pct <= 89:
        return "A"

    elif 90 <= pct:
        return "A+"


pct = int("62")
result = ryerson_letter_grade(pct)
print("result is ", result)