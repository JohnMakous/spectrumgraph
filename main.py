import matplotlib.pyplot as plt
import numpy as np
import asyncio
import js
from js import document, FileReader
from pyodide.ffi import create_proxy
   
def read_complete(event):
	# event is ProgressEvent
   
    content = document.getElementById("content");
    content.innerText = event.target.result

   
async def process_file(x):
	fileList = document.getElementById('upload').files
   
    for f in fileList:
		# reader is a pyodide.JsProxy
    	reader = FileReader.new()
   
		# Create a Python proxy for the callback function
		onload_event = create_proxy(read_complete)
		
		#console.log("done")
		
		reader.onload = onload_event
		
		reader.readAsText(f)
   
	return
   
def main():
	# Create a Python proxy for the callback function
    file_event = create_proxy(process_file)
   
    # Set the listener to the callback
    e = document.getElementById("upload")
    e.addEventListener("change", file_event, False)
   
main()

def plot_spectrum(event):
	data_filename = pydom["input#filename"][0].value
	data_set = np.loadtxt(data_filename+".csv", delimiter=',')
    
   freq = np.zeros(data_set.shape[0])
   signal = np.zeros(data_set.shape[0])
    
   # data_set is a 2-D array.
   # freq[i] values are assigned the data_set(i,0) values; 
   # signal[i] values are assigned the data_set(i,1) values
    
   i = 0
   while (i < data_set.size/2):
      freq[i] = data_set[i][0]
      signal[i] = data_set[i][1]
      i +=1
    
    #Plot data
    
   font1 = {'family': 'serif',
            'color':  'darkred',
            'weight': 'bold',
            'size': 16,
            }
    
   font2 = {'family': 'serif',
            'color':  'darkblue',
            'weight': 'bold',
            'size': 18,
            }
   fig, ax = plt.subplots(1, figsize=(5, 4))
   plt.title("Signal vs. Frequency", fontdict=font2)
    
   plt.scatter(freq, signal)
   plt.xlabel("Frequency (MHz)", fontdict=font1)
   plt.ylabel("Signal", fontdict=font1)
   plt.xlim([1414,1424])
   plt.ylim([0,5000])
    
   #Set tick marks
   ax.xaxis.set_major_locator(plt.MultipleLocator(10))
   ax.xaxis.set_minor_locator(plt.MultipleLocator(5))
   fig
    
   plt.xticks(fontsize= 12)
   plt.yticks(fontsize= 12) 
    
   # Add grid lines
   plt.grid(b=True, which='major', color='#666666', linestyle='-', linewidth=1)
    
   # Show the minor grid lines with very faint and almost transparent grey lines
   plt.minorticks_on()
   plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
    
   plt.show()
   display(fig, target='graph', append=False)
