import os
import datetime
# def check_cpu(command):
#     print(os.system(command))

# def check_date(command):
#     print(os.system(command))

# def check_ram(command):
#     print(os.system)(command)

def run_command(command):
    return os.system(command)

# run_command("date")
# run_command("df -h")
def show_date():
    return datetime.datetime.today()

today = show_date()
print(today)