# Photon Statistics Analysis

## Description
This project relies on the background of gamma-ray bursts originating from exploding stars. The most common and brightest type come from supernovas, the event when a giant star collapses in on its core and condensing it into either a neutron star or a black hole; the latter being the result if the star beforehand had enough mass and the former bearing not enough. The black hole, fresh from its birth, will shoot out jets of gamma-rays from its poles as it rotates at immense speeds. Shorter and smaller bursts come from binary star systems consisting of either two neutron stars, a neutron star and a black hole, or two black holes. Consequently, from the gravitational pull of both celestial bodies affecting each other, the two objects would eventually collide in what is known as a "kilonova". (This does not occur for a black hole-black hole merger.) The new black hole resulting from the collisions would send bursts of gamma-rays across the galaxy, which can be detected from satellites orbiting around our Earth. The purpose of PhotonStatsAnalysis is so its Python files can be applied to collected data of gamma-ray bursts in time series to form visualizations of given data on time, photon energy levels, and the x and y positions of the photons according to the bottom left corner of the display. But the most significant goal is for an algorithm to detect anomalies in the data of Time vs. # of Protons that could possibly be classified as gamma-ray bursts originating from kilonovas. The algorithm will have to detect the starting point of the burst and the ending point of the burst, which can be difficult as the burst slowly dissipates at the end. But using a sliding timeframe model that collects the mean count of photons within the interval, both the start and end of the gamma-ray burst can be found.

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
python3 GraphBurst.py notebooks/sw01088940000bevshsp_uf.evt.gz
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
In the notebook `DetectingBursts.ipynb`, there were four different methods for how gamma-ray bursts could be detected using statistics on a Time vs. # of photons dataset, with the goal to find the most optimal method. \
\
`MeasuringSlope.py` assumes that once the slope between two adjacent points reach a certain point, it will be considered an "anomaly" in the background (areas where there are no bursts).
```bash
python3 MeasuringSlope.py notebooks/sw01088940000bevshsp_uf.evt.gz
```
\
`StandardDeviation.py` is the first step leading to next following three methods as they use the mean and the standard deviation of the number of photons in a certain timeframe. In the example, it is over 5-second timeframes.
```bash
python3 StandardDeviation.py notebooks/sw01088940000bevshsp_uf.evt.gz
```
\
`CompareMeantoSTD.py` compares the mean of the current 5-second timeframe on the graph to the sum of the previous timeframe's mean and three times its standard deviation. If it exceeds the mean + 3*standard deviation, then the point would be considered an anomaly.
```bash
python3 CompareMeantoSTD.py notebooks/sw01088940000bevshsp_uf.evt.gz
```
\
`FiftySecBG.py` assumes that the first fifty second of the time series is part of the background and subtracts the mean of the 50-seconds and three times its standard deviation from the entire time series. This would make it so only bursts above the background would be positive and thus, the start and end points of the bursts can be found.
```bash
python3 FiftySecBG.py notebooks/sw01088940000bevshsp_uf.evt.gz
```
\
`SlidingFrame.py` has a timeframe that goes across the whole dataset with its length starting at 1-second long and ending as a timeframe the same length as the entire dataset. The maximum mean from each of the same-lengthed timeframes are taken and the most frequent starting time of the timeframes would be assumed to be the start of the timeframe while the end time is the end time of the longest timeframe that has the same frequent starting point. This is the most complex method out of the four and also the optimal method for accuracy.
```bash
python3 SlidingFrame.py notebooks/sw01088940000bevshsp_uf.evt.gz
```
## Usage (Presentation and Paper)
Download necessary dependencies for the following. \
To download the presentation form odp to pdf:
```bash
libreoffice --headless --convert-to pdf JaidenLin_GammaRayBursts_Slides.odp
```
\
To open the research paper as a pdf type
```bash
pdflatex JaidenLin_GammaRayBursts_Paper/main.tex
```
Followed by
```bash
biber main
```
Now, recompile the file again
```bash
pdflatex main.tex
```
Open the created pdf by typing
```bash
open main.pdf
```
## License
This is licensed under GNU General Public License v3.0.
