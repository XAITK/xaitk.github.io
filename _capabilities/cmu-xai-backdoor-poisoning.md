---
title: "Explainable poisoned classifier identification"
excerpt: "Demo of our XAI system built to detect backdoor poisoned classifiers with an adversarial approach."
tags: # Select from this set
  - Analytics
  - Computer Vision
  - Human-Machine Teaming
  - Data Poisoning

submission_details:
  resources: # List any resources associated with the contribution. Not all sections are required
    papers:
      - title: Poisoned classifiers are not only backdoored, they are fundamentally broken
        url: https://arxiv.org/abs/2010.09080
    software:
      - title: Official repo
        url: https://github.com/locuslab/breaking-poisoned-classifier
      - title: Classifier forensics tool
        url: https://github.com/Eric-mingjie/xai-classifier-forensics-tool
    demos:
      - title: Explainable XAI Classifier Forensics Tool Demo
        url: https://youtu.be/4XZ6w_SvPDM
    data:
      - title: TrojAI dataset
        url: https://pages.nist.gov/trojai/docs/data.html
   
  # Optional information describing artifact. Leave blank if unused
  version: 
  size: 
  license: https://opensource.org/licenses/MIT
   
  authors:
    - Mingjie Sun<sup>1</sup>
    - Siddhant Agarwal<sup>2</sup>
    - Zico Kolter<sup>1</sup>
  organizations:
    - 1. Carnegie Mellon University
    - 2. IIT, Kharagur
  point_of_contact:
    name: Mingjie Sun
    email: sunmj15@gmail.com
---

## Overview
We propose an approach to analyze and identify backdoor poisoned classifiers with adversarial examples. Based on this approach, we develop a classifier forensics tool, where our tool helps users visualize adversarial examples and test the predictions under different custom patches. For more details on our approach and tool, see our [technical report](https://arxiv.org/abs/2010.09080) and [demo](https://github.com/Eric-mingjie/xai-classifier-forensics-tool).


## Intended Use
Our tool aims to help users easily analyze poisoned classifiers with a user-friendly interface. When users want to analyze a poisoned classifier or identify if a classifier is poisoned, they can use our classifier forensics tool. 


## Limitations
Our approach considers mostly patch based backdoor poisoning. 

## References
{% raw %}
```
@article{sun2020poisoned,
  title={Poisoned classifiers are not only backdoored, they are fundamentally broken},
  author={Sun, Mingjie and Agarwal, Siddhant and Kolter, J. Zico},
  journal = {CoRR},
  volume = {abs/2010.09080},
  url={https://arXiv/abs/2010.09080},
  year={2020}
}
```
{% endraw %}
