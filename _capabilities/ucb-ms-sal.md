---
title: "Multi-step salience with neural modular networks"
excerpt: "Multi-step salience via sub-task decomposition for reasoning tasks"
tags: # Select from this set
  - Analytics
  - Computer Vision
  - Natural Language Processing
  - Visual Question Answering (VQA)
  - Saliency
   
submission_details:
  resources: # List any resources associated with the contribution. Not all sections are required
    papers:
      - title: Explainable Neural Computation via Stack Neural Module Networks
        url: https://arxiv.org/pdf/1807.08556.pdf
    software:
      - title: Official Tensorflow repo
        url: https://github.com/ronghanghu/snmn
   
  # Optional information describing artifact. Leave blank if unused
  version: 
  size: 
  license: https://github.com/ronghanghu/snmn/blob/master/LICENSE.txt
   
  authors:
    - Ronghang Hu, 1
    # Optional for multiple authors and organizations
    - Jacob Andreas, 1
    - Trevor Darrell, 1
    - Kate Saenko, 2
  organizations:
    # Optional for multiple authors and organizations
    - 1. University of California, Berkeley
    - 2. Boston University
  point_of_contact:
    name: Anna Rohrbach
    email: anna.rohrbach@berkeley.edu
---
   
## Overview
Existing models designed to produce interpretable traces of their decision-making process typically require these traces to be supervised at training time. We present a novel neural modular approach that performs compositional reasoning by automatically inducing a desired sub-task decomposition without relying on strong supervision. That is, our approach decomposes a task into multiple steps, and provides visual explanations for the various sub-tasks. Our model allows linking different reasoning tasks though shared modules that handle common routines across tasks.
   
## Intended Use
This software will be of interest to AI researchers interested in explainability for complex reasoning and those interested in modular (inherently explainable) architectures.

The proposed method does not require strong expert supervision of the reasoning steps. It has been shown applicable to two different problems (VQA and referring expression comprehension) and could be extended to other related tasks that require multi-step reasoning.
   
## Model/Data
Depending on a task, the input to the model is an image and a question/query, while the output is an interpretable multi-step salience and an answer/bounding box.

The model is trained on two tasks: a visual question answering dataset and a referring expression comprehension dataset.

## Limitations
The accuracy of the model is slightly below that of a non-modular (not explainable) state-of-the-art model.
   
## References
```tex
@inproceedings{hu2018explainable,
  title={Explainable Neural Computation via Stack Neural Module Networks},
  author={Hu, Ronghang and Andreas, Jacob and Darrell, Trevor and Saenko, Kate},
  booktitle={Proceedings of the European Conference on Computer Vision (ECCV)},
  year={2018}
}
```
