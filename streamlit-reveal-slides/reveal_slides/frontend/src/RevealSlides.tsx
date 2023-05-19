import {
  Streamlit,
  ComponentProps,
  withStreamlitConnection,
  Theme,
} from "streamlit-component-lib"
import { useEffect } from "react"


import Reveal from 'reveal.js';
import RevealMarkdown from 'reveal.js/plugin/markdown/markdown';
import RevealHighlight from 'reveal.js/plugin/highlight/highlight';
import RevealMath from 'reveal.js/plugin/math/math';
import RevealSearch from 'reveal.js/plugin/search/search';
import RevealNotes from 'reveal.js/plugin/notes/notes';
import RevealZoom from 'reveal.js/plugin/zoom/zoom';


import 'reveal.js/dist/reveal.css';
import 'reveal.js/plugin/highlight/monokai.css';

interface RevealSlidesProps extends ComponentProps {
  args: any
  width: number
  disabled: boolean
  theme?: Theme
}

const includedPlugins = {"RevealMarkdown": RevealMarkdown, "RevealHighlight": RevealHighlight, "RevealMath.KaTeX": RevealMath.KaTeX, "RevealMath.MathJax2": RevealMath.MathJax2, "RevealMath.MathJax3": RevealMath.MathJax3, "RevealSearch": RevealSearch, "RevealNotes": RevealNotes, "RevealZoom": RevealZoom}
// const simpleCommands = {"left": Reveal.left, "right": () => {Reveal.right()}, "up": Reveal.up, "down": Reveal.down, "prev": Reveal.prev, "next": Reveal.next, "prevFragment": Reveal.prevFragment, "nextFragment": Reveal.nextFragment, "togglePause": Reveal.togglePause, "toggleAutoSlide": Reveal.toggleAutoSlide, "toggleHelp": Reveal.toggleHelp, "toggleOverview": Reveal.toggleOverview, "shuffle": Reveal.shuffle}
// const commandsWithArgs = {slide: Reveal.slide, togglePause: Reveal.togglePause, toggleAutoSlide: Reveal.toggleAutoSlide, toggleHelp: Reveal.toggleHelp, toggleOverview: Reveal.toggleOverview}


/**
 * This is a React-based component template. The `render()` function is called
 * automatically when your component should be re-rendered.
 */
