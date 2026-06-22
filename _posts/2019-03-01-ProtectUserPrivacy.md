---
title: 'Protecting User Privacy: Untraceable Web Browsing History and Unambiguous User Profiles'
date: 2019-03-1
permalink: /posts/2019/03/protectuserprivacy/
tags:
  - privacy protecting
  - web browing
---

<div class="lang-en" markdown="1">

Paper reading note: [Protecting user privacy: an approach for untraceable web browsing history and unambiguous user profiles](https://arxiv.org/abs/1811.09340), Beigi et al., WSDM'19, Arizona State University

Related: [De-anonymizing web browsing data with social networks](https://cs.stanford.edu/~jtysu/2017-04-07.pdf), Jessica Su et al., Stanford University

> "Beyond web browsers, users' browsing histories are recorded by third-party trackers embedded in web pages. ISPs like AT&T and Verizon have full access to browsing history. After FCC privacy protections were repealed in 2017, ISPs can monitor, collect, share, and sell users' online behavior without consent."

Since removing historical data is impossible, the only option is adding noise. The paper explores this privacy-utility tradeoff through the **PBooster** system:

> "How many links and what links should be added to a user's browsing history to protect privacy while preserving high usability?"

If we only care about privacy (ignoring usability), random link injection is optimal. PBooster approximates this result while preserving most usability — random strategies severely damage history usability, but PBooster retains the majority.

</div>

<div class="lang-zh" markdown="1">

论文解读：[Protecting user privacy: an approach for untraceable web browsing history and unambiguous user profiles](https://arxiv.org/abs/1811.09340), Beigi et al., WSDM'19, 亚利桑那州立大学

相关论文：[De-anonymizing web browsing data with social networks](https://cs.stanford.edu/~jtysu/2017-04-07.pdf), Jessica Su et al., Stanford University

> "除了网络浏览器，用户的历史浏览记录还通过第三方嵌入在网页的跟踪器被记录下来。ISP如AT&T和Verizon拥有用户浏览历史的完整权限。2017年FCC隐私保护被取缔后，ISP可以无需授权地监控、收集、共享和售卖用户在线行为。"

由于从历史中移除信息不可能，唯一能做的是添加噪声。论文通过**PBooster**系统探索隐私与可用性的权衡：

> "多少链接和什么链接应该添加到用户的浏览历史中以保护用户隐私的同时保留高可用性？"

如果仅考虑隐私不考虑可用性，随机添加链接是最好的策略。PBooster尝试接近这种结果的同时保留大部分可用性——随机策略严重影响历史可用性，但PBooster能够保留大部分。

</div>
