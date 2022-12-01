Motivation:<br />
One of the first tasks of a Tagger when he/she enter the shift is to load the specific environments based on his/her Tagger number and shift start hour.
As the company go bigger, the number of environments increasing as well, and so the duration of environments loading from the Tagging Status.
The goal of this project is to load those environments automatically.

Guidelines and Notes:<br />

1. GoogleSheetScraping.py file - the main goal of this file is to scrape the complete data from the 'Tagging status' google sheet into python IDE, and provide 
list of the specific environments you need to load. 
The scrape can be done by using the Google API of google sheets and google drive. In order to read and update the data from google spreadsheets in python, you will have to create a Service Account. It is a special type of account that is used to make authorized API calls to Google Cloud Services (Make sure that you have a google account). Once you create credentials for the service account, and download JSON file which contains the keys to access the API, you can read an modify the tagging status spreadsheet. I'm highly recommend to follow the next guide to complete this step:<br /> https://www.analyticsvidhya.com/blog/2020/07/read-and-update-google-spreadsheets-with-python/?<br />
Make sure you add the JSON file name under 'add .json file here' and add the Tagging Status spreadshhet under 'Add Tagging Status here'.<br />
Later you will ask for the shift number of taggers, your own tagger number and the hour the shift starts. Make sure you enter the correct information.<br />
Remember to import the following Libraries - gspread, pandas, oauth2client.service_account 

2. EnvsLoading.py file - the main goal of this file is to get the list of environments which provided by function call 'google_sheet_control()' (from  GoogleSheetScraping.py) and load the environments on the web Timeline automatically.<br />
Its your responsibility to add your Google Chrome path under 'add Chrome path here'.<br />
Remember to import the following Libraries - pyautogui, webbrowser, time.
 
