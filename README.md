NYC Yellow Taxi Challenge:
================================

#### Disclaimer:
*For this challenge i used the data "as-is" from the website. During my analysis i saw some data quality issues, which delivers averages for a certain month with a date outside of the month. But the data quality issues is not the focus here. We assume IF data quality is perfect, current issues would not be visible.*

### Remark:

For this challenge, it is known that the datasets are quite huge. Storing the data as parquet was for me the logical consequence to better work with it.

Normally, this would be stored on a Blob Storage, but since i wanted to work locally i stored the parquet files locally. But the calculation logic shouldn't need drastic changes, if a Blob Storage should be used instead.

If new data is stored the same way like i did (naming convention), the code could also run new incoming data for 2021 onwards.
Of course in an enterprise setup there would be a different architecture for how to save and store the data and also insuring a good data quality.

Here an example how it could look like, since the size of the NYC Yellow Taxi dataset is for my taste too big for a traditional SQL database.

### insert picture


### Some thoughts on scaling if data size does not fit into one machine
- Blob Storage
- Scalable environment to the run the pipeline