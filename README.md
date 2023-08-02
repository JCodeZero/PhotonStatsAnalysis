# Photon Statistics Analysis

## Description
This project relies on the background of gamma-ray bursts originating from exploding stars. The most common and brightest type come from supernovas, the event when a giant star collapses in on its core and condensing it into either a neutron star or a black hole; the latter being the result if the star beforehand had enough mass and the former bearing not enough. Shorter and smaller bursts come from binary star systems consisting of either two neutron stars or a neutron star and a black hole. Consequently, from the gravitational pull of both celestial bodies affecting each other, the two objects would eventually collide in what is known as a "kilonova". The kilonova sends out bursts of gamma-rays across the galaxy, which can be detected from satellites orbiting around our Earth. The purpose of PhotonStatsAnalysis is so its Python files can be applied to collected data of gamma-ray bursts to form visualizations of given data on time, photon energy levels, and the x and y positions of the photons according to the bottom left corner of the display. But the most significant goal is for an algorithm to detect anomalies in the data of Time vs. # of Protons that could possibly be classified as gamma-ray bursts originating from kilonovas. The algorithm will have to detect the starting point of the burst and the ending point of the burst, which can be difficult as the burst slowly dissipates at the end. But using a sliding timeframe model that collects the mean count of photons within the interval, both the start and end of the gamma-ray burst can be found.

## Installation
This project can be installed using git:
```bash
git clone https://github.com/JCodeZero/PhotonStatsAnalysis.git
```
All libraries required and included in the project can be installed through pip using `max-requirements.txt`
```bash
pip install -r max-requirements.txt
```
Libraries can also be installed using `min-requirements.txt`, which will excludes Jupyterlab dependencies
```bash
pip install -r min-requirements.txt
```
To showcase and replicate the project, download the data file via the hyperlink below that will be used as the example data set (~130 MB): \
https://www.swift.ac.uk/archive/reproc/01088940000/bat/event/sw01088940000bevshsp_uf.evt.gz \
Example data is collected by the UK Swift Science Data Centre. Make sure the file is moved to the "notebook" folder of the project folder for the Jupyter notebooks to function correctly.

## Usage (Notebooks)
Once navigated to the project folder, using `cd notebooks` will change the directory to the notebook folder. The notebooks contain various experiments done with the sample data presented in graphs. To view the notebooks, running `jupyter notebook` and then opening `localhost:8888/notebooks/` in your preferred browser will launch the notebook and from there, you can view the process of how the final algorithms were developed.

## Usage (Graphs)
The project contains multiple Python files capable of providing different visualizations of the data set: scatter plots, histograms, etc. The Jupyter notebooks in the "notebook" folder are present to show the process how each .py file was written. \
\
`GraphBurst.py` will output a histogram of Time (in seconds) vs. the number of photons in each second, displaying the gamma-ray burst visible in the data. This will be the filtered data set that will be used as the example data for furthur experimentation.
```bash
python3 GraphBurst.py sw01088940000bevshsp_uf.evt.gz
```
\
`ScatterPlot.py` outputs a scatter plot with a slider for Time (in seconds), axis for the x and y position, and the energy of each photon as the size of the corresponding dot. \
```bash
python3 ScatterPlot.py notebooks/sw01088940000bevshsp_uf.evt.gz
```
\
`2DHistogram.py` outputs a colored histogram where each bin is located on a x and y axis, and the brighter a bin is, the more photons can be found in that bin.
```bash
python3 2DHistogram.py sw01088940000bevshsp_uf.evt.gz
```
## Usage (Detection Methods)
In the notebook `DetectingBursts.ipnb` 

## License
This is licensed under GNU General Public License v3.0.
