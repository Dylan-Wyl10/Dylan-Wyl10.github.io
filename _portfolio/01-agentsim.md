---
title: "AgentSim: An Agentic Test Engineer for Autonomous-Driving Safety Validation"
excerpt: "Initiated and developed at Inchor (SaferDrive AI). LLM/VLM agents mutate real logged drives into safety-critical corner cases, replay them in closed loop, and a video world model renders the result."
collection: portfolio
project_period: "Mar 2026 – Present"
demo_url: /agentsim-demo/
demo_label: "Demo"
redirect_from:
  - /portfolio/01-terasim/
---

## Overview
AgentSim is an agentic world model for autonomous-driving safety validation. Instead of hand-written test scenarios, a multi-agent framework powered by LLMs and VLMs takes a real logged drive and mutates it into safety-critical corner cases, for example a lead car that brakes hard, a car that cuts in, a red-light runner, or a pedestrian crossing. Each mutation runs in closed loop: every other road user follows its recorded path until the mutation reaches it and then reacts, so the variants stay grounded in the original traffic. A video world model then renders each variant as a front-camera clip from the same first frame as the logged drive, so the clips differ only where the mutation changes the traffic.

## Demo: one real drive, five variants
{% include agentsim-demo-assets.html %}
{% assign first_case = site.data.agentsim_demo.groups | first %}
{% include agentsim-grid.html group=first_case %}

Two more drives, with the same treatment, are on the [full demo page](/agentsim-demo/).

## Milestones
- **Jun 2026**: First draft release of AgentSim, utilizing LLMs and VLMs for safety-critical scenario generation.

## Platform context: TeraSim
AgentSim is built within TeraSim, the city-scale simulation platform of Inchor (SaferDrive AI) that serves as the foundational infrastructure for agentic world models under the Physical AI framework. As a core developer of TeraSim, Yilin also:

- refactored CNDE, its behavioral-layer foundation model built on MotionTransformer, from a dual-state design into a stateless prediction pipeline, implementing vehicle state synchronization, history tensor construction, and coordinate transformation for large-scale inference;
- led the joint project with NVIDIA and the City of San Jose on agent-driven Smart City operation, designing the simulation pipeline (city-scale vehicle injection, dynamic routing, multi-phase demo orchestration) behind the Agentic Incident-to-Operation pipeline that went into active deployment in Mar 2026.

**Tech Stack**: Python, SUMO, PyTorch, CUDA, Docker, FastAPI

<p class="agentsim-note agentsim-attribution">Waymo Open Dataset: An autonomous driving dataset. <a href="https://www.waymo.com/open">https://www.waymo.com/open</a>, 2019–2025.</p>
