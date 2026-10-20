---
title: "AgentSim: An Agentic Test Engineer for Autonomous-Driving Safety Validation"
excerpt: "Initiated and developed at Inchor (SaferDrive AI). LLM/VLM agents mutate real logged drives into safety-critical corner cases, replay them in closed loop, and a video world model renders the result."
collection: portfolio
project_period: "Mar 2026 – Present"
author_profile: false
redirect_from:
  - /agentsim-demo/
---

{% include base_path %}
{% assign demo = site.data.agentsim_demo %}

<p class="agentsim-lead">
AgentSim is an agentic world model for autonomous-driving safety validation. Starting from trajectories from real world with a sentence or two describing the risk to add, LLM/VLM agents create safety-critical
variants of the drive: a lead car that brakes hard, a car that cuts in, a red-light runner, a pedestrian crossing.
Each variant runs in closed loop, so every other road user follows its recorded path until the mutation reaches it
and then reacts, and the variant stays grounded in the original traffic. A video world model then renders each
variant as a 12-second front-camera clip from the same first frame as the logged drive, so the clips differ only
where the mutation changes the traffic. The three drives below, from the Waymo Open Motion Dataset, show each
logged drive and its five variants side by side.
</p>

<p class="agentsim-howto">
<strong>How to read this page.</strong> Each case is one video box: the logged drive and its variants play side by
side, time-synchronized, with a short label in each cell and the full descriptions below. Videos are muted and loop;
they start playing when scrolled into view. Each legend entry links to that clip on its own, and <em>Frame strip</em>
shows all clips of a case as stills at 0, 3, 6, 9 and 11.8 s.
</p>

{% include agentsim-demo-assets.html %}
<style>
  /* This page has no author sidebar, so let it use the full content column on large screens. */
  @media (min-width: 925px) {
    #main .page { float: none; width: 100%; padding-left: 0; padding-right: 0; }
  }
</style>

{% for group in demo.groups %}
{% assign gdir = demo.asset_root | append: "/" | append: group.key %}
<section class="agentsim-group">
  <h2>{{ forloop.index }}. {{ group.title }}</h2>
  {% include agentsim-grid.html group=group %}
  <details class="agentsim-strip">
    <summary>Frame strip: all {{ group.clips.size }} clips at 0, 3, 6, 9 and 11.8 s</summary>
    <a href="{{ base_path }}{{ gdir }}/{{ group.contact_sheet }}">
      <img src="{{ base_path }}{{ gdir }}/{{ group.contact_sheet }}" loading="lazy"
           alt="Frame strip for {{ group.title | escape }}: one row per clip, five frames each">
    </a>
  </details>
</section>
{% endfor %}

<p class="agentsim-note agentsim-attribution">Waymo Open Dataset: An autonomous driving dataset. <a href="https://www.waymo.com/open">https://www.waymo.com/open</a>, 2019–2025.</p>
