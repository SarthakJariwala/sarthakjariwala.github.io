---
title: "LocalDaskExecutor : num_workers"
date: 2021-08-03T16:00:55-07:00
draft: false
authors: ["Sarthak Jariwala"]
tags: ["prefect", "dask"]
categories: []
externalLink: ""
series: []
---

Recently, I was using [prefect](https://docs.prefect.io) to run a few workflows locally. I wanted to run one of the workflows in parallel using `LocalDaskExecutor`. That's when I learned that `LocalDaskExecutor` uses `num_workers` and `DaskExecutor` uses `n_workers` to specify the number of workers.

### With LocalDaskExecutor

```python
from prefect.executors import LocalDaskExecutor

if __name__ == "__main__":
    flow.run(executor=LocalDaskExecutor(scheduler="processes", num_workers=16))
```

### With DaskExecutor

```python
from prefect.executors import DaskExecutor

if __name__ == "__main__":
    flow.run(executor=DaskExecutor(cluster_kwargs={"n_workers": 16}))
```