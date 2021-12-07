---
title: "Explainable AI self-driving controller"
excerpt: "An introspective textual explanation model for self-driving cars and Berkeley Deep Drive-X Dataset"
tags: # Select from this set
  - Autonomy
  - Computer Vision
  - Natural Language Processing
  - Saliency
  - Explanation Framework
   
submission_details:
  resources: # List any resources associated with the contribution. Not all sections are required
    papers:
      - title: Textual Explanations for Self-Driving Vehicles
        url: https://www.ecva.net/papers/eccv_2018/papers_ECCV/papers/Jinkyu_Kim_Textual_Explanations_for_ECCV_2018_paper.pdf
    software:
      - title: Original repo
        url: https://github.com/JinkyuKimUCB/explainable-deep-driving
    data:
      - title: Berkeley Deep Drive-X Dataset
        url: https://github.com/JinkyuKimUCB/BDD-X-dataset
   
  # Optional information describing artifact. Leave blank if unused
  version: 
  size: 
  license: https://github.com/JinkyuKimUCB/explainable-deep-driving/blob/master/LICENSE
   
  authors:
    - Jinkyu Kim, 1
    # Optional for multiple authors and organizations
    - Anna Rohrbach, 1,2
    - Trevor Darrell, 1
    - John Canny, 1
    - Zeynep Akata, 2,3
  organizations:
    - Organization
    # Optional for multiple authors and organizations
    - 1. University of California, Berkeley, USA
    - 2. MPI for Informatics, Saarland Informatics Campus, Saarbrucken, Germany
    - 2. AMLab, University of Amsterdam, Amsterdam, Netherlands
  point_of_contact:
    name: Anna Rohrbach
    email: anna.rohrbach@berkeley.edu
---
   
## Overview
This is the first effort to introduce explainability into a self-driving controller, by enabling it to generate textual explanations of its behavior. Specifically, we propose an introspective textual explanation model for self-driving cars to provide easy-to-interpret explanations for the behavior of a deep vehicle control network. We integrate our explanation generator with the vehicle controller by aligning their attention to ground the explanation. Ours is the first attempt to justify the decisions of a real-time deep controller through a combination of attention and natural language explanations on a stream of images.

We also provide a large-scale Berkeley DeepDrive eXplanation (BDD-X) dataset with over 6,984 video clips annotated by humans with driving descriptions, e.g., “The car slows down” and explanations, e.g., “because it is about to merge with the busy highway”. Our dataset provides a new test-bed for measuring progress towards developing explainable models for self-driving cars.
   
## Intended Use
This software will be of interest to researchers and developers in the area of autonomous driving who are concerned with the issue of explainability. The proposed models require human ground-truth textual action description-explanation pairs, otherwise they could be applied to other scenarios and datasets.
   
## Model/Data
An input to the model is a driving video, an output is ego-motion (acceleration, change of course) and a textual description-explanation pair.

The BDD-X dataset will be of interest to researchers and developers in the area of autonomous driving who are concerned with the issue of explainability. In particular, the collected human ground truth explanations can help inform and improve future self-driving systems and serve as a benchmark for evaluating the correctness of the generated explanations.
   
## Limitations

The proposed models require human ground-truth textual action description-explanation pairs.
   
## References
```tex
@inproceedings{kim2018textual,
  title={Textual explanations for self-driving vehicles},
  author={Kim, Jinkyu and Rohrbach, Anna and Darrell, Trevor and Canny, John and Akata, Zeynep},
  booktitle={Proceedings of the European conference on computer vision (ECCV)},
  pages={563--578},
  year={2018}
}
```
