import json
import logging
import sys
log = logging.getLogger('requests_oauthlib')
log.addHandler(logging.StreamHandler(sys.stdout))
log.setLevel(logging.DEBUG)

import os.path

from google.auth.transport.requests import Request
from google.oauth2 import credentials
from google.oauth2 import service_account
from google_auth_oauthlib.flow import InstalledAppFlow
import googleapiclient.discovery 

# If modifying these scopes, delete the file token.json.
SCOPES = [
    'https://www.googleapis.com/auth/contacts.readonly', 
#    'https://www.googleapis.com/auth/directory.readonly',
#    'https://www.googleapis.com/auth/admin.directory.user'
]

creds = service_account.Credentials.from_service_account_file('minicrm-396015-727d7d82c5a0.json', scopes=SCOPES).with_subject('someusername@some.domain')
print(json.dumps(googleapiclient.discovery.build('people', 'v1', credentials=creds).people().connections().list(resourceName='people/me', pageSize=10, personFields='names,emailAddresses').execute(), indent = 2))

#creds = None
#if os.path.exists('token.json'):
#    creds = credentials.Credentials.from_authorized_user_file('token.json', SCOPES)
#if not creds or not creds.valid:
#    if creds and creds.expired and creds.refresh_token:
#        creds.refresh(Request())
#    else:
#        flow = InstalledAppFlow.from_client_secrets_file('client_secret_309218725468-4sdlo1q90ggrro73fjkvmditvcjuuj0b.apps.googleusercontent.com.json', SCOPES)
#        creds = flow.run_local_server(port=0)
#    with open('token.json', 'w') as token:
#        token.write(creds.to_json())
#print(json.dumps(googleapiclient.discovery.build('admin', 'directory_v1', credentials=creds).users().list(maxResults=100, orderBy='email', customer='C01pvof7d').execute(), indent = 2, ensure_ascii = False))
#print(json.dumps(googleapiclient.discovery.build('people', 'v1', credentials=creds).people().listDirectoryPeople(readMask= 'emailAddresses', sources= ['DIRECTORY_SOURCE_TYPE_DOMAIN_PROFILE'], pageSize= 1000).execute(), indent = 2, ensure_ascii = False))
#print(googleapiclient.discovery.build('people', 'v1', credentials=creds).people().connections().list(resourceName='people/109574715846838467755000', pageSize=10, personFields='names,emailAddresses').execute())
