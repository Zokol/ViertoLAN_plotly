import requests
import re
import datetime
import time
import plotly.plotly as py
from plotly.graph_objs import *
from tokens import streaming_tokens

## Reads the data from web-page, assumes that there is <code>PARSE:</code>-field with data points to be read.
def read_data():
	page = requests.get("http://monni.tnk2.com:53100") # Read html-page
	data = re.findall('\d+.\d+', re.search('<code>PARSE:(.*?)</code>', page.text).group(0)) # Use regexp to filter the data from page, returns an array of data.
	return data

## Sends data to plot.ly using pre-initialized traces. Look into init.plotly.py and run it if you make changes or use fresh tokens!
def stream_data(streams, data_array):
	timestamp = datetime.datetime.now() # Get current time
	for stream in streams: # Iterate through stream-objects
		data = data_array[stream["data_id"]] # Get data point linked to this stream (data points are assumed to be always in the same order)
		stream["stream"].write(dict(y=float(data), x=timestamp)) # FINALLY, send data to plot.ly!

## Create empty array to store streams, look ahead to know why
streams = []

## Fetch data
data = read_data()

## Iterate through datapoints, this is to know how many datapoints we have to log. Create open stream for every datapoint, linking each datapoint to individual trace in the plot. NOTE: each stream/trace requires it's own streaming token. Ensure that there is enough streaming tokens, otherwise you will FAIL!
for i in range(len(data)):
	s = py.Stream(streaming_tokens[i]) # Create streaming object with token
	s.open() # Open stream
	streams.append({"stream": s, "data_id": i}) # Store stream into array for later use

## Run stream
while True:
	data = read_data() # Update data
	#print(data)
	stream_data(streams, data) # Send data to plot.ly using our own function, look UP!
	time.sleep(5)	# Sampling rate
