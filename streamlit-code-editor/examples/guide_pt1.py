import json
import streamlit as st
from code_editor import code_editor

# Opening JSON file
# You can also just use a dictionary but with files (JSON or text for example),
# its easier to transfer or use in multiple projects
with open('example_custom_buttons_bar_adj.json') as json_button_file:
    custom_buttons_alt = json.load(json_button_file)

with open('example_custom_buttons_set.json') as json_button_file:
    custom_buttons = json.load(json_button_file)

# Load Info bar CSS from JSON file
with open('example_info_bar.json') as json_info_file:
    info_bar = json.load(json_info_file)

# Load Code Editor CSS from file
with open('code_editor.scss') as css_file:
    css_text = css_file.read()

st.markdown("## Getting Started")
st.markdown("### Installation")
st.markdown("Install [streamlit-code-editor](https://pypi.org/project/streamlit-code-editor/) with pip:")
st.code("python -m pip install streamlit_code_editor")
st.markdown("replacing `python` with the correct version of python for your setup (e.g. `python3` or `python3.8`). Or if you are certain the correct version of python will be used to run pip, you can install with just:")
st.code("pip install streamlit_code_editor")
st.markdown("Alternatively, you can download the source from the [download page](https://pypi.org/project/streamlit-code-editor/#files) and after unzipping, install with:")
st.code("python setup.py install")
st.markdown("(for the above command to work, make sure you are in the same directory as 'setup.py' in the unzipped folder).")
st.markdown("### Adding a Code Editor")
st.markdown("After importing the module, you can call the `code_editor` function with just a string:")


minimal_code = '''# All you need to add a code editor to your Streamlit app is an\n# import and a string containing your code.
from code_editor import code_editor

response_dict = code_editor(your_code_string)'''

response_start = code_editor(minimal_code)

st.markdown("Without specifying a language, the editor will default to `python`. You can also specify a language with the `lang` argument:")

minimal_code_with_lang = '''# The default value for the lang argument is "python"\nresponse_dict = code_editor(your_code_string, lang="python")'''

response_start_with_lang = code_editor(minimal_code_with_lang)

st.markdown("The two blocks of code above are displayed in code editors. As the name of the component implies, you can edit the code. Try it out! ")
st.markdown("By default, each code editor is styled like streamlit's code component. We will go over how to customize the styling in a later section.")

st.markdown("## Basic customization")
st.markdown("In this section, we will go over the `height`, `theme`, `shortcuts`, and `focus` properties.")
st.markdown("### Height")
st.markdown("The height of the code editor can be set with the `height` argument. The height argument takes one of three types of values: a string, an integer number, or an list of two integers.")
st.code('''# set height of editor to 500 pixels\nresponse_dict = code_editor(your_code_string, height="500px")\n\n# set height to adjust to fit up to 20 lines (and scroll for more)\nresponse_dict = code_editor(your_code_string, height=20)\n\n# set height to display a minimum of 10 lines and a maximum of 20 lines\n# (and scroll for more)\nresponse_dict = code_editor(your_code_string, height=[10, 20])''')
st.markdown("If a string is given, it will be used to set the css height property of the editor part of the code editor component. This means that height can be set with strings like '500px' or '20rem' for example.")
st.markdown("If instead, `height` is set with an integer, it will be used to set the `maxLines` property of the editor. This means that the height will be adjusted to fit the number of lines in the code string upto but not exceeding the integer value given. It might be that you always want the editor to fit the code so that no scrolling is needed. In this case, you can set `height` to a large integer value like 1000.")
st.markdown("As you might have guessed, the inner editor also has a `minLines` property. It is set to 1 by default. If you want to set the minimum number of lines, you can set `height` to an list of two integers. The first integer will be used to set `minLines` and the second integer will be used to set `maxLines`.")

st.success("**Tip:** If you set both `minLines` and `maxLines` to the same value, the editor will fix its size to fit only that number of lines of text. This is useful if you want the editor to have a static size and you want to size it according to number of lines to show.")
st.info("**Note:** The height property does not limit the contents of the editor. Content that exceeds the height will be scrollable.")

