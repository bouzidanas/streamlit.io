streamlit code editor  [![Version](https://img.shields.io/pypi/v/streamlit-code-editor)](https://pypi.org/project/streamlit-code-editor/#history) [![Downloads](https://img.shields.io/pypi/dm/streamlit-code-editor)](https://pypi.org/project/streamlit-code-editor/#files)
============

A code editor component for streamlit.io apps, built on top of react-ace, with custom themes and customizable interface elements for better integration with other components.

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

## Usage
To add a Code Editor to Streamlit python app, import `code_editor` and then call the `code_editor` function with the code you want to edit (as a string):
```
from code_editor import code_editor

response_dict = code_editor(your_code_string)
```
Without specifying a language, the editor will default to `python`. You can also specify a language with the `lang` argument:
```
# The default value for the lang argument is "python"
response_dict = code_editor(your_code_string, lang="javascript")
```
By default, each code editor is styled like streamlit's code component. We will go over how to customize the styling in a later section.
## Basic customization

### Height
The height of the code editor can be set with the `height` argument. The height argument takes one of three types of values: a string, an integer number, or an list of two integers.
```
# set height of editor to 500 pixels
response_dict = code_editor(your_code_string, height="500px")

# set height to adjust to fit up to 20 lines (and scroll if more)
response_dict = code_editor(your_code_string, height=20)

# set height to display a minimum of 10 lines and a maximum of 20 lines
# (and scroll if more)
response_dict = code_editor(your_code_string, height=[10, 20])
```

If a string is given, it will be used to set the css height property of the editable part of the code editor. This means that height can be set with strings like '500px' or '20rem' for example.

If instead, `height` is set with an integer, it will be used to set the `maxLines` property of the editor. This means that the height will be adjusted to fit the number of lines in the code string upto but not exceeding the integer value given.

As you might have guessed, the inner editor also has a `minLines` property. It is set to 1 by default. If you want to set the minimum number of lines, you can set `height` to an list of two integers. The first integer will be used to set `minLines` and the second integer will be used to set `maxLines`.

### Theme
By default, the code editor chooses one of the two custom themes according to the `base` attribute of Streamlit's theme section of config options (see [Advanced features - Theming](https://docs.streamlit.io/library/advanced-features/theming) for more details). To change this behavior, use the `theme` argument of the `code_editor` function. The `theme` argument takes one of four string values: 'default', 'dark', 'light', 'contrast'.

```python
# set theme to 'streamlit-dark' if base is 'dark' and 
# 'streamlit-light' if base is 'light'
response_dict = code_editor(your_code_string, theme="default")
```

```python
# set theme to 'streamlit-light' if base is 'dark' and 
# 'streamlit-dark' if base is 'light'
response_dict = code_editor(your_code_string, theme="contrast")
```

Values 'dark' and 'light' will select 'streamlit-dark' and 'streamlit-light' respectively. The 'default' value will choose the 'streamlit-light' theme if `base="light"` and 'streamlit-dark' if `base="dark"`. Finally, passing in 'contrast' will do the exact opposite of 'default'.

### Shortcuts
The built-in Ace Editor comes with four keyboard handlers: 'vim', 'emacs', 'vscode', and 'sublime'. The keyboard handler dictates what keyboard keys and key combinations will do by default. You can select the handler to start the editor with using the `shortcuts` argument. The `shortcuts` argument takes one of four string values: 'vim', 'emacs', 'vscode', 'sublime'. The default value for `shortcuts` is 'vscode'.

```
# set keyboard handler to 'vim'
response_dict = code_editor(your_code_string, shortcuts="vim")
```

### Focus
You can focus the editor when it loads by setting the `focus` argument to `True`. The default value for `focus` is `False`.

```
# set focus to True
response_dict = code_editor(your_code_string, focus=True)
```

There is one very important detail to note about the `focus` feature. Focus will be given to the editor only when the value of `focus` changes from `False` to `True`. This means that if you set `focus` to `True` in the first run of the script, it will not be given focus in subsequent runs. To give focus to the editor in subsequent runs, you will have to set `focus` to `False` and then `True` again. 
