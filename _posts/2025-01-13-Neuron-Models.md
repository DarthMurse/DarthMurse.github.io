---
title: 'Neuron Models'
date: 2025-1-13
permalink: /posts/2025/01/13/blog-post-1/
tags:
  - Neural Dynamics
---

在这篇博客中，我会总结一些常见的神经元模型。

### 多分枝模型
这是由李国齐团队于2024年提出的多分枝非线性神经元模型(Huang et al. 2024)，其基本思想为在点神经元（Point Neuron）模型的基础上加入多个树突分枝，以增强神经元的表达能力。具体计算方式如下：

$$V_i^d[0] = X_i[0]$$

$$V_i^d[t] = \alpha V_i^d[t-1] + X_i[t]$$

$$Y_i[t] = K_{t, i}f_i(V_i^d[t])$$

$$H^s[t] = \beta V^S[t-1] + (1 - \beta)\sum_{i=1}^BY_i[t]$$

$$S[t] = \Theta(H^s[t] - 1)$$

$$V^s[t] = (1 - S[t])H^s[t]$$

但是从计算角度而言，这个所谓的多分枝模型差不多是把原本神经元间的线性连接从单个线性层变成了一个两层的MLP，为了能够进行并行计算，神经元的状态更新中不能出现关于膜电位的非线性运算（多项式是否可行？）

