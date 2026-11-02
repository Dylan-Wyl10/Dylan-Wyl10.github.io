---
title: "Modeling Car-Following Behavior with Physics-Informed Neural Networks"
excerpt: "Behavior-level reconstruction of human driving, from physics-constrained prediction to cognitively interpretable response: IDM-Follower (IEEE Transactions on Intelligent Vehicles, first author) and Neural Force (manuscript in preparation)."
collection: portfolio
project_period: "Jan 2022 – Present"
paper_url: "https://ieeexplore.ieee.org/abstract/document/10440530"
paper_label: "IEEE T-IV paper"
github_url: "https://github.com/Dylan-Wyl10/IDMFollower"
---

- **Role**: first author of IDM-Follower; co-author of Neural Force
- **Period**: Jan 2022 – Present (IDM-Follower Jan 2022 – Feb 2024; Neural Force 2024 – Present)
- **Affiliation**: CART Lab, Purdue University
- **Funding**: the IDM-Follower study was supported by the USDOT FHWA grant 693JJ32150006 (Smart Intersections)
- **Status**: IDM-Follower published in *IEEE Transactions on Intelligent Vehicles* (2024); Neural Force manuscript in preparation
- **Links**: [IDM-Follower paper](https://ieeexplore.ieee.org/abstract/document/10440530) · [IDM-Follower code on GitHub](https://github.com/Dylan-Wyl10/IDMFollower)

## Overview
This line of work reconstructs human driving behavior by embedding physical and cognitive structure into neural networks, so that learned behavior models stay accurate, robust, and interpretable. Such models form the behavior layer behind sim agents and world models.

## Project 1: IDM-Follower: A Model-Informed Deep Learning Method for Car-Following Trajectory Prediction
*Jan 2022 – Feb 2024*

- **Research question**: how to integrate an explicit, physics-based car-following model into a learning-based predictor to improve training and performance.
- **Contributions**:
  1. A physics-informed neural network (PINN) model that integrates the Intelligent Driver Model (IDM) into a neural trajectory predictor.
  2. The model is robust against real-time GPS noise.
- **Methodology**: a customized attention-based variational autoencoder (VAE), trained with a loss that combines physical-law residuals and the error against ground truth.
- **Outcomes**:
  - **Publication** (first author): Yilin Wang, Yiheng Feng (2024). "[IDM-Follower: A Model-Informed Deep Learning Method for Car-Following Trajectory Prediction](https://ieeexplore.ieee.org/abstract/document/10440530)." *IEEE Transactions on Intelligent Vehicles*, vol. 9, no. 6, pp. 5014-5020, June 2024.
  - **Presentation**: research presentation at the IEEE Intelligent Vehicles Symposium (IV) 2024, Jeju Island, Korea ([talk page]({{ '/talks/2024-ieee-iv-idm' | relative_url }})).
  - **Code**: [GitHub: Dylan-Wyl10/IDMFollower](https://github.com/Dylan-Wyl10/IDMFollower)

## Project 2: Neural Force: Interpretable Learned Car-Following Response Fields
*2024 – Present*

- **Research question**: how does a driver combine perceptual cues (spacing, closing speed, and own speed) into one acceleration decision, and can a learned model keep that combination readable instead of hiding it in a black box?
- **Contributions**:
  1. A cognitively motivated response-field model: acceleration is assembled from signed, weighted gradients of one shared learned scalar, and each term carries a behavioral role (restore spacing, oppose closing, damp speed).
  2. Interpretable readouts (operating gap, gap-restoration gain, and closing-opposition gain) that make learned human behavior comparable across datasets.
  3. Across four naturalistic driving corpora (AD4CHE, highD, LA Highways, and I-24 MOTION), a shared corrective structure with distinct sensitivities: five of six corpus pairs reverse order between the two gains, which rules out a single "response strength" axis.
- **Methodology**: a neural scalar potential with state-dependent convex weights; a Student-t residual for uncertainty; an annealed IDM prior during training.
- **Outcome**: manuscript in preparation (co-author).
