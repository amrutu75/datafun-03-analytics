"""
mrutu_run_all_.py

This script calls all 'get' and 'process' functions from the project modules.
"""

from mrutu_get_csv import main as get_csv_main
from mrutu_get_excel import main as get_excel_main
from mrutu_get_json import main as get_json_main
from mrutu_get_text import main as get_text_main
from mrutu_process_csv import process_csv_file
from mrutu_process_excel import process_excel_file
from mrutu_process_json import process_json_file
from mrutu_process_text import process_text_file

def run_all():
    print("Running all 'get' functions...")
    get_csv_main()
    get_excel_main()
    get_json_main()
    get_text_main()

    print("\nRunning all 'process' functions...")
    process_csv_file()
    process_excel_file()
    process_json_file()
    process_text_file()


if __name__ == "__main__":
    run_all()