+++ 
draft = true
date = 2021-02-24T18:59:05-08:00
title = "Effective Visualization of Multi-Dimension Image Data in Python"
description = "Got multi-dimensional image data? Python can help!"
slug = "multi-dimension-image-data"
authors = []
tags = []
categories = []
externalLink = ""
series = []
+++

Multi-dimensional image data is, generally speaking, cumbersome to visualize. 

In scientific imaging (or in most imaging areas), multi-dimensional images are very common. The additional dimension could be anything from the physical 3rd dimension ("Z axis"), where 2D images are taken at different depths; to the time dimension, where 2D images are taken at different time intervals; to different channels in scientific imaging instruments such as atomic force microscopes or in RGB images.

We will use `seaborn-image`, an open source image visualization library in Python based on `matplotlib`.

>It is heavily inspired by the popular `seaborn` library for statistical visualization

#### Installation

```bash
pip install -U seaborn-image
```
> You can find out more about the `seaborn-image` project on [GitHub](https://github.com/SarthakJariwala/seaborn-image).

#### Load sample 3D data

```python
import seaborn_image as isns

cells = isns.load_image("cells")
cells.shape
```
```
(256, 256, 60)
```

#### Visualize

We will use `ImageGrid` from `seaborn_image` to visualize the data. It will plot a series of images on a grid.

To begin, we will only plot a few selected slices using the `slices` keyword argument.

```python
g = isns.ImageGrid(cells, slices=[10, 20, 30, 40, 50])
```
![multi-dim-image-1](/images/multi-dim-im-1.png)

By default, the slices are taken along the last axis. However, we can take them along another dimension using the `axis` keyword argument.

```python
g = isns.ImageGrid(cells, slices=[10, 20, 30, 40, 50], axis=0)
```
![multi-dim-image-2](/images/multi-dim-im-2.png)

We can also specify different start/stop points as well as step sizes to take using the `start`, `stop` and `step` parameters, respectively.

In the code below, we are starting with the 10th slice and going upto the 40th slice with steps of 3.
>The slices and steps are taken over the last axis if not specified.

```python
g = isns.ImageGrid(cells, start=10, stop=40, step=3)
```
![multi-dim-image-3](/images/multi-dim-im-3.png)

We can also just plot all the images without any indexing or slicing.

```python
g = isns.ImageGrid(cells, cbar=False, height=1, col_wrap=10)
```
> Note - We altered the height of the individual images and the number of image columns.

![multi-dim-image-4](/images/multi-dim-im-4.png)

#### Transformations

Finally, we can also apply transformations to the image and visualize it. Here, we will adjust the exposure using the `adjust_gamma` function from `scikit-image`. 

We can achieve this by passing the function object to the `map_func` parameter. Additional parameters to the function object can be passed as keyword arguments.

```python
from skimage import exposure

g = isns.ImageGrid(
    cells,
    map_func=exposure.adjust_gamma,  # function to map
    gamma=0.5,  # additional keyword for `adjust_gamma`
    cbar=False,
    height=1,
    col_wrap=10)
```
![multi-dim-image-5](/images/multi-dim-im-5.png)

---

You can find out more about the `seaborn-image` project on [GitHub](https://github.com/SarthakJariwala/seaborn-image).

Thanks for reading!
