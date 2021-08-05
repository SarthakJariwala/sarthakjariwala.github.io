+++
title = "Projects"
slug = "projects"
+++

List of some of my projects. You can learn more about the projects below.

- [seaborn-image](#seaborn-image) : Open-source image visualization in Python
- [nrel-dev-api](#nrel-dev-api) : Python API for accessing National Renewable Energy Lab developer resources
- [SQ Web & Desktop App](#sq-desktop-and-web-app) : Calculate solar cell's maximum theoretical efficiency
- [Structure-Property Relationships](#structure-property-relationships-in-novel-solar-energy-materials) : Elucidate structure-property relationships in next-generation solar cell technology
- [Solar Techno-Economic Analysis](#solar-techno-economic-analysis) : To design solar powered community library & school in rural Ghana
- [Automated Defect Discovery](#automated-defect-discovery-using-deep-learning) : Physics-informed _deep learning_ on 2D materials
- [Predictive Peptide Analysis](#predictive-peptide-analysis) : Machine learning for predictive analysis of self-assembled peptides
- [Data Acquisiton Application](#data-acquisition) : Intuitive platform for acquiring data from scientific hardware/instruments
- [GLabViz](#glabviz-data-analysis) : Desktop application for scientific data analysis
- [BZMAN](#bzman) : Business management desktop application
- [BZMAN Website](#bzman-website) : Flask application facilitating application download and other functionalities
- [Other Open-Source Contributions](#other-open-source-contributions) : `matpltolib-scalebar`, `pyscaffold-interactive`, etc.

---
# seaborn-image
**Creator and maintainer** of **[seaborn-image](https://github.com/SarthakJariwala/seaborn-image)**, an open-source image visualization Python package that provides a high level API for drawing attractive, descriptive and effective images.

Learn more about the project [here](/posts/introducing-seaborn-image).

**[GitHub](https://github.com/SarthakJariwala/seaborn-image)** | **[Docs](https://seaborn-image.readthedocs.io/en/stable/)**

![imagehist-demo](/images/imghist_demo.png)

**User Feedback** 

![feedback-1](/images/user-feedback-1.png)

---

# nrel-dev-api 
**Creator and maintainer** of [nrel_dev_api](https://github.com/SarthakJariwala/nrel_dev_api), an open-source Python API for accessing data and services provided by **[National Renewable Energy Lab (NREL)](https://developer.nrel.gov/docs/)**.

Example Usage:
```python
from nrel_dev_api.solar import SolarResourceData

# use address or lat/lon to get information about available solar resource
seattle = SolarResourceData(address="Seattle, WA")
```

```python
from nrel_dev_api.solar import (download_nsrdb_data,
                                get_nsrdb_download_links)

# fetch the available download links
seattle_links = get_nsrdb_download_links(year=2016, interval=60, lat=47.61, lon=-122.35)

# download using the links to a pandas dataframe
seattle_hourly_df = download_nsrdb_data(seattle_links[0], email="YOUR_EMAIL")
```

For more information, refer the [documentation](https://nrel-dev-api.readthedocs.io/en/latest/) or [article](/posts/sunny-in-seattle)

---
# Structure-Property Relationships in Novel Solar Energy Materials
Used **statistical methods** in combination with **expertise in image & data analysis** and domain knowledge to elucidate structure-property relationships in next-generation solar cell technology.

Learn more about the project in the [news coverage](https://www.washington.edu/news/2019/10/31/map-strain-solar-cells/) and [paper](https://doi.org/10.1016/j.joule.2019.09.001).

![joule paper fig](/images/joule-paper-fig4.png)

---
# SQ Desktop and Web App
Developed and deployed a **web and desktop application for scientists** to calculate the maximum efficiency of a solar cell with various materials under different temperatures.
    
[Web application](https://sqcalculator.herokuapp.com/) | [Desktop application](https://github.com/SarthakJariwala/Shockley-Queisser-Calculator)

![sq-desktop](/images/SQ_Calculator_UI.png)

---
# Solar Techno-Economic Analysis 
As a **senior technical member of Global Renewable Infrastructure Development** (GRID) at the University of Washington : 

- Performed **techno-economic analysis** using SAM (System Advisor Model) and PySAM for designing a **solar-powered school & community library** in rural Ghana.

- Developed **remote data tracking system** for monitoring the **health and performance** of installed solar modules and microgrids.

---
# Automated Defect Discovery Using Deep Learning
Developed, packaged, and published a **physics-informed deep learning model** to automate the localization, classification, and visualization of defects in 2D materials. 

Learn more about it [here](https://github.com/yiwen26/DLSSTRP#defect-finder).

![deep-learning](/images/deep-learning-ornl.png)

---
# Predictive Peptide Analysis
Used image processing and machine learning for **predictive analysis** of self-assembled peptides on various substrates as imaged using Atomic Force Microscope.

Learn more about the project [here](https://github.com/liud16/direct18project#safmi-afm-segmentation-of-atomic-force-microscope-images-library-functions-and-predictive-analysis)

![predictive-analysis](/images/direct18-safmi.png)

---
# GLabViz
Simplified exploration and analysis of outcoming data from various scientific hardware using an intuitive GUI written in Python and Qt, leading to an improved and efficient experimental and analysis workflow.

A complete description as well as the application can be found on [GitHub](https://github.com/SarthakJariwala/Python_GUI_apps).

![glabviz](/images/GLabViz_interface_1.png)

---
# Data Acquisition
Developed intuitive platforms for **data acquisition and control using Qt and Python** for various scientific hardware/instruments.

A complete description of the functionalities of the acquisiton platform can be found on the [GitHub repo README](https://github.com/GingerLabUW/Microscope_App).

![mscope-app](/images/mscope_app.png)

---
# BZMAN
BZMAN (_business manager_) - A minimal business management application to simplify daily business activities. It is designed to be minimal and for small business needs. 

It is open-source and written completely in Python. You find more details on the [GitHub repo](https://github.com/SarthakJariwala/bzman) or [website](https://bzman.herokuapp.com/).

[Download](https://bzman.herokuapp.com/downloads)

![bzman](/images/CompanyList.png)

---
# BZMAN Website

A [web application](https://bzman.herokuapp.com/) running a Flask backend primarily built to demonstrate the functionalities of BZMAN and facilitate BZMAN application download.

[Website](https://bzman.herokuapp.com/)

---
# Other Open-Source Contributions
Contributor to **several other open-source python packages** (selected): matplotlib-scalebar, pooch, PyScaffold-Interactive, Scopefoundry. ([GitHub](https://github.com/SarthakJariwala))

---