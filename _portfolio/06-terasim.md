---
title: "TeraSim: City-Scale World Model for Safety Testing on AV and Physical AI"
excerpt: "Core developer of TeraSim, an open-source city-scale traffic simulation platform for AV safety testing: MotionTransformer-based naturalistic driving behavior (NNDE), and a city-scale NVIDIA Metropolis Blueprint demo with NVIDIA and the City of San Jose that was selected for the GTC 2026 keynote."
collection: portfolio
project_period: "Dec 2025 – Mar 2026"
redirect_from:
  - /portfolio/01-terasim/
---

- **Role**: core developer of TeraSim; Simulation Development Engineer Intern
- **Period**: Dec 2025 – Mar 2026, during the Simulation Development Engineer internship (Dec 2025 – Jun 2026)
- **Affiliation**: Inchor (SaferDrive AI), Ann Arbor, MI; joint project with NVIDIA and the City of San Jose
- **Status**: completed (Mar 2026)
- **Links**: [NVIDIA press release, Mar 16, 2026](https://nvidianews.nvidia.com/news/nvidia-t-mobile-and-partners-integrate-physical-ai-applications-on-ai-ran-ready-infrastructure) · [GTC 2026 news post]({{ site.baseurl }}{% post_url 2026-03-16-terasim-gtc-2026-keynote %})

## Overview
TeraSim is an open-source, city-scale traffic simulation platform for autonomous vehicle (AV) safety testing, enabling naturalistic and adversarial testing of AVs at urban scale. The internship work centered on two parts: NNDE, the naturalistic driving behavior layer of TeraSim, and a joint project with NVIDIA and the City of San Jose on agent-driven Smart City operation. It also included implementing a full-stack Driving Foundation Model into product.

## Part 1: Naturalistic Driving Behavior (NNDE)
NNDE (Neural-network Naturalistic Driving Environment) is the behavioral-layer foundation module of TeraSim; it integrates a transformer-based motion model to generate naturalistic driving behavior at city scale.

- Led the integration of MotionTransformer as the foundation model of NNDE, generating naturalistic driving behavior at city scale alongside the NADE adversarial-scenario module.
- Refactored the behavior-model pipeline from a dual-state design into a stateless prediction pipeline for large-scale inference.
- Implemented vehicle state synchronization, history tensor construction, and coordinate transformation for large-scale MotionTransformer inference.

## Part 2: City-Scale Demo with NVIDIA and the City of San Jose
- Led the joint project with NVIDIA and the City of San Jose on agent-driven Smart City operation.
- For that project, led a city-scale urban simulation demo under the NVIDIA Metropolis Blueprint: an integrated "City Operations Agent" and digital twin that perceive, simulate, and optimize traffic operations.
- Designed the full simulation pipeline, including city-scale vehicle injection, dynamic routing, and multi-phase demo orchestration.
- The demo was selected for NVIDIA CEO Jensen Huang's GTC 2026 keynote (Mar 16, 2026, San Jose, CA).

## Tools
Python, SUMO, PyTorch, CUDA, Docker, FastAPI
