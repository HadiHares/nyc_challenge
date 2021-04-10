import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq


def getdata(year: int):
    """
    A helper function to retrieve data and save it locally as parquet file.

    Args:
        Year which should be retrieved.

    Returns:
        saves for each month a parquet file on local drive.
    """

    for month in range(1, 13):
        if month < 10:
            linkurl = f"http://s3.amazonaws.com/nyc-tlc/trip+data/yellow_tripdata_{year}-0{month}.csv"
        elif month >= 10:
            linkurl = f"http://s3.amazonaws.com/nyc-tlc/trip+data/yellow_tripdata_{year}-{month}.csv"

        df = pd.read_csv(linkurl, sep=',')

        table = pa.Table.from_pandas(df)
        pq.write_table(table, f"nyc_yellow{year}-{month}.parquet")
