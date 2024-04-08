# Add days to a date in Python

from datetime import datetime, date, timedelta

my_str = '09-24-2023'  # 👉️ (mm-dd-yyyy)
date_1 = datetime.strptime(my_str, '%m-%d-%Y')

print(date_1)  # 👉️ 2023-09-24 00:00:00

# ✅ Add 3 days to a date
result = date_1 + timedelta(days=3)
print(result)  # 👉️ 2023-09-27 00:00:00