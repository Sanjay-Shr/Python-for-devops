import shutil
import datetime 
import os
def backup_files(source,destination):
    today = datetime.date.today()
    backup_file_name = os.path.join(destination,f"backup_{today}.tar.gz")
    shutil.make_archive(backup_file_name.replace('.tar.gz',''),'gztar',source)

source = r'C:\Users\asksa\OneDrive\Desktop\Python'
destination = r'C:\Users\asksa\OneDrive\Desktop\Python\backups'
backup_files(source,destination)