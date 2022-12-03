
from GoogleSheetScraping import google_sheet_control
from EnvsLoading import run_environments

environments_list, special_envs_list, uninstant_envs_list, start_time = google_sheet_control()
run_environments(environments_list, special_envs_list, uninstant_envs_list, start_time)