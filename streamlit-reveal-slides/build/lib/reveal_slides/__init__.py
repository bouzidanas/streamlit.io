import os
import streamlit.components.v1 as components

# Create a _RELEASE constant. We'll set this to False while we're developing
# the component, and True when we're ready to package and distribute it.
# (This is, of course, optional - there are innumerable ways to manage your
# release process.)
_RELEASE = True

# Declare a Streamlit component. `declare_component` returns a function
# that is used to create instances of the component. We're naming this
# function "_component_func", with an underscore prefix, because we don't want
# to expose it directly to users. Instead, we will create a custom wrapper
# function, below, that will serve as our component's public API.

# It's worth noting that this call to `declare_component` is the
# *only thing* you need to do to create the binding between Streamlit and
# your component frontend. Everything else we do in this file is simply a
# best practice.

if not _RELEASE:
    _component_func = components.declare_component(
        
        "slides",
        # Pass `url` here to tell Streamlit that the component will be served
        # by the local dev server that you run via `npm run start`.
        # (This is useful while your component is in development.)
        url="http://localhost:3001",
    )
else:
    # When we're distributing a production version of the component, we'll
    # replace the `url` param with `path`, and point it to to the component's
    # build directory:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/build")
    _component_func = components.declare_component("reveal_slides", path=build_dir)


# Create a wrapper function for the component. This is an optional
# best practice - we could simply expose the component function returned by
# `declare_component` and call it done. The wrapper allows us to customize
# our component's API: we can pre-process its input args, post-process its
# output value, and add a docstring for users.
def slides(content, height="auto", theme="black", config={}, markdown_props={}, allow_unsafe_html=False, key=None):
    """Create a new instance of "slides".

    Parameters
    ----------
    name: str
        The name of the thing we're saying hello to. The component will display
        the text "Hello, {name}!"
    key: str or None
        An optional key that uniquely identifies this component. If this is
        None, and the component's arguments are changed, the component will
        be re-mounted in the Streamlit frontend and lose its current state.

    Returns
    -------
    int
        The number of times the component's "Click Me" button has been clicked.
        (This is the value passed to `Streamlit.setComponentValue` on the
        frontend.)

    """
    # Call through to our private component function. Arguments we pass here
    # will be sent to the frontend, where they'll be available in an "args"
    # dictionary.
    #
    # "default" is a special argument that specifies the initial return
    # value of the component before the user has interacted with it.
    component_value = _component_func(content=content, height=height, theme=theme, config=config, markdown_props=markdown_props, allow_unsafe_html=allow_unsafe_html, key=key, default={ "indexh": -1, "indexv": -1, "indexf": -1, "paused": False, "overview": False})

    # We could modify the value returned from the component if we wanted.
    # There's no need to do this in our simple example - but it's an option.
    return component_value

# Add some test code to play with the component while it's in development.
# During development, we can run this just as we would any other Streamlit
# app: `$ streamlit run slides/__init__.py`
if not _RELEASE:
    import streamlit as st

    sample_html = r"""<section data-background-color="#78281F" ><h1>Reveal.js + Streamlit</h1></section>
<section>Slide 2</section>"""
    
    # Note that even though we put markdown in a raw string, we still need to escape the backslashes
    # This is why we use 4 backslashes to get 2 backslashes in the latex math code
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
                        
    position = slides(sample_markdown, height=height, theme=theme, config={"width": content_width, "height": content_height, "minScale": scale_range[0], "center": True, "maxScale": scale_range[1], "margin": margin, "plugins": plugins}, markdown_props={"data-separator-vertical":"^--$"}, key="foo")


    pause = st.checkbox("pause", value=False)
    st.write("Horizontal slide position: " + str(position["indexh"]))
    st.write("Vertical slide position: " + str(position["indexv"]))
    if ("indexf" in position):
        st.write("Fragment: " + str(position["indexf"]))