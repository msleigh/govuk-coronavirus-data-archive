# GOV.UK Coronavirus dashboard data

Automatically downloads and archives data used by the Coronavirus Dashboard

## To run

The `download.py` script downloads data and stores it locally as a CSV file.
To run this manually, after cloning this repository:

```bash
pip install uk-covid19
./download.py
```

The file created contains the "last_update" timestamp from the API call - this
is documented [here]()

This repository also contains a GitHub Action to download the data every hour,
and commit it to this repository.
When the "last_update" timestamp from the API call changes (i.e. once per day
when the new data are deployed to the database), a new file is created.
Intermediate runs re-download and over-write the existing data
file with the same timestamp, so nothing should be committed.

