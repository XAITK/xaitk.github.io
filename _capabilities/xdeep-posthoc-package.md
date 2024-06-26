---
title: XDeep - A Post-Hoc Interpretation Package for Model Developers
excerpt: XDeep is an open-source Python package developed to interpret deep models for both practitioners and researchers.
tags:
  - Computer Vision
  - Natural Language Processing
  - Saliency
   
submission_details:
  resources:
    papers:
      - title: XDeep - An Interpretation Tool for Deep Neural Networks
        url: https://arxiv.org/pdf/1911.01005.pdf
    software:
      - title: XDeep
        url: https://github.com/datamllab/xdeep
   
  version: 0.0.9
  size:
  license: https://github.com/datamllab/xdeep/blob/master/LICENSE.md
   
  authors: 
    - Fan Yang<sup>1</sup>
    - Zijian Zhang<sup>*</sup>
    - Haofan Wang<sup>*</sup>
    - Yuening Li<sup>1</sup>
    - Xia (Ben) Hu<sup>1</sup>
  organizations:
    - 1. Texas A&M University, College Station, TX
    - <span>&#42;</span> Contributed during visit at TAMU
  point_of_contact:
    name: Xia (Ben) Hu
    email: hu@cse.tamu.edu
---
   
## Overview
XDeep is developed to help users easily interpret their trained DNNs at hands, which integrates a wide range of post-hoc interpretation algorithms with the well-documented APIs.
   
## Intended Use
XDeep is capable of providing both local and global interpretation for DNN, and it sets up a clear structure for all included algorithms inside the package.

As for the local interpretation scenario, XDeep covers two primary types of methodology from the state-of-the-art (i.e., the gradient-based and perturbation-based method). 
As for the global interpretation scenario, XDeep provides APIs for developers to directly interpret the DNN components, including filter, layer and logit, and further visualize the global features learned by DNN.
   
## Limitations
Currently, XDeep only supports a limited number of post-hoc interpretation methods, and can simply be applied to classification settings. Further updates and extensions are needed.
   
## References
Yang, Fan, Zijian Zhang, Haofan Wang, Yuening Li, and Xia Hu. 
"XDeep: An Interpretation Tool for Deep Neural Networks." 
arXiv preprint arXiv:1911.01005 (2019).
