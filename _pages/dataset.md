---
layout: archive
title: "Datasets"
permalink: /dataset/
author_profile: true
redirect_from:
  - /dataset
---

<div class="lang-en" markdown="1">

This page lists all the datasets we have collected and used in our papers. 
To access them, please send an email to me (suliya@iie.ac.cn).

## Ethereum DEFIER

We collected and reconstructed 42 real-world Dapp attack incidents, consisting of 126 semantic-similar transaction clusters with 58,555 transactions.
We manually annotated them and performed a measurement study on our paper [Evil Under the Sun: Understanding and Discovering Attacks on Ethereum Decentralized Applications](http://academicpages.github.io/files/evil.pdf).


### Format

| column                | type    | description                |
| -------------------- | -------- | -------------------- |
| event              | varchar  | the reported event name   |
| **HashKey**          | varchar  | the hash address of transaction          |
| controlUserAddress   | varchar  | the user who initiated the transaction    |
| gameName             | varchar  | the name of the game involved      |
| gameAddress          | varchar  | the address of the game involved         |
| txDate               | Datetime | the time of transaction             |
| txMethod             | varchar  | the name of the function called     |
| smartContractAddress | varchar  | the first contract address called|
| smartContractName    | varchar  | the first contract name called   |
| group             | varchar  | the related attacking group name    |
| stage             | varchar  | the related attack stage           |

### Citation

> @inproceedings{su2021evil,  
>  title={Evil Under the Sun: Understanding and Discovering Attacks on Ethereum Decentralized Applications},  
>  author={Su, Liya and Shen, Xinyue and Du, Xiangyu and Liao, Xiaojing and Wang, XiaoFeng and Xing, Luyi and Liu, Baoxu},  
>  booktitle={30th USENIX Security Symposium (USENIX Security 21)},  
>  publisher={USENIX},  
>  year={2021}
> }

</div>

<div class="lang-zh" markdown="1">

本页面列出了我们在论文中收集和使用的所有数据集。
如需获取数据，请发送邮件至 suliya@iie.ac.cn。

## 以太坊 DEFIER 数据集

我们收集并重构了 42 起真实的 Dapp 攻击事件，包含 126 个语义相似的交易聚类，共 58,555 笔交易。
我们对数据进行了人工标注，并在论文 [Evil Under the Sun: Understanding and Discovering Attacks on Ethereum Decentralized Applications](http://academicpages.github.io/files/evil.pdf) 中进行了测量研究。


### 数据格式

| 字段                | 类型    | 描述                |
| -------------------- | -------- | -------------------- |
| event              | varchar  | 报告的事件名称   |
| **HashKey**          | varchar  | 交易的哈希地址          |
| controlUserAddress   | varchar  | 发起交易的用户    |
| gameName             | varchar  | 涉及的游戏名称      |
| gameAddress          | varchar  | 涉及的游戏地址         |
| txDate               | Datetime | 交易时间             |
| txMethod             | varchar  | 调用的函数名称     |
| smartContractAddress | varchar  | 调用的第一个合约地址|
| smartContractName    | varchar  | 调用的第一个合约名称   |
| group             | varchar  | 相关攻击组名称    |
| stage             | varchar  | 相关攻击阶段           |

### 引用

> @inproceedings{su2021evil,  
>  title={Evil Under the Sun: Understanding and Discovering Attacks on Ethereum Decentralized Applications},  
>  author={Su, Liya and Shen, Xinyue and Du, Xiangyu and Liao, Xiaojing and Wang, XiaoFeng and Xing, Luyi and Liu, Baoxu},  
>  booktitle={30th USENIX Security Symposium (USENIX Security 21)},  
>  publisher={USENIX},  
>  year={2021}
> }

</div>