const RevealSlides = ({ args, disabled }: RevealSlidesProps) => {  
  
  const configStr = JSON.stringify(args["config"])

  // const commandStr = JSON.stringify(args["commands"])

  useEffect(() => {
    // code to run on component mount goes here
    import('../node_modules/reveal.js/dist/theme/' + args.theme + '.css')
    // import('../node_modules/reveal.js/plugin/highlight/monokai.css')
  }, [args.theme]);

  useEffect(() => {
    const config = JSON.parse(configStr)
    // code to run after render goes here
    if (args["allow_unsafe_html"]) {
      // do nothing
    }
    else {
      if ('plugins' in config){
        var arr = config['plugins'];
        arr.forEach(function(moduleName: string, index: number) {
          if (moduleName in includedPlugins){
            arr[index] = (includedPlugins as any)[moduleName];
          }
          else {
            arr[index] = null;
          }
        });
        config['plugins'] = arr.filter((x:any) => !!x) as any[];
        if(!config['plugins'].includes(RevealMarkdown)){
          config['plugins'].push(RevealMarkdown);
        }
      }
      else {
        config['plugins'] = [RevealMarkdown];
      }
      console.log(config['plugins']);
    }
    Reveal.initialize(config).then(() => {
      // reveal.js is ready

      // For some yet to be determined reason, the highlight plugin is not initialized.
      // Setting highlight config option highlightOnLoad to true (before passing to initialize function)
      // does not work
      let highlighter = Reveal.getPlugin('highlight') as any;
      console.log(highlighter);
      if (highlighter){
        highlighter.init(Reveal);
      } 

      // Send slide position indecies back to Streamlit on initialization and on slide change
      const index = Reveal.getIndices();
      Streamlit.setComponentValue({indexh: index.h, indexv: index.v});
      Reveal.on( 'slidechanged', event => {
        Streamlit.setComponentValue({indexh: (event as any).indexh, indexv: (event as any).indexv});
      });
    });

    return () => {
      // code to run on component unmount goes here
      Reveal.destroy();  
    }
  }, [configStr, args["allow_unsafe_html"]]);

  useEffect(() => {
    if (Reveal.isReady()){
      if (disabled){
        Reveal.togglePause(true);
        let viewport = Reveal.getViewportElement();
        if (viewport){
          viewport.style.pointerEvents = "none";
          viewport.style.cursor = "not-allowed";
          viewport.style.opacity = "0.5";
        }
      }
      else {  
        Reveal.togglePause(false);
        let viewport = Reveal.getViewportElement();
        if (viewport){
          viewport.style.pointerEvents = "auto";
          viewport.style.cursor = "auto";
          viewport.style.opacity = "1";
        }
      }
    }
  }, [disabled]);

  //To do: add support for commands
  //-----------------
  // useEffect(() => {
  //   const commands = JSON.parse(commandStr)
  //   if (Array.isArray(commands) && commands.length > 0 && Reveal.isReady()){
  //     commands.forEach((command: any) => {
  //       if (typeof command === "string" && command in simpleCommands){
  //         (simpleCommands as any)[command]();
  //       }
  //       else if (Array.isArray(command) && command.length > 0 && typeof command[0] === "string" && command[0] in commandsWithArgs){
  //         if (command[0] === "slide"){
  //           if (command.length === 3){
  //             Reveal.slide(command[1], command[2]);
  //           }
  //           else if (command.length === 4){
  //             Reveal.slide(command[1], command[2], command[3]);
  //           }
  //           else {
  //             console.warn("Invalid slide command: slide command array must have 3 or 4 elements.");
  //           }
  //         }
  //         else {
  //           (commandsWithArgs as any)[command[0]](command[1]);
  //         }
  //       }
  //       else {
  //         console.warn("Invalid command: command must be a string or an array containing a string as its first element.");
  //       }
  //     });
  //   }
  //   else if (!Array.isArray(args["commands"])) {
  //     console.warn("Invalid commands property value: commands must be an array containing at least one command.");
  //   }
  // }, [commandStr]);

    /**
   * resizeObserver observes changes in elements its given to observe and is used here
   * to communicate to streamlit the height of the component that has changed
   * so that streamlit can adjust the iframe containing the component accordingly.
   */
  const resizeObserver = new ResizeObserver((entries: any) => {
    // If we know that the body will always fully contain our component (without cutting it off)
    // then we can use docuemnt.body height instead
    if (args["height"] === "auto" || typeof args["height"] !== "number"){
      Streamlit.setFrameHeight((entries[0].contentBoxSize.blockSize ?? entries[0].contentRect.height)); 
      if (Reveal.isReady()){
        Reveal.layout();
      }
    }
    else {
      Streamlit.setFrameHeight(args["height"]);
      if (Reveal.isReady()){
        Reveal.layout();
      }
    }
    
  })

  const observe = (divElem: any) => {
    divElem ? resizeObserver.observe(divElem as HTMLDivElement) : resizeObserver.disconnect();
  }

  if (args["allow_unsafe_html"]) {
    return (
      <div ref={observe} className="slides" dangerouslySetInnerHTML={{__html: args["content"]}}>
      </div>
    )
  }
  else {
    return (
      <div ref={observe} className="slides">
        <section data-markdown={""} {...args["markdown_props"]}>
          <script type={"text/template"}>
          {args["content"]}
          </script>
        </section>
      </div>
    )
  }
}

// "withStreamlitConnection" is a wrapper function. It bootstraps the
// connection between your component and the Streamlit app, and handles
// passing arguments from Python -> Component.
//
// You don't need to edit withStreamlitConnection (but you're welcome to!).
export default withStreamlitConnection(RevealSlides)
