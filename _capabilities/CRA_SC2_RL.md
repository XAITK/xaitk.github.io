---
title: "Counterfactual Explanations for Enhancing Human-Machine Teaming"
excerpt: "This contribution provides a framework for generating counterfactual explanations for AI agents in the domain of StarCraft 2."
tags: # Select from this set
  - Analytics
  - Autonomy
  - Reinforcement Learning
  - Human-Machine Teaming
  - Data Poisoning
  - Explanation Framework
   
submission_details:
  resources: # List any resources associated with the contribution. Not all sections are required
    papers:
      - title: "Brittle AI, Causal Confusion, and Bad Mental Models: Challenges and Successes in the XAI Program"
        url: https://arxiv.org/abs/2106.05506
    software:
      - title: CAMEL Software
        url: https://data.kitware.com/api/v1/item/620283684acac99f427d40a9/download
    demos:
      - title: Demo Video
        url: https://cra.com/xai/
   
  # Optional information describing artifact. Leave blank if unused
  version:
  size:
  license: https://opensource.org/licenses/BSD-3-Clause
   
  authors:
    - Jeff Druce
    - James Niehaus
    - Joseph Campolongo
  organizations:
    - Charles River Analytics
  point_of_contact:
    name: Jeff Druce
    email: jdruce@cra.com 
---
   
## Overview
The purpose of this contribution is to provide a framework for explaining AI agents in a Human-Machine Teaming (HMT) scenario in the domain of StarCraft 2. The contribution includes a custom StarCraft 2 map that allows a human to either take control over a squad of marines, or allow an AI to take control in defending a central base. Explanations in the form of narrative statements for the AI's actions are produced by using a Causal Model to Explain Learning (CAMEL). The statements are received via a Explanation User Interface (XUI) in the form of an After Action Review (AAR) following an episode.

## Intended Use
The intended use of this contribution is to provide users of an AI a better sense of the driving factors behind an AI's actions, and a better sense of what scenarios an AI is sufficiently performant and can be reasonably trusted.

This contribution can be applied to our custom map in StarCraft 2.

## Model/Data
The model which provides explanations is a graphical causal model. In effect, it is a joint probability model over derived variables and the output of the AI; derived variables are high-level, human understandable variables that can be derived from low level variables (e.g. we provide a variable called "number of enemies in the top half of the screen which can be computed from a feature map showing the locations of the enemies"). At inference time, our model takes in the full set of derived variables, and finds out what values of the derived variables could be perturbed to change the action of the AI; this produces a counterfactual statement for the AI (e.g. "The AI would have moved to location A3, if the number of enemies in the top half was greater than 2.")

The model was trained on a corpus of data providing the derived variables and actions for the AI over a collection of several hundred episodes of the AI. This data allowed us to produce a model that was over 99% accurate on a held-out testing set.
