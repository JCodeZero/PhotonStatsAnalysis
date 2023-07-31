Libraries used: mathplotlib, astropy, numpy, pandas

Example data file download hyperlink (~130 MB): https://www.swift.ac.uk/archive/reproc/01088940000/bat/event/sw01088940000bevshsp_uf.evt.gz
Data collected by UK Swift Science Data Centre. Make sure the data file is in the same directory as the Python files (.py).

PhotonStatsAnalysis contains Python files that form visualizations of  given data on time, photon energy levels, and the x and y positions of the photons according to the bottom left corner of the display. But the most significant goal is for an algorithm to detect anomalies in the data of Time vs. # of Protons that could possibly be gamma-ray bursts.

GraphingShorterData.py
Introducing the given gamma-ray burst found in this data file, the code here will result in a histogram graph of the number of photons (dependent variable) at a given time (independent variable). This is only appliable to the example data file as the start and end times of the gamma-ray burst is assumed.

ScatterPlot.py
This Python file displays a scatter plot with x and y axis that represent the position of the photons. The size of the scatter points represent the energy of each photon, and an interactive slider below the graph is the variable for time (in seconds) where the user can adjust the timeframe the graph is displaying. ScatterPlot.py can be appliable to other data files by replacing the inputted data file at the variable "filename".
