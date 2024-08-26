KGP_WEBSITE_URL = "http://www.iitkgp.ac.in/"
DEPT_FETCH_URL = "https://www.iitkgp.ac.in/Departments/fetchAllFacListByDept"
TIMETABLE_FETCH_URL = (
    "https://erp.iitkgp.ac.in/Acad/timetable_track.jsp?action=second&dept=%s"
)
DEFAULT_REQUEST_HEADERS = {
    "timeout": "20",
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:58.0) Gecko/20100101 Firefox/58.0",
}
DEPARTMENT_CODES = [
    "AE",
    "AF",
    "AG",
    "AI",
    "AR",
    "AT",
    "BE",
    "BM",
    "BS",
    "BT",
    "CD",
    "CE",
    "CH",
    "CL",
    "CR",
    "CS",
    "CY",
    "DE",
    "DH",
    "EC",
    "EE",
    "EF",
    "ES",
    "ET",
    "FH",
    "GG",
    "GS",
    "HS",
    "ID",
    "IM",
    "IP",
    "IT",
    "KS",
    "MA",
    "ME",
    "MI",
    "MM",
    "MS",
    "MT",
    "NA",
    "NT",
    "PH",
    "RD",
    "RE",
    "RJ",
    "RO",
    "RT",
    "RW",
    "RX",
    "SD",
    "SE",
    "SH",
    "SL",
    "TS",
    "WM",
]

SLOTS_COORDINATE_MAP = {
    "A2": [(0, 0), (0, 1)],
    "A3": [(0, 0), (0, 1), (1, 4)],
    "B2": [(1, 0), (1, 1)],
    "B3": [(0, 3), (1, 0), (1, 1)],
    "C2": [(2, 0), (2, 1)],
    "C3": [(0, 2), (2, 0), (2, 1)],
    "C4": [(0, 2), (2, 0), (2, 1), (3, 2)],
    "D2": [(1, 2), (1, 3)],
    "D3": [(0, 4), (1, 2), (1, 3)],
    "D4": [(0, 4), (1, 2), (1, 3), (3, 0)],
    "E2": [(4, 1), (4, 2)],
    "E3": [(2, 4), (3, 3), (4, 1)],
    "E4": [(2, 4), (3, 3), (4, 1), (4, 2)],
    "F2": [(4, 3), (4, 4)],
    "F3": [(2, 2), (3, 1), (4, 3)],
    "F4": [(2, 2), (3, 1), (4, 3), (4, 4)],
    "G3": [(2, 3), (3, 4), (4, 0)],
    "H2": [(1, 7), (1, 8)],
    "H3": [(0, 5), (1, 7), (1, 8)],
    "I2": [(3, 5), (4, 7)],
    "J": [(0, 5), (0, 6), (0, 7)],
    "K": [(1, 2), (1, 3), (1, 4)],
    "L": [(1, 5), (1, 6), (1, 7)],
    "M": [(3, 2), (3, 3), (3, 4)],
    "N": [(3, 5), (3, 6), (3, 7)],
    "O": [(4, 2), (4, 3), (4, 4)],
    "P": [(4, 5), (4, 6), (4, 7)],
    "Q": [(0, 2), (0, 3), (0, 4)],
    "R": [(2, 2), (2, 3), (2, 4)],
    "S3": [(0, 8), (3, 8), (4, 8)],
    "U2": [(0, 6), (0, 7)],
    "U3": [(0, 6), (0, 7), (1, 6)],
    "U4": [(0, 6), (0, 7), (1, 5), (1, 6)],
    "V2": [(3, 6), (3, 7)],
    "V3": [(3, 6), (3, 7), (4, 6)],
    "V4": [(3, 6), (3, 7), (4, 5), (4, 6)],
    "X": [(2, 5), (2, 6), (2, 7), (2, 8)],
    "X4": [(2, 5), (2, 6), (2, 7), (2, 8)],
}
"""This is a map of timetable slot names to time slot coordinates on the central timetable.
- The first coordinate represents the day (0: Monday, 4: Friday)
- The second coordinate represents the time (0: 8-9, 8: 5-6) excluding 1-2 lunch hour

This has to be updated if the central timetable format is changed.

Note: This data was initially parsed from the now deprecated `data/slots.1` file.
"""