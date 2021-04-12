import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
from prepare import getdata


def calcavg_month(year: int, month: int):
    if not 2018 <= year <= 2020:
        raise ValueError("Please provide a Year as integer and between 2018-2020!")
    if not 1 <= month <= 12:
        raise ValueError("Please provide months as integer or between 1 and 12!")
    df = pq.read_pandas(f'nyc_yellow{year}-{month}.parquet',
                        columns=['tpep_pickup_datetime', 'tpep_dropoff_datetime', 'trip_distance']).to_pandas()
    month_avg = df['trip_distance'].mean()
    return f"Average Trip length for the input {year}-{month} is " + str(round(month_avg, 2)) + " miles"



def roll_avg(year: int, start_month: int, end_month: int):
    appended_data = []
    if not 2018 <= year <= 2020:
        raise ValueError("Please provide a Year between 2018-2020")
    if not 1 <= start_month <= 12 and 1 <= end_month <= 12:
        raise ValueError("Please provide months as integer")
    if start_month > end_month:
        raise ValueError("you provided end_month earlier than start_month!")
    for month in range(start_month, end_month+1):
        df = pq.read_pandas(f'nyc_yellow{year}-{month}.parquet',
                            columns=['tpep_pickup_datetime', 'trip_distance']).to_pandas()
        df['tpep_pickup_datetime'] = pd.to_datetime(df.tpep_pickup_datetime)
        df['date'] = df.tpep_pickup_datetime.dt.date
        mean_per_day = df.groupby('date').mean()
        # store DataFrame in list
        appended_data.append(mean_per_day)

    appended_data = pd.concat(appended_data)
    roll45mean = appended_data.trip_distance.rolling(window=45).mean()
    return roll45mean


# d = roll_avg(2020, 1, 3)
# print(d)

# print(calcavg_month(2018, 13))
