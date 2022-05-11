---
title: "Automated Defect Discovery Using Deep Learning"
date: ""
draft: false
tags: ["deep-learning", "materials-informatics"]
author: ["Sarthak Jariwala, Ph.D."]
showToc: true
TocOpen: false
hidemeta: false
comments: false
description: "Deep Learning of Solid-State Transformations and Reaction Pathways in 2D Materials."
# canonicalURL: "https://canonical.url/to/page"
disableHLJS: true # to disable highlightjs
disableShare: true
disableHLJS: false
hideSummary: false
searchHidden: false
ShowReadingTime: true
ShowBreadCrumbs: true
ShowPostNavLinks: true
cover:
    image: "/images/automated_defect_discovery.gif" # image path/url
#     alt: "<alt text>" # alt text
#     caption: "<text>" # display caption under
---
![automated-defect-discovery](/images/automated_defect_discovery.gif#center)

> Developed, packaged, and published a **physics-informed deep learning model** to automate the localization, classification, and visualization of defects in 2D materials. 

Advances in scanning transmission electron microscopy (STEM) have allowed unprecedented insight into the elementary mechanisms behind the solid-state phase transformations and reactions. 

However, the ability to quickly acquire large, high-resolution datasets has created a challenge for rapid physics-based analysis of STEM images and movies.

In this project, I developed a software package, `defectfinder`, that allows the user to develop a convolutional neural network (CNN) based framework to **automate the localization, classification and visualization of defects in 2D materials** from dynamic STEM data. 

`defectfinder` allows the user to localize and extract the defects frame by frame using fast-fourier transform (FFT), subtraction and lattice periodicity, and predict the defect type for all the localized defects. `defectfinder` also allows defect visualization by type and the interplay between the different defect types and time.

Learn more about it [here](https://github.com/yiwen26/DLSSTRP#defect-finder).

![deep-learning](/images/deep-learning-ornl.png)
