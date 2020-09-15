# Introduction to spatial data analysis and mapping with Python

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/wcjochem/py-geospatial-2020/master)

Geographic data seem to be everywhere now – from geo-tagged photos and tweets, GPS watches and fitness trackers, spatially-referenced survey data, even high-resolution satellite imagery. While such data present many new opportunities to study our world, they also present unique challenges for analyses. The objective of this workshop is to introduce participants to the fundamentals of how to use, combine, analyse, and present spatial data while avoiding common pitfalls.

This two-day workshop uses a mixture of short lectures and live demos to introduce concepts, and then the majority of time will be spent in hands-on labs working with real datasets. Participants will meet virtually and have the opportunity to collaborate in small groups for the activities. All material uses Python and several key packages (including geopandas, pyproj, and folium). The workshop is intended for anyone wishing to gain familiarity with spatial data and core analysis techniques.

No previous experience with spatial data is expected. Participants should have experience with Python. Some knowledge of pandas and/or numpy would be helpful but is not required. 

This workshop is offered by the EPSRC Centre for Doctoral Training in Next Generation Computational Modelling ([CDT-NGCM](http://www.ngcm.soton.ac.uk/))

Registration on EnventBrite: https://www.eventbrite.co.uk/e/cdt-ngcm-introduction-to-spatial-data-analysis-and-mapping-with-python-tickets-113099585906

### Instructors
* [Chris Jochem](https://www.wcjochem.com) - [WorldPop](https://www.worldpop.org) in the [School of Geography and Environmental Science](https://www.southampton.ac.uk/geography), Univ. of Southampton
* Josephine Baulch - [School of Geography and Environmental Science](https://www.southampton.ac.uk/geography/postgraduate/research_students/jb7e16.page), Univ. of Southampton
* Chris Tomsett - [School of Geography and Environmental Science](https://www.southampton.ac.uk/geography/postgraduate/research_students/ct9g13.page), Univ. of Southampton

## Workshop outline

### Schedule
The workshop will run for 2 full days, starting from 9am and running to about 5pm each day. There will be morning, afternoon, and lunch breaks.

### Expectations
Participants are asked to engage and to be active participants for the full two days. 

This workshop is different because it now has to be online. We will use a blend of live lectures, practicals and chat discussions on our MS Teams site. The instructors will be available for guidance and support, answering technical questions, and the practicals are meant to provide experience in key concepts. Additional materials and coding challenges will be suggested for further practice.

## Materials
All the presentations, practicals, and datasets that we will use are available on this website. Download the files by clicking on the green "Code" button at the top of this page and unzip the folder on your local machine (note the location of the files you download). 

Alternatively, you can clone the repository to your own workspace using GitHub.

## Installation and set-up
This workshop will require a suite of somewhat specialised packages that depend on spatial libraries which are non-trivial to install (especially on Windows). 

If you want to install the software and run the practicals on your local machine, I recommend that you use the [conda](https://docs.conda.io/projects/conda/en/latest/index.html) package manager to install them on your system (and not something like `pip`).

First, install `conda` (or [miniconda](https://docs.conda.io/en/latest/miniconda.html)) on your system following the instructions on their site. 

Next, open your terminal program (if on Linux) or anaconda command program. Navigate to the folder location where you have downloaded or cloned the workshop files. 

Finally, create a new conda environment and install all the required packages and their dependencies by running this command:

```
conda env create -f environment.yml 
```

This will take a few moments to download and install all the packages. You may be prompted to confirm the installation. When that step has finished, test your install by running the following small script (located in the workshop folder).

Enable the environment:

```
conda activate py-geospatial-2020
```

Run the test script from the workshop files:

```
python check_setup.py
```

If you get an error in this step, please take a screenshot or copy the complete error message and contact the instructors for assistance.

The practicals use [Jupyter Notebooks](https://jupyter.org/index.html). This should have been automatically installed in the previous conda install step. Launch the Notebook interface by typing the following in the command prompt (you should still be in the location of the workshop files):

```
jupyter notebook
```

The workshop folder contains all the Practicals in notebook format in the `notebooks` directory. You are now ready 

If for some reason this last step doesn't work, you may need to install Jupyter. This can also be done within conda. From the command prompt enter:

```
conda install -c conda-forge notebook
```

### Non-installation alternative 
Alternatively, if you can't (or don't want to) install Python locally, the practical notebooks can be run in Binder through this link: [https://mybinder.org/v2/gh/wcjochem/py-geospatial-2020/master](https://mybinder.org/v2/gh/wcjochem/py-geospatial-2020/master). Be patient when first loading the repository.

Note that Binder has some resource limitations on processing power and memory. Importantly, you will need to manually save any files you modify/create in Binder as they will not persist after your session.

### Acknowledgements
This workshop benefited from several sources of teaching materials and coding examples, especially:
* Arribas-Bel, Dani. (2019). "A course on Geographic Data Science." *The Journal of Open Source Education*, 2(14). [https://doi.org/10.21105/jose.00042](https://doi.org/10.21105/jose.00042).
* [AugtoGIS course](https://automating-gis-processes.github.io/site/#) by Henrikki Tenkanen and Vuokko Heikinheimo. 
* [Introduction to Geospatial Data Analysis with Python](https://github.com/geopandas/scipy2018-geospatial-data) Scipy 2018 Tutorial by Wolf, Rey, Arribas-Bel, and Van den Bossche

We thank the authors for making their materials open. If you re-use or share this course material, please acknowledge this course and the original sources.