st.markdown("### Theme")
st.markdown("As mentioned earlier, the code editor component contains an inner editor component. This inner editor is an [Ace Editor](https://ace.c9.io/) which comes with 20 built in themes. These themes share certain characteristics in appearance that I feel clash with streamlit's modern look. For better integration with streamlit's look, I have created a two custom Ace Editor themes called 'streamlit-dark' and 'streamlit-light'. These two themes can be used as a starting point for further customization of appearence as we will see in later sections.")
st.markdown("By default, the code editor chooses one of the two custom themes according to the `base` attribute of streamlit's theme section of config options (see [Advanced features - Theming](https://docs.streamlit.io/library/advanced-features/theming) for more details). For more control over which of the two is chosen, you can use the `theme` argument of Code Editor. The `theme` argument takes one of four string values: 'default', 'dark', 'light', 'contrast'.")
response_theme_light = code_editor('''# set theme to 'streamlit-dark' if base is 'dark' and \n# 'streamlit-light' if base is 'light'\nresponse_dict = code_editor(your_code_string, theme="default")''', theme="default")
response_theme_contrast = code_editor('''# set theme to 'streamlit-light' if base is 'dark' and \n# 'streamlit-dark' if base is 'light'\nresponse_dict = code_editor(your_code_string, theme="contrast")''', theme="contrast")
st.markdown('''Values 'dark' and 'light' will select 'streamlit-dark' and 'streamlit-light' respectively. The 'default' value will choose the 'streamlit-light' theme if `base="light"` and 'streamlit-dark' if `base="dark"`. Finally, passing in 'contrast' will do the exact opposite of 'default'.''')

st.markdown("### Shortcuts")
st.markdown("Ace Editor comes with four keyboard handlers: 'vim', 'emacs', 'vscode', and 'sublime'. The keyboard handler dictates what keyboard keys and key combinations will do by default. You can select the handler to start the editor with using the `shortcuts` argument. The `shortcuts` argument takes one of four string values: 'vim', 'emacs', 'vscode', 'sublime'. The default value for `shortcuts` is 'vscode'.")
response_shortcuts = code_editor('''# set keyboard handler to 'vim'\nresponse_dict = code_editor(your_code_string, shortcuts="vim")''', shortcuts="vim")

st.markdown("### Focus")
st.markdown("There maybe times when you want to focus the editor when it loads (to start or continue editing after script is run/re-run without having to click into the editor). You can do this by setting the `focus` argument to `True`. The default value for `focus` is `False`.")
response_focus = code_editor('''# set focus to True\nresponse_dict = code_editor(your_code_string, focus=True)''', focus=True)
st.markdown("There is one very important detail to note about the `focus` feature. Focus will be given to the editor only when the value of `focus` changes from `False` to `True`. This means that if you set `focus` to `True` in the first run of the script, it will not be given focus in subsequent runs. To give focus to the editor in subsequent runs, you will have to set `focus` to `False` and then `True` again. This is to avoid giving focus to the editor when it is not intended because streamlit script re-runs are not the only cause of component re-renders (resizing the browser window, for example, can also cause components to re-render) and each time the editor re-renders, it will respond to the value of the `focus` argument. ")

st.markdown("## Advanced usage")
st.markdown("Up to this point, we have not talked about what a `code_editor` returns and the bi-directional communication capabilities of the component. There is also a lot more you can add to the editor and a lot more you can customize.")

st.markdown("### Return value")
st.markdown("The return value of this code editor is the text/code contents of the editor a long with a few other pieces of information. You might expect the code_editor to return its contents after every edit but this is not the case. The decision was made from the start to avoid doing this because it would have been detrimental to the user experience. Communicating back to the streamlit script results in a re-run of the script and there is a period of time during this re-run where you cannot access/interact with the `code_editor` component. Even when the resulting delay between keystrokes is small, it still noticeable impacts the user experience. Instead, `code_editor` communicates back to the script (returns a dictionary containing the contents and more) when it is told to execute a command that does so. Code Editor components have a set of built-in commands, a few of which tell it to send back/return information to the script. There are a few ways the user can tell the editor to execute these commands and commands in general with the main way being through custom buttons.")

