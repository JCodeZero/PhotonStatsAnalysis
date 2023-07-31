# Photon Statistics Analysis

## Description
PhotonStatsAnalysis contains Python files that form visualizations of  given data on time, photon energy levels, and the x and y positions of the photons according to the bottom left corner of the display. But the most significant goal is for an algorithm to detect anomalies in the data of Time vs. # of Protons that could possibly be gamma-ray bursts.

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
To showcase and replicate the project, download the data file via the hyperlink below that will be used as the example data set (~130 MB):
https://www.swift.ac.uk/archive/reproc/01088940000/bat/event/sw01088940000bevshsp_uf.evt.gz
Example data is collected by the UK Swift Science Data Centre. Make sure the file is in the project folder.

Libraries used: mathplotlib, astropy, numpy, pandas, sys

## Usage


## License
This is licensed under GNU General Public License v3.0.
