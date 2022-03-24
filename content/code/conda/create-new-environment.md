---
title: "Create New Environment"
date: 2022-03-23T22:44:29-07:00
tags: ["conda", "python"]
author: ["Sarthak Jariwala, Ph.D."]
showToc: false
TocOpen: false
draft: false
hidemeta: false
comments: false
description: ""
# canonicalURL: "https://canonical.url/to/page"
disableHLJS: true # to disable highlightjs
disableShare: false
disableHLJS: false
hideSummary: true
searchHidden: false
ShowReadingTime: true
ShowBreadCrumbs: true
ShowPostNavLinks: true
# cover:
#     image: "<image path/url>" # image path/url
#     alt: "<alt text>" # alt text
#     caption: "<text>" # display caption under cover
#     relative: false # when using page bundles set this to true
#     hidden: true # only hide on current single page
# editPost:
#     URL: "https://github.com/<path_to_repo>/content"
#     Text: "Suggest Changes" # edit text
#     appendFilePath: true # to append file path to Edit link
---

### Create a new conda environment
```bash
# create a new conda environment called ml-ninja
conda create --name ml-ninja
```

### Create a new environment with packages
```bash
# create a new environment with python=3.9 and numpy installed
conda create --name ml-ninja python=3.9 numpy
```

### Verify environment creation
```bash
conda env list

# conda environments:
#
# base *
# ml-ninja
```
