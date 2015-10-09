# ViertoLAN_plotly
Simple plot.ly script for monitoring power consumption
Example: https://plot.ly/~Zokol/32/viertolan-voltage-and-current-monitor/


NOTE: Assumes that you have tokens.py updated with working streaming tokens from plot.ly. Check https://plot.ly/python/streaming-tutorial/ for more info.

Structure for tokens.py:
streaming_tokens = [
	"aaaaaaaaaaaa",
	"bbbbbbbbbbbb",
	"cccccccccccc",
	"dddddddddddd",
	"eeeeeeeeeeee",
	"ffffffffffff"
]

Script currently assumes that there are six variables. To change this, you have to modify the labels in init_plotly.py and tokens in tokens.py

If you change your tokens or update plot structure in init_plotly.py, you have to run init_plotly.py. This will open the new plot in your web browser, the old plot is replaced with the new one in plot.ly.

To change the website you are logging from, change it into both init_plotly.py and log_plotly.py.

Run log_plotly.py and leave it running to update the plot.

Requirements:
* python3
* pip
* plotly-library: https://plot.ly/python/getting-started/
