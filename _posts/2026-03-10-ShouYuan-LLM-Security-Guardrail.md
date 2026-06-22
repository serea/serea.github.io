---
title: '为OpenClaw们装上智能安全锁，长亭发布"守元"大模型安全围栏'
date: 2026-03-10
permalink: /posts/2026/03/shouyuan-llm-security-guardrail/
tags:
  - AI安全
  - 大模型
  - 守元
  - 智能体安全
---

<div class="lang-en" markdown="1">

> Originally published on Chaitin Technology's WeChat account. [Read original](https://mp.weixin.qq.com/s/hs5ULgveu807qBv7sbCt3Q)

OpenClaw went viral — the era of mass AI agent adoption is here. But security concerns are more urgent than ever.

According to CNNVD, as of March 9, OpenClaw has 82 known vulnerabilities, with 33 rated critical or high severity. The security landscape is alarming.

As a leader in intelligent security, Chaitin Technology officially launches **"ShouYuan" (守元) LLM Security Guardrail** — featuring innovative streaming async detection, multi-model hybrid detection, data flywheel self-evolution, and agent risk cognition technologies.

## Four AI Risks, One Solution

**Content Safety:** Auto-filters hate speech, violence, pornography, and value-misaligned content.

**Model Jailbreak Attacks:** Prevents carefully crafted prompts from bypassing safety limits.

**Data Leakage:** Real-time detection of sensitive information (IDs, bank accounts, trade secrets) in inputs/outputs.

**Unsafe Execution:** Prevents agents from performing unauthorized, non-compliant, or destructive operations.

## Streaming Async Detection: Performance Meets Security

Traditional approaches use "generate → full scan → return," causing latency. ShouYuan innovates with **streaming async detection**: while the model generates tokens, a parallel copy streams to the security engine for real-time risk assessment. Risks trigger immediate alerts or interceptions — zero perceptible delay.

## Multi-Model Hybrid Detection

ShouYuan 1.0 employs a lightweight dynamic multi-model recognition system:

- **Text models**: 8B, 4B, and 0.6B variants, aligned to national standards (5 major categories, 31 subcategories), supporting Chinese, English, and 50+ dialects
- **Small models**: RoBERTa-based, trained on 800K proprietary samples with long-sequence understanding
- **Multimodal**: VL and Whisper models covering images, audio, and video risks

Models are orchestrated via DAG graphs to form a collaborative "intelligent defense matrix."

## Data Flywheel Self-Evolution

ShouYuan integrates offense ("spear" — security evaluation) and defense ("shield" — guardrail) through full-pipeline data exchange. By identifying false positives and false negatives in real deployments, the system continuously self-adapts to each customer's unique scenario.

## Agent Risk Cognition

For agents like OpenClaw operating in open environments, risks span the entire workflow — input, reasoning, tool calls, and execution. ShouYuan's proprietary **agent risk framework** decomposes risks across 4 key dimensions and defines **10 agent-specific risk categories** (task intent hijacking, unsafe tool calls, etc.) for precise full-chain security diagnosis.

</div>

<div class="lang-zh" markdown="1">

> 原文发布于长亭科技微信公众号，[点击阅读原文](https://mp.weixin.qq.com/s/hs5ULgveu807qBv7sbCt3Q)

OpenClaw爆火，全民养虾时代来临。但安全问题已是刻不容缓。

据国家信息安全漏洞库（CNNVD）统计，截至3月9日，OpenClaw漏洞多达82个，其中超危和高危漏洞有33个。安全风险可谓触目惊心。

身为国内智能安全领域的排头兵，长亭科技正式推出**"守元"大模型安全围栏**——聚焦大模型应用核心风险，创新流式异步检测、多模型混合检测、数据飞轮自进化、智能体风险认知等技术。

## 四大AI风险，一个解决方案

**内容安全风险：** 自动识别并过滤价值观偏离、暴力、色情、仇恨言论等不良内容。

**模型越狱攻击：** 防范通过精心设计的提示词绕过安全限制。

**数据泄露风险：** 实时检测输入输出中的敏感信息，防止"提示词注入"攻击导致数据外泄。

**不安全执行：** 防止智能体执行未授权、不合规、破坏性的操作。

## 流式异步检测：体验与安全兼得

传统安全方案采用"生成-全量检测-返回"模式，导致响应延迟。"守元"创新采用**流式异步检测技术**：大模型生成Token流的同时，实时复制到安全检测引擎进行动态研判。一旦识别风险，立即触发告警或拦截——用户零感知延迟。

## 多模型混合检测

"守元"1.0版本采用轻量化动态多模型识别方案：

- **文本识别模型**：8b、4b、0.6b三种规格，适配国家标准"五大类31小类"恶意行为分类，支持中文、英文及50多种方言
- **小模型**：RoBERTa架构，基于长亭自有80万语料对训练，具备长序列理解能力
- **多模态能力**：借助VL与Whisper模型，覆盖图片、语音、视频风险场景

借助DAG图编排防护能力构建"智能防御矩阵"。

## 数据飞轮自进化

整合"矛"——长亭大模型安全评估服务，与"盾"——大模型安全围栏能力，依托全流程数据互通，精准识别错误拦截与错误放行，实现在客户环境中的持续更新适配。

## 自研智能体风险认知

传统LLM安全围栏已管不住智能体新风险。长亭自研**智能体风险框架**，把风险拆成4个关键环节（用户输入、基础模型调用、工具调用、外部服务调用），定义了**10类智能体专属风险**（任务意图劫持、不安全工具调用等），实现安全诊断的精准落地。

</div>
