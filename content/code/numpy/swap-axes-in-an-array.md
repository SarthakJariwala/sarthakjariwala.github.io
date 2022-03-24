---
title: "Swap Axes in Array"
date: 2022-03-23T21:23:56-07:00
tags: ["python", "numpy"]
authors: ["Sarthak Jariwala"]
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

### Preliminary
```python
# load library
import numpy as np
```

### Create a multi-dimensional array
```python
m = np.zeros(shape=(100, 32, 50))
```

### Swap dimensions
```python
# swap axis 1 and 2 with each other in array `m`
m_swapped = np.swapaxes(m, 1, 2)

# view the shape
m_swapped.shape
```
```python
(100, 50, 32)
```