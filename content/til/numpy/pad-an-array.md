---
title: "Array Padding - Only One Side"
date: 2021-11-02T15:51:33-07:00
draft: false
authors: ["Sarthak Jariwala"]
tags: ["python", "numpy"]
categories: []
externalLink: ""
series: []
---

[`numpy.pad`](https://numpy.org/doc/stable/reference/generated/numpy.pad.html) provides an easy way to pad a numpy array. For instance, if you want to add two 3's and four -7's to an array, you can do the following - 

```python
import numpy as np

a = np.array([1, 2, -1])

np.pad(a, (2, 4), "constant", constant_values=(3, -7))

# array([ 3,  3,  1,  2, -1, -7, -7, -7, -7])
```

But, what if you _**only**_ want to pad the right side or left side?

```python
""" Pad only left side"""
np.pad(a, (2, 0), "constant", constant_values=(3))
# array([ 3,  3,  1,  2, -1])

""" Pad only right side"""
np.pad(a, (0, 4), "constant", constant_values=(-7))
# array([ 1,  2, -1, -7, -7, -7, -7])
```
