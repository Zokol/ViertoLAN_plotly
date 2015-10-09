import requests
import re
import plotly.plotly as py
from plotly.graph_objs import *
from tokens import streaming_tokens

## Reads the data from web-page, assumes that there is <code>PARSE:</code>-field with data points to be read.
page = requests.get("http://monni.tnk2.com:53100")
data = re.findall('\d+.\d+', re.search('<code>PARSE:(.*?)</code>', page.text).group(0))

## To lable the traces, we need this. NOTE: datapoints are assumed to always be in the same order!
data_labels = ["Voltage - L1", "Voltage - L2", "Voltage - L3", "Current - L1", "Current - L2", "Current - L3"]

## Check for token count
if len(data) > len(streaming_tokens):
	print("Not enough streaming tokens, visit plot.ly and generate more tokens")
	quit()

# Init trace array for later use
traces = []

for i in range(len(data)):

	### XXX UGLY HACK, would be better to split parseable data in the original website into two sections
	if i < len(data) / 2:
		y_axis = "y"
	else:
		y_axis = "y2"

	## Create trace. This is the individual line on the graph, representing one data type
	trace = Scatter(
	    x=[],
	    y=[],
	    stream=dict(
	    	token=streaming_tokens[i], # Fetch individual streaming token
	    	maxpoints=25200	# Set to hold log for one week @ 1 sample / sec
	    ),
	    name=data_labels[i], # Fetch label from array we created above
	    yaxis=y_axis # Set y-axis to either voltage or current
	)
	traces.append(trace) # Add trace-object to array for later plotting

#print(traces)

## Create layout. This determines how the plot looks like.
layout = Layout(
	title = "ViertoLAN voltage and current monitor",
	yaxis=YAxis(
		title='Voltage'
	),
	yaxis2=YAxis(
		title='Current',
		side='right',
		overlaying='y'
	)
)

## Plotly-library stuff, pretty straight forward
fig = Figure(data=Data(traces), layout=layout)
py.plot(fig, filename="legends-labels")