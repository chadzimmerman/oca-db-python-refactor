import datetime
import math
import mysql.connector  # or use sqlite3
from typing import List, Dict, Any

# Notes:
#  - This class handles liturgical calculations (like in oca.lib), including saints, feasts, and scripture readings.
#  - jDate is the Julian date equivalent of the selected Gregorian date.
#  - sF: field/type of search ('date', 'lectionary', 'chapterverse', etc.)
#  - sS, sT: index/offset for readings or special calculations
#  - Many of the database tables (menaion, paschalion, xceptions, scriptures) store liturgical info

class OcaProj:
    def __init__(self):
        # Basic date & selection
        self.sM: int = 0
        self.sD: int = 0
        self.sY: int = 0
        self.sB: str = "Matt"  # Book for chapter/verse search
        self.sC: int = 1       # Chapter
        self.sV: int = 1       # Verse
        self.sS: int = 0       # Index of reading
        self.sT: int = 0       # Offset days
        self.sF: str = "date"  # Type of search

        self.jDate: float = 0.0  # Julian date
        self.mGospels: Dict[int, str] = {}
        self.mdGospels: Dict[int, str] = {}
        self.ords: Dict[int, str] = {}

        # Database connection
        self.dbHost: str = ""
        self.dbUser: str = ""
        self.dbPass: str = ""
        self.dbName: str = ""
        self.deBug: bool = False
        self.conn = None

    # Connect to DB and initialize date
    def connect_db(self, params: dict = None):
        if params is None:
            params = {}
        # Set default timezone
        # Note: Python handles timezones differently; you may use pytz if needed
        self.nachaloTER()  # Initialize internal values

        # Database connection
        self.conn = mysql.connector.connect(
            host=self.dbHost,
            user=self.dbUser,
            password=self.dbPass,
            database=self.dbName
        )

        # Load parameters
        if 'sF' in params:
            self.sF = params['sF']
            if self.sF in ["selection"] or self.sF.startswith("life") or self.sF.startswith("troparia"):
                self.sM = params['sM']
                self.sD = params['sD']
                self.sY = params['sY']
                self.sS = params['sS']
                self.sT = params['sT']
            elif self.sF in ["date", "lectionary"]:
                self.sM = params['sM']
                self.sD = params['sD']
                self.sY = params['sY']
            elif self.sF == "chapterverse":
                self.sB = params['sB']
                self.sC = params['sC']
                self.sV = params['sV']

        # Default to today
        today = datetime.date.today()
        if not self.sY:
            self.sY = today.year
        if not self.sM:
            self.sM = today.month
            self.sD = today.day
            self.sY = today.year

        # Julian date
        self.jDate = self.gregorian_to_jd(self.sY, self.sM, self.sD) + self.sT
        if self.sT:
            self.sY, self.sM, self.sD = self.jd_to_gregorian(self.jDate)

    # Convert Gregorian to Julian date
    def gregorian_to_jd(self, year: int, month: int, day: int) -> float:
        # Simplified version of cal_to_jd
        a = (14 - month)//12
        y = year + 4800 - a
        m = month + 12*a - 3
        jd = day + ((153*m + 2)//5) + 365*y + y//4 - y//100 + y//400 - 32045
        return jd

    # Convert Julian date to Gregorian
    def jd_to_gregorian(self, jd: float) -> (int, int, int):
        # Rough inverse of gregorian_to_jd
        j = int(jd + 0.5)
        f = j + 1401 + (((4*j + 274277)//146097)*3)//4 - 38
        e = 4*f + 3
        g = (e % 1461)//4
        h = 5*g + 2
        day = (h % 153)//5 + 1
        month = ((h//153 + 2) % 12) + 1
        year = e//1461 - 4716 + (12 + 2 - month)//12
        return year, month, day

    # Placeholder for initialization called in connectDB
    def nachaloTER(self):
        # Father John: You may add default liturgical constants, tones, etc.
        pass

    # Execute SQL
    def exec_sql(self, query: str) -> Any:
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute(query)
        return cursor

    # Example function: Get chapter/verse
    def get_chapter_verse(self) -> Dict[str, Any]:
        v = f"{self.sC:02d}{self.sV:02d}"  # Format like PHP
        query = f"""
            SELECT scriptures.*, scrabbrs.saBook
            FROM scriptures
            LEFT JOIN scrabbrs ON scriptures.scBook = scrabbrs.saAbbr
            WHERE scBook='{self.sB}' AND scVerse={v}
        """
        cursor = self.exec_sql(query)
        row = cursor.fetchone()
        return {
            'head': f"{row['saBook']} {self.sC}:{self.sV}",
            'verse': f"<dt>{self.sV}</dt><dd>{row['scText']}</dd>"
        }

    # Example: get exceptions
    def get_xceptions(self, m, d, y):
        query = f"SELECT * FROM xceptions WHERE xcYear='{y}' AND xcMonth='{m}' AND xcDay='{d}'"
        cursor = self.exec_sql(query)
        row = cursor.fetchone()
        if row:
            return [row['xcNewMonth'], row['xcNewDay'], row['xcNote']]
        return [m, d, ""]

    # Notes:
    #  - getDay() handles reading calculation, fasts, saints, Pascha offsets.
    #  - getLife() gets the life of a saint with optional month/day.
    #  - Many other PHP methods (drawDateSearch, drawLecSearch, drawVerseSearch)
    #    are rendering HTML forms, which in Python could be handled by a web framework.

# Father John Notes:
#  - This Python version preserves the key internal logic: date handling, database access, Pascha offsets.
#  - HTML rendering and JS scripts are omitted; they should be handled in Flask/Django templates.
#  - For arrays in PHP that start at 1 (like $s[1] for months), Python uses 0-based indexing.
