---
title: "Publications"
permalink: /publications/
classes: wide2
header:
  overlay_color: "#0066CC"
excerpt: >
  Explore papers from the latest state-of-the-art research in explainable AI.<br />
last_modified_at: 2021-10-04
---
The following is a list of papers from the field of explainable AI. Please feel free to submit a pull request to contribute to this list.

<div>
{% for year in (2017..2021) reversed %}
{% assign year_cits = site.data.xai_pubs | where: 'pub_year', year %}
    {% unless year_cits.size == 0 %}
        <h2> {{year}} </h2>
    {% endunless %}
    <ul style="list-style-type:none;">
    {% for cit in year_cits %}
        <li style="margin: 30px 0;">{{ cit.citation }}</li>
    {% endfor %}
    </ul>
{% endfor %}
</div>
