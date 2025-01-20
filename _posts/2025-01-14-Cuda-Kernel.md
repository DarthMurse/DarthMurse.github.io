---
title: 'GPU并行加速'
date: 2025-1-14
permalink: /posts/2025/01/14/blog-post-1/
tags:
  - GPU Acceleration
---

做深度学习的朋友们一定对pytorch不陌生吧？虽然pytorch提供了一套非常方便的自动求导框架，同时实现大部分常用的算子，但是对于某些操作（比如Transformer中的QKV Attention），使用pytorch原生的算子计算并不是那样的高效。通过自己编写CUDA kernel，可以使算子的速度和显存占用都得到大幅度的优化（[Flash-attention](https://github.com/Dao-AILab/flash-attention)），这篇博客将记录我探索CUDA kernel的过程。

## Mamba