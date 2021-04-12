"""
Example to run the code
"""
from avgdrive.prepare import getdata
from avgdrive.nycavg import calcavg_month, roll_avg


# run this function only if you want to save locally all months of 2020 as parquet.
# getdata(2020)

# # calculate the average trip length of all Yellow Taxis for a month.
s1 = calcavg_month(year=2020, month=1)
print(s1)
# calculate the 45 day rolling average trip length
d = roll_avg(2020, 1, 3)
print(d)