st.markdown("### Custom buttons")
st.markdown("Adding buttons is easy. You can add a button by passing a dictionary to the `custom_buttons` argument of the `code_editor` function.")

custom_button_code ='''# add a button with text: 'Copy'\ncustom_btns = [{"name": "Copy"}]\nresponse_dict = code_editor(your_code_string, buttons=custom_btns)'''
custom_button_code_show ='''[{"name": "Copy", "hasText": True}]'''
custom_button_code_show_always ='''[{"name": "Copy", "hasText": True, "alwaysOn": True,}]'''
custom_button_code_show_always_right ='''[{
  "name": "Copy",
  "hasText": True,
  "alwaysOn": True,
  "style": {"top": "0.46rem", "right": "0.4rem"}
}]'''
btn_show_always_right_icon ='''[{
  "name": "Copy",
  "feather": "Copy",
  "alwaysOn": True,
  "style": {"top": "0.46rem", "right": "0.4rem"}
}]'''

btn_show_always_right_icon_cmd ='''[{
  "name": "Copy",
  "feather": "Copy",
  "alwaysOn": True,
  "commands": ["copyAll"],
  "style": {"top": "0.46rem", "right": "0.4rem"}
}]'''

response_custom_button = code_editor(custom_button_code, lang="python", buttons=[{"name": "Copy"}])
st.markdown("Although you cant see it yet, a button has been added. The only required attribute to add a button is the `name` attribute containing a string. The `name` attribute should contain the text that will be displayed on the button. The name attribute is also used in the id of the HTML button element so make sure it is unique. You can put any assortment of characters in the name attribute including spaces.")
st.markdown("To show the text we have to set the `hasText` attribute to `True`.")
response_custom_button_show = code_editor(custom_button_code_show, lang="python", buttons=[{"name": "Copy", "hasText": True}])
st.markdown("The result is a button with the text 'Copy' that is only visible when you hover over it. To get it to be always visible, we can set the alwaysOn attribute to True.")
response_custom_button_show_always = code_editor(custom_button_code_show_always, lang="python", buttons=[{"name": "Copy", "hasText": True, "alwaysOn": True}])
st.markdown("The placement of the button in this example is not ideal. To position a custom button, you can use the `style` attribute. This attribute sets the buttons element's [style property](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/style). By default, custom buttons have their CSS postion property set to absolute so that they can be positioned anywhere (inside the iframe containing the Code Editor component) easily.")
response_btn_show_always_right = code_editor(custom_button_code_show_always_right, lang="python", buttons=[{"name": "Copy", "hasText": True, "alwaysOn": True, "style": {"top": "0.46rem", "right": "0.4rem"}}])
st.markdown("What if, instead of text, you want the button to have an icon like Streamlit's code component's copy button? Code Editor allows you add any [Feather](https://feathericons.com/) icon to a custom button. To do so, set the `feather` attribute to the name of the icon you want to use. Make sure that the name of the icon is formatted: the first letter of each word separated with a dash is capitalized and the dash is removed. For example, 'alert-circle' becomes 'AlertCircle'. If we just want to show the icon, we can remove the text by removing the `hasText` attribute or setting it to `False`.")
response_btn_show_always_right_icon = code_editor(btn_show_always_right_icon, lang="python", buttons=[{"name": "Copy", "feather": "Copy", "alwaysOn": True, "style": {"top": "0.46rem", "right": "0.4rem"}}])
st.markdown("There is still one major issue with the button. It does not do anything. To make the button do something, we have to give it a list of commands we want Code Editor to execute when the button is clicked. We can do this by giving the `commands` attribute a list of the names of the commands we want executed. You can find a list of the built-in commands [here]().")
response_btn_show_always_right_icon_cmd = code_editor(btn_show_always_right_icon_cmd, lang="python", buttons=[{"name": "Copy", "feather": "Copy", "alwaysOn": True, "commands": ["copyAll"], "style": {"top": "0.46rem", "right": "0.4rem"}}])
st.markdown("The 'copyAll' command simply copies the entire contents of the editor to the clipboard.")

