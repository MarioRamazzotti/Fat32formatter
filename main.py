import subprocess
import os


print("Geben sie das Laufwerk , dasss formatiert werden soll wie folgt ein. Suchen sie im explorer ob das Laufwerk erkannt wurde , wenn ja schauen die welchen BUchstaben das Laufwerk hat und geben sie diesen Buchstebn gefolgt von einem : ein")

def format_files(drive):
    try:
        subprocess.run(["attrib", "-R", drive + "\\*.*"], check=True)
        subprocess.run(["del", drive + "\\*.*"], check=True)
        print("Files formatted successfully.")
    except:
        print("No files found to format.")

def format_usb(drive, format_exe):
    try:
        subprocess.run([format_exe, drive, "/FS:FAT32", "/Q"], check=True)
        print("USB drive formatted successfully.")
    except subprocess.CalledProcessError as error:
        if error.returncode == 4:
            print("USB drive already formatted as FAT32.")
            format_files(drive)
        else:
            print("Formatting failed with error code", error.returncode)

def get_format_exe():
    if os.path.isfile("C:\\Windows\\System32\\format.exe"):
        return "C:\\Windows\\System32\\format.exe"
    else:
        return "C:\\Windows\\System32\\format.com"

drive = input("Enter the drive letter (e.g. E:): ")
format_exe = get_format_exe()
format_usb(drive, format_exe)
