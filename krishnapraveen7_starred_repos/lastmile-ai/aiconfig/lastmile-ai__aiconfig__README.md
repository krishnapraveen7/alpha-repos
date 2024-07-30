<div align="center"><picture>
  <img alt="aiconfig" src="aiconfig-docs/static/img/readme_small_logo.png" width="200"/>
</picture></div>
<br/>

<p align="center">
    <b>AIConfig - the open-source framework for building production-grade AI applications</b> <br />
</p>

<p align="center">
  <a href="https://github.com/lastmile-ai/aiconfig/actions/workflows/main_python.yml"><img src="https://github.com/lastmile-ai/aiconfig/actions/workflows/main_python.yml/badge.svg" alt="Python"></a>&nbsp;
  <a href="https://github.com/lastmile-ai/aiconfig/actions/workflows/main-typescript.yml"><img src="https://github.com/lastmile-ai/aiconfig/actions/workflows/main-typescript.yml/badge.svg" alt="Node"></a>&nbsp;
  <a href="https://github.com/lastmile-ai/aiconfig/actions/workflows/test-deploy-docs.yml"><img src="https://github.com/lastmile-ai/aiconfig/actions/workflows/test-deploy-docs.yml/badge.svg" alt="Docs"></a>&nbsp;
  <a href="https://discord.com/invite/xBhNKTetGx"><img src="https://img.shields.io/badge/Discord-LastMile%20AI-Blue?color=rgb(37%2C%20150%2C%20190)" alt="Discord"></a>
  <br>
  <a href="https://aiconfig.lastmileai.dev/"><strong>Documentation</strong></a>
</p>

AIConfig is a framework that makes it easy to build generative AI applications for production. It manages generative AI prompts, models and model parameters as JSON-serializable configs that can be version controlled, evaluated, monitored and opened in a local editor for rapid prototyping.

It allows you to store and iterate on generative AI behavior _separately from your application code_, offering a streamlined AI development workflow.

<div align="center"><picture>
  <img alt="aiconfig" src="aiconfig-docs/static/img/aiconfig_dataflow.png" width="500"/>
</picture></div>

