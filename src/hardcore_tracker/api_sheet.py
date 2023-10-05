from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

import data.constants as constants

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

GW2_HARDCORE_SEASONAL_SIGN_UP_SHEET_ID = constants.GW2_HARDCORE_SEASONAL_SIGN_UP_SHEET_ID
RANGE_OF_API_KEYS_AND_USERNAMES = constants.RANGE_OF_API_KEYS_AND_USERNAMES


def get_all_users():
    """Gets all the users in the spreadsheet for the hardcore season

    Returns a list of all the users by username.#### : API_KEY
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    api_keys = get_gw2_api_keys(creds)
    all_users = map_api_keys(api_keys)
    return all_users

def map_api_keys(list_of_api_keys):
    all_users = {}
    for row in list_of_api_keys:
        all_users[row[1]] = row[0]
    return all_users


def get_gw2_api_keys(creds):
    try:
        service = build('sheets', 'v4', credentials=creds)

        # Call the Sheets API
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=GW2_HARDCORE_SEASONAL_SIGN_UP_SHEET_ID,
                                    range=RANGE_OF_API_KEYS_AND_USERNAMES).execute()
        gw2_api_keys = result.get('values', [])

        if not gw2_api_keys:
            print('No data found.')
            return

        return gw2_api_keys[1:]
    except HttpError as err:
        print(err)