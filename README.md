# Introduction to spatial data analysis and mapping with Python

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/wcjochem/py-geospatial-2020/master)

Geographic data seem to be everywhere now – from geo-tagged photos and tweets, GPS watches and fitness trackers, spatially-referenced survey data, even high-resolution satellite imagery. While such data present many new opportunities to study our world, they also present unique challenges for analyses. The objective of this workshop is to introduce participants to the fundamentals of how to use, combine, analyse, and present spatial data while avoiding common pitfalls.

This two-day workshop uses a mixture of short lectures and live demos to introduce concepts, and then the majority of time will be spent in hands-on labs working with real datasets. Participants will meet virtually and have the opportunity to collaborate in small groups for the activities. All material uses Python and several key packages (including geopandas, rasterio, pySAL, and folium). The workshop is intended for anyone wishing to gain familiarity with spatial data and core analysis techniques.

No previous experience with spatial data is expected. Participants should have experience with Python. Some knowledge of pandas and/or numpy would be helpful but is not required. 

This workshop is offered by the EPSRC Centre for Doctoral Training in Next Generation Computational Modelling ([CDT-NGCM](http://www.ngcm.soton.ac.uk/))

Registration on EnventBrite: https://www.eventbrite.co.uk/e/cdt-ngcm-introduction-to-spatial-data-analysis-and-mapping-with-python-tickets-113099585906

### Instructors
* [Chris Jochem](https://www.wcjochem.com) - [WorldPop](https://www.worldpop.org) in the [School of Geography and Environmental Science](https://www.southampton.ac.uk/geography), Univ. of Southampton


## Workshop outline

### Schedule
Day 1

Day 2

### Expectations

## Materials
All the presentations, practicals, and datasets that we will use are available on this website. Download the files by clicking on the green "Code" button at the top of this page and unzip the folder on your local machine. Alternatively, you can clone the repository to your workspace using GitHub.

## Installation and set-up
This workshop will require a suite of somewhat specialised packages that depend on some low-level libraries which are non-trivial to install (especially on Windows). I recommend that you use the [conda](https://docs.conda.io/projects/conda/en/latest/index.html) package manager to install them on your system (and not something like `pip`).

First install conda (or [miniconda](https://docs.conda.io/en/latest/miniconda.html)) on your system following the instructions on their site. 

Then enter your terminal or command prompt program. Navigate to the folder location where you have downloaded or cloned the workshop files. Finally, create a new conda environment and install all the required packages and their dependencies by running this command:

```
conda env create -f environment.yml 
```

This will take a few moments to download and install all the packages. You may be prompted to confirm the installation. When that step has finished, test your install by running the following small script.

```
# enable the environment
conda activate py-geospatial-2020

# run the test script from the workshop files
python check_setup.py
```

The practicals use [Jupyter Notebooks](https://jupyter.org/index.html). If you want to run the notebooks locally on your machine, you will need to have Jupyter installed. This step can also be done in conda. From the command prompt enter:

```
conda install -c conda-forge notebook
```

Then launch the interface by typing the following in the command prompt:

```
jupyter notebook
```

Alternatively, if you can't install things locally, the practical notebooks can be run in Binder through this link: [https://mybinder.org/v2/gh/wcjochem/py-geospatial-2020/master](https://mybinder.org/v2/gh/wcjochem/py-geospatial-2020/master). Note that Binder has some resource limitations on processing power and memory.

### Acknowledgements
This workshop benefited from 


