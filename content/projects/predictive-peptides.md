---
title: "Predicting Peptide Interface Parameters"
date: ""
draft: false
tags: ["machine-learning", "image-processing"]
author: ["Sarthak Jariwala, Ph.D."]
showToc: true
TocOpen: false
hidemeta: false
comments: false
description: ""
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
    image: "/images/direct18-safmi.png" # image path/url
#     alt: "<alt text>" # alt text
#     caption: "<text>" # display caption under
---

![predictive-analysis](/images/direct18-safmi.png)

> Used image processing and machine learning for **predictive analysis** of self-assembled peptides on various substrates as imaged using Atomic Force Microscope.

Developed software framework using image processing and machine learning to identify different textural components and their segmentation in Atomic Force Microscope (AFM) images of self-assembled peptide structures. 

From AFM image data, the software helps end users:
- Approximate the effect of natural tip drift which is ubiquitous in AFM characterization
- Correct for noise
- Detect different textures based on how _ordered or disordered the self-assembly_ is 
- Calculate:
    - Percent coverage of each texture
    - Overall percent coverage of the self assembled peptides
    - Ordered to disordered ratio (Degree of disorder) 

This helps evaluate the self assembly properties of the peptides on the substrates for the processing conditions.

Learn more about the project [here](https://github.com/liud16/direct18project#safmi-afm-segmentation-of-atomic-force-microscope-images-library-functions-and-predictive-analysis)
