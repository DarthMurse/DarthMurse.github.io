---
title: 'Linear Attention'
date: 2025-01-12
category: Linear Attention
readTime: 10 min read
---

# Linear Attention
在这篇文章中，我将总结几种Softmax Attention和几种Linear Attention的并行训练和递推推理的计算方式以及相应的复杂度。

### Softmax Attention
下文中均假设网络的输入为$$[L, D]$$，其中$$L$$为序列长度，$$D$$为表征向量的大小，$$H$$为Attention头数量（并行、减少计算量），$$D_H$$为每个Head的表征向量大小。$$@$$代表矩阵乘法，$$\cdot$$代表向量内积。

训练：（计算量$$O(LD^2 + L^D)$$）

$$Q = X@W_Q, Q[L, D] \rightarrow Q[H, L, D_H]$$

$$K = X@W_K, K[L, D] \rightarrow K[H, L, D_H]$$

$$V = X@W_V, V[L, D] \rightarrow V[H, L, D_H]$$

对每一个Head $$Y = Softmax(Q @ K^T // \sqrt{D_H})@V$$

$$Y[H, L, D_H] \rightarrow Y[L, D], O = Y@W_O$$

推理：（计算了$$O(D^2 + LD)$$）

$$CK_{t-1}, CV_{t-1}[H, t-1, D_H], x_t[D]$$

$$q_t = x_t@W_Q, q_t[D] \rightarrow  q_t[H, D_H]$$

$$k_t = x_t@W_K, k_t[D] \rightarrow k_t[H, D_H]$$

$$v_t = x_t@W_V, v_t[D] \rightarrow v_t[H, D_H]$$

对每一个Head $$CK_t = [CK_{t-1}, k_t], CV_t = [CV_{t-1}, v_t], y_t = Softmax(CK_t @ q_t^T// \sqrt{D_H}) @ CV_t$$

$$y_t[H, D_H] \rightarrow y_t[D], o_t = y_t@W_O$$

### Linear Attention
训练：（计算量$$O(LD^2)$$）

$$Q = X@W_Q, Q[L, D] \rightarrow Q[H, L, D_H]$$

$$K = X@W_K, K[L, D] \rightarrow K[H, L, D_H]$$

$$V = X@W_V, V[L, D] \rightarrow V[H, L, D_H]$$

对每一个Head $$Y = \phi(Q) @ \psi(K)^T @ V$$

$$Y[H, L, D_H] \rightarrow Y[L, D], O = Y@W_O$$

推理：（计算量$$O(D^2)$$）

$$CKV_{t-1}[H, D_H, D_H], x_t[D]$$

$$q_t = x_t@W_Q, q_t[D] \rightarrow  q_t[H, D_H]$$

$$k_t = x_t@W_K, k_t[D] \rightarrow k_t[H, D_H]$$

$$v_t = x_t@W_V, v_t[D] \rightarrow v_t[H, D_H]$$

对每一个Head $$CKV_t = CKV_{t-1} + \psi(v_t)^T @ k_t^T, y_t = \phi(q_t) @ CKV_t$$

$$y_t[H, D_H] \rightarrow y_t[D], o_t = y_t@W_O$$

### RetNet
训练：（计算量$$O(LD^2)$$）

$$Q = X@W_Q, Q[L, D] \rightarrow Q[H, L, D_H]$$

$$K = X@W_K, K[L, D] \rightarrow K[H, L, D_H]$$

$$V = X@W_V, V[L, D] \rightarrow V[H, L, D_H]$$

对每一个Head $$Y = (\phi(Q) @ \psi(K)^T \odot P) @ V, P_{nm} = \gamma^{n-m}, n \geq m, 0, n < 0$$

$$Y[H, L, D_H] \rightarrow Y[L, D], O = Y@W_O$$

推理：（计算量$$O(D^2)$$）

$$CKV_{t-1}[H, D_H, D_H], x_t[D]$$

$$q_t = x_t@W_Q, q_t[D] \rightarrow  q_t[H, D_H]$$

$$k_t = x_t@W_K, k_t[D] \rightarrow k_t[H, D_H]$$

$$v_t = x_t@W_V, v_t[D] \rightarrow v_t[H, D_H]$$

对每一个Head $$CKV_t = \gamma CKV_{t-1} + \psi(v_t)^T @ k_t^T), y_t = \phi(q_t) @ CKV_t$$

$$y_t[H, D_H] \rightarrow y_t[D], o_t = y_t@W_O$$

### Gated Linear Attention


推理：（计算量$$O(D^2)$$）

$$CKV_{t-1}[H, D_H, D_H], x_t[D]$$

$$q_t = x_t@W_Q, q_t[D] \rightarrow  q_t[H, D_H]$$

$$k_t = x_t@W_K, k_t[D] \rightarrow k_t[H, D_H]$$

$$v_t = x_t@W_V, v_t[D] \rightarrow v_t[H, D_H]$$

$$r_t = \sigma(x_t@W_R), r_t[D] \rightarrow r_t[H, D_H]$$

$$\alpha_t = \sigma(x_tW_{\alpha 1}W_{\alpha 2} + b_{\alpha}) W_{\alpha 1}[D, 16] W_{\alpha 2}[16, D]$$

$$G_t = Diag(\alpha_t)$$

对每一个Head $$CKV_t = G_t \odot CKV_{t-1} + v_t^T @ k_t^T, y_t = r_t \odot (q_t @ CKV_t)$$

$$y_t[H, D_H] \rightarrow y_t[D], o_t = y_t@W_O$$

### A General Recursive Form
对每一个Head $$CKV_t = G_t \odot CKV_{t-1} + v_t^T @ k_t^T, y_t = q_t @ CKV_t$$

![GLA 形式整理](https://darthmurse.github.io/images/GLA-summary.png)
