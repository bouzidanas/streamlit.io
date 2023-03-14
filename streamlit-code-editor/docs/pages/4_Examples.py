import json
import streamlit as st
from code_editor import code_editor

html_style_string = '''<style>
@media (min-width: 576px)
section div.block-container {
  padding-left: 20rem;
}
section div.block-container {
  padding-left: 4rem;
  padding-right: 4rem;
  max-width: 80rem;
}  
.floating-side-bar {
    display: flex;
    flex-direction: column;
    position: fixed;
    margin-top: 2rem;
    margin-left: 2.75rem;
    margin-right: 2.75rem;
}
.flt-bar-hd {
    color: #5e6572;
    margin: 1rem 0.1rem 0 0;
}
.floating-side-bar a {
    color: #b3b8c2;

}
.floating-side-bar a:hover {

}
.floating-side-bar a.l2 {

}
</style>'''

st.markdown(html_style_string, unsafe_allow_html=True)

with open('pages/resources/example_custom_buttons_set.json') as json_button_file:
    custom_buttons = json.load(json_button_file)

# Load Code Editor CSS from file
with open('pages/resources/code_editor.scss') as css_file:
    css_text = css_file.read()

col1, col2 = st.columns([6,2])
with col1:
    st.markdown("#### Disable line wrapping")
    code_styles_comp_demo = """# change editor (session) option 'wrap' to False to disable line wrapping
response_dict = code_editor(code_styles_comp_demo,lang="python", height = [2, 4], options={"wrap": False})"""
    # construct component props dictionary (->Code Editor)
    comp_props = {"css": css_text, "globalCSS": ":root {--streamlit-dark-background-color: #111827;}"}

    response_dict = code_editor(code_styles_comp_demo,lang="python", height = [2, 4], options={"wrap": False})

    if response_dict['type'] == "submit" and len(response_dict['text']) != 0:
        st.write("Response type: ", response_dict['type'])
        st.code(response_dict['text'], language=response_dict['lang'])

    st.warning("This section is incomplete. Please check back later.", icon="⚠️")