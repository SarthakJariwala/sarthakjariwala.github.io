---
title: "Pad Numpy Array"
date: 2022-03-23T21:36:24-07:00
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

### Preliminaries

```python
import numpy as np

# create an array
a = np.array([1, 2, -1])
```

### Pad array on both sides with constant values

Add two 3's to the left of the array and four -7's to the right of the array.
```python
np.pad(a, (2, 4), "constant", constant_values=(3, -7))

# array([ 3,  3,  1,  2, -1, -7, -7, -7, -7])
```

### Pad array on only one side

But, what if you _**only**_ want to pad the right side or left side?

#### Pad only left side
```python
# Pad only left side
np.pad(a, (2, 0), "constant", constant_values=(3))

# array([ 3,  3,  1,  2, -1])
```

#### Pad only right side
```python
# Pad only right side"""
np.pad(a, (0, 4), "constant", constant_values=(-7))

# array([ 1,  2, -1, -7, -7, -7, -7])
```