st.markdown("#### Response commands")
st.markdown("Among the commands (that can be given to be executed when a button is clicked) are special commands called 'response commands' which call Streamlit's `setComponentValue` function to return a dictionary to the script. For example, the 'submit' command sends the following dictionary to the streamlit script as the return value of the `code_editor` function (corresponding to the Code Editor that executed the command):")

btn_submit_return = '''{
  "type": "submit",
  "lang": "python",
  "text": "the code in the editor",
}'''
st.code(btn_submit_return, language="python")

st.markdown("#### Demo")
st.markdown("The following is an example dictionary that adds multiple buttons, some that execute single commands, some that execute response commands and some that execute multiple commands. The buttons are also positioned differently and have different features turned on or off.")

btns_demo = '''[
 {
   "name": "Copy",
   "feather": "Copy",
   "hasText": True,
   "alwaysOn": True,
   "commands": ["copyAll"],
   "style": {"top": "0.46rem", "right": "0.4rem"}
 },
 {
   "name": "Shortcuts",
   "feather": "Type",
   "class": "shortcuts-button",
   "hasText": True,
   "commands": ["toggleKeyboardShortcuts"],
   "style": {"bottom": "calc(50% + 1.75rem)", "right": "0.4rem"}
 },
 {
   "name": "Collapse",
   "feather": "Minimize2",
   "hasText": True,
   "commands": ["selectall",
                "toggleSplitSelectionIntoLines",
                "gotolinestart",
                "gotolinestart",
                "backspace"],
   "style": {"bottom": "calc(50% - 1.25rem)", "right": "0.4rem"}
 },
 {
   "name": "Save",
   "feather": "Save",
   "hasText": True,
   "commands": ["save-state", ["response","saved"]],
   "response": "saved",
   "style": {"bottom": "calc(50% - 4.25rem)", "right": "0.4rem"}
 },
 {
   "name": "Run",
   "feather": "Play",
   "primary": True,
   "hasText": True,
   "showWithIcon": True,
   "commands": ["submit"],
   "style": {"bottom": "0.44rem", "right": "0.4rem"}
 },
 {
   "name": "Command",
   "feather": "Terminal",
   "primary": True,
   "hasText": True,
   "commands": ["openCommandPallete"],
   "style": {"bottom": "3.5rem", "right": "0.4rem"}
 }
]'''

response_btns_demo = code_editor(btns_demo, lang="python", height=20, buttons=custom_buttons)
st.markdown("Something you might've noticed is that the buttons on the bottom right get highlighted in a different color when the mouse is hovered over them. This is because the `primary` attribute is set to `True` for those buttons. This attribute tells Code Editor to get the color from the 'primary' config option (in the theme section of the Streamlit config file).")
st.info("**Note:** Some commands like 'response' take an argument. This argument may be a string, a number, or a dictionary. In the case of the 'response' command, the argument is a string. To add a command that takes an argument to the `commands` attribute, instead of a string with the name of the command, you add a list of two elements to the commands list. The first element of this inner list should be a string containing the name of the command and the second element should be the argument (string|number|dictionary)")
st.success("**Tip:** For better reusability, you can store the buttons in a file (like a JSON file) and then load the buttons from the file. This way, you can easily reuse buttons you have created for one Streamlit app in another. A side benefit is that you can change the buttons without having to change the code.")
st.markdown("For reference, here is the list of button attributes:")

