---
layout: about
title: about
permalink: /
description: >
    <a href="https://lti.cmu.edu/people/students/xie-yiqing.html">Language Technologies Institute, CMU</a>. <a href="mailto:yiqingxi@andrew.cmu.edu?subject=Hi">yiqingxi@andrew.cmu.edu</a>
profile:
  align: right
  image: website_photo.jpg
  address: >
    <p>Rm 6413, Gates and Hillman Centers</p>
    <p>4902 Forbes Ave</p>
    <p>Pittsburgh, PA 15213, USA</p>

news: true  # includes a list of news items
sections: true
selected_papers: true # includes a list of papers marked as "selected={true}"
social: true  # includes social icons at the bottom of the page
---

I am a fourth-year Ph.D. student at the Language Technologies Institute of Carnegie Mellon University and I am working with [Carolyn Rosé](https://cp3a.github.io/) and [Daniel Fried](https://dpfried.github.io){:target="\_blank"}. Previously, I obtained my Master degree in the data mining group at the University of Illinois Urbana-Champaign supervised by [Jiawei Han](http://hanj.cs.illinois.edu){:target="\_blank"} and obtained my Bachelor degree in Hong Kong University of Science and Technology, where I received the Academic Achievement Medal.

My research mainly focuses on synthetic training data construction and automatic evaluation, especially for coding agent.
The topics include: 
(i) Constructing scalable synthetic training data;
(ii) Training models to generalize across diverse tasks; 
(iii) Improving model performance with auxiliary models and evaluation benchmarks. 

<br>

**Scalable Synthetic Training Data**
 * Pretraining & continuous pretraining ([Anchor-DR](https://arxiv.org/abs/2305.05834), [METRO-T0](https://arxiv.org/abs/2305.12567))
 * Training environment ([RepoST](https://repost-code-gen.github.io/), [Hybrid-Gym](https://github.com/yiqingxyq/Hybrid-Gym))
 * Model-generated Reward Signals ([FenCE](https://arxiv.org/abs/2410.18359))
 * Data augmentation ([Eider](https://arxiv.org/abs/2106.08657), [Anchor-DR](https://arxiv.org/abs/2305.05834), [CMTrans](https://arxiv.org/abs/2311.00317), [FenCE](https://arxiv.org/abs/2410.18359))
 * Guidance under heuristic metrics or prior knowledge ([RL-MMR](https://arxiv.org/abs/2010.00117), [AlaGCN](https://www.cs.emory.edu/~jyang71/files/alagnn.pdf), [KoMen](https://www.cs.emory.edu/~jyang71/files/komen.pdf))
 * Unsupervised or Semi-supervised methods ([Set-CoExpan](https://arxiv.org/abs/2001.10106), [CoRel](https://arxiv.org/abs/2010.06714))

**Training Models for Task Generalization**
 * Zero-shot retriever training ([Anchor-DR](https://arxiv.org/abs/2305.05834), [METRO-T0](https://arxiv.org/abs/2305.12567))
 * General-purpose coding agent post-training ([Hybrid-Gym](https://github.com/yiqingxyq/Hybrid-Gym))
 * Few-shot graph-based interaction recommendation ([KoMen](https://www.cs.emory.edu/~jyang71/files/komen.pdf))

**Auxiliary Model Training and Benchmark Construction**
  * Evaluation Benchmarks ([CodeBenchGen](https://arxiv.org/abs/2404.00566), [CodeRAG-Bench](https://arxiv.org/abs/2406.14497), [TheAgentCompany](https://arxiv.org/abs/2412.14161), [RepoST](https://repost-code-gen.github.io/))
  * Evaluation frameworks ([DocLens](https://arxiv.org/abs/2311.09581))
  * Auxiliary models in training and inference ([FenCE](https://arxiv.org/abs/2410.18359), [Strong-Weak-Colab](https://arxiv.org/abs/2505.20182))

**Code Generation and Coding Agent**
  * Code generation training ([CMTrans](https://arxiv.org/abs/2311.00317), [RepoST](https://repost-code-gen.github.io/))
  * Code generation inference ([SACL](https://arxiv.org/abs/2506.20081), [Strong-Weak-Colab](https://arxiv.org/abs/2505.20182))
  * Code generation evaluation ([CodeBenchGen](https://arxiv.org/abs/2404.00566), [CodeRAG-Bench](https://arxiv.org/abs/2406.14497), [TheAgentCompany](https://arxiv.org/abs/2412.14161), [RepoST](https://repost-code-gen.github.io/))