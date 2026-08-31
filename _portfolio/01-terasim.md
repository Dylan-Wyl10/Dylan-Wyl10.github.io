---
title: "TeraSim: A City-Scale Agentic World Model Platform for Physical AI"
excerpt: "Core developer at Inchor (SaferDrive AI). A city-scale simulation platform serving as foundational infrastructure for agentic world models under the Physical AI framework."
collection: portfolio
---

**Role**: Core Developer | Inchor (SaferDrive AI)
**Period**: Dec 2025 – Present

## Overview
TeraSim is a city-scale simulation platform serving as the foundational infrastructure for agentic world models under the Physical AI framework, enabling naturalistic and adversarial testing of autonomous vehicles at urban scale.

## Core Module — CNDE (Conditional Neural-network Driving Environment)
- CNDE serves as the behavioral-layer foundation model within the TeraSim ecosystem, integrating MotionTransformer for neural network-based driving behavior generation.
- Refactored the CNDE architecture from a dual-state management system to a stateless prediction pipeline, where TeraSim manages all vehicle states and CNDE operates as a pure prediction function.
- Implemented vehicle state synchronization, history tensor construction, and coordinate transformation for large-scale MotionTransformer inference.

## Milestones — NVIDIA & City of San Jose Joint Project
- Led a joint project with NVIDIA and the City of San Jose on agent-driven Smart City operation, building an integrated "City Operations Agent" and digital twin that can perceive, simulate, and optimize traffic operations.
- Designed and implemented the full simulation pipeline including city-scale vehicle injection, dynamic routing, and multi-phase demo orchestration.
- **Mar 2026**: Active deployment with NVIDIA and the City of San Jose as an Agentic Incident-to-Operation pipeline, bringing TeraSim from simulation into real-world city operations.
- **Jun 2026**: First draft release of Agent-Sim, utilizing LLMs and VLMs for safety-critical scenario generation.

**Tech Stack**: Python, SUMO, PyTorch, CUDA, Docker, FastAPI