btn_attr_dict = '''{
  "name":            ,# string (required) 
  "feather":         ,# string
  "iconSize":        ,# integer number
  "primary":         ,# boolean
  "hasText":         ,# boolean
  "showWithIcon":    ,# boolean
  "alwaysOn":        ,# boolean 
  "style":           ,# dictionary
  "theme":           ,# dictionary 
  "class":           ,# string
  "classToggle":     ,# string
  "commands":        ,# list
  "toggledCommands": ,# list
}'''

st.code(btn_attr_dict, language="python")

st.markdown("### Info bar")
st.markdown("The info bar is a component within Code Editor that can be used to display information. Adding one is similar to adding a button. You pass a dictionary to the `info` argument of the `code_editor` function. The dictionary should have the following attributes:")

info_attr_dict = '''{
  "name":    ,# string
  "css":     ,# string
  "style":   ,# dictionary
  "info":    ,# Array of dictionaries
}'''
st.code(info_attr_dict, language="python")

st.markdown("Example: Info bar with a single info item")
info_ex_dict = """# css to inject related to info bar
css_string = \'''\nbackground-color: #bee1e5;\n\nbody > #root .ace-streamlit-dark~& {\n   background-color: #262830;\n}\n\n.ace-streamlit-dark~& span {\n   color: #fff;\n   opacity: 0.6;\n}\n\nspan {\n   color: #000;\n   opacity: 0.5;\n}\n\n.code_editor-info.message {\n   width: inherit;\n   margin-right: 75px;\n   order: 2;\n   text-align: center;\n   opacity: 0;\n   transition: opacity 0.7s ease-out;\n}\n\n.code_editor-info.message.show {\n   opacity: 0.6;\n}\n\n.ace-streamlit-dark~& .code_editor-info.message.show {\n   opacity: 0.5;\n}\n\''' 

# create info bar dictionary
info_bar = {
  "name": "language info",
  "css": css_string,
  "style": {
            "order": "1",
            "display": "flex",
            "flexDirection": "row",
            "alignItems": "center",
            "width": "100%",
            "height": "2.5rem",
            "padding": "0rem 0.75rem",
            "borderRadius": "8px 8px 0px 0px",
            "zIndex": "9993"
           },
  "info": [{
            "name": "python",
            "style": {"width": "100px"}
           }]
}

# add info bar to code editor
response_dict = code_editor(your_code_string, lang="python", height=20, info=info_bar)"""
response_info_ex = code_editor(info_ex_dict, lang="python", height=20, info=info_bar)
st.markdown("There is a lot going on here with css and style that will be covered in the next section. For now, consider the `info` attribute. To add info items to the info bar, you add a dictionary to the list given to the `info` attribute. An info item dictionary can have the following attributes:")

info_item_attr_dict = '''{
  "name":    ,# string containing displayed text (required)
  "class":   ,# string
  "style":   ,# dictionary
  "theme":   ,# dictionary
}'''

st.code(info_item_attr_dict, language="python")

st.markdown("#### Info message")
st.markdown("When you add an info bar with at least one info item to the code editor, an additional, special info item is added to the bar that is specifically setup to display text sent to it via the 'infoMessage' command. ")

code_btns_info = '''# create copy button with 'infoMessage' command
custom_btns = [{
    "name": "Copy",
    "feather": "Copy",
    "hasText": True,
    "alwaysOn": True,
    "commands": ["copyAll", 
                 ["infoMessage", 
                  {
                   "text":"Copied to clipboard!",
                   "timeout": 2500, 
                   "classToggle": "show"
                  }
                 ]
                ],
    "style": {"right": "0.4rem"}
  }]

# add button and previous info bar to code editor
response_dict = code_editor(your_code_string, lang="python", height=20, info=info_bar, buttons=custom_btns)
'''

response_btn_info_msg = code_editor(code_btns_info, lang="python", height=20, info=info_bar, buttons=[{
    "name": "Copy",
    "feather": "Copy",
    "hasText": True,
    "alwaysOn": True,
    "commands": ["copyAll", ["infoMessage", {"text":"Copied to clipboard!", "timeout": 2500, "classToggle": "show"}]],
    "style": {"right": "0.4rem"}
  }])

