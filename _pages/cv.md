---
layout: archive
title: "CV"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

My CV comes as two documents:

* **[Resume](/assets/Resume_YilinWang.pdf)**: a short industry resume.
* **[Full CV](/assets/CV_YilinWang.pdf)**: the complete academic CV.

Project details are on the [Projects](/portfolio/) pages.

Education
======
* Ph.D. in Civil Engineering (Transportation and Infrastructure Systems Engineering), Purdue University, Aug 2021 – May 2027 (expected)
  * Dissertation (tentative title): *A Cooperative Traffic Monitoring System with a Scenario Reconstruction*
  * Advisor: Dr. Yiheng Feng
  * Research Area: Connected and Automated Vehicle, Cooperative Perception, Physics-informed Machine Learning, Robotaxi Operation and Control
  * GPA: 3.8/4.00
* M.S. in Advanced Infrastructure Systems, Carnegie Mellon University, Aug 2019 – Dec 2020
  * Research advisor: Dr. Pingbo Tang
  * Area: Smart City, Deep Learning, Natural Language Processing
  * Courses: Deep Learning, Reinforcement Learning, Geo-Informatics System
  * GPA: 3.87/4.00
* B.S. in Civil Engineering, Tongji University, Aug 2015 – Jun 2019
  * Area: Geo-technical and Underground Engineering

Research and Professional Experience
======
* Fall 2021 – Present: **Graduate Research Assistant**, Connected Automated and Resilient Transportation (CART) Lab, Lyles School of Civil and Construction Engineering, Purdue University, West Lafayette, IN
  * Supervisor: Prof. Yiheng Feng
  * Research area: connected and automated vehicles, cooperative perception, V2X communication.
  * Robotaxi and CAV fleet routing for traffic monitoring, an individual dissertation project ([RoboSense](/portfolio/02-robosense/)).
  * Physics-informed and interpretable car-following models ([IDM-Follower and Neural Force](/portfolio/04-idm-follower/)).
  * Cooperative driving automation projects funded by USDOT, Michigan DOT, and Leidos: lead developer and researcher of the Smart Intersections project, mentor and developer for the Detroit QLine, CDASim development with Leidos, and a V2X-based connected automated vehicle ([MMITSS](/portfolio/05-v2x-tsc/)).
  * Project leader of a cooperative perception project: a CAV safety study funded by NSF, then an infrastructure-vehicle cooperative perception system funded by the Center for Connected and Automated Transportation (CCAT) ([project page](/portfolio/03-cooperative-perception/)).
  * Teaching assistant for CCE 361 and guest lecturer for CCE 565 ([Teaching](/teaching/)).
* Dec 2025 – Jun 2026: **Simulation Technical Leader Intern**, Inchor (SaferDrive AI), Ann Arbor, MI
  * Supervisor: Prof. Henry Liu
  * **TeraSim: Naturalistic Driving Behavior** (core developer, Dec 2025 – Mar 2026; [project page](/portfolio/06-terasim/))
    * Core developer of TeraSim, an open-source city-scale traffic simulation platform for AV safety testing, delivered to paying enterprise customers.
    * Led integration of MotionTransformer as the foundation model of NNDE, generating naturalistic driving behavior at city scale alongside the NADE adversarial-scenario module; refactored the behavior-model pipeline from a dual-state design into a stateless prediction pipeline for large-scale inference.
    * Implemented vehicle state synchronization, history tensor construction, and coordinate transformation for large-scale MotionTransformer inference.
    * Implemented a full-stack Driving Foundation Model into product; independently secured and led the joint project with NVIDIA and the City of San Jose on agent-driven Smart City operation.
    * For that project, led a city-scale urban simulation demo under the NVIDIA Metropolis Blueprint: an integrated "City Operations Agent" and digital twin that perceive, simulate, and optimize traffic operations; designed the full simulation pipeline, including city-scale vehicle injection, dynamic routing, and multi-phase demo orchestration.
    * The TeraSim demo with NVIDIA and the City of San Jose was selected for NVIDIA CEO Jensen Huang's GTC 2026 keynote.
  * **AgentSim: Agentic Synthetic Scenario Generation** (initiator and lead architect, Mar 2026 – Present; [demo](/portfolio/01-agentsim/))
    * An end-to-end pipeline from a trajectory or text description to safety-critical scenarios with ego camera-view data.
    * An agentic platform in which LLM/VLM agents collaborate to reconstruct, mutate, and render driving scenarios.
    * The agents take a real logged drive and mutate it into safety-critical variants (a lead car braking hard, a cut-in, a red-light runner, a pedestrian crossing). Each variant runs in closed loop, so other road users follow their recorded paths until the mutation reaches them and then react; a video world model renders each variant as front-camera video.
    * The closed-loop simulation base was built from scratch, embedded with neural behavior models and supporting multi-modal inputs, and the pipeline includes full scene reconstruction from trajectory-only data; the whole pipeline is benchmarked on the Waymo Open Dataset.
  * **Safety Instinct for Physical AI**: independent project, Feb 2026 – Apr 2026 ([project page](/portfolio/07-safety-instinct/)).
* Jan 2020 – Dec 2020: **Research Assistant**, Carnegie Mellon University, Pittsburgh, PA
  * Supervisor: Prof. Pingbo Tang
  * Research on nuclear power plant operations, including workflow extraction and automatic error correction, using natural language processing.

Publications
======
  <ul>{% for post in site.publications reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>

Talks
======
  <ul>{% for post in site.talks reversed %}
    {% include archive-single-talk-cv.html  %}
  {% endfor %}</ul>

Professional Service
======
* **Reviewer**
  * Transportation Research Part C: Emerging Technologies: 3 manuscripts (2024, 2026)
  * IEEE Transactions on Intelligent Transportation Systems: 2 manuscripts
  * IEEE Transactions on Intelligent Vehicles (2024, 2025)
  * Journal of Intelligent Transportation Systems: 5 manuscripts (2023–2025)
  * Multimedia Tools and Applications: 2 manuscripts (2023, 2024)
  * Tunnelling and Underground Space Technology: 1 manuscript (2026)
  * Virtual Reality: 1 manuscript (2026)
  * Transportation Research Board (TRB) Annual Meeting: 7 papers
  * IEEE Intelligent Transportation Systems Conference (ITSC) (2024)
* **Committee**: IEEE-IV24 Workshop on Socially Interactive Autonomous Mobility, Committee Member (2024)
* **Professional memberships**: Transportation Research Board (TRB); IEEE Intelligent Transportation Systems Society; INFORMS

Honors and Awards
======
* Honorable Mention, [Mathematical Contest in Modeling (MCM)](https://www.contest.comap.com/undergraduate/contests/mcm/contests/2018/problems/), 2018
* Silver Award, China College Students' "Internet+" Innovation and Entrepreneurship Competition (team leader), 2018

Skills
======
* **Programming Languages**: Python, C++, MATLAB, JavaScript
* **Data Science & Machine Learning**: PyTorch, CUDA, Hugging Face
* **Simulation & Optimization**: SUMO, CARLA, CARMA, NVIDIA Isaac Sim, Gurobi
* **Cloud Technologies**: AWS, SSH
* **DevOps & Version Control**: Linux, Docker, Conda
* **Cooperation Platform & Project Management**: Jira, Slack, GitHub
* **Other Tools & Technologies**: Microsoft Office, AutoCAD, ArcGIS
* **Research Skills**: Critical Thinking, Research Talk, Comprehensive Writing, Literature Review
