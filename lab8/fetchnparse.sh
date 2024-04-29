#!/bin/bash

# Fetch the METAR data from NOAA Aviation Weather API
curl -s "https://aviationweather.gov/api/data/metar?ids=KMCI&format=json&taf=false&hours=12&bbox=40%2C-90%2C45%2C-85" > aviation.json

# Parse the JSON data and extract the first six receiptTime values
jq '.data[] | .receiptTime' aviation.json | head -n 6