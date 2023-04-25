import streamlit as st
import requests as req
import pandas as pd

def get_data():
	# Get data from airtable api
	url = "https://api.airtable.com/v0/app1yMkrLXydPq4sm/tbl9JfGJ4iw3JJB9I"
	headers = {
		"Authorization": f"Bearer {st.secrets['airtable_token']}"
	}
	response = req.get(url, headers=headers)
	records = response.json()['records']

	data = list(map(lambda x: x['fields'], records))

	df = pd.DataFrame(data)

	return df