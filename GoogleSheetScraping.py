import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
from turtle import Screen


def get_shift_info():
    screen = Screen()
    valid_shift_numbers = ['5', '6']
    valid_tagger_numbers = ['1', '2', '3', '4', '5', '6']
    valid_start_hours = ['00:00', '05:00', '10:00', '15:00', '19:00']
    shift_number_of_taggers = screen.textinput(title="Shift info", prompt="How many tagger in the shift?")
    tagger_number = screen.textinput(title="Shift info", prompt="What your tagger number?")
    start_time = screen.textinput(title="Shift info", prompt="What hour the shift starts?")
    while ((shift_number_of_taggers not in valid_shift_numbers) or (tagger_number not in valid_tagger_numbers)
        or (start_time not in valid_start_hours)):
        shift_number_of_taggers = screen.textinput(title="Shift info", prompt="How many tagger in the shift?")
        tagger_number = screen.textinput(title="Shift info", prompt="What your tagger number?")
        start_time = screen.textinput(title="Shift info", prompt="What hour the shift starts?")
    first_loading_time = list(start_time)
    first_loading_time[3] = '1'
    first_loading_time = ''.join(first_loading_time)
    return  shift_number_of_taggers, tagger_number, first_loading_time


def google_sheet_control():
    # define the scope:
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    # add credentials to the account:
    creds = ServiceAccountCredentials.from_json_keyfile_name('add .json file here', scope)
    # authorize the clientsheet:
    client = gspread.authorize(creds)
    # get the instance of the Spreadsheet:
    sheet = client.open('Add Tagging Status here')
    # get the worksheets of the Spreadsheet:
    six_tagger_sheet = sheet.get_worksheet(0)
    five_tagger_sheet = sheet.get_worksheet(1)
    special_envs_sheet = sheet.get_worksheet(2)
    uninstant_envs_sheet = sheet.get_worksheet(3)
    # get all the records of the data: (we get it as dictionary of: key = column title and values = all cells below)
    six_tagger_shift_records_data = six_tagger_sheet.get_all_records()
    five_tagger_shift_records_data = five_tagger_sheet.get_all_records()
    special_envs_records_data = special_envs_sheet.get_all_records()
    uninstant_envs_records_data = uninstant_envs_sheet.get_all_records()

    # convert the json file to dataframe:
    six_tagger_shift_table = pd.DataFrame.from_dict(six_tagger_shift_records_data)
    five_tagger_shift_table = pd.DataFrame.from_dict(five_tagger_shift_records_data)
    special_envs_table = pd.DataFrame.from_dict(special_envs_records_data)
    uninstant_envs_table = pd.DataFrame.from_dict(uninstant_envs_records_data)

    # convert last two dataframes to list (actually list of lists)
    special_envs_list = special_envs_table.values.tolist()
    uninstant_envs_list = uninstant_envs_table.values.tolist()

    number_of_taggers, tagger_number, first_loading_time = get_shift_info()

    if int(number_of_taggers) == 6:
        i = 0
        six_taggers_shift_list_of_environments = []
        while (i < len(six_tagger_shift_table[f'Tagger {tagger_number}']) and
               six_tagger_shift_table[f'Tagger {tagger_number}'].loc[six_tagger_shift_table.index[i]] != ''):
            six_taggers_shift_list_of_environments.append(
                six_tagger_shift_table[f'Tagger {tagger_number}'].loc[six_tagger_shift_table.index[i]].split()[-1])
            i += 1

        # sort six_taggers_shift_list_of_environments that special envs will be first (for the automation script)
        six_taggers_shift_list_of_environments = sorted(six_taggers_shift_list_of_environments,
                                                        key=lambda env: int(env) in special_envs_list[0], reverse=True)
        return six_taggers_shift_list_of_environments, special_envs_list, uninstant_envs_list, first_loading_time

    else:
        i = 0
        five_taggers_shift_list_of_environments = []
        while (i < len(five_tagger_shift_table[f'Tagger {tagger_number}']) and
               five_tagger_shift_table[f'Tagger {tagger_number}'].loc[five_tagger_shift_table.index[i]] != ''):
            five_taggers_shift_list_of_environments.append(
                five_tagger_shift_table[f'Tagger {tagger_number}'].loc[five_tagger_shift_table.index[i]].split()[-1])
            i += 1

        # sort five_taggers_shift_list_of_environments that special envs will be first (for the automation script)
        five_taggers_shift_list_of_environments = sorted(five_taggers_shift_list_of_environments,
                                                         key=lambda env: int(env) in special_envs_list[0], reverse=True)
        return five_taggers_shift_list_of_environments, special_envs_list, uninstant_envs_list, first_loading_time
