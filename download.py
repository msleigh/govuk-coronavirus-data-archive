#!/usr/bin/env python

# Documentation for the PHE Python SDK for the UK Gov Coronavirus API is at:
# https://publichealthengland.github.io/coronavirus-dashboard-api-python-sdk

# URL to download 'Cases by specimen date' for 'UK total' in CSV:
# https://api.coronavirus.data.gov.uk/v1/data?filters=areaType=overview&structure=%7B%22areaType%22:%22areaType%22,%22areaName%22:%22areaName%22,%22areaCode%22:%22areaCode%22,%22date%22:%22date%22,%22newCasesBySpecimenDate%22:%22newCasesBySpecimenDate%22,%22cumCasesBySpecimenDate%22:%22cumCasesBySpecimenDate%22%7D&format=csv

import os
from uk_covid19 import Cov19API

# Construct a filter
# ------------------

uk_filter = ["areaType=overview"]

# Define the structure
# --------------------

# Same structure as for downloads from the web page (URL above)
cases_by_specimen_date = {
    "areaType": "areaType",
    "areaName": "areaName",
    "areaCode": "areaCode",
    "date": "date",
    "newCasesBySpecimenDate": "newCasesBySpecimenDate",
    "cumCasesBySpecimenDate": "cumCasesBySpecimenDate",
}

# Instantiate API object
# ----------------------

api = Cov19API(filters=uk_filter, structure=cases_by_specimen_date)

# Get timestamps
# --------------

api_last_update = api.last_update
release_timestamp = Cov19API.get_release_timestamp()

filestamp = api_last_update.replace(":", "").split(".")[0]

# print("API timestamp (time the specific data requested were uploaded to the database): ", api_last_update)
# print("Release timestamp (time the data were released to the API and website (post QC):", release_timestamp)

# Extract data

# As CSV
# data = api.get_csv()
# print(data)

# As Pandas dataframe
# data = api.get_dataframe()
# print(data)
# print(data.dtypes)

# Write to local CSV file
api.get_csv(save_as=os.path.join("data", "data_" + filestamp + ".csv"))
