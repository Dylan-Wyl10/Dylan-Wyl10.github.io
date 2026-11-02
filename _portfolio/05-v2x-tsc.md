---
title: "Cooperative Driving Automation System for Urban Areas (MMITSS)"
excerpt: "MMITSS, an open-source connected-vehicle signal priority system: field deployments at Mcity and on Ann Arbor's Ellsworth Road corridor (USDOT FHWA), the Detroit QLine extension (WSP for Michigan DOT), CDASim co-simulation integration (Leidos for USDOT FHWA), and a signal-aware connected vehicle."
collection: portfolio
project_period: "Sept 2021 – Jun 2026"
github_url: "https://github.com/Dylan-Wyl10/mmitss-CART"
---

- **Roles**: Lead Developer and Researcher (Smart Intersections); Mentor and Developer (Intelligent Woodward Corridor, Detroit QLine); Developer (CDASim integration with Leidos); Core Team Member (signal V2X-based connected vehicle)
- **Period**: Sept 2021 – Jun 2026
- **Sponsors**: USDOT Federal Highway Administration (FHWA); Michigan DOT through WSP; Leidos for USDOT FHWA
- **Affiliation**: CART Lab, Purdue University
- **Status**: the funded projects ended by Jun 2026; transit signal priority has served Route 6 transit buses on the Ellsworth corridor in Ann Arbor since August 2025
- **Links**: [MMITSS on GitHub](https://github.com/Dylan-Wyl10/mmitss-CART) · [deployment configurations](https://github.com/Dylan-Wyl10/SIP-MMITSS) · Docker Hub: [roadside](https://hub.docker.com/r/cartlabpurdue/mmitss-mrp-x86), [vehicle-side](https://hub.docker.com/r/cartlabpurdue/mmitss-vsp-x86) · FHWA repositories: [cda-mmitss](https://github.com/usdot-fhwa-stol/cda-mmitss/tree/develop), [mmitss](https://github.com/usdot-fhwa-stol/mmitss), [cdasim-config](https://github.com/usdot-fhwa-stol/cdasim-config/tree/release/timtsp)

## Overview
A vehicle-infrastructure cooperative (V2X) system that connects traffic signals, roadside units, and vehicles, so that intersections can grant signal priority to transit vehicles and guide connected and automated vehicles. The work runs from software through hardware-in-the-loop testing to field deployment, co-simulation, and a test vehicle. Its core is MMITSS (Multi-Modal Intelligent Traffic Signal System), an open-source connected-vehicle signal priority system.

## Part 1: MMITSS Development and Field Deployment

### Smart Intersections: Paving the Way for a National CAV Deployment
*USDOT FHWA, grant 693JJ32150006 (grant period Oct 2021 – Jun 2026). Role: Lead Developer and Researcher, Oct 2023 – Jun 2026.*

1. Redeveloped MMITSS, with a roadside processor (priority request server and solver, NTCIP signal controller interface) and a vehicle-side processor that forms priority requests from SAE J2735 messages (BSM, MAP, SPaT, SRM, SSM). [GitHub](https://github.com/Dylan-Wyl10/mmitss-CART)
2. Built MMITSS deployment configurations for Mcity and for the Ellsworth Road corridor (Braeburn, Stoneschool, and Varsity intersections), integrating commercial roadside units, on-board units, and traffic signal controllers. [GitHub](https://github.com/Dylan-Wyl10/SIP-MMITSS)
3. Set up hardware-in-the-loop testing with the whole SAE J2735 message protocol.
4. Maintained and updated the roadside and vehicle-side applications, released as public Docker images ([roadside](https://hub.docker.com/r/cartlabpurdue/mmitss-mrp-x86), [vehicle-side](https://hub.docker.com/r/cartlabpurdue/mmitss-vsp-x86)) with over 700 pulls on Docker Hub as of October 2026.
5. Field testing, installation, and data processing for buses and real intersections; transit signal priority has served Route 6 transit buses on the Ellsworth corridor in Ann Arbor since August 2025.
6. Field tests with signal priority on and off; built trip-level datasets that align vehicle-side and roadside messages (BSM, SRM, SSM, SPaT) to evaluate priority performance.

### Development of Transit Signal Priority and EV Preemption for the Intelligent Woodward Corridor Project
*WSP, for Michigan DOT's ATCMTD project on M-1 (Woodward Avenue) in Detroit. Role: Mentor and Developer, Jan 2024 – Jun 2026.*

- Implemented MMITSS for the [QLine](https://www.qlinedetroit.com/) streetcar in Detroit, MI.
- Extended MMITSS to the NTCIP 1211 operation protocol. [GitHub](https://github.com/Dylan-Wyl10/mmitss-CART/tree/Dev-1211)

### Class Demo
MMITSS is the class demo of Purdue CCE 565: Traffic Operations and Control ([Teaching]({{ '/teaching/' | relative_url }})).

## Part 2: CDASim Development and MMITSS Integration, with Leidos for USDOT FHWA

### Integration CDASim with MMITSS and Performance Analysis
*Leidos, for USDOT FHWA's CARMA cooperative driving automation program (Saxton Transportation Operations Laboratory). Role: Developer, Sept 2024 – Apr 2025.*

1. Integrated MMITSS into CARMA-CARLA-SUMO co-simulation: added the MMITSS roadside and vehicle-side processors to CDASim, FHWA's co-simulation platform, so that signal priority can be tested with simulated connected vehicles. [GitHub](https://github.com/usdot-fhwa-stol/cdasim-config/tree/release/timtsp)
2. Added new features for time synchronization, message brokers, and parallel processing to support MMITSS in CDASim. [GitHub](https://github.com/usdot-fhwa-stol/cda-mmitss/tree/develop)
3. Packaged and tested the message transceivers that link MMITSS to CARMA (Kafka to CARMA Streets on the roadside, ROS 2 to the CARMA Platform on the vehicle side); fixed SSM sending, SRM encoding, and the NTCIP (SNMP) link to the signal controller. [GitHub](https://github.com/usdot-fhwa-stol/mmitss)
4. Built integration testing and a demo with the released configuration.
5. Worked with Leidos engineers through FHWA's CARMA development process (issue tickets and code reviews); 12 pull requests merged into three FHWA repositories.

## Part 3: Connected Vehicle Development

### Signal V2X-Based Versatile Connected Autonomous Vehicle
*A full-stack, closed-loop infrastructure-to-AV system that plans the vehicle trajectory in real-world deployment. Role: Core Team Member.*

1. Roadside: connected the traffic signal controller to the roadside V2X unit with the SAE J2735 protocol.
2. Vehicle side: developed the signal-aware speed advisory algorithm and deployed it on a real vehicle; took part in all internal tests.
3. Took part in the 2024 Mcity 2.0 Challenge (May – August 2024), Mcity, University of Michigan.

## Technical Demonstrations
- **Jun 2026**: IEEE Intelligent Vehicles Symposium (IV 2026), Mcity, Ann Arbor, MI: MMITSS transit signal priority demonstration for symposium attendees and USDOT officials ([news]({{ site.baseurl }}{% post_url 2026-06-22-mmitss-ieee-iv-2026 %})).
- **Jun 2026**: ITS America Conference & Expo 2026, Detroit, MI: MMITSS phase-2 demonstration for Michigan DOT and other state DOT officials ([news]({{ site.baseurl }}{% post_url 2026-06-12-mmitss-its-america-2026 %})).
- **Oct 2025**: UMTRI 60th Anniversary Symposium, Mcity, Ann Arbor, MI: live demonstration of V2X-enabled transit signal priority with a transit bus ([news]({{ site.baseurl }}{% post_url 2025-10-03-umtri-tsp-demo %}) · [Purdue CCE news](https://engineering.purdue.edu/CCE/AboutUs/News/Transportation_Features/purdue-cart-lab-invited-to-participate-in-umtri-symposium)).
