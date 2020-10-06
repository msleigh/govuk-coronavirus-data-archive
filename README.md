# GOV.UK Coronavirus dashboard data

Automatically downloads and archives data used by the UK Gov Coronavirus
Dashboard.

The data retrieved are the 'Cases by specimen date' for the whole UK.

Data are downloaded each day and placed in the `data` directory of
this repository (CSV format).

The daily download is automated by a GitHub Action that runs the `download.py`
script.

The data filenames contain the 'release' timestamp from the API call - this
is documented
[here](https://publichealthengland.github.io/coronavirus-dashboard-api-python-sdk/pages/examples/timestamps.html)
.

## To run locally

The `download.py` script downloads the and stores it locally as a CSV
file, and can be executed manually to get a one-off download.

To run it manually, after cloning this repository:

```bash
pip install uk-covid19
./download.py
```