st.markdown("### Menu bar")
st.markdown("The menu bar is another component within Code Editor that can be used to add a menu. Adding one is similar to adding the info bar. ")
st.markdown('[//]: # "TODO: complete this section"')


st.markdown("## Advanced customization")
st.markdown("In the previous section, there is an issue with the appearance of the info and menu bar examples. The top two corners of the editor component are rounded which does not allow for a seemless connection of the left and right edges with the edges of the info/menu bar. On top of this, you might want the bars to appear on the bottom or even on the sides of the editor instead of on top. This is where `css` and `style` attributes really come in to play. ")
st.markdown("To get a better understanding of how to use these attributes, we need to go over the layout of the Code Editor component.")
st.markdown("### Code Editor component layout")
st.image("code_editor_layout.png")
st.markdown('On the left (in the diagram) is the layout of the Code Editor component in the HTML/DOM. As you can see, it is relatively flat. On the right is the physical layout of the Code Editor component in the Streamlit app. Here, there are somethings to note. By default, the Code Editor component has its CSS `display` property set to "flex" and its `flex-direction` property set to "column". This means that Code Editor will stack its inner components on top of one another in a column. Additionally, the Ace Editor component has its CSS `order` property set to "3". Altogether, this provides a default setup that allows for easy rearrangment of the stacking order of the components inside the Code Editor. For example, setting the `order` property of the info bar component to a value less than 3 will put it above the Ace Editor like in the examples in the previous section. Setting it to 3 or greater will put the info bar below.')
st.markdown('''Custom buttons are not positioned like the Ace Editor, info bar, and menu bar components are. By default, they have their CSS `position` property set to "absolute" which makes it easier to position them anywhere within the iframe/document that contains the Code Editor component. ''')

st.markdown("### Customizing the Ace Editor")
st.markdown("The Ace Editor inside of Code Editor is highly configurable. There are so many configuration options in fact the decision was made to split them up into three groups: general properties, editor properties, editor options.")
st.markdown("- Set general properties by passing a dictionary to the `props` argument of the `code_editor` function. You can find the list of the properties in this group [here](https://github.com/securingsincity/react-ace/blob/master/docs/Ace.md).")
st.markdown("- Set editor properties by passing a dictionary to the `editor_props` argument of the `code_editor` function. You can find a list of the properties in this group [here](https://github.com/securingsincity/react-ace/blob/master/src/types.ts)")
st.markdown("- Set editor options by passing a dictionary to the `options` argument of the `code_editor` function. You can find a list of the properties in this group [here](https://github.com/ajaxorg/ace/wiki/Configuring-Ace#editor-options)")
st.info("**Note:** The general props group actually contains the other two groups as subgroups. The decision to use three different arguments (of `code_editor` function) is to allow you to set properties in each of the groups separately to simplify things, but you can just set everything via the `props` argument if you desire.")
st.warning("**Warning:** Currently, Code Editor allows access to pretty much all of the Ace Editor's configuration options including the callback functions which can allow you to pass in code that will be executed on the frontend. **_This is not secure!!_** Some of these options might be removed in the future.")

st.markdown("### Style and CSS")
st.markdown("""Code Editor and the components inside (Ace Editor, Info/Menu bars, and buttons) all have a way to set their `style` property. With the exception of Ace Editor and outer containers (like Code Editor), this is done via the `style` attribute of the corresponding dictionary. For example, the `style` attribute of the info bar dictionary is used to set the `style` property of the info bar component. In contrast, Ace Editor's `style` property is set via the `style` attribute in the dictionary you give to the `props` argument of the `code_editor` function. The style attribute corresponding to the Code Editor (outermost container labeled "Code Editor" in the diagram) should be in the dictionary you give to the function's `component_props` argument/parameter""")

