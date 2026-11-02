---
title: 'AgentSim Public Demo Is Live'
date: 2026-10-17
excerpt: "The AgentSim demo is public: three real logged drives, each with five generated safety-critical variants rendered as synchronized front-camera video."
tags:
  - AgentSim
  - Autonomous Driving
  - Safety Validation
  - Demo
---

The public demo of [AgentSim]({{ '/portfolio/01-agentsim/' | relative_url }}), an agentic test engineer for autonomous-driving safety validation that I initiated at Inchor (SaferDrive AI), is live. It shows three real logged drives from the Waymo Open Motion Dataset, each with five generated safety-critical variants rendered as synchronized front-camera video.

LLM/VLM agents mutate each logged drive into safety-critical variants such as a lead car braking hard, a cut-in, a red-light runner, or a pedestrian crossing. Each variant runs in closed loop, so other road users follow their recorded paths until the mutation reaches them and then react; a video world model then renders the variant as front-camera video.
