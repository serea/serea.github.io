---
title: '区块链论文解读———未知智能合约的逆向'
date: 2018-09-29
permalink: /posts/2018/09/smartcontractreverse/
tags:
  - Smart Contract
  - Reverse
---

<div class="lang-en" markdown="1">

This is a paper reading note on "Erays: Reverse Engineering Ethereum's Opaque Smart Contracts" published at USENIX Security 2018 by the University of Illinois Urbana-Champaign.

Smart contracts only need to execute bytecode and can keep their source code unknown — this poses significant challenges for analysis. The paper proposes a reverse engineering tool for EVM bytecode that produces higher-level representations suitable for manual analysis.

* Author: Liya Su, Ph.D. candidate at IIE, CAS. Research area: Cyberspace Security and Big Data.
* Paper: [Erays: Reverse Engineering Ethereum's Opaque Smart Contracts](https://www.usenix.org/conference/usenixsecurity18/presentation/zhou)
* Authors: Yi Zhou, Deepak Kumar, Surya Bakshi, Joshua Mason, Andrew Miller, Michael Bailey

## Introduction

Smart contracts are programs that facilitate traceable, irreversible digital transactions. In 2018, Ethereum smart contracts held over $10 billion and facilitated crowdfunding, decentralized exchanges, and supply chain tracking. However, many contracts lack publicly available source code, making auditing extremely difficult.

## Key Contributions

1. **Erays** — a reverse engineering tool that takes compiled EVM bytecode and returns high-level pseudocode suitable for manual analysis, converting from stack-based to register-based representation
2. Measurement of the Ethereum smart contract ecosystem (code complexity and code reuse)
3. "Fuzzy hashing" mechanism to link opaque contracts to publicly available source code
4. Four case studies: high-value multisig wallets, arbitrage bots, exchange accounts, and CryptoKitties

## System Design

1. **Disassembly & Basic Block Identification**: Disassemble hex strings into EVM instructions, partition into basic blocks
2. **Control Flow Graph Recovery**: Model stack states through CFG, handling three cases — sequential flow, termination instructions, and branch instructions (JUMP/JUMPI)
3. **Lifting**: Convert stack-based instructions to register-based
4. **Optimization**: Constant folding, constant propagation, copy propagation, dead code elimination
5. **Aggregation**: Combine definitions with their uses for more compact output
6. **Validation**: 15,855 historical transactions tested; 3.22% failure rate (196 construction failures, 314 validation failures)

## Experiments

On 34K unique contracts: median block count is 100, median instructions per block is 15. 79% of contracts contain no function with McCabe complexity >10. Code reuse analysis shows the most popular function implementations appear in 11K contracts. Using Erays on the top-10 highest-balance opaque contracts, 66% of functions were successfully matched on average, with one contract achieving 100% match (holding 488K ETH ≈ $500M in 2018).

## Case Studies

- **High-value multisig wallets**: Reverse-engineered access control revealing 2-of-3 admin signature requirements
- **Arbitrage bots**: Discovered batch-trading contracts for synchronized EtherDelta trades
- **CryptoKitties**: Fully reconstructed the `mixGenes` function in 3 hours, identifying gene selection probabilities and mutation mechanics

</div>

<div class="lang-zh" markdown="1">

本文是伊利诺伊大学香槟分校发表于USENIX 2018 的工作，文章提出了一种在逆向分析以太坊上智能合约代码的模型。

智能合约只需要执行代码，可以保持源代码未知给智能合约分析带来了巨大的挑战。文章使用逆向分析技术，给出智能合约执行代码的更高级别表示以满足人工分析的需求。

* 关于编辑作者：苏莉娅，中国科学院信工所博士，研究方向为网络空间安全与大数据。
* 论文原文: Erays: Reverse Engineering Ethereum's Opaque Smart Contracts
* 论文下载链接: [paper-download](https://www.usenix.org/conference/usenixsecurity18/presentation/zhou)
* 论文作者: Yi Zhou / Deepak Kumar / Surya Bakshi / Joshua Mason / Andrew Miller / Michael Bailey

## 引言

智能合约是促进可跟踪、不可逆转的数字交易的程序。2018年以太坊智能合约持有超过100亿美元。但许多智能合约没有可用的公共源代码，使得审计工作非常困难。

## 主要贡献

1. **Erays**：将编译后的EVM智能合约作为输入，返回适合手动分析的高级伪代码，将基于堆栈的语言转换为基于寄存器的表示
2. 测量以太坊智能合约生态系统（代码复杂性和代码重用）
3. "模糊散列"机制，将不透明合约链接到公开源代码
4. 四个案例研究：高价值多重签名钱包、套利机器人、交换账户、CryptoKitties

## 系统设计

1. **反汇编和基本块识别**：将十六进制字符串反汇编为EVM指令，分区为基本块
2. **恢复控制流图**：对堆栈状态建模，处理三种情况——顺序流、终止指令、分支指令(JUMP/JUMPI)
3. **提升**：将基于堆栈的指令转变为基于寄存器的指令
4. **优化**：常量折叠、常量传播、复制传播、死代码消除
5. **聚合**：将定义与用法组合，产生更紧凑的输出
6. **验证**：测试15,855笔历史交易；失败率3.22%

## 实验

在34K唯一合约上：中位数块数100，中位数指令数15。79%的合约不包含McCabe复杂度>10的函数。代码重用分析显示最流行的函数实现出现在11K个合约中。对余额最高的10个不透明合约使用Erays，平均成功匹配66%的功能，其中一个合约实现100%匹配（持有488K ETH ≈ 2018年5亿美元）。

## 案例研究

- **高价值多重签名钱包**：逆向工程揭示2-of-3管理员签名要求
- **套利机器人**：发现EtherDelta同步批量交易合约
- **CryptoKitties**：3小时内完全重建`mixGenes`函数，识别基因选择概率和突变机制

</div>
