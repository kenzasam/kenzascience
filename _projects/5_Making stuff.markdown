---
layout: post
title: Portfolio
description: Design and stuff
img: /img/des1.jpg
---
<br>
<div class="img_row">
	<img class="col one" src="{{ site.baseurl }}/img/TreeofLight2.gif" alt="" title="VR doodle"/>
	<img class="col one" src="{{ site.baseurl }}/img/business.png" alt="" title="example image"/>
	<img class="col one" src="{{ site.baseurl }}/img/tabular.gif" alt="" title="example image"/>
</div>
<br>
<h3>Biodesign</h3>
<div class="img_row">
	<img class="col one" src="{{ site.baseurl }}/img/motherwater1.jpg" alt="" title="VR doodle"/>
	<img class="col one" src="{{ site.baseurl }}/img/motherwater2.jpg" alt="" title="example image"/>
	<img class="col one" src="{{ site.baseurl }}/img/kombuchalamp.jpg" alt="" title="example image"/>
</div>
<br>
<h3>Illustrations</h3>
<div class="img_row">
	<img class="col one" src="{{ site.baseurl }}/img/sci_ill_1.png" alt="" title=""/>
</div>
<br>
<h3>Code & Creative code</h3>
<br>
<h4> Code </h4>
Most of my work is done in Python. You can find my academic work on the [Shihlab bitbucket](https://bitbucket.org), and personal work on my [Github](https://github.com/kenzasam).
<br>
<h4>Creative coding</h4>
The homepage shows a DNA sequence (currently MI transposon insertion flanking sequence of *Drosophila melanogaster*) that you can draw out using your cursor. You can explore the full version of this project [here](/alleles.html).
<br>
ALLE(LE)S is an ongoing project, with which I hope to show both the complexity and intricacy of the basics of life: DNA. DNA, in a biological sense, means everything and nothing. DNA is the hard drive of our bodies, it contains our genes, the mutations we care, our ancestry. And every cell in your body, roughly has exactly the same genetic makeup. However, without the regulatory machinery around it, without the encoded RNA, we won't make proteins, and without proteins, well, there will not be life, since DNA can't even be transcribed into RNA without them... So, DNA on it's own, doesn't really mean much. And that becomes very clear, when you compare the sizes of different genomes. Plants can have DNA 10 times 'longer' than ours. And *E.coli*, has DNA only times smaller.
<br>
ALLE(LE)S is a data visualisation project.
The interactive visualisation, allows you to search and draw out any DNA sequence (playing a polymerase), allows you to decide when to generate RNA (playing a ribosome): a visual experience that brings you closer to the complexity of your biology, and the essence of what it is to be.
<br>
<h4>How to add a p5  or Processing canvas to a Github hosted webpage</h4>
<br>
If you are interested in how to build a website like this yourself, I'm including a short tutorial here. The homepage was made using Processing and [p5.js](https://p5js.org).
Processing is an easy to learn tool for creative coding and lets you draw onto a canvas using code, simply put. p5.js is based on Processing and allows you to transfer this canvas into a format that can be viewed online.
<br>
<br>
Here, a short tutorial on how to display p5.js on Github hosted Jekyll sites (I found this quite challenging and not much info is out there on this topic.) <br>
To be able to show this p5 canvas on your Github hosted Jekyll site, you can follow these steps:

1. Make a p5js folder in your Jekyll repository, containing your sketch file. You can find my sketch file [here](https://github.com/kenzasam/kenzascience/blob/gh-pages/p5js/sketch.js). I also currently provide the text (DNA sequence) as a separate txt file, placed in my main Jekyll repository.
2. Add Processing and p5.js functionality to your sites. Add [this](https://github.com/kenzasam/kenzascience/blob/gh-pages/processing.js) processing.js file to your main repository.
    Add the following code to your header.html file:

    ```
    {% assign p5_version = '0.5.16' %}
    {% if page.p5 %}
       {% for lib in page.p5 %}
       <script src="https://cdnjs.cloudflare.com/ajax/libs/p5.js/{{ p5_version }}/{{ lib }}.js"></script>
       {% endfor %}
    {% endif %}
    ```

    This will add a new markdown class. Now you're basically able to mention in the markdown prematter, the p5 libraries you want to load on that page.
3. Add this to your front matter of the page where you wish to display the canvas.

    ```
     ---
     layout: default
     p5:
      - p5
      - addons/p5.dom
     sketches:
      - sketch
     ---
    ```

<br>
<br>
<a href="javascript:javascript:history.go(-1)">  <font size="15"> < </font> </a>
<br>
