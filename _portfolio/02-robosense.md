---
title: "RoboSense: Leveraging Robotaxi Fleets as Drive-by Sensors for Urban Traffic Monitoring"
excerpt: "A dynamic robotaxi routing framework that turns centrally controlled fleets into cooperative drive-by sensors for urban traffic monitoring. [GitHub](https://github.com/Dylan-Wyl10/RoboSense)"
collection: portfolio
redirect_from:
  - /portfolio/03-dynamic-routing/
  - /portfolio/03-robosense/
---

**Authors**: Yilin Wang, Yiheng Feng (Purdue University)
**Role**: Individual Research Project
**Period**: Apr 2023 – Present
**Status**: Preprint, under review
**Code**: [GitHub — Dylan-Wyl10/RoboSense](https://github.com/Dylan-Wyl10/RoboSense) · **Paper**: [Preprint PDF](https://github.com/Dylan-Wyl10/RoboSense/blob/main/paper/RoboSense-preprint.pdf)

## Overview
Robotaxis are dispatched to carry passengers, but a centrally controlled fleet can also double as a network of drive-by sensors. RoboSense is a dynamic routing framework that makes traffic monitoring an explicit objective of fleet operation. It combines:

- a **cell-based network representation** aligned with vehicle sensing range, built on Cell Transmission Model (CTM) traffic-state prediction;
- a **cell-level spatiotemporal coverage metric** quantifying how well the fleet observes the network;
- a **rolling-horizon MILP** that trades off passenger travel time against network monitoring coverage.

The framework is evaluated in SUMO on a 5×5 urban grid network at 2%, 5%, and 10% robotaxi market penetration rates. A key finding: with appropriate objective weights, monitoring performance and robotaxi average speed improve *simultaneously* — better sensing also makes the fleet faster, a win-win that could incentivize operators to contribute vehicles as drive-by sensors.

![RoboSense framework overview](/images/robosense-framework.png)

## Earlier Work: Dynamic Routing of CAVs for Improving Network Coverage
- Formulated the CAV routing problem considering network coverage as one objective.
- Proposed heuristic algorithms with greedy search to solve the multi-objective optimization.
- Conducted simulation experiments in a grid network to verify feasibility and relations between travel cost and network coverage.
- **Outcome**: Accepted by [TRB Annual Meeting 2024](https://www.nationalacademies.org/event/806_01-2024_trb-annual-meeting) as poster presentation.
