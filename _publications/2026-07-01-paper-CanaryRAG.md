---
title: "Detecting RAG Extraction Attack via Dual-Path Runtime Integrity Game"
collection: publications
permalink: /publication/2026-07-01-paper-CanaryRAG
date: 2026-07-01
venue: 'Proceedings of the 64th Annual Meeting of the Association for Computational Linguistics (ACL 2026)'
paperurl: 'https://aclanthology.org/2026.acl-long.385/'
doi: '10.18653/v1/2026.acl-long.385'
citation: 'Yuanbo Xie, Yingjie Zhang, Yulin Li, Shouyou Song, Xiaokun Chen, Zhihan Liu, Liya Su, Tingwen Liu. Detecting RAG Extraction Attack via Dual-Path Runtime Integrity Game. In Proceedings of the 64th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pp. 8503-8518, ACL 2026, San Diego, California, United States.'
---

[Download paper here](https://aclanthology.org/2026.acl-long.385.pdf)

Recommended citation: Yuanbo Xie, Yingjie Zhang, Yulin Li, Shouyou Song, Xiaokun Chen, Zhihan Liu, Liya Su, Tingwen Liu. Detecting RAG Extraction Attack via Dual-Path Runtime Integrity Game. In Proceedings of the 64th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pp. 8503-8518, ACL 2026, San Diego, California, United States. DOI: 10.18653/v1/2026.acl-long.385.

## Abstract

Retrieval-Augmented Generation (RAG) systems augment large language models with external knowledge, yet introduce a critical security vulnerability: RAG Knowledge Base Leakage, wherein adversarial prompts can induce the model to divulge retrieved proprietary content. Recent studies reveal that such leakage can be executed through adaptive and iterative attack strategies (named RAG extraction attack), while effective countermeasures remain notably lacking. To bridge this gap, we propose CanaryRAG, a runtime defense mechanism inspired by stack canaries in software security. CanaryRAG embeds carefully designed canary tokens into retrieved chunks and reformulates RAG extraction defense as a dual-path runtime integrity game. Leakage is detected in real time whenever either the target or oracle path violates its expected canary behavior, including under adaptive suppression and obfuscation. Extensive evaluations against existing attacks demonstrate that CanaryRAG provides robust defense, achieving substantially lower chunk recovery rates than state-of-the-art baselines while imposing negligible impact on task performance and inference latency. Moreover, as a plug-and-play solution, CanaryRAG can be seamlessly integrated into arbitrary RAG pipelines without requiring retraining or structural modifications, offering a practical and scalable safeguard for proprietary data.
