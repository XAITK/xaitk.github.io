---
title: "Natural Language Explanations for Fine-grained Image Classification"
excerpt: "A method to produce visual explanations using natural language justifications."
tags: # Select from this set
  - Analytics
  - Computer Vision
  - Natural Language Processing
  - Explanation Framework
   
submission_details:
  resources: # List any resources associated with the contribution. Not all sections are required
    papers:
      - title: Generating Visual Explanations
        url: https://arxiv.org/pdf/1603.08507.pdf
    software:
      - title: Official Caffe version
        url: https://github.com/LisaAnne/ECCV2016
      - title: Unofficial Pytorch version
        url: https://github.com/salaniz/pytorch-gve-lrcn
   
  # Optional information describing artifact. Leave blank if unused
  version: 
  size: 
  license: https://github.com/LisaAnne/ECCV2016/blob/master/LICENSE
   
  authors:
    - Lisa Anne Hendricks<sup>1</sup>
    # Optional for multiple authors and organizations
    - Zeynep Akata<sup>2</sup>
    - Marcus Rohrbach<sup>1,3</sup>
    - Jeff Donahue<sup>1</sup>
    - Bernt Schiele<sup>2</sup>
    - Trevor Darrell<sup>1</sup>
  organizations:
    - 1. UC Berkeley, Berkeley, CA, United States
    # Optional for multiple authors and organizations
    - 2. Max Planck Institute for Informatics, Saarbruecken, Germany
    - 3. ICSI, Berkeley, CA, United States
  point_of_contact:
    name: Anna Rohrbach
    email: anna.rohrbach@berkeley.edu
---
   
## Overview
We propose the first method to produce deep visual explanations using natural language justifications. Our vision and language explanation model combines classification and sentence generation and incorporates a loss function operating over sampled sentences. Our results on a fine-grained bird species classification dataset show that our model is able to generate explanations which are not only consistent with an image but also more discriminative than descriptions produced by existing captioning methods.
Importantly, there is no need of having ground-truth textual explanations available at training time.

## Intended Use
This software will be of interest to researchers and developers working on fine-grained recognition, in particular in scenarios where no expert annotations are available or are easy to obtain.

The proposed model could be applied to any fine-grained classification dataset that has some natural language descriptions associated with the images (they do not need to be expert explanations).
   
## Model/Data
The input is an image and a predicted class label. The output is a natural language visual explanation (both visually accurate and class-discriminative).

The model is trained on a parallel corpus of images with assicialted textual descriptions (they do not need to be explanations).

## Limitations
The model requires a parallel corpus of images with associated textual descriptions.
   
## References
```tex
@inproceedings{hendricks2016generating, 
title={Generating Visual Explanations}, 
author={Hendricks, Lisa Anne and Akata, Zeynep and Rohrbach, Marcus and Donahue, Jeff and Schiele, Bernt and Darrell, Trevor}, 
conference={Proceedings of the European Conference on Computer Vision (ECCV)}, 
year={2016}}
```
