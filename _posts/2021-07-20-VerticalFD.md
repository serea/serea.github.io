---
title: 'Vertical Federated Learning in Finance'
title_zh: '金融领域的纵向联邦学习'
date: 2021-07-20
permalink: /posts/2021/07/verticalfd/
tags:
  - Federated Learning
  - Internship
---

<div class="lang-en" markdown="1">

Federated learning can be categorized into *horizontal*, *vertical*, and *federated transfer learning* based on how participants' data is distributed.

**Horizontal FL** splits by samples and allows relatively general solutions. **Vertical FL** is more challenging and widely applied in industry — different parties hold different feature dimensions of the same samples (due to different business functions).

In risk control scenarios, vertical FL is particularly prevalent: labels are held by only one party (Guest), while others (Host) hold partial features. The Guest wants to improve model performance through collaboration while both parties must ensure data security.

## SecureBoost

In risk control, tree models (especially **XGBoost**) are widely used for their interpretability. SecureBoost extends XGBoost to vertical FL using homomorphic encryption:

1. **Encrypted sample alignment** using Private Set Intersection (PSI)
2. **Encrypted model training**: Guest computes first/second-order gradients, encrypts and sends to Host parties. Host computes aggregated split gains under encryption and returns to Guest for decryption. Best splits are selected without exposing raw data.

## Interpretability Requirements

In single-party sub-model scenarios (Guest has only labels, Host has features), new requirements emerge:
- Guest needs to understand node feature meanings for model interpretability
- But knowing predictions + tree structure could allow Guest to reverse-engineer Host's feature values
- Conversely, Host cannot access Guest's labels or leaf weights

Current SecureBoost cannot simultaneously satisfy both requirements — a key limitation for real-world deployment.

## Efficiency Challenges

Homomorphic encryption requires massive ciphertext communication per training round. SecureBoost provides high security but at enormous communication cost, significantly reducing practical usability — a major obstacle for deployment.

</div>

<div class="lang-zh" markdown="1">

依据联邦学习的不同参与方持有数据的特点，可分为*横向联邦学习*、*纵向联邦学习*以及*联邦迁移学习*。

**横向联邦学习**是样本的分割，可设计较为通用的方案。**纵向联邦学习**更困难且业界应用广泛——不同数据持有方具备同一样本的不同特征维度。

在风控场景中纵向联邦学习应用最广泛：标签仅为Guest方持有，Host方拥有部分特征。Guest方希望通过合作提升模型效果，同时双方需保证数据安全。

## SecureBoost

风控中树模型（**XGBoost**）因可解释性被广泛应用。SecureBoost使用同态加密将XGBoost扩展到纵向联邦：

1. **加密样本对齐**：基于隐私求交技术
2. **加密模型训练**：Guest计算一阶、二阶梯度并加密传输给Host，Host在密文上计算分裂增益聚合值返回Guest解密，选择最优分裂

## 可解释性要求

单方子模型场景（Guest仅有标签，Host有特征）下的新要求：
- Guest需了解模型节点特征含义以满足可解释性
- 但知道预测值+树结构可能推测出Host方特征值
- 同时Host不可获取Guest方标签和叶子节点权重

现有SecureBoost方案无法同时满足这两个要求——实际落地的关键限制。

## 效率挑战

基于同态计算的联邦学习需要在每轮训练中传递大量密文，通讯成本巨大，大大降低了模型可用性，成为实际落地的主要困难。

</div>
