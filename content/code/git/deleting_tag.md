---
title: "Delete Git Tag"
date: 2022-04-20T09:54:26-07:00
tags: ["git"]
author: ["Sarthak Jariwala, Ph.D."]
showToc: false
TocOpen: false
draft: false
hidemeta: false
comments: false
description: ""
# canonicalURL: "https://canonical.url/to/page"
disableHLJS: false # to disable highlightjs
disableShare: false
disableHLJS: false
hideSummary: true
searchHidden: false
ShowReadingTime: true
ShowBreadCrumbs: true
ShowPostNavLinks: true
---

### Delete a git tag

```bash
git tag -d v1.0.1
```

Here, `v1.0.1` is the tag we want to delete.

### Remove it from remote/GitHub

```bash
git push origin :v1.0.1
```

> Note the ":" before the tag you want to remove from remote.
