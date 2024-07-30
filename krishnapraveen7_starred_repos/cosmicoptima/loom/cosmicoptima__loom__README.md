# [loom](https://github.com/cosmicoptima/loom)

# loom(sidian)

**READ THE README IF YOU PLAN TO USE THIS PLUGIN. IT IS USEFUL**

This is a reimplementation of [Loom](https://github.com/socketteer/loom) as an Obsidian plugin, designed to be easier to use and more modular and extensible.

Loom is a recursively branching interface to GPT-3 and other language models; it is designed to be conducive to exploratory and experimental use of base models. The workflow primarily consists of this: you hit `Ctrl+Space` from a point in the text, and Loom generates `n` child nodes of the current node, where each child contains a different completion of the text leading up to the cursor. This is paired with a tree interface and settings panel in the right sidebar, as well as a pane containing the full text of the current node and its siblings.

Loom can request completions from the following providers: [Cohere](https://docs.cohere.ai/docs), [TextSynth](https://textsynth.com/documentation.html), [OpenAI](https://platform.openai.com/docs/introduction), and [Azure OpenAI Service](https://learn.microsoft.com/en-us/azure/ai-services/openai). It can also request completions from implementations of [openai-cd2-proxy](https://github.com/cosmicoptima/openai-cd2-proxy), in which case you must provide the base URL in the Loom tab in Settings.

If you are interested in funding this plugin's development, you can **[support me on Patreon](https://patreon.com/parafactual)**; I would then be able to devote more time to this and other independent projects.

**If you are new to Obsidian:** if you want to see the tree interface, make sure to open the right sidebar using the button on the top right, or using `Ctrl+P` then `Toggle right sidebar`. Once you've done that, go to the Loom tab, which is signified by a network icon.

**Default hotkeys:**

- generate - `Ctrl+Space`
- generate siblings - `Ctrl+Shift+Space`
- split at point - `Alt+s`
- split at point and create child - `Alt+c`
- delete (current node) - `Alt+Backspace`
- merge (current node) with parent - `Alt+m`

Navigation:
- switch to next sibling - `Alt+Down`
- switch to previous sibling - `Alt+Up`
- switch to parent - `Alt+Left`
- switch to (most recently visited) child - `Alt+Right`

In the editor:
- `Shift+click` on the text corresponding to a node to switch to it

**Loom can be installed in the Obsidian store.** If you don't want to do that:

1. Go to the latest release under the "Releases" subheading on the right
2. Download the zip file under "Assets"
3. Unzip the file you downloaded in `[path to vault]/.obsidian/plugins`, creating the `plugins` directory if necessary
4. Go to the "Community plugins" tab in Obsidian settings, then enable "Loom"

Alternatively, you can build Loom from source:

1. Clone this repository (`git clone https://github.com/cosmicoptima/loom`) in `[path to vault]/.obsidian/plugins`, creating the `plugins` directory if necessary
2. Run the following: `cd loom; npm i; npm run build`
3. Go to the "Community plugins" tab in Obsidian settings, then enable "Loom"
4. To update, go to the repository and `git pull; npm i; npm run build`, then disable and re-enable Loom

**If you are using MacOS:** a few hotkeys -- `Alt+s`, `Alt+c`, and `Alt+m` -- are bound to special characters. You can either:

1. Disable MacOS's special character shortcuts, as explained here: https://superuser.com/questions/941286/disable-default-option-key-binding
2. Rebind the Loom hotkeys you want to use in the Hotkeys tab in Settings
