---
title: "AgentSim Demo: Scenario Mutations of Real Drives, Rendered by a Video World Model"
permalink: /agentsim-demo/
author_profile: false
excerpt: "Three real drives from the Waymo Open Motion Dataset, each mutated by AgentSim into safety-critical variants and rendered as 12-second front-camera video by a video world model."
---

{% include base_path %}
{% assign demo = site.data.agentsim_demo %}

<p class="agentsim-lead">
Same drive, different danger. For each of three real drives, <strong><a href="{{ base_path }}/portfolio/01-agentsim/">AgentSim</a></strong>
replays the logged drive (<em>base</em>) and several variants it wrote itself: a lead car that brakes hard, a car that
cuts in, a red-light runner, a pedestrian crossing. Every variant runs in closed loop, so other road users follow
their recorded paths until the mutation reaches them and then react. A video world model renders each variant as a
12-second front-camera clip. All clips of a drive start from the same first frame, so they differ only where the
mutation changes the traffic.
</p>

<p class="agentsim-howto">
<strong>How to read this page.</strong> Each case is one video box: the logged drive and its variants play side by
side, time-synchronized, with a short label in each cell; the full descriptions are listed under the box. Videos are
muted and loop; they start playing when scrolled into view. Each legend entry links to that clip on its own, and
<em>Frame strip</em> shows all clips of a case as stills at 0, 3, 6, 9 and 11.8 s.
</p>

{% include agentsim-demo-assets.html %}
<style>
  /* This page has no author sidebar, so let it use the full content column on large screens. */
  @media (min-width: 925px) {
    #main .page { float: none; width: 100%; padding-left: 0; padding-right: 0; }
  }
  .agentsim-lead { font-size: 1.05em; }
  .agentsim-howto { font-size: 0.85em; color: var(--global-text-color-light); }
  .agentsim-group { margin-top: 2.5em; }
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
