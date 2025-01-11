---
title: RWKV
date: 2025-01-10
permalink: /posts/RWKV/
tags: 
  - Linear Attention
---

在如今的大语言模型（Large Language Model, LLM）领域，Transformer是占据绝对主流的模型架构。然而，Transformer中的核心注意力模计算复杂度随上下文长度S的平方增长的特性使得其在长上下文的推理和训练中会消耗更多的时间和能量。为此，学者们提出了许多具有线性甚至更低复杂度的注意力机制用于替代Transformer中的Attention。在接下来的几篇博客中，我将整理出目前关注度较高的几种线性注意力模型，探究它们设计中的核心理念，并在小规模的模型和数据量下比较一下这些模型的性能。

## RWKV结构
RWKV（读作RwaKuv）是2023年由Bo Peng设计训练的一种类似RNN的线性注意力大语言模型，其模块中除了常见的残差连接和LayerNorm之外，最核心的部分就是TimeMixing和ChannelMixing模块。和GPT系列模型相似，RWKV采用自监督学习的方式训练网络，输入的语段经过tokenizer和单词嵌入（wordembedding）之后变为形状为$[B, S, D]$的张量，其中$B$为batch\_size，$S$为上下文长度（context length），$D$为特征（channel）维度的大小。模型的输出同样是形状为$[B, S, D]$的张量，经过输出的单词嵌入矩阵和Softmax之后变为对应位置下个单词（token）的概率分布。下面为了简单起见，我们将忽略$B$维度，假设网络的输入和输出均为$[S, D]$大小的张量（即$B = 1$）。
![RWKV结构](https://simg.baai.ac.cn/uploads/2023/05/729cfd6129f57e173b1bd7b881b7e327.png)
### Time Mixing 
假设输入为大小为$[S, D]$的张量，Time Mixing模块的计算方式如下：
$$r_t = W_r \cdot (\mu_r + (1 - \mu_r)x_{t-1}),$$$$k_t = W_k \cdot (\mu_k + (1 - \mu_k)x_{t-1}),$$$$v_t = W_v \cdot (\mu_v + (1 - \mu_v)x_{t-1}),$$$$wkv_t = \frac{\sum_{i=1}^{t-1}e^{-(t-1-i)w+k_i}v_i + e^{u+k_t}v_t}{\sum_{i=1}^{t-1}e^{-(t-1-i)w+k_i} + e^{u+k_t}},$$$$o_t = W_o \cdot (\sigma(r_t) \odot wkv_t),$$
其中$x_t, r_t, k_t, v_t, o_t$均为长度为$D$的向量，$W_r, W_k, W_v, W_o$均为大小为$[D, D]$的矩阵，$\mu_r, \mu_k, \mu_v$均为长度为$D$的向量参数，$w, u$均为长度为$D$（其实在代码中是$H$，即注意力头的大小）的向量参数。这个模块主要采用$wkv_t$代替Transformer中的Attention结构，把$k_i$作为类似Softmax中的指数项来控制$v_i(i=1,2,\ldots, t)$的权重，实现注意力的功能。同时采用了RNN中常见的门控单元进一步对信息进行过滤，实现更强的记忆功能，也可以防止梯度爆炸和梯度消失的出现。

### Channel Mixing
假设输入为大小为$[S, D]$的张量，Channel Mixing模块的计算方式如下：
$$r_t = W_r \cdot (\mu_r + (1 - \mu_r)x_{t-1}),$$$$k_t = W_k \cdot (\mu_k + (1 - \mu_k)x_{t-1}),$$$$o_t = \sigma(r_t) \odot (W_v \cdot max(k_t, 0)^2),$$
和Time Mixing相比，Channel Mixing不含注意力单元，仅仅包含了一个门控模块，可以类比为Transformer中的MLP层（由简单的线性层和激活函数组成的结构）。

### 关于结构设计的一些思考
[RWKV的原始论文](https://arxiv.org/abs/2305.13048)中并没有解释为何两个核心模块中大量出现的类似$$r_t = W_r \cdot (\mu_r + (1 - \mu_r)x_{t-1}$$的信息编码中需要同时用到$t$和$t-1$时刻的信息进行消融实验（ablation study），只是将其解释为一种针对时间的差值或者说卷积。我认为这种做法的合理性值得进行进一步探索和分析。

## RWKV模型效果
在经过预训练之后，RWKV在LAMBADA，PIQA，WinoGrande，Arc\_easy等数据集上取得了和Transformer结构相当甚至更好的效果。但是由于预训练的语料质量会对训练结果造成很大的影响，并且RWKV的原始论文中并没有详细说明其数据预处理方法以及是否进行过数据增强，因此下图中与Transformer模型的对比可能只能在一定程度上说明问题。
![RWKV效果](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/blog/142_rwkv/RWKV-eval.png)
在之后的一些研究中有学者指出，RWKV在处理长时间的文本依赖时效果较差，这也是RNN结构内在的一个缺点。

在计算上，RWKV单个Block的计算复杂度为$O(BSD^2)$，显然这是一个随$S$计算复杂度线性增长的模型。它还具有高度并行训练的能力，大大提高了训练速度，同时在推理时又可以向RNN那样迭代计算。

## 一些细节
RWKV的参数初始化非常复杂，同时还对训练的结果有较大的影响。

## 复现结果
敬请期待