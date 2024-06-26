---
title: Detecting Mis-Information with XAI
excerpt: Our research investigates the effects of XAI assistants embedded in news review platforms for combating the propagation of mis-info.
tags: 
  - Analytics
  - Natural Language Processing
  - Human-Machine Teaming
   
submission_details:
  resources: 
    papers:
      - title: Machine Learning Explanations to Prevent Overtrust in Fake News Detection
        url: https://ojs.aaai.org/index.php/ICWSM/article/view/18072
    software:
      - title: XAI_FakeNews
        url: https://gitlab.com/nacoyang/xai_fakenews_phase2
    demos:
      - title: XAI_FakeNews_demo
        url: https://youtu.be/Ei8WSL4vr4A
    data:
      - title: XAI_FakeNews_dataset
        url: https://drive.google.com/drive/folders/1yvinR7VnzVj8T8dcLQIacv6EvgChxhWT?usp=sharing 
   
  version: 1.0
  size: 
  license: 
   
  authors:
    - Sina Mohseni<sup>1</sup>
    - Fan Yang<sup>1</sup>
    - Shiva Pentyala<sup>1</sup>
    - Mengnan Du<sup>1</sup>
    - Yi Liu<sup>1</sup> 
    - Nic Lupfer<sup>1</sup> 
    - Xia Hu<sup>1</sup>
    - Shuiwang Ji<sup>1</sup> 
    - Eric Ragan<sup>2</sup>
  organizations:
    - 1. Texas A&M University, College Station, TX
    - 2. University of Florida, Gainesville, FL 
  point_of_contact:
    name: Xia (Ben) Hu
    email: hu@cse.tamu.edu
---
   
## Overview
Combating fake news and misinformation propagation is a challenging task in the post-truth era. 
News feed and search algorithms could potentially lead to unintentional large-scale propagation of false and fabricated information with users being exposed to algorithmically selected false content.
We design a news reviewing and sharing interface, create a dataset of news stories, and train four interpretable fake news detection algorithms to study the effects of algorithmic transparency on end-users.
   
## Intended Use
This contribution is intended to deeply understand some deployed NLP models for misinformation detection tasks.
Besides, with the aid of this contribution, it is possible to further study the interactions between user engagement, mental model, trust, and performance measures in the process of explaining.

This contribution can generally be applied to the natural language processing domains, especially for the classification settings. 
   
## Model/Data
Model inputs: textual statement/claim for news stories;

Model outputs: confidence score for mis-information prediction + various interpretation outcomes (with XAI assistants);

Data for training: labelled news claims from snopes + unlabelled related news articles from Google search
   
## Limitations
The quality of the collected news claims is limited, considering the fact that some news labels are time-sensitive.
To have a more reliable XAI system, we need trustworthy labelled datasets for training. 
   
No significant failures observed.
   
## References
Mohseni, S., Yang, F., Pentyala, S., Du, M., Liu, Y., Lupfer, N., Hu, X., Ji, S., & Ragan, E. (2021). 
Machine Learning Explanations to Prevent Overtrust in Fake News Detection. 
Proceedings of the International AAAI Conference on Web and Social Media, 15(1), 421-431.
