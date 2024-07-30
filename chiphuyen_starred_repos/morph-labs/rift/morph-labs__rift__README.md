# [rift](https://github.com/morph-labs/rift)

# Rift

### [Download for VSCode](https://marketplace.visualstudio.com/items?itemName=Morph.rift-vscode)

Rift is open-source infrastructure for AI-native development environments. Rift makes your IDE *agentic*. Software will soon be written mostly by AI software engineers that work alongside you. Codebases will soon be living, spatial artifacts that *maintain context*, *listen to*, *anticipate*, *react to*, and *execute* your every intent. The [Rift Code Engine](./rift-engine/) implements an AI-native extension of the [language server protocol](https://microsoft.github.io/language-server-protocol/). The [Rift VSCode extension](./editors/rift-vscode) implements a client and end-user interface which is the first step into that future.

https://github.com/morph-labs/rift/assets/13114790/726f35ed-4959-4f69-9a80-fd903b26f909

- [Discord](https://discord.gg/wa5sgWMfqv)
- [Features](#features)
  - Conversational Code Editing
  - Codebase-wide Edits
  - Contextual Codebase Generation
  - Auto Docstring Generation
- [Tips](#tips)
- [Getting Started](#getting-started)
- [Manual Installation](#manual-installation)
- [The Road Ahead](#the-road-ahead)
- [Contributing](#contributing)
- [Feedback](#feedback)



## Features
**Conversational Code Editing**

![code edit screencast](https://github.com/morph-labs/rift/blob/pranav/dev/assets/code-edit.gif)

**Codebase-wide Edits**

![aider screencast](https://github.com/morph-labs/rift/blob/pranav/dev/assets/aider.gif)

**Contextual Codebase Generation**

![smol screencast](https://github.com/morph-labs/rift/blob/pranav/dev/assets/smol.gif)

**Auto Docstring Generation**

![auto doc screencast](https://github.com/morph-labs/rift/blob/main/assets/auto-doc.gif)

**Auto Type Annotation Generation**

![type inference screencast](https://github.com/morph-labs/rift/blob/main/assets/type-inference.gif)

## Tips
- Press Command+M to focus the Rift Omnibar.
  - Once focused, you can either engage with the current chat or use a slash-command (e.g. `/aider`) to spawn a new agent.
- Each instance of a Rift Chat or Code Edit agent will remain attached to the open file / selection you used to spawn it.
  - To switch to a new file or request a code edit on a new selection, spawn a new agent by pressing Command+M and running a slash-command (e.g. `/edit`)
  - Both Rift Chat and Code Edit see a window around your cursor or selection in the currently active editor window. To tell them about other resources in your codebase, mention them with `@`.
  - Code Edit 
- You can `@`-mention files and directories to tell your agents about other parts of the codebase.
  - `@`-mentioning files currently only works with Aider if those files are tracked by git.
- Currently, Rift works best when the active workspace directory is the same as the root directory of the `git` project.
- Command+Shift+P -> "Rift: Start Server" restarts the server if it has been auto-installed.


## Getting Started
Install the VSCode extension from the VSCode Marketplace. By default, the extension will attempt to automatically start the Rift Code Engine every time the extension is activated. During this process, if a `rift` executable is not found in a virtual environment under `~/.morph`, the extension will ask you to attempt an automatic installation of a Python environment and the Rift Code Engine. To disable this behavior, such as for development, go to the VSCode settings, search for "rift", and set `rift.autostart` to `false`.

When `rift.autostart` is `true`, the extension will attempt to automatically start the Rift Code Engine. You can set `rift.riftPath` to change the path of the Rift executable, which may be necessary due to interactions with WSL on Windows.

When `rift.autostart` is `false`, the extension will display a loading indicator while it waits for a server instance to connect to `rift.riftServerPort` (default 7797). In this scenario, you will have to start the Rift server instance manually by running it in a terminal, e.g. with

```bash
source ~/.morph/env/bin/activate
rift --port 7797
```

Upon installation, when one changes the 'Code Edit Model' in the settings to our Rift Coder 7B model, it will automatically install an 8-bit quantized version of the model. [The raw model can be found here](https://huggingface.co/morph-labs/rift-coder-v0-7b-gguf).


If the automatic installation of the Rift Code Engine fails, follow the below instructions for manual installation.

### Manual Installation
**Rift Code Engine**:
- Set up a Python virtual environment for Python 3.10 or higher.
  - On Mac OSX:
    - Install [homebrew](https://brew.sh).
    - `brew install python@3.10`
    - `mkdir -p ~/.morph/ && cd ~/.morph/ && python3.10 -m venv env`
    - `source ./env/bin/activate`
  - On Linux:
    - On Ubuntu:
      - `sudo apt install software-properties-common -y`
      - `sudo add-apt-repository ppa:deadsnakes/ppa`
      - `sudo apt install python3.10 && sudo apt install python3.10-venv`
      - `mkdir -p ~/.morph/ && cd ~/.morph/ && python3.10 -m venv env`
      - `source ./env/bin/activate`
    - On Arch:
      - `yay -S python310`
      - `mkdir -p ~/.morph/ && cd ~/.morph/ && python3.10 -m venv env`
      - `source ./env/bin/activate`
  - On Windows:
    - We recommend that you use [WSL](https://learn.microsoft.com/en-us/windows/wsl/install) with Ubuntu. Once inside a WSL shell, follow the Ubuntu installation instructions above.
    - Make sure **inbound connections over port 7797 from WSL to Windows** are allowed (e.g. try following this [guide](https://www.nextofwindows.com/allow-server-running-inside-wsl-to-be-accessible-outside-windows-10-host) but for port 7797 instead of 3000).
    - On Windows we recommend that users disable `rift.autostart` in VSCode and run Rift manually as `~/.morph/env/bin/rift` after following the installation instructions below.
- Install Rift. We recommend that you `pip install` Rift in a dedicated Python >=3.10 virtual environment from this repository.
  - Make sure that `which pip` returns a path whose prefix matches the location of a virtual environment, such as the one installed above.
  <!-- - Using `pip` and PyPI: -->
  <!--   - `pip install --upgrade 'pyrift[all]'` -->
  <!--     - `[all]` is required to pull in direct dependencies needed for third-party agents like Aider, Smol Dev, and GPT Engineer. -->
  - using `pip` from GitHub:
    - `pip install "git+https://github.com/morph-labs/rift.git@main#egg=pyrift&subdirectory=rift-engine"`
  - From source:
    - `cd ~/.morph/ && git clone git@github.com:morph-labs/rift && cd ./rift/rift-engine/ && pip install -e .`
      
**Rift VSCode Extension** (via `code --install-extension`, change the executable as needed):
- From the repository root: `cd ./editors/rift-vscode && npm i && bash reinstall.sh`. Make sure your OpenAI API key is set in the VSCode settings (open with `Ctrl + ,` then search for "rift").

## The Road Ahead
<!-- TODO(jesse): rephrase / polish in light of Rift 2.0 -->
Existing code generation tooling is presently mostly code-agnostic, operating at the level of tokens in / tokens out of code LMs. The [language server protocol](https://microsoft.github.io/language-server-protocol/) (LSP) defines a standard for *language servers*, objects which index a codebase and provide structure- and runtime-aware interfaces to external development tools like IDEs.

The Rift Code Engine is an AI-native language server which will expose interfaces for code transformations and code understanding in a uniform, model- and language-agnostic way --- e.g. `rift.summarize_callsites` or `rift.launch_ai_swe_async` should work on a Python codebase with [StarCoder](https://huggingface.co/blog/starcoder) as well as it works on a Rust codebase using [CodeGen](https://github.com/salesforce/CodeGen). Within the language server, models will have full programmatic access to language-specific tooling like compilers, unit and integration test frameworks, and static analyzers to produce correct code with minimal user intervention. We will develop UX idioms as needed to support this functionality in the Rift IDE extensions.

## Contributing
We welcome contributions to Rift at all levels of the stack, for example:
- adding support for new open-source models in the Rift Code Engine
- implementing the Rift API for your favorite programming language
- UX polish in the VSCode extension
- adding support for your favorite editor.

See our [contribution guide](/CONTRIBUTORS.md) for details and guidelines.

Programming is evolving. Join the [community](https://discord.gg/wa5sgWMfqv), contribute to our roadmap, and help shape the future of software.

## Feedback

We'd love to hear your feedback on Rift! Share your thoughts with us [here](https://docs.google.com/forms/d/e/1FAIpQLSd6YXKYqsXI720Q2ZrxjloCfMrO_1MjF7O6ZkvdEMZZqpbmmw/viewform).