code_setting_style = """# style dict for Ace Editor
ace_style = {"borderRadius": "0px 0px 8px 8px"}

# style dict for Code Editor
code_style = {"width": "100%"}

# set style of info bar dict from previous example
info_bar["style"] = {**info_bar["style"], "order": "1", "height": "2.0rem", "padding": "0rem 0.6rem", "padding-bottom": "0.2rem"}
response_dict = code_editor(your_code_string, height=20, info=info_bar, props={"style": ace_style}, component_props={"style": code_style})
"""
info_bar["style"] = {**info_bar["style"], "order": "1", "height": "2.0rem", "padding": "0rem 0.6rem", "padding-bottom": "0.2rem"}
response_info_ex_fixed = code_editor(code_setting_style, height=20, info=info_bar, props={"style": {"borderRadius": "0px 0px 8px 8px"}})
st.markdown("What if you want to not only style the component but also the elements inside of it? This is where `css` attributes come into the picture. You can pass in CSS to be applied to the component and its children. The way this CSS string is added to the already existing CSS is by prepending the automatically generated class name (given to the component) to the selectors of all rule sets in the string and any property-value pairs that are not in a rule set are added to a general rule set with the generated class name as the selector. In the following example, a CSS string is passed to Code Editor's `css` property: ")
code_setting_css = """# CSS string for Code Editor
css_string = '''
font-weight: 600;
&.streamlit_code-editor .ace-streamlit-dark.ace_editor {
  background-color: #111827;
  color: rgb(255, 255, 255);
}
&.streamlit_code-editor .ace-streamlit-light.ace_editor {
        background-color: #eeeeee;
        color: rgb(0, 0, 0);
}
'''

# same as previous example but with CSS string
response_dict = code_editor(your_code_string, height=20, info=info_bar, props={"style": ace_style}, component_props={"style": code_style, "css": css_string})
"""
css_string = '''
font-weight: 600;
&.streamlit_code-editor .ace-streamlit-dark.ace_editor {
  background-color: #111827;
  color: rgb(255, 255, 255);
}
&.streamlit_code-editor .ace-streamlit-light.ace_editor {
        background-color: #eeeeee;
        color: rgb(0, 0, 0);
}
'''
response_info_ex_fixed = code_editor(code_setting_css, height=20, info=info_bar, props={"style": {"borderRadius": "0px 0px 8px 8px"}}, component_props={"css": css_string})

st.markdown("Passing in the `css_string` results in the following CSS:")

css_result = """
.jBzdJR {
    font-weight: 500;
}

.jBzdJR.streamlit_code-editor .ace-streamlit-dark.ace_editor {
  background-color: #111827;
  color: rgb(255, 255, 255);
}
.jBzdJR.streamlit_code-editor .ace-streamlit-light.ace_editor {
        background-color: #eeeeee;
        color: rgb(0, 0, 0);
}
"""
st.code(css_result, language="css")
st.markdown('''"jBzdJR" is one of the generated class names given to the outermost Code Editor component HTML element.''')
st.info("**Note:** The ampersand ('&') in the CSS string is replaced with a class name that is generated when the component is first constructed. If a selector doesnt contain an ampersand, the generated class name is prepended and separated by a space. This means that you cannot select an element outside of the component. ")
st.success("**Tip:** You can use the ampersand to make the css selector more specific which allows you to override existing CSS rules pertaining to the element you want to style. Take a look at the `css_string` in info bar example from the previous section for examples of how this is done.")
st.markdown("The dictionaries used to add Info/Menu bars also have a `css` attribute which you can use to style the Info/Menu bar components and their children. ")
st.info("**Note:** Since the Info/Menu bars and Custom buttons are inside (and thus children) of the Code Editor component, you can style all of them via Code Editor's `css` property. Reasons you might opt for using the `css` attribute of the Info/Menu bar dictionaries instead include better organization and improving integration with other Code Editors (reusability). Each of these dictionaries should have everything needed to fully setup a component.")

st.markdown("#### Adding classes")
st.markdown("You can add a class to a component you are adding using the `class` attribute of the dictionary you pass in to the `code_editor` function. This can make it easier to target a component and its children using CSS.")
st.markdown("Furthermore, component dictionaries that have a `classToggle` attribute allow you to choose a class that you can toggle on the component via commands.")

