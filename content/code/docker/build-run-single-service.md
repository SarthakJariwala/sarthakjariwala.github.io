---
title: "Build & Run a Single Service from docker-compose"
date: 2021-09-25T19:59:05-07:00
tags: ["docker", "docker-compose"]
author: ["Sarthak Jariwala, Ph.D."]
showToc: false
TocOpen: false
draft: false
hidemeta: false
comments: false
description: "Build and run single service using docker-compose"
disableHLJS: true # to disable highlightjs
disableShare: false
disableHLJS: false
hideSummary: true
searchHidden: false
ShowReadingTime: true
ShowBreadCrumbs: true
ShowPostNavLinks: true
---

### Preliminaries

If you have multiple services listed in your `docker-compose` file as shown below:
```YAML
# example docker-compose.yml
version: "3.7"

services:
  test:
    image: ezconda-test
    build:
      context: ./
      dockerfile: Dockerfile
    
    container_name: ezconda-test
  
  dev:
    image: ezconda-dev
    build:
      context: ./
      dockerfile: Dockerfile.dev
    
    container_name: ezconda-dev
```

### Build and Run a Specific Service

To only build and run the `dev` service:

```bash
docker-compose build dev && docker-compose run dev bash
```
> Here, `bash` is the command that we want to run in the container.