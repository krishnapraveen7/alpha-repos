# h2oGPT

Turn ★ into ⭐ (top-right corner) if you like the project!

Query and summarize your documents or just chat with local private GPT LLMs using h2oGPT, an Apache V2 open-source project.

- **Private** offline database of any documents [(PDFs, Excel, Word, Images, Video Frames, YouTube, Audio, Code, Text, MarkDown, etc.)](docs/README_LangChain.md#supported-datatypes)
  - **Persistent** database (Chroma, Weaviate, or in-memory FAISS) using accurate embeddings (instructor-large, all-MiniLM-L6-v2, etc.)
  - **Efficient** use of context using instruct-tuned LLMs (no need for LangChain's few-shot approach)
  - **Parallel** summarization and extraction, reaching an output of 80 tokens per second with the 13B LLaMa2 model
  - **HYDE** (Hypothetical Document Embeddings) for enhanced retrieval based upon LLM responses
  - **Semantic Chunking** for better document splitting (requires GPU)
- **Variety** of models supported (LLaMa2, Mistral, Falcon, Vicuna, WizardLM.  With AutoGPTQ, 4-bit/8-bit, LORA, etc.)
  - **GPU** support from HF and LLaMa.cpp GGML models, and **CPU** support using HF, LLaMa.cpp, and GPT4ALL models
  - **Attention Sinks** for [arbitrarily long](https://github.com/tomaarsen/attention_sinks) generation (LLaMa-2, Mistral, MPT, Pythia, Falcon, etc.)
- **UI** or CLI with streaming of all models
  - **Upload** and **View** documents through the UI (control multiple collaborative or personal collections)
  - **Vision Models** LLaVa, Claude-3, Gemini-Pro-Vision, GPT-4-Vision
  - **Image Generation** Stable Diffusion (sdxl-turbo, sdxl, SD3) and PlaygroundAI (playv2)
  - **Voice STT** using Whisper with streaming audio conversion
  - **Voice TTS** using MIT-Licensed Microsoft Speech T5 with multiple voices and Streaming audio conversion
  - **Voice TTS** using MPL2-Licensed TTS including Voice Cloning and Streaming audio conversion
  - **AI Assistant Voice Control Mode** for hands-free control of h2oGPT chat
  - **Bake-off** UI mode against many models at the same time
  - **Easy Download** of model artifacts and control over models like LLaMa.cpp through the UI
  - **Authentication** in the UI by user/password via Native or Google OAuth
  - **State Preservation** in the UI by user/password
- **Linux, Docker, macOS, and Windows** support
  - [**Easy Windows Installer**](#windows-1011-64-bit-with-full-document-qa-capability) for Windows 10 64-bit (CPU/CUDA)
  - [**Easy macOS Installer**](#macos-cpum1m2-with-full-document-qa-capability) for macOS (CPU/M1/M2)
- **Inference Servers** [support](docs/README_InferenceServers.md) for oLLaMa, HF TGI server, vLLM, Gradio, ExLLaMa, Replicate, Together.ai, OpenAI, Azure OpenAI, Anthropic, MistralAI, Google, and Groq
- **OpenAI-compliant**
  - Server Proxy [API](docs/README_CLIENT.md) (h2oGPT acts as drop-in-replacement to OpenAI server)
  - Supports Chat and Text Completions (streaming and non-streaming), Audio Transcription (STT), Audio Generation (TTS), Image Generation, and Embedding
- **JSON Mode** with any model via code block extraction.  Also supports MistralAI JSON mode, Claude-3 via function calling with strict Schema, OpenAI via JSON mode, and vLLM via guided_json with strict Schema  
- **Web-Search** integration with Chat and Document Q/A
- **Agents** for Search, Document Q/A, Python Code, CSV frames (Experimental, best with OpenAI currently)
- **Open Web UI** with h2oGPT as backend via OpenAI Proxy
  - Supports chat completion with streaming, document Q/A, STT, TTS, and image generation.  See [Start-up Docs](docs/FAQ.md#open-web-ui).
- **Evaluate** performance using reward models
- **Quality** maintained with over 1000 unit and integration tests taking over 4 GPU-hours

### Get Started

[![GitHub license](https://img.shields.io/github/license/NVIDIA/nvidia-docker?style=flat-square)](https://raw.githubusercontent.com/h2oai/h2ogpt/main/LICENSE)
[![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)](https://github.com/h2oai/h2ogpt/blob/main/docs/README_LINUX.md)
[![macOS](https://img.shields.io/badge/mac%20os-000000?style=for-the-badge&logo=macos&logoColor=F0F0F0)](https://github.com/h2oai/h2ogpt/blob/main/docs/README_MACOS.md)
[![Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)](https://github.com/h2oai/h2ogpt/blob/main/docs/README_WINDOWS.md)
[![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)](https://github.com/h2oai/h2ogpt/blob/main/docs/README_DOCKER.md)

#### Limited Doc Q/A trial

To quickly try out h2oGPT with limited document Q/A capability, create a fresh Python 3.10 environment and run:
* CPU or MAC (M1/M2):
   ```bash
   # for windows/mac use "set" or relevant environment setting mechanism
   export PIP_EXTRA_INDEX_URL="https://download.pytorch.org/whl/cpu"
   ```
* Linux/Windows CPU/CUDA/ROC:
   ```bash
   # for windows/mac use "set" or relevant environment setting mechanism
   export PIP_EXTRA_INDEX_URL="https://download.pytorch.org/whl/cu121 https://huggingface.github.io/autogptq-index/whl/cu121"
   # for cu118 use export PIP_EXTRA_INDEX_URL="https://download.pytorch.org/whl/cu118 https://huggingface.github.io/autogptq-index/whl/cu118"
   ```
Then choose your llama_cpp_python options, by changing `CMAKE_ARGS` to whichever system you have according to [llama_cpp_python backend documentation](https://github.com/abetlen/llama-cpp-python?tab=readme-ov-file#supported-backends).
E.g. CUDA on Linux:
```bash
export LLAMA_CUBLAS=1
export CMAKE_ARGS="-DLLAMA_CUBLAS=on -DCMAKE_CUDA_ARCHITECTURES=all"
export FORCE_CMAKE=1
```
Note for some reason things will fail with llama_cpp_python if don't add all cuda arches, and building with all those arches does take some time.
Windows CUDA:
```cmdline
set CMAKE_ARGS=-DLLAMA_CUBLAS=on -DCMAKE_CUDA_ARCHITECTURES=all
set LLAMA_CUBLAS=1
set FORCE_CMAKE=1
```
Note for some reason things will fail with llama_cpp_python if don't add all cuda arches, and building with all those arches does take some time.
Metal M1/M2:
```bash
export CMAKE_ARGS="-DLLAMA_METAL=on"
export FORCE_CMAKE=1
```

#### Chat with h2oGPT

```bash
Then run the following commands on any system:
   ```bash
   git clone https://github.com/h2oai/h2ogpt.git
   cd h2ogpt
   pip install -r requirements.txt
   pip install -r reqs_optional/requirements_optional_langchain.txt

   pip uninstall llama_cpp_python llama_cpp_python_cuda -y
   pip install -r reqs_optional/requirements_optional_llamacpp_gpt4all.txt --no-cache-dir

   pip install -r reqs_optional/requirements_optional_langchain.urls.txt
   # GPL, only run next line if that is ok:
   pip install -r reqs_optional/requirements_optional_langchain.gpllike.txt

   # choose up to 32768 if have enough GPU memory:
   python generate.py --base_model=TheBloke/Mistral-7B-Instruct-v0.2-GGUF --prompt_type=mistral --max_seq_len=4096
   ```
Next, go to your browser by visiting [http://127.0.0.1:7860](http://127.0.0.1:7860) or [http://localhost:7860](http://localhost:7860).  Choose 13B for a better model than 7B.

#### Chat template based GGUF models

For newer chat template models, a `--prompt_type` is not required on CLI, but for GGUF files one should pass the HF tokenizer so it knows the chat template, e.g. for LLaMa-3:
```bash
python generate.py --base_model=llama --model_path_llama=https://huggingface.co/QuantFactory/Meta-Llama-3-8B-Instruct-GGUF/resolve/main/Meta-Llama-3-8B-Instruct.Q5_K_M.gguf?download=true --tokenizer_base_model=meta-llama/Meta-Llama-3-8B-Instruct --max_seq_len=8192
```
Or for Phi:
```bash
python generate.py  --tokenizer_base_model=microsoft/Phi-3-mini-4k-instruct --base_model=llama --llama_cpp_model=https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-gguf/resolve/main/Phi-3-mini-4k-instruct-q4.gguf --max_seq_len=4096 
```
the `--llama_cpp_path` could be a local path as well if you already downloaded it, or we will also check the `llamacpp_path` for the file.

See [Offline](docs/README_offline.md#tldr) for how to run h2oGPT offline.

---

Note that for all platforms, some packages such as DocTR, Unstructured, Florence-2, Stable Diffusion, etc. download models at runtime that appear to delay operations in the UI. The progress appears in the console logs.

#### Windows 10/11 64-bit with full document Q/A capability
  * One-Click Installer
    * CPU or GPU: Download [h2oGPT Windows Installer](https://h2o-release.s3.amazonaws.com/h2ogpt/Jan2024/h2oGPT_0.0.1.exe) (1.3GB file)
      * Once installed, feel free to change start directory for icon from `%HOMEDRIVE%\%HOMEPATH%` to (e.g.) `%HOMEDRIVE%\%HOMEPATH%\h2ogpt_data` so all created files (like database) go there.  All paths saved are relative to this path.
    * CPU: Click the h2oGPT icon in the Start menu.  Give it about 15 seconds to open in a browser if many optional packages are included.  By default, the browser will launch with the actual local IP address, not localhost.
    * GPU: Before starting, run the following commands (replace `pseud` with your user):
      ```
      C:\Users\pseud\AppData\Local\Programs\h2oGPT\Python\python.exe -m pip uninstall -y torch
      C:\Users\pseud\AppData\Local\Programs\h2oGPT\Python\python.exe -m pip install https://h2o-release.s3.amazonaws.com/h2ogpt/torch-2.1.2%2Bcu118-cp310-cp310-win_amd64.whl
      ```
      Now click the h2oGPT icon in the Start menu.  Give it about 20 seconds to open in a browser if many optional packages are included.  By default, the browser will launch with the actual local IP address, not localhost.
      * Some other users may have python located here: `C:\Program Files (x86)\h2oGPT\Python\python.exe`.
    * To debug any issues, run the following (replace `pseud` with your user):
      ```
      C:\Users\pseud\AppData\Local\Programs\h2oGPT\Python\python.exe "C:\Users\pseud\AppData\Local\Programs\h2oGPT\h2oGPT.launch.pyw"
      ```
      Any start-up exceptions are appended to log, e.g. `C:\Users\pseud\h2ogpt_exception.log`.
  * To control startup, tweak the python startup file, e.g. for user `pseud`: `C:\Users\pseud\AppData\Local\Programs\h2oGPT\pkgs\win_run_app.py`
    * In this Python code, set ENVs anywhere before main_h2ogpt() is called
      * E.g. `os.environ['name'] = 'value'`, e.g. `os.environ['n_jobs'] = '10'` (must be always a string).
    * Environment variables can be changed, e.g.:
      * `n_jobs`: number of cores for various tasks
      * `OMP_NUM_THREADS` thread count for LLaMa
      * `CUDA_VISIBLE_DEVICES` which GPUs are used.  Recommend set to single fast GPU, e.g. `CUDA_VISIBLE_DEVICES=0` if have multiple GPUs.  Note that UI cannot control which GPUs (or CPU mode) for LLaMa models.
      * Any CLI argument from `python generate.py --help` with environment variable set as `h2ogpt_x`, e.g. `h2ogpt_h2ocolors` to `False`.
      * Set env `h2ogpt_server_name` to actual IP address for LAN to see app, e.g. `h2ogpt_server_name` to `192.168.1.172` and allow access through firewall if have Windows Defender activated.
  * One can tweak installed h2oGPT code at, e.g. `C:\Users\pseud\AppData\Local\Programs\h2oGPT`.
  * To terminate the app, go to System Tab and click Admin and click Shutdown h2oGPT.
    * If startup fails, run as console and check for errors, e.g. and kill any old Python processes.

  * [Full Windows 10/11 Manual Installation Script](docs/README_WINDOWS.md)
    * Single `.bat` file for installation (if you do not skip any optional packages, takes about 9GB filled on disk).
    * Recommend base Conda env, which allows for DocTR that requires pygobject that has otherwise no support (except `mysys2` that cannot be used by h2oGPT).
    * Also allows for the TTS package by Coqui, which is otherwise not currently enabled in the one-click installer.

---

#### Linux (CPU/CUDA) with full document Q/A capability
  * [Docker Build and Run Docs](docs/README_DOCKER.md)
  * [Linux Manual Install and Run Docs](docs/README_LINUX.md)

---

#### macOS (CPU/M1/M2) with full document Q/A capability
* One-click Installers (Experimental and subject to changes, we haven't tested each and every feature with these installers, we encourage the community to try them and report any issues)

  Mar 07, 2024
  - [h2ogpt-osx-m1-cpu](https://h2o-release.s3.amazonaws.com/h2ogpt/Mar2024/h2ogpt-osx-m1-cpu)
  - [h2ogpt-osx-m1-gpu](https://h2o-release.s3.amazonaws.com/h2ogpt/Mar2024/h2ogpt-osx-m1-gpu)
  
  Nov 08, 2023
  - [h2ogpt-osx-m1-cpu](https://h2o-release.s3.amazonaws.com/h2ogpt/Nov2023/h2ogpt-osx-m1-cpu)
  - [h2ogpt-osx-m1-gpu](https://h2o-release.s3.amazonaws.com/h2ogpt/Nov2023/h2ogpt-osx-m1-gpu)
  
  Download the runnable file and open it from the Finder. It will take a few minutes to unpack and run the application.
  These one-click installers are experimental. Report any issues with steps to reproduce at https://github.com/h2oai/h2ogpt/issues.

  **Note:** The app bundle is unsigned. If you experience any issues with running the app, run the following commands:
  ```bash
  $ xattr -dr com.apple.quarantine {file-path}/h2ogpt-osx-m1-gpu
  $ chmod +x {file-path}/h2ogpt-osx-m1-gpu
  ```
* [macOS Manual Install and Run Docs](docs/README_MACOS.md)

---

### Live Demos
- [![img-small.png](docs/img-small.png) Live h2oGPT Document Q/A Demo](https://gpt.h2o.ai/)
- [🤗 Live h2oGPT Chat Demo 1](https://huggingface.co/spaces/h2oai/h2ogpt-chatbot)
- [🤗 Live h2oGPT Chat Demo 2](https://huggingface.co/spaces/h2oai/h2ogpt-chatbot2)
- [![](https://colab.research.google.com/assets/colab-badge.svg) h2oGPT CPU](https://colab.research.google.com/drive/13RiBdAFZ6xqDwDKfW6BG_-tXfXiqPNQe?usp=sharing)
- [![](https://colab.research.google.com/assets/colab-badge.svg) h2oGPT GPU](https://colab.research.google.com/drive/143-KFHs2iCqXTQLI2pFCDiR69z0dR8iE?usp=sharing)

### Resources
- [Discord](https://discord.gg/WKhYMWcVbq)
- [Models (LLaMa-2, Falcon 40, etc.) at 🤗](https://huggingface.co/h2oai/)
- [YouTube: 100% Offline ChatGPT Alternative?](https://www.youtube.com/watch?v=Coj72EzmX20)
- [YouTube: Ultimate Open-Source LLM Showdown (6 Models Tested) - Surprising Results!](https://www.youtube.com/watch?v=FTm5C_vV_EY)
- [YouTube: Blazing Fast Falcon 40b 🚀 Uncensored, Open-Source, Fully Hosted, Chat With Your Docs](https://www.youtube.com/watch?v=H8Dx-iUY49s)
- [Technical Paper: https://arxiv.org/pdf/2306.08161.pdf](https://arxiv.org/pdf/2306.08161.pdf)

### Partners

- [Live Leaderboard](https://evalgpt.ai/) for GPT-4 Elo Evaluation of Instruct/Chat models with [h2o-LLM-eval](https://github.com/h2oai/h2o-LLM-eval).
- Advanced fine-tuning with [H2O LLM Studio](https://github.com/h2oai/h2o-llmstudio)

### Video Demo

https://github.com/h2oai/h2ogpt/assets/2249614/2f805035-2c85-42fb-807f-fd0bca79abc6

YouTube 4K version: https://www.youtube.com/watch?v=_iktbj4obAI

### Docs Guide
<!--  cat README.md | ./gh-md-toc  -  But Help is heavily processed -->
* [Get Started](#get-started)
   * [Linux (CPU or CUDA)](docs/README_LINUX.md)
   * [macOS (CPU or M1/M2)](docs/README_MACOS.md)
   * [Windows 10/11 (CPU or CUDA)](docs/README_WINDOWS.md)
   * [GPU (CUDA, AutoGPTQ, exllama) Running Details](docs/README_GPU.md)
   * [CPU Running Details](docs/README_CPU.md)
   * [CLI chat](docs/README_CLI.md)
   * [Gradio UI](docs/README_ui.md)
   * [Client API (Gradio, OpenAI-Compliant)](docs/README_CLIENT.md)
   * [Inference Servers (oLLaMa, HF TGI server, vLLM, Groq, Anthropic, Google, Mistral, Gradio, ExLLaMa, Replicate, OpenAI, Azure OpenAI)](docs/README_InferenceServers.md)
   * [Build Python Wheel](docs/README_WHEEL.md)
   * [Offline Installation](docs/README_offline.md)
   * [Low Memory](docs/FAQ.md#low-memory-mode)
   * [Docker](docs/README_DOCKER.md)
* [LangChain Document Support](docs/README_LangChain.md)
* [Compare to PrivateGPT et al.](docs/README_LangChain.md#what-is-h2ogpts-langchain-integration-like)
* [Roadmap](#roadmap)
* [Development](#development)
* [Help](#help)
   * [LangChain file types supported](docs/README_LangChain.md#supported-datatypes)
   * [CLI Database control](docs/README_LangChain.md#database-creation)
   * [FAQ](docs/FAQ.md)
     * [Model Usage Notes](docs/FAQ.md#model-usage-notes)
     * [Adding LLM Models (including using GGUF and Attention Sinks)](docs/FAQ.md#adding-models)
     * [Adding Embedding Models](docs/FAQ.md#add-new-embedding-model)
     * [Adding Prompts](docs/FAQ.md#adding-prompt-templates)
     * [In-Context Learning](docs/FAQ.md#in-context-learning-via-prompt-engineering)
     * [Multiple GPUs](docs/FAQ.md#multiple-gpus)
     * [Low-Memory Usage](docs/FAQ.md#low-memory-mode)
     * [Environment Variables](docs/FAQ.md#what-envs-can-i-pass-to-control-h2ogpt)
     * [HTTPS access for server and client](docs/FAQ.md#https-access-for-server-and-client)
   * [Useful Links](docs/LINKS.md)
   * [Fine-Tuning](docs/FINETUNE.md)
   * [Triton](docs/TRITON.md)
   * [Commercial viability](docs/FAQ.md#commercial-viability)
* [Acknowledgements](#acknowledgements)
* [Why H2O.ai?](#why-h2oai)
* [Disclaimer](#disclaimer)

### Experimental features

These are not part of normal installation instructions and are experimental.

* [Agents](docs/README_Agents.md) -- in Alpha testing.  Optimal for OpenAI, but that also fails sometimes.

### Roadmap

- Complement h2oGPT chatbot with other APIs like [ToolBench](https://github.com/OpenBMB/ToolBench), Wolfram Alpha, Semantic Scholar, etc.
- Enhance h2oGPT with reliable agentic control

### Development

- To create a development environment for training and generation, follow the [installation instructions](docs/INSTALL.md).
- To fine-tune any LLM models on your data, follow the [fine-tuning instructions](docs/FINETUNE.md).
- To run h2oGPT tests:
    ```bash
    pip install requirements-parser pytest-instafail pytest-random-order playsound==1.3.0
    conda install -c conda-forge gst-python -y
    sudo apt-get install gstreamer-1.0
    pip install pygame
    GPT_H2O_AI=0 CONCURRENCY_COUNT=1 pytest --instafail -s -v tests
    # for openai server test on already-running local server
    pytest -s -v -n 4 openai_server/test_openai_server.py::test_openai_client
    ```
  or tweak/run `tests/test4gpus.sh` to run tests in parallel.

### Help

- [FAQs](docs/FAQ.md)

- [README for LangChain](docs/README_LangChain.md)

- Useful [links](docs/LINKS.md) for additional context and information on competitors, models, and datasets

### Inference Benchmarks for Summarization & Generation

* [Benchmark results for Llama2](https://github.com/h2oai/h2ogpt/blob/main/benchmarks/perf.md)
* [pytest to create benchmark results](https://github.com/h2oai/h2ogpt/blob/main/tests/test_perf_benchmarks.py)
* [Raw benchmark results (JSON)](https://github.com/h2oai/h2ogpt/blob/main/benchmarks/perf.json)

### Acknowledgements

* Some training code was based upon March 24 version of [Alpaca-LoRA](https://github.com/tloen/alpaca-lora/).
* Used high-quality created data by [OpenAssistant](https://open-assistant.io/).
* Used base models by [EleutherAI](https://www.eleuther.ai/).
* Used OIG data created by [LAION](https://laion.ai/blog/oig-dataset/).

### Why H2O.ai?

Our [Makers](https://h2o.ai/company/team/) at [H2O.ai](https://h2o.ai) have built several world-class Machine Learning, Deep Learning and AI platforms:
- #1 open-source machine learning platform for the enterprise [H2O-3](https://github.com/h2oai/h2o-3)
- The world's best AutoML (Automatic Machine Learning) with [H2O Driverless AI](https://h2o.ai/platform/ai-cloud/make/h2o-driverless-ai/)
- No-Code Deep Learning with [H2O Hydrogen Torch](https://h2o.ai/platform/ai-cloud/make/hydrogen-torch/)
- Document Processing with Deep Learning in [Document AI](https://h2o.ai/platform/ai-cloud/make/document-ai/)

We also built platforms for deployment and monitoring, and for data wrangling and governance:
- [H2O MLOps](https://h2o.ai/platform/ai-cloud/operate/h2o-mlops/) to deploy and monitor models at scale
- [H2O Feature Store](https://h2o.ai/platform/ai-cloud/make/feature-store/) in collaboration with AT&T
- Open-source Low-Code AI App Development Frameworks [Wave](https://wave.h2o.ai/) and [Nitro](https://nitro.h2o.ai/)
- Open-source Python [datatable](https://github.com/h2oai/datatable/) (the engine for H2O Driverless AI feature engineering)

Many of our customers are creating models and deploying them enterprise-wide and at scale in the [H2O AI Cloud](https://h2o.ai/platform/ai-cloud/):
- Multi-Cloud or on Premises
- [Managed Cloud (SaaS)](https://h2o.ai/platform/ai-cloud/managed)
- [Hybrid Cloud](https://h2o.ai/platform/ai-cloud/hybrid)
- [AI Appstore](https://docs.h2o.ai/h2o-ai-cloud/)

We are proud to have over 25 (of the world's 280) [Kaggle Grandmasters](https://h2o.ai/company/team/kaggle-grandmasters/) call H2O home, including three Kaggle Grandmasters who have made it to world #1.

### Disclaimer

Please read this disclaimer carefully before using the large language model provided in this repository. Your use of the model signifies your agreement to the following terms and conditions.

- Biases and Offensiveness: The large language model is trained on a diverse range of internet text data, which may contain biased, racist, offensive, or otherwise inappropriate content. By using this model, you acknowledge and accept that the generated content may sometimes exhibit biases or produce content that is offensive or inappropriate. The developers of this repository do not endorse, support, or promote any such content or viewpoints.
- Limitations: The large language model is an AI-based tool and not a human. It may produce incorrect, nonsensical, or irrelevant responses. It is the user's responsibility to critically evaluate the generated content and use it at their discretion.
- Use at Your Own Risk: Users of this large language model must assume full responsibility for any consequences that may arise from their use of the tool. The developers and contributors of this repository shall not be held liable for any damages, losses, or harm resulting from the use or misuse of the provided model.
- Ethical Considerations: Users are encouraged to use the large language model responsibly and ethically. By using this model, you agree not to use it for purposes that promote hate speech, discrimination, harassment, or any form of illegal or harmful activities.
- Reporting Issues: If you encounter any biased, offensive, or otherwise inappropriate content generated by the large language model, please report it to the repository maintainers through the provided channels. Your feedback will help improve the model and mitigate potential issues.
- Changes to this Disclaimer: The developers of this repository reserve the right to modify or update this disclaimer at any time without prior notice. It is the user's responsibility to periodically review the disclaimer to stay informed about any changes.

By using the large language model provided in this repository, you agree to accept and comply with the terms and conditions outlined in this disclaimer. If you do not agree with any part of this disclaimer, you should refrain from using the model and any content generated by it.

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=h2oai/h2ogpt&type=Timeline)](https://star-history.com/#h2oai/h2ogpt&Timeline)
