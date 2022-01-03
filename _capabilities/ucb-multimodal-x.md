---
title: "Datasets with multimodal explanations"
excerpt: "Datasets with multimodal explanations for activity recognition (ACT-X) and visual question answering (VQA-X)."
tags: # Select from this set
  - Analytics
  - Computer Vision
  - Natural Language Processing
  - Visual Question Answering (VQA)
   
submission_details:
  resources: # List any resources associated with the contribution. Not all sections are required
    papers:
      - title: "Multimodal Explanations: Justifying Decisions and Pointing to the Evidence"
        url: https://openaccess.thecvf.com/content_cvpr_2018/papers/Park_Multimodal_Explanations_Justifying_CVPR_2018_paper.pdf
    data:
      - title: Official repo
        url:  https://github.com/Seth-Park/MultimodalExplanations
   
  # Optional information describing artifact. Leave blank if unused
  version: 
  size: 
  license: https://github.com/Seth-Park/MultimodalExplanations/blob/master/LICENSE
   
  authors:
    - Dong Huk Park<sup>1</sup>
    # Optional for multiple authors and organizations
    - Lisa Anne Hendricks<sup>1</sup>
    - Zeynep Akata<sup>2,3</sup>
    - Anna Rohrbac<sup>1,3</sup>
    - Bernt Schiele<sup>3</sup>
    - Trevor Darrell<sup>1</sup>
    - Marcus Rohrbach<sup>4</sup>
  organizations:
    # Optional for multiple authors and organizations
    - 1. University of California, Berkeley, USA
    - 2. AMLab, University of Amsterdam, Amsterdam, Netherlands
    - 3. MPI for Informatics, Saarland Informatics Campus, Saarbrucken, Germany
    - 4. Facebook AI Research, USA
  point_of_contact:
    name: Anna Rohrbach
    email: anna.rohrbach@berkeley.edu
---

     
## Overview
This is the first dataset that provides multimodal human ground-truth explanations (both textual and visual) for two down-stream tasks, namely visual question answering (VQA-X) and activity recognition (ACT-X).

## Intended Use
This dataset will be of interest to AI researchers interested in explainability in multimodal contexts, serving as a benchmark for evaluating the correctness of the generated explanations.
   
## Model/Data
Our datasets define visual and textual justifications of a classification decision for activity recognition tasks (ACT-X) and for visual question answering tasks (VQA-X).
   
## References
```tex
@inproceedings{park2018multimodal,
  title={Multimodal explanations: Justifying decisions and pointing to the evidence},
  author={Park, Dong Huk and Hendricks, Lisa Anne and Akata, Zeynep and Rohrbach, Anna and Schiele, Bernt and Darrell, Trevor and Rohrbach, Marcus},
  booktitle={Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition},
  pages={8779--8788},
  year={2018}
}
```
