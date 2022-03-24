---
title: "Dask Executor in Prefect"
date: 2021-08-03T16:00:55-07:00
draft: false
authors: ["Sarthak Jariwala"]
tags: ["prefect", "dask", "python"]
categories: []
externalLink: ""
series: []
---


### Preliminaries
```python
from prefect.executors import LocalDaskExecutor,  DaskExecutor
from prefect import task, Flow

from typing import Iterable
```

### Create a Prefect Task
```python
# create sample prefect task to run in a flow
@task
def add(list_of_int: Iterable[int]):
    return list_of_int[0] + list_of_int[1]
```
### Create a Prefect Flow

```python
# list of integers to add
list_of_ints = [[1, 2], [-3, 5], [4, 5], [9, 0], [3, -8]]

# create prefect Flow to run with Dask Executors
with Flow("sample-flow") as flow:
    result = add.map(list_of_ints)
```

### With `LocalDaskExecutor`
```python
if __name__ == "__main__":
    flow.run(executor=LocalDaskExecutor(scheduler="processes", num_workers=4))
```

### With `DaskExecutor`
```python
if __name__ == "__main__":
    flow.run(executor=DaskExecutor(cluster_kwargs={"n_workers": 4}))
```
> Note: `LocalDaskExecutor` uses `num_workers` and `DaskExecutor` uses `n_workers` to specify the number of workers.
