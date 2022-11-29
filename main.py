import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
import pyautogui
import webbrowser

from GoogleSheetScraping import google_sheet_control
from EnvsLoading import run_environments

environments_list, special_envs_list, uninstant_envs_list, start_time = google_sheet_control()
run_environments(environments_list, special_envs_list, uninstant_envs_list, start_time)