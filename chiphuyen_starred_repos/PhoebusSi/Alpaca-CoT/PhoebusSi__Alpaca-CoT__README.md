# [Alpaca-CoT](https://github.com/PhoebusSi/Alpaca-CoT)

[**中文**](./CN_README.md) | [**English**](./README.md)

<div id="top"></div>

![Alpaca-CoT](./figures/Alpaca-CoT-2.jpg)
# Alpaca-CoT: An Instruction-Tuning Platform with Unified Interface for Instruction Collection, Parameter-efficient Methods, and Large Language Models
[![LICENSE](https://img.shields.io/github/license/PhoebusSi/Alpaca-CoT)](https://github.com/PhoebusSi/Alpaca-CoT/blob/main/LICENSE.txt)
[![torch](https://img.shields.io/badge/pytorch-%3E=1.13-red?logo=pytorch)](https://pytorch.org/)
[![data](https://img.shields.io/badge/huggingface-dataset-yellow?logo=data:image/png;base64,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)](https://huggingface.co/datasets/QingyiSi/Alpaca-CoT)
[![model](https://img.shields.io/badge/huggingface-model-yellow?logo=data:image/png;base64,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)](https://huggingface.co/QingyiSi/Alpaca-CoT)
[![wandb](https://img.shields.io/badge/wandb-tools-orange?logo=WeightsAndBiases)](https://wandb.ai)
[![colab](https://img.shields.io/badge/Google-Colab-blue?logo=Google%20Colab)](https://colab.research.google.com/drive/1wfrKqyPkz5BGD1Gkij_cvbUeweIDdRav?usp=sharing)


This is the repository for the `Alpaca-CoT` project, which aims to build an instruction finetuning (IFT) platform with extensive instruction collection (especially the CoT datasets) and a unified interface for various large language models and parameter-efficient methods.  We are constantly expanding our [instruction-tuning data collection](https://huggingface.co/datasets/QingyiSi/Alpaca-CoT/), and integrating more LLMs and more parameter-efficient methods. In addition, we created a new branch [`tabular_llm`](https://github.com/PhoebusSi/Alpaca-CoT/tree/tabular_llm) to build a Tabular LLM for solving Table Intelligence Tasks.

You are warmly welcome to provide us with any non-collected instruction-tuning datasets (or their sources). We will uniformly format them, train the Alpaca model (and other LLMs in the early future) with these datasets, open source the [model checkpoints](https://huggingface.co/QingyiSi/Alpaca-CoT/tree/main), and conduct extensive empirical studies. We hope that our project can make a modest contribution to the open-source process of large language models, and reduce its threshold for NLP researchers to get started.

<img src="./figures/wechat.jpg" width = "100" height = "100" align=right />
You can also choose to join our group chat (WeChat) and communicate with more people with the same interests. At present, the number of group members is too large to join the group directly through the group QR code. You need to connect with me first to get into the group.

## News
-  ⚠ If you want to use other methods besides LORA, please install the edited version in our project `pip install -e ./peft`.

-  🚀12.8: LLM `InternLM` was merged.
-  🚀8.16: `4bit quantization` is available for `lora`, `qlora` and `adalora`.  
-  🚀8.16: Parameter-efficient methods `Qlora`, `Sequential adapter` and `Parallel adapter` was merged.  
-  🚀7.24: LLM `ChatGLM v2` was merged.
-  🚀7.20: LLM `Baichuan` was merged.
-  6.25: Add model evaluation code, including belle and MMCU.
<details><summary> - more </summary>
<p>
    
-  5.20: fixes bugs in model saving and add wandb support.
-  5.15: more datasets like `GPT4Tools`, `Auto CoT`, `pCLUE` are add.
-  🚀5.5: A new branch [`tabular_llm`](https://github.com/PhoebusSi/Alpaca-CoT/tree/tabular_llm) is created to build a Tabular LLM. We collect instruction fine-tuning data for table-related tasks like table question answering and use them to fine-tune LLMs in this repo.
-  🚀5.4: All parameter-efficient methods in PEFT (e.g., p-tuning) were merged, which can be set by hyper-parameter directly.
-  🚀5.4: LLM `MOSS` was merged.
-  4.21: Datasets `GAOKAO`, `camel`, `FLAN-Muffin`, `COIG` are collected and formatted.
-  4.15: Datasets `webGPT`, `dolly`, `baize`, `hh-rlhf`, `OIG(part)` are collected and formatted.
-  4.12: Now you can try Alpaca-CoT on <a href="https://colab.research.google.com/drive/1wfrKqyPkz5BGD1Gkij_cvbUeweIDdRav?usp=sharing" >Google Colab</a>.
-  4.11: Added function `multi-turn conversation` by [@paulcx](https://github.com/paulcx).
-  4.9: Datasets `firefly`, `instruct`, `Code Alpaca` are collected and formatted, which can be found [here](https://huggingface.co/datasets/QingyiSi/Alpaca-CoT/tree/main).
-  4.7: Added functions `Parameter merging`, `Local chatting`, `Batch predicting` and `Web service building` by [@weberr](https://github.com/weberrr).
-  4.4: Datasets `GPTeacher`,`Guanaco`,`HC3`,`prosocial-dialog`, `belle-chat&belle-math`, `xP3` and `natural-instructions` are collected and formatted.
-  4.3: The Chinese CoT dataset `CoT_CN_data.json` can be found [here](https://huggingface.co/datasets/QingyiSi/Alpaca-CoT/tree/main).
  
</p>
</details> 

## Overview

![img](./figures/platform-en.png)


[LLaMA](https://arxiv.org/abs/2302.13971v1) [1] is a great work that demonstrates the amazing zero-shot and few-shot ability. It significantly reduces the cost of training, finetuning, and using competitive large language models, i.e., LLaMA-13B outperforms GPT-3(175B) and LLaMA-65B is competitive with PaLM-540B. Recently, to boost the instruction-following ability of LLaMA, [Stanford Alpaca](https://github.com/tatsu-lab/stanford_alpaca) [2] finetuned LLaMA-7B on 52K instruction-following data generated by the [Self-Instruct](https://arxiv.org/abs/2212.10560) [3] techniques. However, at present, the LLM research community still faces three challenges: 1. Even LLaMA-7b still has high requirements for computing resources; 2. There are few open source datasets for instruction finetuning; and 3. There is a lack of empirical study on the impact of various types of instruction on model abilities, such as the ability to respond to Chinese instruction and the CoT reasoning.

To this end, we propose this project, which leverages various improvements that were subsequently proposed, with the following advantages:
- 1. This repo contains code, modified from [here](https://github.com/tloen/alpaca-lora) and [here](https://github.com/huggingface/peft), that can **_finetune LLaMA cheaply and efficiently_** (without performance degradation compared to Stanford Alpaca) by using [low-rank adaptation (LoRA)](https://arxiv.org/pdf/2106.09685.pdf) [4], [PEFT](https://github.com/huggingface/peft) and [bitsandbytes](https://github.com/TimDettmers/bitsandbytes). The `7b`, `13b` and `30b` versions of LLaMA models can be easily trained on a single 80G A100.
- 2. The models published in this repo significantly **_improve the CoT (reasoning) capability_**.
- 3. The models published in this repo significantly **_improve the ability to follow Chinese instructions_**.
- 4. This repo contains **_a [collection of instruction-finetuning datasets](https://huggingface.co/datasets/QingyiSi/Alpaca-CoT) that are continuously collected_**, which so far include English, Chinese and CoT instructions. In addition, a collection of checkpoints trained with various instruction datasets is also provided.
- 5. This repo  **_integrates multiple LLMs and unifies their interfaces_**, It can be easily switched through hyperparameters. Currently, it includes **LLaMA**, **ChatGLM**[5], **Bloom**[6] and **MOSS**, and more will continue to be added in the future for researchers to easily invoke and compare different LLMs.
- 6. This repo  **_integrates multiple parameter-efficient methods and unifies their interfaces_**, It can be easily switched through hyperparameters. Currently, it includes **LoRA**, **P-tuning**[5], **adalora** and **prefix tuning**, and more will continue to be added in the future for researchers to easily invoke and compare different parameter-efficient methods.
- 7. This repo contains **_extensive empirical studies and qualitative analysis_**, which may provide valuable findings and promote the exploration of LLM in the future.


**To the best of our knowledge, this work is the first to study _CoT reasoning_ based on LLaMA and Alpaca.** Therefore, we abbreviate our work to `Alpaca-CoT`.

## Data Collection

The relative size of collected datasets can be shown by this graph:

![img](./figures/show.png)


Referring to [this](https://github.com/yaodongC/awesome-instruction-dataset) ([@yaodongC](https://github.com/yaodongC)), we labeled each collected dataset according to the following rules:

(Lang)Lingual-Tags:
- EN: Instruction datasets in English
- CN: Instruction datasets in Chinese
- ML: [Multi-lingual] Instruction datasets in multiple languages

(Task)Task-Tags:
- MT: [Multi-task] Datasets containing multiple tasks
- TS: [Task-specific] Datasets tailored for specific tasks

(Gen)Generation-method:
- HG: [Human Generated Dataset] Datasets created by humans
- SI: [Self-Instruct] Datasets generated using self-instruct methods
- MIX: [Mixed Dataset] Dataset contains both human and machine generated data
- COL: [Collection of Dataset] Dataset made from a collection of other datasets

### Statistics

| Dataset                                                                        | Nums     | Lang         | Task      | Gen        | Type                                                                                                              | Src                                                                            | Url                                                                                             |
| :----------------------------------------------------------------------------- | :------- | :----------- | :-------- | :----------| :---------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------- |
| [Chain of Thought](https://github.com/google-research/FLAN)                    | 74771    | EN/CN        | MT        | HG         | instruct with cot reasoning                                                                                       | annotating CoT on existing data                                                | [download](https://huggingface.co/datasets/QingyiSi/Alpaca-CoT/tree/main/Chain-of-Thought)      |
| [GPT4all](https://github.com/nomic-ai/gpt4all)                                 | 806199   | EN           | MT        | COL        | code, stories and dialogs                                                                                          | distillation from GPT-3.5-turbo                                                | [download](https://huggingface.co/datasets/QingyiSi/Alpaca-CoT/tree/main/GPT4all)               |
| [GPTeacher](https://github.com/teknium1/GPTeacher)                             | 29013    | EN           | MT        | SI         | general, roleplay, toolformer                                                                                     | GPT-4 & toolformer                                                             | [download](https://huggingface.co/datasets/QingyiSi/Alpaca-CoT/tree/main/GPTeacher)             |
| [Guanaco](https://huggingface.co/datasets/JosephusCheung/GuanacoDataset)       | 534610   | ML           | MT        | SI         | various linguistic tasks                                                                                          | text-davinci-003                                                               | [download](https://huggingface.co/datasets/QingyiSi/Alpaca-CoT/tree/main/Guanaco)               |
| [HC3](https://huggingface.co/datasets/Hello-SimpleAI/HC3)                      | 37175    | EN/CN        | TS        | MIX        | dialogue evaluation                                                                                               | human or ChatGPT                                                               | [download](https://huggingface.co/datasets/QingyiSi/Alpaca-CoT/tree/main/HC3)                   |
| [alpaca](https://github.com/tatsu-lab/stanford_alpaca)                         | 52002    | EN           | MT        | SI         | general instruct                                                                                                  | text-davinci-003                                                               | [download](https://huggingface.co/datasets/QingyiSi/Alpaca-CoT/tree/main/alpaca)                |
| [Natural Instructions](https://github.com/allenai/natural-instructions)        | 5040134  | ML           | MT        | COL        | diverse nlp tasks                                                                                                 | human annotated datasets collection                                            | [download](https://huggingface.co/datasets/QingyiSi/Alpaca-CoT/tree/main/Natural-Instructions)  |
| [belle_cn](https://huggingface.co/BelleGroup)                                  | 1079517  | CN           | TS/MT     | SI         | general, mathematical reasoning, dialogue                                                                         | text-davinci-003                                                               | [download](https://huggingface.co/datasets/QingyiSi/Alpaca-CoT/tree/main/belle_cn)              |
| [instinwild](https://github.com/XueFuzhao/InstructionWild)                     | 52191    | EN/CN        | MT        | SI         | generation, open-qa, mind-storm                                                                                   | text-davinci-003                                                               | [download](https://huggingface.co/datasets/QingyiSi/Alpaca-CoT/tree/main/instinwild)            |
| [prosocial dialog](https://huggingface.co/datasets/allenai/prosocial-dialog)   | 165681   | EN           | TS        | MIX        | dialogue                                                                                                          | GPT-3 rewrites questions + humans feedback manually                            | [download](https://huggingface.co/datasets/QingyiSi/Alpaca-CoT/tree/main/prosocial-dialog)      |
| [finance_en](https://huggingface.co/datasets/gbharti/finance-alpaca)           | 68912    | EN           | TS        | COL        | financial related qa                                                                                              | GPT3.5                                                                         | [download](https://huggingface.co/datasets/QingyiSi/Alpaca-CoT/tree/main/)                      |
| [xP3](https://huggingface.co/datasets/bigscience/xP3)                          | 78883588 | ML           | MT        | COL        | a collection of prompts & datasets across 46 of languages & 16 NLP tasks                                          | human annotated datasets collection                                            | [download](https://huggingface.co/datasets/QingyiSi/Alpaca-CoT/tree/main/xP3)                   |
| [firefly](https://github.com/yangjianxin1/Firefly)                             | 1649398  | CN           | MT        | COL        | 23 nlp tasks                                                                                                      | human annotated datasets collection                                            | [download](https://huggingface.co/datasets/QingyiSi/Alpaca-CoT/tree/main/firefly)               |
| [instruct](https://huggingface.co/datasets/swype/instruct)                     | 888969   | EN           | MT        | COL        | augmented of GPT4All, Alpaca, open-source Meta datasets                                                           | augmentation performed using the advanced NLP tools provided by AllenAI        | [download](https://huggingface.co/datasets/QingyiSi/Alpaca-CoT/tree/main/instruct)              |
| [Code Alpaca](https://github.com/sahil280114/codealpaca)                       | 20022    | EN           | TS        | SI         | code generation, editing, optimization                                                                            | text-davinci-003                                                               | [download](https://huggingface.co/datasets/QingyiSi/Alpaca-CoT/tree/main/CodeAlpaca)            |
| [Alpaca_GPT4](https://github.com/Instruction-Tuning-with-GPT-4/GPT-4-LLM)      | 52002    | EN/CN        | MT        | SI         | general instruct                                                                                                  | generated by GPT-4 using Alpaca                                                | [download](https://huggingface.co/datasets/QingyiSi/Alpaca-CoT/tree/main/alpacaGPT4)            |
| [webGPT](https://huggingface.co/datasets/openai/webgpt_comparisons)            | 18994    | EN           | TS        | MIX        | information retrieval (IR) QA                                                                                     | fine-tuned GPT-3, each instruction has two outputs, select better one          | [download](https://huggingface.co/datasets/QingyiSi/Alpaca-CoT/tree/main/webGPT)                |
| [dolly 2.0](https://github.com/databrickslabs/dolly)                           | 15015    | EN           | TS        | HG         | closed QA , summarization and etc, Wikipedia as references                                                        | human annotated                                                                | [download](https://huggingface.co/datasets/QingyiSi/Alpaca-CoT/tree/main/dolly)                 |
| [baize](https://github.com/project-baize/baize-chatbot)                        | 653699   | EN           | MT        | COL        | a collection from Alpaca, Quora, StackOverFlow and MedQuAD questions                                              | human annotated datasets collection                                            | [download](https://huggingface.co/datasets/QingyiSi/Alpaca-CoT/tree/main/baize)                 |
| [hh-rlhf](https://github.com/anthropics/hh-rlhf)                               | 284517   | EN           | TS        | MIX        | dialogue                                                                                                          | dialog between human and RLHF models                                           | [download](https://huggingface.co/datasets/QingyiSi/Alpaca-CoT/tree/main/hh-rlhf)               |
| [OIG(part)](https://laion.ai/blog/oig-dataset/)                                | 49237    | EN           | MT        | COL        | created from various tasks, such as question and answering                                                        | using data augmentation, human annotated datasets collection                   | [download](https://huggingface.co/datasets/QingyiSi/Alpaca-CoT/tree/main/OIG)                   |
| [GAOKAO](https://github.com/OpenLMLab/GAOKAO-Bench)                            | 2785     | CN           | MT        | COL        | Multiple-choice, Fill-in-the-blank and Open-ended questions from examination                                      | human annotated                                                                | [download](https://huggingface.co/datasets/QingyiSi/Alpaca-CoT/tree/main/GAOKAO)                |
| [camel](https://github.com/lightaime/camel)                                    | 760620   | EN           | MT        | SI         | Role-Playing conversations in AI Society, Code, Math, Physics, Chemistry, Biolog                                  | gpt-3.5-turbo                                                                  | [download](https://huggingface.co/datasets/QingyiSi/Alpaca-CoT/tree/main/camel)                 |
| [FLAN-Muffin](https://huggingface.co/datasets/Muennighoff/flan)                | 1764800  | EN           | MT        | COL        | 60 nlp tasks                                                                                                      | human annotated datasets collection                                            | [download](https://huggingface.co/datasets/QingyiSi/Alpaca-CoT/tree/main/FLAN-Muffin)           |
| [COIG(FlagInstruct)](https://huggingface.co/datasets/BAAI/COIG)                | 298428   | CN           | MT        | COL        | collect fron Exam, Translated, Human Value Alignment Instructions and Counterfactural Correction Multi-round Chat | using automatic tool and manual verification                                   | [download](https://huggingface.co/datasets/QingyiSi/Alpaca-CoT/tree/main/COIG)                  |
| [GPT4Tools](https://github.com/StevenGrove/GPT4Tools)                          | 71446    | EN           | MT        | SI         | a collection of tool-related instructions                                                                         | gpt-3.5-turbo                                                                  | [download](https://huggingface.co/datasets/QingyiSi/Alpaca-CoT/tree/main/gpt4tools)             |
| [ShareChat](https://huggingface.co/datasets/RyokoAI/ShareGPT52K)               | 1663241  | EN           | MT        | MIX        | general instruct                                                                                                  | crowdsourcing to collect conversations between people and ChatGPT (ShareGPT)   | [download](https://huggingface.co/datasets/QingyiSi/Alpaca-CoT/tree/main/ShareGPT)              |
| [Auto CoT](https://github.com/amazon-science/auto-cot)                         | 5816     | EN           | MT        | COL        | arithmetic, commonsense, symbolic, and other logical reasoning tasks                                              | human annotated datasets collection                                            | [download](https://huggingface.co/datasets/QingyiSi/Alpaca-CoT/tree/main/Auto-CoT)              |
| [MOSS](https://github.com/OpenLMLab/MOSS)                                      | 1583595  | EN/CN        | TS        | SI         | general instruct                                                                                                  | text-davinci-003                                                               | [download](https://huggingface.co/datasets/QingyiSi/Alpaca-CoT/tree/main/MOSS)                  |
| [ultrachat](https://github.com/thunlp/UltraChat)                               | 28247446 | EN           |           |            | Questions about the World, Writing and Creation, Assistance on Existent Materials                                 | two separate gpt-3.5-turbo                                                     | [download](https://huggingface.co/datasets/QingyiSi/Alpaca-CoT/tree/main/ultrachat)             |
| [Chinese-medical](https://github.com/Toyhom/Chinese-medical-dialogue-data)     | 792099   | CN           | TS        | COL        | Questions about medical advice                                                                                    | crawl                                                                          | [download](https://huggingface.co/datasets/QingyiSi/Alpaca-CoT/tree/main/Chinese-medical)       |
| [CSL](https://github.com/ydli-ai/csl)                                          | 396206   | CN           | MT        | COL        | paper text generation, keyword extraction, text summarization and text classification                             | crawl                                                                          | [download](https://huggingface.co/datasets/QingyiSi/Alpaca-CoT/tree/main/CSL)                   |
| [pCLUE](https://github.com/CLUEbenchmark/pCLUE)                                | 1200705  | CN           | MT        | COL        | general instruct                                                                                                  |                                                                                | [download](https://huggingface.co/datasets/QingyiSi/Alpaca-CoT/tree/main/pCLUE)                 |
| [news_commentary](https://huggingface.co/datasets/P01son/instructions)         | 252776   | CN           | TS        | COL        | translate                                                                                                         |                                                                                | [download](https://huggingface.co/datasets/QingyiSi/Alpaca-CoT/tree/main/news_commentary)       |
| [StackLLaMA](https://huggingface.co/datasets/lvwerra/stack-exchange-paired)    | todo     | EN           |           |            |                                                                                                                   |                                                                                |                                                                                                 |




### Download
You can download all the formatted data [here](https://huggingface.co/datasets/QingyiSi/Alpaca-CoT/tree/main). Then you should put them in the [data](https://github.com/PhoebusSi/alpaca-CoT/tree/main/data) folder.

You can download all checkpoints trained on various types of instruction data from [here](https://huggingface.co/QingyiSi/Alpaca-CoT/tree/main). Then, after setting `LoRA_WEIGHTS` (in `generate.py`) to the local path, you can directly execute the model inference.


### Data Formatting
All data in our collection is formatted into the same templates, where each sample is as follows:
```
[
{"instruction": instruction string,
"input": input string, # (may be empty)
"output": output string}
]
```
Note that, for CoT datasets, we first use the [template](https://github.com/google-research/FLAN/blob/main/flan/v2/templates.py) provided by FLAN to change the original dataset into various Chain-of-Thoughts forms, and then convert it to the above format. The formatting script can be found [here](https://github.com/PhoebusSi/alpaca-CoT/blob/main/data/origin_cot_data/formating.py).


## Multi-interface Unified Platform
### Setup
```
pip install -r requirements.txt
```
Note that, make sure python>=3.9 when finetuning ChatGLM.

**PEFT**
* if you want to use other methods besides LORA, please install the edited version in our project
```
pip install -e ./peft
```


### Instruction Finetuning
In order for researchers to conduct systematic IFT research on LLMs, we have collected different types of instruction data, integrated multiple LLMs, and unified interfaces, making it easy to customize the desired collocation:
- `--model_type` : Set the LLM you want to use. Currently, [llama, chatglm, bloom, moss] are supported. The latter two have strong Chinese capabilities, and more LLMs will be integrated in the future.
- `--peft_type`: Set the PEFT you want to use. Currently, [lora, adalora, prefix tuning, p tuning, prompt] are supported.
- `--data`: Set the data type used for IFT to flexibly tailor the desired command compliance ability. For example, for strong reasoning ability, set "alpaca-cot", for strong Chinese ability, set "belle1.5m", for coding and story generation ability, set "gpt4all", and for financial related response ability, set "finance".
- `--model_name_or_path`: This is set to load different versions of the model weights for the target LLM  `--model_type`. For example, to load the llama's 13b version of weights, you can set decapoda-research/llama-13b-hf.

**Single GPU**
- for LLaMA
```
python3 uniform_finetune.py --model_type llama --model_name_or_path decapoda-research/llama-7b-hf \
    --data alpaca-belle-cot --lora_target_modules q_proj v_proj \
    --per_gpu_train_batch_size 4 --learning_rate 3e-4 --epochs 1
```

Note: for multiple datasets, you can use `--data` like `--data ./data/alpaca.json ./data/finance.json <path2yourdata_1>`

- for ChatGLM
```
python3 uniform_finetune.py   --model_type chatglm --model_name_or_path THUDM/chatglm-6b \
    --data alpaca-belle-cot --lora_target_modules query_key_value \
    --lora_r 32 --lora_alpha 32 --lora_dropout 0.1 --per_gpu_train_batch_size 2 \
    --learning_rate 2e-5 --epochs 1
```
Note that `load_in_8bit` is not yet suitable for ChatGLM, so batch_size must be smaller than others.

- for BLOOM
```
python3 uniform_finetune.py   --model_type bloom --model_name_or_path bigscience/bloomz-7b1-mt \
    --data alpaca-belle-cot --lora_target_modules query_key_value \
    --per_gpu_train_batch_size 4 --learning_rate 3e-4 --epochs 1
```

- for MOSS
```
python3 uniform_finetune.py   ---model_type moss --model_name_or_path fnlp/moss-moon-003-sft  \
    --data alpaca --lora_target_modules q_proj v_proj --per_gpu_train_batch_size 1 \
    --learning_rate 3e-4 --epochs 3
```

- for InternLM
```
python3 uniform_finetune.py   --model_type internlm --model_name_or_path internlm/internlm-7b \
    --data alpaca --lora_target_modules q_proj v_proj --lora_r 32 --lora_alpha 32 \
    --lora_dropout 0.1 --per_gpu_train_batch_size 1 --learning_rate 2e-5 --epochs 1 \
    --compute_dtype="fp32"
```

Note that you can also pass the local path (where LLM weights saved) to `--model_name_or_path`. And the data type `--data` can be freely set according to your interests.

**Multiple GPUs**
``` bash
torchrun --nnodes 1 --nproc_per_node $ngpu uniform_finetune.py $args --data $data 
```

- for LLaMA
```
python3 -m torch.distributed.launch --nproc_per_node 4  \
    --nnodes=1 --node_rank=0 --master_addr=xxx --master_port=yyy uniform_finetune.py \
    --model_type llama --model_name_or_path decapoda-research/llama-7b-hf \
    --data alpaca-belle-cot --lora_target_modules q_proj v_proj \
    --per_gpu_train_batch_size 4 --learning_rate 3e-4 --epochs 1
```
- for ChatGLM
```
python3 -m torch.distributed.launch --nproc_per_node 4  \
    --nnodes=1 --node_rank=0 --master_addr=xxx --master_port=yyy \
    uniform_finetune.py   --model_type chatglm --model_name_or_path THUDM/chatglm-6b \
    --data alpaca-belle-cot --lora_target_modules query_key_value \
    --lora_r 32 --lora_alpha 32 --lora_dropout 0.1 --per_gpu_train_batch_size 2 \
    --learning_rate 2e-5 --epochs 1
```
Note that `load_in_8bit` is not yet suitable for ChatGLM, so batch_size must be smaller than others.

- for BLOOM
```
python3 -m torch.distributed.launch --nproc_per_node 4  \
    --nnodes=1 --node_rank=0 --master_addr=xxx --master_port=yyy \
    uniform_finetune.py   --model_type bloom --model_name_or_path bigscience/bloomz-7b1-mt \
    --data alpaca-belle-cot --lora_target_modules query_key_value \
    --per_gpu_train_batch_size 4 --learning_rate 3e-4 --epochs 1
```

- for InternLM
```
python3 -m torch.distributed.launch --nproc_per_node 4  \
    --nnodes=1 --node_rank=0 --master_addr=xxx --master_port=yyy \
    uniform_finetune.py   --model_type internlm --model_name_or_path internlm/internlm-7b \
    --data alpaca --lora_target_modules q_proj v_proj --lora_r 32 --lora_alpha 32 \
    --lora_dropout 0.1 --per_gpu_train_batch_size 1 --learning_rate 2e-5 --epochs 1 \
    --compute_dtype="fp32"
```



### Inference
```
python3 generate.py  --data alpaca-belle-cot --model_type llama

python3 generate.py  --data alpaca-belle-cot --model_type chatglm

python3 generate.py  --data alpaca-belle-cot --model_type bloom

```
More details of instruction finetuing and inference can be found [here](https://github.com/tloen/alpaca-lora) where we modified from. Note that the folders `saved-xxx7b` are the save path for LoRA weights, and LLaMA weights are automatically downloaded from Hugging Face.


### Inference Hyper-parameter Explanation
```
top_p=0.9,
        #Moderately increase the probability threshold of nucleus sampling to increase the quantity of candidate tokens and increase generation diversity.

temperature=1.0,
        #The previous low temperature parameter could lead to a severe polarization in the probability distribution of generated words, which degenerates the generation strategy into greedy decoding.

do_sample=True,
        #do_sample parameter is set to False by default. After setting to True, the generation methods turn into beam-search multinomial sampling decoding strategy.

no_repeat_ngram_size=6,
        #Configure the probability of the next repeating n-gram to 0, to ensure that there are no n-grams appearing twice. This setting is an empirical preliminary exploration.

repetition_penalty=1.8,
        #For words that have appeared before, in the subsequent prediction process, we reduce the probability of their reoccurrence by introducing the repetition_penalty parameter. This setting is an empirical preliminary exploration.
```


### Parameter merging
```
python3 merge.py --model_type llama --size 7b --lora_dir xxx --merged_dir yyy
```

### Local chatting
```
python3 server.py --model_type chatglm --size 6b --lora_dir xxx
```
### Batch predicting
```
python3 predict.py --model_type chatglm --size 6b --data for_dict_data --lora_dir xxx --result_dir yyy
```

### Web service building

```
python3 web.py --model_type chatglm --size 6b --lora_dir xxx
```

## Empirical Study of Instruction-tuning Open LLMs in Chinese (As of June 25th)
<details><summary>Note: The following experimental results are all obtained from ___An Empirical Study of Instruction-tuning Large Language Models in Chinese___.</summary>
<p>

### 1. Benchmarks
This paper selects two evaluation benchmarks, Belle-eval and MMCU, to comprehensively evaluate LLM competencies in Chinese.

Belle-eval is constructed by self-instruct with ChatGPT, which has 1,000 diverse instructions that involve 10 categories covering common NLP tasks (e.g., QA) and challenging tasks (e.g., code and math). We use ChatGPT to rate the model responses based on the golden answers. This benchmark is considered to be as the assessment of AGI (instruction-following) capability.

MMCU is a collection of Chinese multiple choice questions in four professional disciplines of medicine, law, psychology and education (e.g., Gaokao examination). It allows LLMs to take exams in human society in a multiple-choice test manner, making it suitable for evaluating the breadth and depth of knowledge of LLMs across multiple disciplines. 

<p align="center">
    <img src="./figures/chinesellms-benchmarks.png" width="35%">
</p>

Data statistics of Belle-eval and MMCU are shown in the table above.

### 2. Main Factors
We conduct experiments to study the three main factors in instruction-tuning LLMs: LLM bases, Parameter-efficient Methods, Chinese Instruction Datasets.

#### 2.1 LLM Bases
For open LLMs, we test existing LLMs and LLMs fine-tuned with LoRA on Alpaca-GPT4 on Belle-eval and MMCU, respectively.


   <p align="center">
    <img src="./figures/chinesellms-llms1.png" width="80%">
    <img src="./figures/chinesellms-llms2.png" width="40%">
</p>

Table 2 shows the scores of open LLMs on Belle-eval. Table 3 shows the accuracy of LLMs on MMCU. They fine-tune all the open LLMs with the same parameter-efficient method LoRA and the same instruction dataset Alpaca-GPT4. 

___Experimental Results:___
1. Evaluation of Existing LLMs


    ___Performance on Belle-eval___

    (1) For base LLMs, Bloom performs the best.

    (2) For sft LLMs, ChatGLM outperforms others by large margins, thanks to the fact that it is trained with the most Chinese tokens and HFRL.

    (3) The Open QA, Math, CloseQA and Extract categories are still very challenging for existing open LLMs.

    (4) Vicuna and moss-sft have clear improvements compared to their bases, LLaMA and moss-base, respectively.

    (5) In contrast, the performance of sft models, Bloomz and Bloomz-mt, is reduced compared to the base model Bloom, because they tend to generate a shorter response.

    ___Performance on MMCU___

    (1) All base LLMs perform poorly because it is almost difficult to generate content in the specified format before fine-tuning, e.g., outputting option numbers.

    (2) All sft LLMs outperform their corresponding base LLMs, respectively. In particular, Bloomz performs the best (even beats ChatGLM) because it can generate option number directly as required without generating other irrelevant content, which is also due to the data characteristics of its supervised fine-tuning dataset xP3.

    (3) Among the four disciplines, law is the most challenging for LLMs.



   <p align="center">
    <img src="./figures/chinesellms-llms3.png" width="40%">
</p>

The performance results of LLMs after instruction-tuning on Alpaca-GPT4-zh are shown in Figure 1.

2. Instruction-tuning Different LLMs



    (1) On Belle-eval, the performance improvement of sft LLMs brought by instruction-tuning is not as significant as that of base LLMs, except for sft Bloomz and Bloomz-mt.

    (2) Vicuna and ChatGLM encounter performance drops after instruction-tuning, because Vicuna is trained from real human-ChatGPT conversations, with better quality than Alpaca-GPT4. ChatGLM adopts HFRL, which may be no longer suitable for further instruction-tuning. 

    (3) On MMCU, most LLMs achieve performance boosts after instruction-tuning, with the exception of Bloomz and Bloomz-mt, which have unexpectedly significantly decreased performance.

    (4) After instruction-tuning, Bloom has significant improvements and performs well on both benchmarks. Although ChatGLM beats Bloom consistently, it suffers performance drop during instruction-tuning. Therefore, among all open LLMs, Bloom is most suitable as a foundation model in the subsequent experiments for Chinese instruction-tuning exploration.

#### 2.2 Parameter-efficient Methods
For parameter-efficient methods other than LoRA, the paper collects a range of parameter-efficient methods to instruction-tune Bloom on the Alpaca-GPT4 dataset.

<p align="center">
    <img src="./figures/chinesellms-para1.png" width="40%">
    <img src="./figures/chinesellms-para2.png" width="40%">
</p>

___Experimental Results:___

1. Comparison of Parameter-efficient Methods

    (1) SadapterH performs the best among all parameter-efficient methods, which can be used as an alternative to LoRA.

    (2) P-tuning and prompt-tuning underperform others by large margins, indicating that only adding trainable layers in the embedding layer are not enough to support LLMs for generation tasks. 

    (3) Although AdaLoRA is an improvement of LoRA, its performance has a clear drop, possibly because the LoRA's trainable parameters for LLMs are not suitable for further reduction. 

    (4) Comparing the upper and lower parts, it can be seen that increasing the number of trainable parameters for sequential adapters (i.e., SadapterP and SadapterH) does not bring gain, while the opposite phenomenon is observed for parallel adapters(i.e., P-adapter)

2. Training Loss

    (1) Prompt-tuning and P-tuning converge the slowest and has the highest losses after convergence. This shows that embedding-only adapters are not suitable for instruction-tuning LLMs. 

    (2) The initial loss of AdaLoRA is very high because it requires simultaneous learning of parameter budget allocation, which makes the model unable to fit the training data well. 

    (3) The other methods can quickly converge on training data and fit it well.

#### 2.3 Chinese instruction Datasets
For the impact of various types of Chinese instruction datasets, authors gather popular open Chinese instructions (as shown in Table 5) to fine-tune Bloom with LoRA.

<p align="center">
    <img src="./figures/chinesellms-data1.png" width="80%">
    <img src="./figures/chinesellms-data2.png" width="80%">
    <img src="./figures/chinesellms-data3.png" width="40%">
</p>

Table 6 and Table 7 show Bloom's fine-tuning on different instruction datasets.

___Experimental Results:___

1. Performance on Belle-eval

    (1) the instruction data constructed by ChatGPT (e.g., using self-instruction methods or collecting real human-ChatGPT conversations) consistently enhances the instruction-following ability with 3.1 ∼ 11-point score increases. 

    (2) Among these datasets, Belle has the best performance due to the largest amount of instruction data. However, the performance of models trained on moss-sft-data, containing more data built in a similar way, is unsatisfactory.

    (3) The performance brought by the Alpaca-GPT4 instructions is the second best, with only 49K being comparable to the 1.54M Belle.

    (4) Instinwild brings the least performance gains among them because the seed instructions it crawls from Tweet ("in wild") are not as comprehensive as those (like Alpaca) carefully designed by humans.

    (5) These ChatGPT-based data mainly have a significant improvement effect on open generation tasks such as Brain Storm and Generation, while there is a significant decrease in tasks that require high reading comprehension skills, such as Close QA and Extract.

    (6) These instruction datasets cause damage to the model's instruction-following ability, because the form and intent of each NLP or examination dataset are unitary, which can easily be overfitted. 

    (7) Among them, COIG-trans performs the best because it involves over 2000 different tasks with a wide variety of task instructions. In contrast, xP3 and COIG-ccmc have the worst negative impact on model performance. Both of them only cover a few types of tasks (translation and QA for the former, counterfactual correction conversations for the latter), which hardly cover the popular instructions and tasks for humans.

2. Performance on MMCU

    (1) Instruction-tuning on each dataset can always result in performance improvement. 

    (2) Among the ChatGPT-based data shown in the upper part, ShareGPT-zh underperforms others by large margins. This may be due to the fact that real users rarely ask multiple choice questions about academic topics. 

    (3) Among the dataset-collection data shown in the lower part, HC3 and COIG-ccmc results in the lowest accuracy because the unique questions of HC3 are only 13K, and the task format of COIG-ccmc is significantly different from MMCU. 
    
    (4) COIG-exam brings the greatest accuracy improvement, benefiting from the similar task format as MMCU.

### 3. Other Factors
Four Other Factors: CoT, Expansion of Chinese Vocabulary, Language of Prompts and Human-value Alignment

#### 3.1 CoT
For CoT, authors compare the performance before and after adding CoT data during instruction-tuning.

___Experiment Settings:___

We collect 9 CoT datasets and their prompts from FLAN, and then translate them into Chinese using Google Translate. They compare the performance before and after adding CoT data during instruction-tuning.

First note the way to add CoT data as "Alpaca-GPT4+CoT". In addition, add a sentence "先思考，再决定" ("think step by step" in Chinese) at the end of each instruction, to induce the model to respond to instructions based on the CoT, and label this way as "Alpaca-GPT4+CoT*".

<p align="center">
    <img src="./figures/chinesellms-cot.png" width="40%">
</p>

___Experimental Results:___ 

1. "Alpaca-GPT4+CoT" outperforms "Alpaca-GPT4" in Code and Math tasks that require strong reasoning ability. Besides, there is also a significant improvement in the MMCU Education task.

2. As shown in the line of "Alpaca-GPT4+CoT*", the simple sentence can further improve the performance of reasoning tasks Code and Education, while the Math performance is slightly inferior to "Alpaca-GPT4+CoT". This may require further exploring of more robust prompts.

#### 3.2 Expansion of Chinese Vocabulary
For expansion of Chinese vocabulary, authors test the influence of the number of Chinese tokens in the tokenizer’s vocabulary on LLMs’ ability to express Chinese. For example, if a Chinese character is in the vocabulary, it can be represented by a single token, otherwise it may require multiple tokens to represent it.

___Experiment Settings:___ Authors mainly conduct experiments on LLaMA, which uses SentencePiece(32K vocabulary size of Chinese characters) covering fewer Chinese characters than Bloom(250K).

<p align="center">
    <img src="./figures/chinesellms-voc.png" width="45%">
</p>

___Experimental Results:___

1. Pre-training on more Chinese corpus with expansion of Chinese vocabulary is consistently helpful for instruction-following ability.

2. And counterintuitively, "llama-voc-pre-l" (100B) is inferior to "llama-voc-pre" (20B) on MMCU, which shows that pre-training on more data may not necessarily lead to higher performance for academic exams.

#### 3.3 Language of Prompts

For the language of prompts, authors test the suitability of instruction fine-tuning for using Chinese prompts.

<p align="center">
    <img src="./figures/chinesellms-lan.png" width="60%">
</p>

Figure 4 shows the results of using Chinese and English prompts based on LLaMA and Bloom.  When instruction-tuning LLaMA, using Chinese prompts can improve the performance on both benchmarks compared to English prompts, while the opposite phenomenon can be observed on Bloom.

___Experimental Results:___

1. For models with weaker Chinese abilities(e.g., LLaMA), using Chinese prompts can effectively help respond in Chinese.

2. For models with good Chinese abilities (e.g., Bloom), using prompts in English (the language they are better at) can better guide the model to understand the process of fine-tuning with instructions.

#### 3.4 Human-value Alignment
To avoid LLMs generating toxic content, aligning them with human values is a crucial issue. We add human-value alignment data built by COIG into instruction-tuning to explore its impact. 

<p align="center">
    <img src="./figures/chinesellms-human.png" width="30%">
</p>

Figure 5 compares the results of instruction-tuning with and without human-value alignment.

___Experimental Results:___ The human-value alignment results in a slight performance drop. How to balance the harmlessness and performance of LLMs is a research direction worth exploring in the future.


</p>
</details> 

## Quantitative Analysis
<details><summary>Note: The following figure shows the statistics of the dataset collected as of March 26, which is only displayed as a motivation of data collection. More datasets have been collected, such as financial related instruction datasets.</summary>
<p>

![data collection statistics](./figures/piechart.png)
The current collection of instruction-finetuning datasets consists mainly of three parts:
- `alpaca_data_cleaned.json`: about 52K English instruction-following training samples.
- `CoT_data.json`: 9 CoT datasets involving about 75k samples. (published by FLAN[7])
- `belle_data_cn.json`:  about 0.5M Chinese |instruction-following training samples. (published by BELLE [8])

### Ablation of CoT and Chinese Instructions


![ablation-cot](./figures/ablation-cot.png)
"w/o CoT" and "w/o CN" denote models that exclude CoT data and Chinese instructions from their instruction finetuning data, respectively.

The above table shows two examples (involving with numerical calculations) that require a certain amount of reasoning ability to respond correctly.
As shown in the middle column, `Ours w/o CoT` fails to generate the correct response, which shows that once the finetuning data does not contain CoT data, the model's reasoning ability significantly decreases. This further demonstrates that CoT data is essential for LLM models.

![ablation-cot](./figures/ablation-cn.png)

The above table shows two examples that require the ability to respond to Chinese instructions.
As shown in the right column, either the generated content of `Ours w/o CN` is unreasonable, or the Chinese instructions are answered in English by `Ours w/o CN`. This shows that removing Chinese data during finetuning will cause the model to be unable to handle Chinese instructions, and further demonstrates the need to collect Chinese instruction finetuning data.


![ablation-cot](./figures/ablation-both.png)

The above table shows a relatively difficult example, which requires both a certain accumulation of knowledge of Chinese history and a logical and complete ability to state historical events. As shown in this table, `Ours w/o CN` can only generate a short and erroneous response, because due to the lack of Chinese finetuning data, the corresponding knowledge of Chinese history is naturally lacking.  Although `Ours w/o CoT` lists some relevant Chinese historical events, its logic of expression is self-contradictory, which is caused by the lack of CoT data.
`

**In summary, the models finetuned from our complete dataset (English, Chinese, and CoT instruction data) can significantly improve model reasoning and Chinese instruction following abilities.**

### The Effect of CoT Data

![CoT-comparison](./figures/CoT-comparison.png)
Samples of each odd number of rows do not apply the CoT prompt, such as "step-by-step reasoning." Both `Ours(w/CoT)` and Alpaca are based on LLaMA-7B, and the only difference between them two is that the instruction-finetuning data of `Ours(w/CoT)` has a extra CoT data than that of Alpaca.

From the above table, we find that:
- `Ours(w/CoT)` always generates the correct rationale before the answer, while Alpaca fails to generate any reasonable rationale, as shown in the first 4 examples (commonsense questions). This shows that using CoT data for finetuning can significantly improve reasoning ability.
- For `Ours(w/CoT)`, the CoT prompt (e.g., concatenate 'step-by-step' with the input question) has little effect on easy examples (e.g., commonsense questions) and has an important effect on challenging questions (e.g., questions requiring reasoning, like the last four examples).
- For Alpaca, CoT prompt always has little effect or even negative impact. For the last two examples, after adding CoT prompt, Aplpaca changes the correct generated answer to the wrong one. This may be due to the inconsistency between the input forms of finetuning and inference.


### The Effect of Chinese Instruction Data

_Quantitative comparison of responses to Chinese instructions._
![CN_compare_CN](./figures/CN-compareCN.png)

Our model is finetuned from a 7B LLaMA on 52K English instructions and 0.5M Chinese instructions. Stanford Alpaca (our reimplementation) is finetuned from a 7B LLaMA on 52K English instructions. BELLE is finetuned from a 7B BLOOM on 2B Chinese instructions.

From the above table, several observations can be found:
- Compared to Alpaca, `ours (w/ CN)` has a stronger ability to understand Chinese instructions. For the first example, Alpaca fails to distinguish between the `instruction` part and `input` part, while we do.
- Chinese instruction finetuning data can significant enhance the ability to interact in Chinese. For the second example, `ours (w/ CN)` not only provides the correct code, but also provides the corresponding Chinese annotation, while Alpaca does not. In addition, as shown in the 3-5 examples, Alpaca can only respond to Chinese instruction with an English response.
- Compared to BELLE, `ours (w/ CN)`'s performance on instructions requiring an open response (as shown in last two examples) still needs to be improved. BELLE's outstanding performance against such instructions is due to: 1. Its BLOOM backbone model encounters much more multilingual data during pre-training; 2. Its Chinese instruction finetuning data is more than ours, that is, 2M vs 0.5M.



 _Quantitative comparison of responses to English instructions. The purpose of this subsection is to explore whether finetuning on Chinese instructions has a negative impact on Alpaca._
![CN_compare_EN](./figures/CN_compareEN.png)


From the above table, we find that:
- Finetuning with Chinese instruction data does not weaken the original English instruction–following ability, on the contrary, there is also a certain enhancement in generating a better response to English instructions. The response of `ours (w/ CN)` shows more detail than that of Alpaca, e.g. for the third example, `ours (w/ CN)` list three more provinces than Alpaca.

</p>
</details> 




## Citation
Please cite the repo if you use the data collection, code, and experimental findings in this repo.
```
@misc{si2023empirical,
      title={An Empirical Study of Instruction-tuning Large Language Models in Chinese}, 
      author={Qingyi Si and Tong Wang and Zheng Lin and Xu Zhang and Yanan Cao and Weiping Wang},
      year={2023},
      eprint={2310.07328},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```
For data and models, please cite the original data, parameter-efficient methods and LLMs source as well.

We would like to express our special gratitude to APUS AilMe Lab for sponsoring the 8 A100 GPUs for the experiments.


<p align="right">(<a href="#top">back to top</a>)</p>

## All Thanks To Our Contributors 

<a href="https://github.com/PhoebusSi/Alpaca-CoT/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=PhoebusSi/Alpaca-CoT" />
</a>
