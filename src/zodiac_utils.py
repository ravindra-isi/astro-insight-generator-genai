from datetime import datetime

ZODIAC_RANGES = {
    "Capricorn": ((12, 22), (1, 19)),  # Note: Special handling needed for Capricorn's year crossover
    "Aquarius": ((1, 20), (2, 18)),
    "Pisces": ((2, 19), (3, 20)),
    "Aries": ((3, 21), (4, 19)),
    "Taurus": ((4, 20), (5, 20)),
    "Gemini": ((5, 21), (6, 20)),
    "Cancer": ((6, 21), (7, 22)),
    "Leo": ((7, 23), (8, 22)),
    "Virgo": ((8, 23), (9, 22)),
    "Libra": ((9, 23), (10, 22)),
    "Scorpio": ((10, 23), (11, 21)),
    "Sagittarius": ((11, 22), (12, 21)),
   
}

def get_zodiac(birth_date: str) -> str:
    """Input: '1995-08-20' → Output: 'Leo'"""
    month, day = map(int, birth_date.split("-")[1:])
    for sign, ((start_m, start_d), (end_m, end_d)) in ZODIAC_RANGES.items():
        if (month == start_m and day >= start_d) or (month == end_m and day <= end_d):
            return sign
    return "Unknown"
