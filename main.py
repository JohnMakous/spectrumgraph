from js import document
from io import BytesIO
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pyscript import display
from pyscript import when

@when('change', '#upload')
	
async def processFile(*args):
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
	ax1.set_xlim(1419, 1422)
	#ax1.set_ylim(y_min, y_max)
	ax1.tick_params(axis='x', labelsize=4)
	ax1.tick_params(axis='y', labelsize=4)
	#ax1.margins(1)
	ax1.grid()

	plt.close('all')
	
	display(fig1, target='graph', append=False)
