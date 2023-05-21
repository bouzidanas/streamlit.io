import streamlit as st
import reveal_slides as rs

sample_markdown = r"""
# Reveal.js + Streamlit
Add <a target="_blank" href="https://revealjs.com/">Reveal.js</a> presentations to your Streamlit app.
---
A paragraph with some text and a markdown [link](https://hakim.se). 
Markdown links get displayed within the parent iframe.
--
Another paragraph containing the same <a target="_blank" href="https://hakim.se">link</a>.
However, this link will open in a new tab instead. 
This is done using an HTML `<a>` tag with `target="_blank"`.
---
## Backgrounds
--
<!-- .slide: data-background-color="#283747" -->
Change the background to a solid color using the `data-background-color` attribute.
--
<!-- .slide: data-background-video="https://bouzidanas.github.io/videos/pexels-cottonbro-9665235.mp4" data-background-video-loop data-background-video-muted -->
Add a video as the background using the `data-background-video` attribute. Add data-background-video-loop to loop the video in the background and add data-background-video-muted to mute it.
---
<!-- .slide: data-background-color="#78281F" -->
## The Lorenz Equations

$$
\begin{aligned}
\dot{x} & = \sigma(y-x) \\\\
\dot{y} & = \rho x - y - xz \\\\
\dot{z} & = -\beta z + xy
\end{aligned}
$$
---
## Code blocks
```js [1-2|3|4]
let a = 1;
let b = 2;
let c = x => 1 + 2 + x;
c(3);
```
---
## Element attributes
- Item 1 <!-- .element: class="fragment" data-fragment-index="2" -->
- Item 2 <!-- .element: class="fragment" data-fragment-index="1" -->
---
## Last slide
"""

with st.sidebar:
    st.subheader("Parameters")
    theme = st.selectbox("Theme", ["black", "black-contrast", "blood", "dracula", "moon", "white", "white-contrast", "league", "beige", "sky", "night", "serif", "simple", "solarized"])
    height = st.number_input("Height", value=500)
    content_height = st.number_input("Content Height", value=900)
    content_width = st.number_input("Content Width", value=900)
    scale_range = st.slider("Scale Range", min_value=0.0, max_value=5.0, value=[0.1, 0.5], step=0.1)
    margin = st.slider("Margin", min_value=0.0, max_value=0.8, value=0.1, step=0.05)
    plugins = st.multiselect("Plugins", ["RevealMath.KaTeX", "RevealHighlight", "RevealSearch", "RevealNotes", "RevealZoom", "RevealMath.MathJax2", "RevealMath.MathJax3"], ["RevealMath.KaTeX", "RevealHighlight"])
                    
position = rs.slides(sample_markdown, height=height, theme=theme, config={"width": content_width, "height": content_height, "minScale": scale_range[0], "center": True, "maxScale": scale_range[1], "margin": margin, "plugins": plugins}, markdown_props={"data-separator-vertical":"^--$"}, key="foo")

st.write("Horizontal slide position: " + str(position["indexh"]))
st.write("Vertical slide position: " + str(position["indexv"]))
if ("indexf" in position):
    st.write("Fragment: " + str(position["indexf"]))