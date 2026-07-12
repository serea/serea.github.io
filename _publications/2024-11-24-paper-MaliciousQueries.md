---
title: "Can LLMs deeply detect complex malicious queries? A framework for jailbreaking via obfuscating intent"
collection: publications
permalink: /publication/2024-11-24-paper-MaliciousQueries
date: 2024-11-24
venue: 'The Computer Journal, 2024, British Computer Society / Oxford University Press'
paperurl: 'https://doi.org/10.1093/comjnl/bxae124'
doi: '10.1093/comjnl/bxae124'
citation: 'Shang Shang, Xinqiang Zhao, Zhongjiang Yao, Yepeng Yao, Liya Su, Zijing Fan, Xiaodan Zhang, Zhengwei Jiang. Can LLMs deeply detect complex malicious queries? A framework for jailbreaking via obfuscating intent. The Computer Journal, 2024.'
---

[Download paper here](https://doi.org/10.1093/comjnl/bxae124)

Recommended citation: Shang Shang, Xinqiang Zhao, Zhongjiang Yao, Yepeng Yao, Liya Su, Zijing Fan, Xiaodan Zhang, Zhengwei Jiang. Can LLMs deeply detect complex malicious queries? A framework for jailbreaking via obfuscating intent. The Computer Journal, 2024. DOI: 10.1093/comjnl/bxae124.

## Abstract

This paper delves into a possible security flaw in large language models (LLMs), particularly in their capacity to identify malicious intent within intricate or ambiguous inquiries. We have discovered that LLMs might overlook the malicious nature of highly veiled requests, even without alterations to the malevolent text in those queries, thus exposing a significant weakness in their content analysis systems. To be specific, we pinpoint and scrutinize two aspects of this vulnerability: (i) LLMs' diminished capability to perceive maliciousness when parsing extremely obscured queries, and (ii) LLMs' inability to discern malicious intent in queries that have been intentionally altered to increase their ambiguity by modifying the malevolent content itself. To illustrate and tackle this problem, we propose a theoretical framework and analytical strategy, and introduce a novel black-box jailbreak attack technique called IntentObfuscator. This technique exploits the identified vulnerability by concealing the genuine intentions behind user prompts, thereby compelling LLMs to inadvertently produce restricted content and circumvent their inherent content safety protocols. We elaborate on two specific applications within this framework: "Obscure Intention" and "Create Ambiguity," which skillfully manipulate the complexity and ambiguity of queries to effectively dodge the detection of malicious intent. We empirically confirm the efficacy of the IntentObfuscator approach across various models, including ChatGPT-3.5, ChatGPT-4, Qwen, and Baichuan, achieving an average jailbreak success rate of 69.21%. Remarkably, our tests on ChatGPT-3.5, boasting 100 million weekly active users, yielded an impressive success rate of 83.65%. Additionally, we verify our approach across a range of sensitive content categories, including graphic violence, racism, sexism, political sensitivity, cybersecurity threats, and criminal techniques, further highlighting the considerable impact of our findings on refining "Red Team" tactics against LLM content security frameworks.
