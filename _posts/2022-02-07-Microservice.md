---
title: 'Google Cloud-Native Microservice Architecture'
title_zh: 'Google 云原生微服务架构'
date: 2022-02-07
permalink: /posts/2022/02/Microservice/
tags:
  - Cloud Native
---

<div class="lang-en" markdown="1">

### Cloud Native & Microservices

Cloud native, as championed by CNCF, includes key technologies: **containers, service meshes, microservices, immutable infrastructure, and declarative APIs**. Microservices decompose application tasks into independently developed, managed services — each with its own API, release cycle, scaling, and quota management. They are **independent, modular, dynamic, and ephemeral**.

### Cloud-Native Security

Google's cloud-native security system **BeyondProd** shifts from traditional perimeter-based security (trusting users based on network context like IP/hostname) to service-based trust through code provenance and service identity verification.

Key changes from traditional security:
1. **Network layer**: From perimeter security (WAF) to zero-trust — all services are untrusted, authentication is service-based
2. **Application**: From monolithic security policies to cross-service consistent enforcement with individual microservice updates
3. **Hardware**: From VMs/physical machines to workload isolation where different services share the operating system

### Cloud-Native Security vs. Zero Trust

Zero trust focuses on user identity verification with encryption for user-level security management. Cloud-native security emphasizes microservice-level boundary security with different trust levels and controls. Identity is based on services, not IP addresses.

### BeyondProd Components

1. **Edge network protection** → Google Front End (GFE)
2. **No inherent inter-service trust** → Application Layer Transport Security (ALTS)
3. **Known-provenance code execution** → Binary Authorization for Borg (BAB), Host Integrity (HINT)
4. **Cross-service policy enforcement** → Service Access Policy, End User Context tickets (EUC)
5. **Simple, automated, standardized releases** → Borg tooling
6. **Workload isolation on shared OS** → gVisor

Key products:
- **GFE**: TLS termination, edge proxy
- **ALTS**: RPC authentication, integrity, encryption
- **BAB**: Code review, binary verification
- **HINT**: Secure boot, digital signature verification on BIOS/BMC/bootloader/kernel
- **EUC**: Integrity-protected, centrally-issued, forwardable credentials
- **gVisor**: User-space kernel intercepting syscalls, reducing host interaction

</div>

<div class="lang-zh" markdown="1">

### 云原生与微服务

云原生技术由CNCF推广，代表技术包括**容器、服务网格、微服务、不可变基础设施和声明式API**。微服务将应用任务分离成单独服务，每项服务独立开发管理，具有自己的API、发布、扩缩和配额管理。微服务是**独立的、模块化的、动态的、短暂的**。

### 云原生安全

Google云原生安全系统**BeyondProd**从传统的边界安全（基于IP/主机名信任用户）转向对服务的信任，通过代码出处和服务身份认证实现。

三方面变化：
1. **网络层**：从边界安全(WAF)转向零信任——所有服务间无信任，基于服务认证
2. **应用**：从整体更新转向跨服务一致安全策略，可频繁更新个别微服务
3. **硬件**：从虚拟机/物理机转向封装工作负载的隔离机制，不同应用共享操作系统

### 云原生安全与零信任

零信任针对用户身份验证，借助加密实现用户级安全管理。云原生安全强调微服务级细分的边界安全，身份基于服务而非IP地址。

### BeyondProd六大安全组件

1. **边缘网络保护** → Google Front End (GFE)
2. **服务间无固有信任** → Application Layer Transport Security (ALTS)
3. **已知出处代码执行** → Binary Authorization for Borg (BAB)、Host Integrity (HINT)
4. **跨服务策略执行** → Service Access Policy、End User Context tickets (EUC)
5. **简单自动化标准化发布** → Borg tooling
6. **共享OS上的工作负载隔离** → gVisor

核心产品：
- **GFE**：TLS终止，边缘代理
- **ALTS**：RPC认证、完整性、加密
- **BAB**：代码审计，二进制验证
- **HINT**：安全启动，BIOS/BMC/bootloader/内核数字签名验证
- **EUC**：完整性保护的集中签发可转发凭证
- **gVisor**：用户空间内核拦截系统调用，减少与主机交互

</div>