st.markdown("#### Global styles")
st.markdown("What if you want to style the `body` element, the `html` document, or anything outside of the `CodeEditor` component? This can be done by adding global styles. You can add global styles by passing in a CSS string to the `globalCSS` attribute of the `component_props` dictionary.")
st.success("**Tip:** You can change global CSS variables via the `globalCSS` attribute. This can be an easier and more efficient way to customize the two built-in themes ('streamlit-dark' and 'streamlit-light') which rely on several CSS variables. ")

st.markdown("#### Demo")
code_styles_comp_demo = """# Load custom buttons from file
with open('example_custom_buttons_bar_adj.json') as json_button_file:
    custom_buttons = json.load(json_button_file)

# Load Info Bar from file
with open('example_info_bar.json') as json_info_file:
    info_bar = json.load(json_info_file)

# Load Code Editor CSS from file
with open('code_editor.scss') as css_file:
    css_text = css_file.read()

# construct component props dictionary (->Code Editor)
comp_props = {"css": css_text, "globalCSS": ":root {--streamlit-dark-background-color: #111827;}"}

# construct props dictionary (->Ace Editor)
ace_props = {"style": {"borderRadius": "0px 0px 8px 8px"}}

# add code editor component
response_dict = code_editor(your_code_string,  height = [19, 22], theme="contrast", buttons=custom_buttons, info=info_bar, component_props=comp_props, props=ace_props) 

# handle response to the Run button being clicked (command: submit)
if response_dict['type'] == "submit" and len(response_dict['text']) != 0:
    st.write("Response type: ", response_dict['type'])
    st.code(response_dict['text'], language=response_dict['lang'])
"""
# construct component props dictionary (->Code Editor)
comp_props = {"css": css_text, "globalCSS": ":root {--streamlit-dark-background-color: #111827;}"}

# construct props dictionary (->Ace Editor)
ace_props = {"style": {"borderRadius": "0px 0px 8px 8px"}}
response_dict = code_editor(code_styles_comp_demo,  height = [19, 22], theme="contrast", buttons=custom_buttons_alt, info=info_bar, component_props=comp_props, props=ace_props)

if response_dict['type'] == "submit" and len(response_dict['text']) != 0:
    st.write("Response type: ", response_dict['type'])
    st.code(response_dict['text'], language=response_dict['lang'])
#====================================================================================
# Sample string containing code
# code_input = \
#         '''#!/usr/local/bin/python

# import string, sys

# # If no arguments were given, print a helpful message
# if len(sys.argv)==1:
#     print 
#     sys.exit(0)

# # Loop over the arguments
# for i in sys.argv[1:]:
#     try:
#         fahrenheit=float(string.atoi(i))
#     except string.atoi_error:
#         print repr(i), "not a numeric value"
#     else:
#         celsius=(fahrenheit-32)*5.0/9.0
#         print 'Done' '''

# # Opening JSON file
# with open('example_info_bar.json') as json_info_file:
#     infoBar = json.load(json_info_file)

# # Opening text file
# with open('code_editor.scss') as css_file:
#     css_text = css_file.read()

# #comp_props = {"css": css_text, "globalCSS": "body > #root~div.ace-streamlit-dark.ace_editor.ace_autocomplete{\n    background-color: #111827;\n}\nbody > #root~div .ace_prompt_container {\n    background: #111827;\n}"}
# comp_props = {"css": css_text, "globalCSS": ":root {--streamlit-dark-background-color: #111827;}"}


# code_back = code_editor(code_input, lang="python", height = [19, 22], theme="contrast", buttons=custom_buttons, component_props=comp_props, key="editor2")
# if code_back['type'] == "submit" and len(code_back['text']) != 0:
#     st.write("TYPE: ", code_back['type'])
#     st.code(code_back['text'], language=code_back['lang'])
