---
title: "Codespell - check spelling"
date: 2021-08-04T21:36:58-07:00
draft: false
---

I came across `codespell` via [Simon Willison's tweet](https://twitter.com/simonw/status/1422601066156158977).

[Codespell](https://github.com/codespell-project/codespell) is a python library that provides a cli to check and fix common misspellings in text files.

Just running it against the content of this website, I discovered a few misspellings.

```bash
codespell content
```
![codespell](/images/codespell.png)

The changes suggested by `codespell` can be implemented with a `-w` flag.