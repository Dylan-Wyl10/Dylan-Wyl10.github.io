---
title: "AgentSim Demo: Scenario Mutations of Real Drives, Rendered by a Video World Model"
permalink: /agentsim-demo/
author_profile: false
excerpt: "Three real drives from the Waymo Open Motion Dataset, each mutated by AgentSim into safety-critical variants and rendered as 12-second front-camera video by a video world model."
---

{% include base_path %}
{% assign demo = site.data.agentsim_demo %}

<p class="agentsim-lead">
Same drive, different danger. For each of three real drives, <strong>AgentSim</strong> replays the logged drive
(<em>base</em>) and several variants it wrote itself: a lead car that brakes hard, a car that cuts in, a
red-light runner, a pedestrian crossing. Every variant runs in closed loop, so other road users follow their
recorded paths until the mutation reaches them and then react. A video world model renders each variant as a
12-second front-camera clip. All clips of a drive start from the same first frame, so they differ only where the
mutation changes the traffic.
</p>

<p>
AgentSim is the agentic scenario-generation module that Yilin Wang initiated within the
<a href="{{ base_path }}/portfolio/01-terasim/">TeraSim</a> platform at Inchor (SaferDrive AI): a multi-agent framework
driven by LLMs and VLMs that mutates logged drives into safety-critical corner cases for autonomous-vehicle testing.
</p>

<p class="agentsim-howto">
<strong>How to read this page.</strong> Each section is one drive. The first row is the logged drive; the rows
below it are AgentSim's variants. Clips are muted and loop; they start playing when scrolled into view.
Expand <em>Frame strip</em> under a drive to see all of its clips as still frames at 0, 3, 6, 9 and 11.8 s.
</p>

{% for group in demo.groups %}
{% assign gdir = demo.asset_root | append: "/" | append: group.key %}
<section class="agentsim-group" id="{{ group.key }}">
  <h2>{{ forloop.index }}. {{ group.title }}</h2>
  <p class="agentsim-group__meta">{{ group.dataset }}, scene <code>{{ group.scenario_id }}</code>.
    {{ group.clips.size | minus: 1 }} variants.</p>

  <div class="agentsim-rows">
  {% for clip in group.clips %}
    <div class="agentsim-row{% if clip.index == 'base' %} agentsim-row--base{% endif %}">
      <div class="agentsim-row__text">
        <span class="agentsim-row__index">{% if clip.index == 'base' %}Logged drive{% else %}Variant {{ clip.index | remove: 'var' }}{% endif %}</span>
        <p class="agentsim-row__desc">{{ clip.description }}</p>
      </div>
      <div class="agentsim-row__media">
        <video class="agentsim-clip" muted loop playsinline controls preload="none"
               width="960" height="528"
               poster="{{ base_path }}{{ gdir }}/{{ clip.poster }}"
               aria-label="{{ group.title | escape }}, {{ clip.index }}: {{ clip.description | escape }}">
          <source src="{{ base_path }}{{ gdir }}/{{ clip.video }}" type="video/mp4">
          <a href="{{ base_path }}{{ gdir }}/{{ clip.video }}">Download the {{ clip.index }} clip (MP4)</a>.
        </video>
      </div>
    </div>
  {% endfor %}
  </div>

  <details class="agentsim-strip">
    <summary>Frame strip: all {{ group.clips.size }} clips at 0, 3, 6, 9 and 11.8 s</summary>
    <a href="{{ base_path }}{{ gdir }}/{{ group.contact_sheet }}">
      <img src="{{ base_path }}{{ gdir }}/{{ group.contact_sheet }}" loading="lazy"
           alt="Frame strip for {{ group.title | escape }}: one row per clip, five frames each">
    </a>
  </details>
</section>
{% endfor %}

<section class="agentsim-credits">
  <h2>Credits</h2>
  <p>
    Driving scenes from the <a href="https://waymo.com/open/">Waymo Open Motion Dataset</a>, used under the
    Waymo Open Dataset License Agreement for Non-Commercial Use. First frames generated with NVIDIA
    Cosmos-Transfer1 (NVIDIA Open Model License). Videos generated with NVIDIA OmniDreams. This page shows
    rendered videos and images only; no dataset files are redistributed.
  </p>
  <p class="agentsim-note">
    These are research outputs. The rendered videos follow AgentSim's simulated traffic closely but not
    exactly; small, distant road users are occasionally not drawn.
  </p>
</section>

<style>
  /* This page has no author sidebar, so let it use the full content column on large screens. */
  @media (min-width: 925px) {
    #main .page { float: none; width: 100%; padding-left: 0; padding-right: 0; }
  }
  .agentsim-lead { font-size: 1.05em; }
  .agentsim-howto, .agentsim-group__meta, .agentsim-note { font-size: 0.85em; color: var(--global-text-color-light); }
  .agentsim-group { margin-top: 2.5em; }
  .agentsim-rows { display: flex; flex-direction: column; gap: 0.9em; margin: 1em 0; }
  .agentsim-row {
    display: grid;
    grid-template-columns: minmax(10em, 2fr) 3fr;
    gap: 1.2em;
    align-items: center;
    padding: 0.6em 0;
    border-bottom: 1px solid var(--global-border-color);
  }
  .agentsim-row--base { background: var(--global-code-background-color); border-radius: 6px; padding: 0.6em 0.8em; }
  .agentsim-row__index { display: block; font-weight: bold; margin-bottom: 0.25em; }
  .agentsim-row--base .agentsim-row__index { color: var(--global-link-color); }
  .agentsim-row__desc { margin: 0; font-size: 0.95em; }
  .agentsim-row__media { min-width: 0; }
  .agentsim-clip { display: block; width: 100%; height: auto; aspect-ratio: 960 / 528; background: #000; border-radius: 4px; }
  .agentsim-strip { margin: 0.5em 0 1em; font-size: 0.85em; }
  .agentsim-strip summary { cursor: pointer; }
  .agentsim-strip img { display: block; width: 100%; height: auto; margin-top: 0.75em; border: 1px solid var(--global-border-color); }
  .agentsim-credits { margin-top: 2.5em; }
  @media (max-width: 600px) {
    .agentsim-row { grid-template-columns: 1fr; gap: 0.5em; }
  }
</style>

<script>
  // Play each clip while it is on screen, pause it when it leaves. Autoplay is only
  // allowed because the clips are muted; without JavaScript the controls still work.
  (function () {
    var clips = document.querySelectorAll('video.agentsim-clip');
    if (!('IntersectionObserver' in window) || clips.length === 0) { return; }
    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        var video = entry.target;
        if (entry.isIntersecting) {
          var p = video.play();
          if (p && typeof p.catch === 'function') { p.catch(function () {}); }
        } else if (!video.paused) {
          video.pause();
        }
      });
    }, { threshold: 0.4 });
    clips.forEach(function (video) { observer.observe(video); });
  })();
</script>
