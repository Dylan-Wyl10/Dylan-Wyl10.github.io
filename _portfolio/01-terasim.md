---
title: "TeraSim: A City-Scale Agentic World Model Platform for Physical AI"
excerpt: "Core developer at SaferDrive.AI. A city-scale simulation platform serving as foundational infrastructure for agentic world models under the Physical AI framework."
collection: portfolio
---

**Role**: Core Developer | SaferDrive.AI
**Period**: Dec 2024 – Present

## Overview
TeraSim is a city-scale simulation platform serving as the foundational infrastructure for agentic world models under the Physical AI framework, enabling naturalistic and adversarial testing of autonomous vehicles at urban scale.

## Core Module — CNDE (Conditional Neural-network Driving Environment)
- CNDE serves as the behavioral-layer foundation model within the TeraSim ecosystem, integrating MotionTransformer for neural network-based driving behavior generation.
- Refactored the CNDE architecture from a dual-state management system to a stateless prediction pipeline, where TeraSim manages all vehicle states and CNDE operates as a pure prediction function.
- Implemented vehicle state synchronization, history tensor construction, and coordinate transformation for large-scale MotionTransformer inference.

## Milestone — NVIDIA GTC 2025 San Jose Demo
- Led the development of a city-scale urban simulation demo under the NVIDIA Metropolis Blueprint, building an integrated "City Operations Agent" and digital twin that can perceive, simulate, and optimize traffic operations for Smart City applications.
- Designed and implemented the full simulation pipeline including city-scale vehicle injection, dynamic routing, and multi-phase demo orchestration.
- Selected for NVIDIA CEO Jensen Huang's GTC 2025 keynote presentation, with follow-up proof-of-concept and city-level implementation phases in progress.

**Tech Stack**: Python, SUMO, PyTorch, CUDA, Docker, FastAPI