**[More context here](#why-is-this-important).**

## Quickstart

For VS Code Users:

- Install the [AIConfig Editor VS Code Extension](https://marketplace.visualstudio.com/items?itemName=lastmile-ai.vscode-aiconfig)

If you're not using VS Code, follow these steps:

1. `pip3 install python-aiconfig`
2. `export OPENAI_API_KEY='your-key'`
3. `aiconfig edit`

## Getting Started Tutorial

Check out the full [Getting Started tutorial](https://aiconfig.lastmileai.dev/docs/getting-started/).

### Install

```bash
# for python installation:
pip3 install python-aiconfig
# or using poetry: poetry add python-aiconfig

# for node.js installation:
npm install aiconfig
# or using yarn: yarn add aiconfig
```

**Note:** You need to install the python AIConfig package to use AIConfig Editor to create and iterate on prompts even if you plan to use the Node SDK to interact with your aiconfig in your application code.

You must specify your [OpenAI API Key](https://platform.openai.com/account/api-keys). Open your Terminal and add this line, replacing ‘your-api-key-here’ with your API key: `export OPENAI_API_KEY='your-api-key-here'`.

### Open AIConfig Editor in VS Code

[AIConfig Editor](https://marketplace.visualstudio.com/items?itemName=lastmile-ai.vscode-aiconfig) helps you visually create and edit the prompts and model parameters stored as AIConfigs.

1. Install the [AIConfig Editor for VS Code](https://marketplace.visualstudio.com/items?itemName=lastmile-ai.vscode-aiconfig)
2. Open the `travel.aiconfig.json` file in VS Code. This will automatically open the AIConfig Editor in VS Code.

### Run Prompts in the Editor

With AIConfig Editor, you can create and run prompts with complex chaining and variables. The editor auto-saves every 15 seconds and you can manually save with the Save button. Your updates will be reflected in the AIConfig JSON file. See this example of a prompt chain created with the editor:

<div align="center"><picture>
  <img alt="aiconfig" src="https://github.com/lastmile-ai/aiconfig/assets/129882602/1dff39d5-d7fc-40f5-8143-22173dac713f" width="800"/>
</picture></div>

<br>

**Corresponding AIConfig JSON file:**

<details style="border: 1px solid #e8e8e8; padding: 10px; border-radius: 10px;">
<summary style="cursor: pointer; color: #ffffff; user-select: none; font-weight: bold; padding:5px 10px">travel.aiconfig.json</summary>
<pre style="font-size: 14px; color: #444;">
<code>
{
  "name": "NYC Trip Planner",
  "description": "Intrepid explorer with ChatGPT and AIConfig",
  "schema_version": "latest",
  "metadata": {
    "models": {
      "gpt-3.5-turbo": {
        "model": "gpt-3.5-turbo",
        "top_p": 1,
        "temperature": 1
      },
      "gpt-4": {
        "model": "gpt-4",
        "max_tokens": 3000
      }
    },
    "default_model": "gpt-3.5-turbo"
  },
  "prompts": [
    {
      "name": "get_activities",
      "input": "Tell me 10 fun attractions to do in NYC."
    },
    {
      "name": "gen_itinerary",
      "input": "Generate an itinerary ordered by {{order_by}} for these activities: {{get_activities.output}}.",
      "metadata": {
        "model": "gpt-4",
        "parameters": {
          "order_by": "geographic location"
        }
      }
    }
  ]
}
</code></pre>
</details>

### Use the AIConfig SDK

You can run the prompts from the aiconfig generated from AIConfig Editor in your application code using either python or Node SDK. We’ve shown the python SDK below.

```python
# load your AIConfig
from aiconfig import AIConfigRuntime, InferenceOptions
import asyncio

config = AIConfigRuntime.load("travel.aiconfig.json")

# setup streaming
inference_options = InferenceOptions(stream=True)

# run a prompt
async def gen_nyc_itinerary():
  gen_itinerary_response = await config.run("gen_itinerary", params = {"order_by" : "location"}, options=inference_options, run_with_dependencies=True)

asyncio.run(gen_nyc_itinerary())

# save the aiconfig to disk and serialize outputs from the model run
config.save('updated_travel.aiconfig.json', include_outputs=True)
```

### Edit your AIConfig

You can quickly iterate and edit your aiconfig using AIConfig Editor.

1. Open your Terminal
2. Run this command: `aiconfig edit --aiconfig-path=travel.aiconfig.json`

A new tab with AIConfig Editor opens in your default browser at http://localhost:8080/ with the prompts, chaining logic, and settings from `travel.aiconfig.json`. The editor auto-saves every 15 seconds and you can manually save with the Save button. Your updates will be reflected in the AIConfig file.

## Why is this important?

Today, application code is tightly coupled with the gen AI settings for the application -- prompts, parameters, and model-specific logic is all jumbled in with app code.

- results in increased complexity
- makes it hard to iterate on the prompts or try different models easily
- makes it hard to evaluate prompt/model performance

AIConfig helps unwind complexity by separating prompts, model parameters, and model-specific logic from your application.

- simplifies application code -- simply call `config.run()`
- open the `aiconfig` in a playground to iterate quickly
- version control and evaluate the `aiconfig` - it's the AI artifact for your application.

## Features

- **Prompts as Configs**: [standardized JSON format](https://aiconfig.lastmileai.dev/docs/overview/ai-config-format) to store prompts and model settings in source control.
- **Editor for Prompts**: Prototype and quickly iterate on your prompts and model settings with [AIConfig Editor](https://aiconfig.lastmileai.dev/docs/editor).
- **Model-agnostic and multimodal SDK**: Python & Node SDKs to use `aiconfig` in your application code. AIConfig is designed to be **model-agnostic** and **multi-modal**, so you can extend it to work with any generative AI model, including text, image and audio.
- **Extensible**: Extend AIConfig to work with any model and your own endpoints.
- **Collaborative Development**: AIConfig enables different people to work on prompts and app development, and collaborate together by sharing the `aiconfig` artifact.

## Use cases

AIConfig makes it easy to work with complex prompt chains, various models, and advanced generative AI workflows. Start with these recipes and access more in [`/cookbooks`](https://github.com/lastmile-ai/aiconfig/tree/main/cookbooks):

- [RAG with AIConfig](https://github.com/lastmile-ai/aiconfig/tree/main/cookbooks/RAG-with-ChromaDB)
- [Function Calling with OpenAI](https://github.com/lastmile-ai/aiconfig/tree/main/cookbooks/Function-Calling-OpenAI)
- [CLI Chatbot](https://github.com/lastmile-ai/aiconfig/tree/main/cookbooks/Wizard-GPT)
- [Prompt Routing](https://github.com/lastmile-ai/aiconfig/tree/main/cookbooks/Basic-Prompt-Routing)
- [Multi-LLM Consistency](https://github.com/lastmile-ai/aiconfig/tree/main/cookbooks/Multi-LLM-Consistency)
- [Safety Guardrails for LLMs - LLama Guard](https://github.com/lastmile-ai/aiconfig/tree/main/cookbooks/LLaMA-Guard)
- [Chain-of-Verification](https://github.com/lastmile-ai/aiconfig/tree/main/cookbooks/Chain-of-Verification)

## Schema

- [AIConfig Schema](https://aiconfig.lastmileai.dev/docs/overview/ai-config-format/)

## Supported Models

AIConfig supports the following models out of the box. See examples:

- [OpenAI models (GPT-3, GPT-3.5, GPT-4, DALLE3)](https://github.com/lastmile-ai/aiconfig/tree/main/cookbooks/Function-Calling-OpenAI)
- [Gemini](https://github.com/lastmile-ai/aiconfig/tree/main/cookbooks/Gemini)
- [LLaMA](https://github.com/lastmile-ai/aiconfig/tree/main/cookbooks/llama)
- [LLaMA Guard](https://github.com/lastmile-ai/aiconfig/tree/main/cookbooks/LLaMA-Guard)
- [Google PaLM models (PaLM chat)](https://github.com/lastmile-ai/aiconfig/tree/main/cookbooks/Multi-LLM-Consistency)
- [Hugging Face Text Generation Task models (Ex. Mistral-7B)](https://github.com/lastmile-ai/aiconfig/tree/main/cookbooks/HuggingFace)

If you need to use a model that isn't provided out of the box, you can implement a `ModelParser` for it.
See [instructions](https://aiconfig.lastmileai.dev/docs/extensibility#1-bring-your-own-model) on how to support a new model in AIConfig.

## Extensibility

AIConfig is designed to be customized and extended for your use-case. The [Extensibility](https://aiconfig.lastmileai.dev/docs/extensibility) guide goes into more detail.

Currently, there are 3 core ways to extend AIConfig:

1. [Supporting other models](https://aiconfig.lastmileai.dev/docs/extensibility#1-bring-your-own-model) - define a ModelParser extension
2. [Callback event handlers](https://aiconfig.lastmileai.dev/docs/extensibility#2-callback-handlers) - tracing and monitoring
3. [Custom metadata](https://aiconfig.lastmileai.dev/docs/extensibility#3-custom-metadata) - save custom fields in `aiconfig`

## Contribute to AIConfig

We are rapidly developing AIConfig! We welcome PR contributions and ideas for how to improve the project.

- [Join the conversation on Discord](https://discord.com/invite/xBhNKTetGx) - `#aiconfig` channel
- [Open an issue for feature requests](https://github.com/lastmile-ai/aiconfig/issues)
- [Read our contributing guide](https://aiconfig.lastmileai.dev/docs/contributing/)

## Latest Updates

We currently release new tagged versions of the `pypi` and `npm` packages every week. Hotfixes go out when completed.

- [Changelog](https://github.com/lastmile-ai/aiconfig/blob/main/CHANGELOG.md): Check out our latest updates.
- [Roadmap](https://aiconfig.lastmileai.dev/docs/roadmap): What we're building next - please feel free to contribute. See our contributing guide [here](<(https://aiconfig.lastmileai.dev/docs/contributing/)>).
