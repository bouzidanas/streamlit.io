streamlit code editor  [![PYPI](https://img.shields.io/pypi/v/streamlit-code-editor)](https://pypi.org/project/streamlit-code-editor/#history)
============

A code editor component for streamlit.io apps, built on top of react-ace, with custom themes and customizable interface elements for better integration with other components.


---

## Installation
Install [streamlit-code-editor](https://pypi.org/project/streamlit-code-editor/) with pip:
```
python -m pip install streamlit_code_editor
```
replacing `python` with the correct version of python for your setup (e.g. `python3` or `python3.8`). Or if you are certain the correct version of python will be used to run pip, you can install with just:
```
pip install streamlit_code_editor
```
Alternatively, you can download the source from the [download page](https://pypi.org/project/streamlit-code-editor/#files) and after unzipping, install with:
```
python setup.py install
```
(for the above command to work, make sure you are in the same directory as 'setup.py' in the unzipped folder).

## Adding a Code Editor to Streamlit app
After importing the module, you can call the `code_editor` function with just a string:
```import streamlit as st
from code_editor import code_editor

response_dict = code_editor(your_code_string)
```
Without specifying a language, the editor will default to `python`. You can also specify a language with the `lang` argument:
```
# The default value for the lang argument is "python"\nresponse_dict = code_editor(your_code_string, lang="python")
```
 By default, each code editor is styled like streamlit's code component. We will go over how to customize the styling in a later section.
---

## License
