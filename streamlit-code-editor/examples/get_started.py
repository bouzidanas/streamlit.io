import json
import streamlit as st
from code_editor import code_editor

# Sample string containing code
code_input = \
        '''#!/usr/local/bin/python

import string, sys

# If no arguments were given, print a helpful message
if len(sys.argv)==1:
    print 
    sys.exit(0)

# Loop over the arguments
for i in sys.argv[1:]:
    try:
        fahrenheit=float(string.atoi(i))
    except string.atoi_error:
        print repr(i), "not a numeric value"
    else:
        celsius=(fahrenheit-32)*5.0/9.0
        print 'Done' '''

# Opening JSON file
# You can also just use a dictionary but with files (JSON or text for example),
# its easier to transfer or use in multiple projects
with open('example_custom_buttons_set.json') as json_button_file:
    customButtons = json.load(json_button_file)

# Opening JSON file
with open('example_info_bar.json') as json_info_file:
    infoBar = json.load(json_info_file)

# Opening text file
with open('code_editor.scss') as css_file:
    cssText = css_file.read()

#comp_props = {"css": cssText, "globalCSS": "body > #root~div.ace-streamlit-dark.ace_editor.ace_autocomplete{\n    background-color: #111827;\n}\nbody > #root~div .ace_prompt_container {\n    background: #111827;\n}"}
comp_props = {"css": cssText, "globalCSS": ":root {--streamlit-dark-background-color: #111827;}"}


code_back = code_editor(code_input, lang="python", height = [19, 22], theme="contrast", buttons=customButtons["buttons"], component_props=comp_props, key="editor2")
if code_back['type'] == "submit" and len(code_back['text']) != 0:
    st.write("TYPE: ", code_back['type'])
    st.code(code_back['text'], language=code_back['lang'])
