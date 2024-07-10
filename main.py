from js import document
from io import BytesIO
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pyscript import display
from pyscript import when
from pyweb import pydom

@when('change', '#upload')

async def processFile(*args):
	if pydom["input#xmin"][0].value != "":
		x_min = pydom["input#xmin"][0].value
		x_min = float(x_min)
	else:
		x_min = 1419
	
	if pydom["input#xmax"][0].value != "":
		x_max = pydom["input#xmax"][0].value
		x_max= float(x_max)
	else:
		x_max = 1422

	if pydom["input#ymin"][0].value != "":
		y_min = pydom["input#ymin"][0].value
		y_min = float(y_min)
	else:
		y_min = 0
	
	if pydom["input#ymax"][0].value != "":
		y_max = pydom["input#ymax"][0].value
		y_max= float(y_max)
	else:
		y_max = 200

	csv_file = document.getElementById('upload').files.item(0)
	
	array_buf = await csv_file.arrayBuffer() # Get arrayBuffer from file
	file_bytes = array_buf.to_bytes() # convert to raw bytes array 
	csv_file = BytesIO(file_bytes) # Wrap in Python BytesIO file-like object
	
	# Read the CSV file into a Pandas DataFrame
	df = pd.read_csv(csv_file)
	#display(df)
	
	dataArray = df.to_numpy()
	x = dataArray[:,0]
	y = dataArray[:,1]

	fig1, ax1 = plt.subplots(1, dpi=150, figsize=(6,4))
	plt.plot(x, y, linewidth=1)
	#ax1.scatter(x, y, 1)
	plt.title("Signal vs Frequency", fontsize=6)
	#plt.xlabel(x_label, fontsize=6)  
	#plt.ylabel(y_label, fontsize=6)
	ax1.set_xlabel("Frequency", fontsize=6, labelpad=1)
	ax1.set_ylabel("Signal", fontsize=6, labelpad=1)
	ax1.set_xlim(x_min, x_max)
	ax1.set_ylim(y_min, y_max)
	ax1.tick_params(axis='x', labelsize=4)
	ax1.tick_params(axis='y', labelsize=4)
	#ax1.margins(1)
	ax1.grid()

	plt.close('all')
	
	display(fig1, target='graph', append=False)

def update_graph(df):
	if pydom["input#xmin"][0].value != "":
		x_min = pydom["input#xmin"][0].value
		x_min = float(x_min)
	else:
		x_min = 1419
	
	if pydom["input#xmax"][0].value != "":
		x_max = pydom["input#xmax"][0].value
		x_max= float(x_max)
	else:
		x_max = 1422

	if pydom["input#ymin"][0].value != "":
		y_min = pydom["input#ymin"][0].value
		y_min = float(y_min)
	else:
		y_min = 0
	
	if pydom["input#ymax"][0].value != "":
		y_max = pydom["input#ymax"][0].value
		y_max= float(y_max)
	else:
		y_max = 200
		
	dataArray = df.to_numpy()
	x = dataArray[:,0]
	y = dataArray[:,1]
	fig1, ax1 = plt.subplots(1, dpi=150, figsize=(6,4))
	plt.plot(x, y, linewidth=1)
	#ax1.scatter(x, y, 1)
	plt.title("Signal vs Frequency", fontsize=6)
	#plt.xlabel(x_label, fontsize=6)  
	#plt.ylabel(y_label, fontsize=6)
	ax1.set_xlabel("Frequency", fontsize=6, labelpad=1)
	ax1.set_ylabel("Signal", fontsize=6, labelpad=1)
	ax1.set_xlim(x_min, x_max)
	ax1.set_ylim(y_min, y_max)
	ax1.tick_params(axis='x', labelsize=4)
	ax1.tick_params(axis='y', labelsize=4)
	#ax1.margins(1)
	ax1.grid()
