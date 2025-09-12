import os

# Disk usage (works in CMD)
print("Disk Usage:")
os.system('wmic logicaldisk get size,freespace,caption')

# Uptime (PowerShell command)
print("\nSystem Uptime:")
os.system('powershell -Command "(Get-CimInstance Win32_OperatingSystem).LastBootUpTime"')

# RAM usage (PowerShell command)
print("\nRAM Info:")
os.system('powershell -Command "Get-CimInstance Win32_OperatingSystem | Select-Object TotalVisibleMemorySize, FreePhysicalMemory"')
