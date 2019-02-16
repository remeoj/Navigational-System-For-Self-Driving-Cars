import gspread
from oauth2client.service_account import ServiceAccountCredentials
import time

# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('Navi_secret.json', scope)
client = gspread.authorize(creds)

# Database Parameters
sheet_index = 0
CAR_ONE_SPEED_ROW = 2
CAR_ONE_SPEED_COLUMN = 2
CAR_TWO_SPEED_ROW = 2
CAR_TWO_SPEED_COLUMN = 5

# Car Parameters
carOneRow = 2
CAR_ONE_COLUMN = 1
carTwoRow = 2
CAR_TWO_COLUMN = 4

# While Loop Parameter
continue_reading = True

# Time Parameters
startTime1 = endTime1 = timeDif1 = time.time()
startTime2 = endTime2 = timeDif2 = time.time()

# Distance Parameters
DISTANCE = 0.0254

sheet = client.open("Database").get_worksheet(sheet_index)

if sheet.cell(carOneRow, CAR_ONE_COLUMN).value != "":
    startTime1 = time.time()

if sheet.cell(carTwoRow, CAR_TWO_COLUMN).value != "":
    startTime2 = time.time()

while continue_reading:

    # Detects changes and updates speed value for Car One
    if sheet.cell(carOneRow, CAR_ONE_COLUMN).value != "":
        endTime1 = time.time()
        timeDif1 = endTime1 - startTime1

        # Updates speed cell in Google Sheets to make current speed available for any calculations
        sheet.update_cell(CAR_ONE_SPEED_ROW, CAR_ONE_SPEED_COLUMN, DISTANCE/timeDif1)

        # Resets the start time and shifts if function focus to next empty cell to get the future time difference
        startTime1 = time.time()
        carOneRow += 1

    # Detects changes and updates speed value for Car Two
    if sheet.cell(carTwoRow, CAR_TWO_COLUMN).value != "":
        endTime2 = time.time()
        timeDif2 = endTime2 - startTime2
        sheet.update_cell(CAR_TWO_SPEED_ROW, CAR_TWO_SPEED_COLUMN, DISTANCE / timeDif2)
        startTime2 = time.time()
        carTwoRow += 1

print("test")
