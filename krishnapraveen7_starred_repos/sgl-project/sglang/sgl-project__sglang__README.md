<div align="center">
<img src="assets/logo.png" alt="logo" width="400"></img>
</div>

--------------------------------------------------------------------------------

| [**Blog**](https://lmsys.org/blog/2024-01-17-sglang/) | [**Paper**](https://arxiv.org/abs/2312.07104) |

SGLang is a fast serving framework for large language models and vision language models.
It makes your interaction with models faster and more controllable by co-designing the backend runtime and frontend language.

The core features include:
- **Fast Backend Runtime**: Efficient serving with RadixAttention for prefix caching, jump-forward constrained decoding, continuous batching, token attention (paged attention), tensor parallelism, flashinfer kernels, and quantization (AWQ/FP8/GPTQ/Marlin).
- **Flexible Frontend Language**: Enables easy programming of LLM applications with chained generation calls, advanced prompting, control flow, multiple modalities, parallelism, and external interactions.

## News
- [2024/04] 🔥 SGLang is used by the official **LLaVA-NeXT (video)** release ([blog](https://llava-vl.github.io/blog/2024-04-30-llava-next-video/)).
- [2024/02] 🔥 SGLang enables **3x faster JSON decoding** with compressed finite state machine ([blog](https://lmsys.org/blog/2024-02-05-compressed-fsm/)).
- [2024/01] SGLang provides up to **5x faster inference** with RadixAttention ([blog](https://lmsys.org/blog/2024-01-17-sglang/)).

<details>
<summary>More</summary>

- [2024/01] SGLang powers the serving of the official **LLaVA v1.6** release demo ([usage](https://github.com/haotian-liu/LLaVA?tab=readme-ov-file#demo)).

</details>

## Contents
- [Install](#install)
- [Backend: SGLang Runtime (SRT)](#backend-sglang-runtime-srt)
- [Frontend: Structured Generation Language (SGLang)](#frontend-structured-generation-language-sglang)
- [Benchmark And Performance](#benchmark-and-performance)
- [Roadmap](#roadmap)
- [Citation And Acknowledgment](#citation-and-acknowledgment)

## Install

### Method 1: With pip
```
pip install "sglang[all]"

# Install FlashInfer CUDA kernels
pip install flashinfer -i https://flashinfer.ai/whl/cu121/torch2.3/
```

### Method 2: From source
```
git clone https://github.com/sgl-project/sglang.git
cd sglang

pip install -e "python[all]"

# Install FlashInfer CUDA kernels
pip install flashinfer -i https://flashinfer.ai/whl/cu121/torch2.3/
```

### Method 3: Using docker
The docker images are available on Docker Hub as [lmsysorg/sglang](https://hub.docker.com/r/lmsysorg/sglang/tags).

```bash
docker run --gpus all \
    -p 30000:30000 \
    -v ~/.cache/huggingface:/root/.cache/huggingface \
    --env "HUGGING_FACE_HUB_TOKEN=<secret>" \
    --ipc=host \
    lmsysorg/sglang:latest \
    python3 -m sglang.launch_server --model-path meta-llama/Meta-Llama-3-8B --host 0.0.0.0 --port 30000
```

### Common Notes
- If you see errors from the Triton compiler, please install the [Triton Nightly](https://triton-lang.org/main/getting-started/installation.html) by
```
pip uninstall -y triton triton-nightly
pip install -U --index-url https://aiinfra.pkgs.visualstudio.com/PublicPackages/_packaging/Triton-Nightly/pypi/simple/ triton-nightly
```
- If you cannot install FlashInfer, check out its [installation](https://docs.flashinfer.ai/installation.html#) page. If you still cannot install it, you can use the slower Triton kernels by adding `--disable-flashinfer` when launching the server.
- If you only need to use the OpenAI backend, you can avoid installing other dependencies by using `pip install "sglang[openai]"`.

## Backend: SGLang Runtime (SRT)
The SGLang Runtime (SRT) is an efficient serving engine.

### Quick Start
Launch a server
```
python -m sglang.launch_server --model-path meta-llama/Meta-Llama-3-8B-Instruct --port 30000
```

Send a request
```
curl http://localhost:30000/generate \
  -H "Content-Type: application/json" \
  -d '{
    "text": "Once upon a time,",
    "sampling_params": {
      "max_new_tokens": 16,
      "temperature": 0
    }
  }'
```
Learn more about the argument format [here](docs/sampling_params.md).

### OpenAI Compatible API
In addition, the server supports OpenAI-compatible APIs.

```python
import openai
client = openai.Client(
    base_url="http://127.0.0.1:30000/v1", api_key="EMPTY")

# Text completion
response = client.completions.create(
	model="default",
	prompt="The capital of France is",
	temperature=0,
	max_tokens=32,
)
print(response)

# Chat completion
response = client.chat.completions.create(
    model="default",
    messages=[
        {"role": "system", "content": "You are a helpful AI assistant"},
        {"role": "user", "content": "List 3 countries and their capitals."},
    ],
    temperature=0,
    max_tokens=64,
)
print(response)
```

It supports streaming, vision, and most features of the Chat/Completions/Models endpoints specified by the [OpenAI API Reference](https://platform.openai.com/docs/api-reference/).

### Additional Server Arguments
- Add `--tp 2` to enable tensor parallelism. If it indicates `peer access is not supported between these two devices`, add `--enable-p2p-check` option.
```
python -m sglang.launch_server --model-path meta-llama/Meta-Llama-3-8B-Instruct --port 30000 --tp 2
```
- Add `--dp 2` to enable data parallelism. It can also be used together with tp. Data parallelism is better for throughput if there is enough memory.
```
python -m sglang.launch_server --model-path meta-llama/Meta-Llama-3-8B-Instruct --port 30000 --dp 2 --tp 2
```
- If you see out-of-memory errors during serving, please try to reduce the memory usage of the KV cache pool by setting a smaller value of `--mem-fraction-static`. The default value is `0.9`
```
python -m sglang.launch_server --model-path meta-llama/Meta-Llama-3-8B-Instruct --port 30000 --mem-fraction-static 0.7
```
- See [hyperparameter_tuning.md](docs/hyperparameter_tuning.md) on tuning hyperparameters for better performance.
- Add `--nnodes 2` to run tensor parallelism on multiple nodes. If you have two nodes with two GPUs on each node and want to run TP=4, let `sgl-dev-1` be the hostname of the first node and `50000` be an available port.
```
# Node 0
python -m sglang.launch_server --model-path meta-llama/Meta-Llama-3-8B-Instruct --tp 4 --nccl-init sgl-dev-1:50000 --nnodes 2 --node-rank 0

# Node 1
python -m sglang.launch_server --model-path meta-llama/Meta-Llama-3-8B-Instruct --tp 4 --nccl-init sgl-dev-1:50000 --nnodes 2 --node-rank 1
```
- If the model does not have a template in the Hugging Face tokenizer, you can specify a [custom chat template](docs/custom_chat_template.md).

### Supported Models

- Llama / Llama 2 / Llama 3
- Mistral / Mixtral
- Gemma / Gemma 2
- Qwen / Qwen 2 / Qwen 2 MoE
- LLaVA 1.5 / 1.6
  - `python -m sglang.launch_server --model-path liuhaotian/llava-v1.5-7b --tokenizer-path llava-hf/llava-1.5-7b-hf --chat-template vicuna_v1.1 --port 30000`
  - `python -m sglang.launch_server --model-path liuhaotian/llava-v1.6-vicuna-7b --tokenizer-path llava-hf/llava-1.5-7b-hf --chat-template vicuna_v1.1 --port 30000`
  - `python -m sglang.launch_server --model-path liuhaotian/llava-v1.6-34b --tokenizer-path liuhaotian/llava-v1.6-34b-tokenizer --port 30000`
- LLaVA-NeXT-Video
  - see [examples/usage/llava_video](examples/usage/llava_video)
- Yi-VL
  - see [srt_example_yi_vl.py](examples/quick_start/srt_example_yi_vl.py).
- StableLM
- Command-R
- DBRX
- Grok
- ChatGLM
- InternLM 2

Instructions for supporting a new model are [here](https://github.com/sgl-project/sglang/blob/main/docs/model_support.md).

### Benchmark Performance

- Benchmark a single static batch. Run the following command without launching a server. The arguments are the same as those for `launch_server.py`.
  ```
  python -m sglang.bench_latency --model-path meta-llama/Meta-Llama-3-8B-Instruct --batch 32 --input-len 256 --output-len 32
  ```
- Benchmark online serving. Launch a server first and run the following command.
  ```
  python3 -m sglang.bench_serving --backend sglang --num-prompt 10
  ```

## Frontend: Structured Generation Language (SGLang)
The frontend language can be used with local models or API models.

### Quick Start
The example below shows how to use sglang to answer a mulit-turn question.

#### Using Local Models
First, launch a server with
```
python -m sglang.launch_server --model-path meta-llama/Meta-Llama-3-8B-Instruct --port 30000
```

Then, connect to the server and answer a multi-turn question.

```python
from sglang import function, system, user, assistant, gen, set_default_backend, RuntimeEndpoint

@function
def multi_turn_question(s, question_1, question_2):
    s += system("You are a helpful assistant.")
    s += user(question_1)
    s += assistant(gen("answer_1", max_tokens=256))
    s += user(question_2)
    s += assistant(gen("answer_2", max_tokens=256))

set_default_backend(RuntimeEndpoint("http://localhost:30000"))

state = multi_turn_question.run(
    question_1="What is the capital of the United States?",
    question_2="List two local attractions.",
)

for m in state.messages():
    print(m["role"], ":", m["content"])

print(state["answer_1"])
```

#### Using OpenAI Models
Set the OpenAI API Key
```
export OPENAI_API_KEY=sk-******
```

Then, answer a multi-turn question.
```python
from sglang import function, system, user, assistant, gen, set_default_backend, OpenAI

@function
def multi_turn_question(s, question_1, question_2):
    s += system("You are a helpful assistant.")
    s += user(question_1)
    s += assistant(gen("answer_1", max_tokens=256))
    s += user(question_2)
    s += assistant(gen("answer_2", max_tokens=256))

set_default_backend(OpenAI("gpt-3.5-turbo"))

state = multi_turn_question.run(
    question_1="What is the capital of the United States?",
    question_2="List two local attractions.",
)

for m in state.messages():
    print(m["role"], ":", m["content"])

print(state["answer_1"])
```

#### More Examples

Anthropic and VertexAI (Gemini) models are also supported.
You can find more examples at [examples/quick_start](examples/quick_start).

### Language Feature
To begin with, import sglang.
```python
import sglang as sgl
```

`sglang` provides some simple primitives such as `gen`, `select`, `fork`, `image`.
You can implement your prompt flow in a function decorated by `sgl.function`.
You can then invoke the function with `run` or `run_batch`.
The system will manage the state, chat template, parallelism and batching for you.

The complete code for the examples below can be found at [readme_examples.py](examples/usage/readme_examples.py)

#### Control Flow
You can use any Python code within the function body, including control flow, nested function calls, and external libraries.

```python
@sgl.function
def tool_use(s, question):
    s += "To answer this question: " + question + ". "
    s += "I need to use a " + sgl.gen("tool", choices=["calculator", "search engine"]) + ". "

    if s["tool"] == "calculator":
        s += "The math expression is" + sgl.gen("expression")
    elif s["tool"] == "search engine":
        s += "The key word to search is" + sgl.gen("word")
```

#### Parallelism
Use `fork` to launch parallel prompts.
Because `sgl.gen` is non-blocking, the for loop below issues two generation calls in parallel.

```python
@sgl.function
def tip_suggestion(s):
    s += (
        "Here are two tips for staying healthy: "
        "1. Balanced Diet. 2. Regular Exercise.\n\n"
    )

    forks = s.fork(2)
    for i, f in enumerate(forks):
        f += f"Now, expand tip {i+1} into a paragraph:\n"
        f += sgl.gen(f"detailed_tip", max_tokens=256, stop="\n\n")

    s += "Tip 1:" + forks[0]["detailed_tip"] + "\n"
    s += "Tip 2:" + forks[1]["detailed_tip"] + "\n"
    s += "In summary" + sgl.gen("summary")
```

#### Multi Modality
Use `sgl.image` to pass an image as input.

```python
@sgl.function
def image_qa(s, image_file, question):
    s += sgl.user(sgl.image(image_file) + question)
    s += sgl.assistant(sgl.gen("answer", max_tokens=256)
```

See also [srt_example_llava.py](examples/quick_start/srt_example_llava.py).

#### Constrained Decoding
Use `regex` to specify a regular expression as a decoding constraint.
This is only supported for local models.

```python
@sgl.function
def regular_expression_gen(s):
    s += "Q: What is the IP address of the Google DNS servers?\n"
    s += "A: " + sgl.gen(
        "answer",
        temperature=0,
        regex=r"((25[0-5]|2[0-4]\d|[01]?\d\d?).){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)",
    )
```

#### JSON Decoding
Use `regex` to specify a JSON schema with a regular expression.

```python
character_regex = (
    r"""\{\n"""
    + r"""    "name": "[\w\d\s]{1,16}",\n"""
    + r"""    "house": "(Gryffindor|Slytherin|Ravenclaw|Hufflepuff)",\n"""
    + r"""    "blood status": "(Pure-blood|Half-blood|Muggle-born)",\n"""
    + r"""    "occupation": "(student|teacher|auror|ministry of magic|death eater|order of the phoenix)",\n"""
    + r"""    "wand": \{\n"""
    + r"""        "wood": "[\w\d\s]{1,16}",\n"""
    + r"""        "core": "[\w\d\s]{1,16}",\n"""
    + r"""        "length": [0-9]{1,2}\.[0-9]{0,2}\n"""
    + r"""    \},\n"""
    + r"""    "alive": "(Alive|Deceased)",\n"""
    + r"""    "patronus": "[\w\d\s]{1,16}",\n"""
    + r"""    "bogart": "[\w\d\s]{1,16}"\n"""
    + r"""\}"""
)

@sgl.function
def character_gen(s, name):
    s += name + " is a character in Harry Potter. Please fill in the following information about this character.\n"
    s += sgl.gen("json_output", max_tokens=256, regex=character_regex)
```

See also [json_decode.py](examples/usage/json_decode.py) for an additional example on specifying formats with Pydantic models.

#### Batching
Use `run_batch` to run a batch of requests with continuous batching.

```python
@sgl.function
def text_qa(s, question):
    s += "Q: " + question + "\n"
    s += "A:" + sgl.gen("answer", stop="\n")

states = text_qa.run_batch(
    [
        {"question": "What is the capital of the United Kingdom?"},
        {"question": "What is the capital of France?"},
        {"question": "What is the capital of Japan?"},
    ],
    progress_bar=True
)
```

#### Streaming
Add `stream=True` to enable streaming.

```python
@sgl.function
def text_qa(s, question):
    s += "Q: " + question + "\n"
    s += "A:" + sgl.gen("answer", stop="\n")

state = text_qa.run(
    question="What is the capital of France?",
    temperature=0.1,
    stream=True
)

for out in state.text_iter():
    print(out, end="", flush=True)
```

#### Tips and Implementation Details
- The `choices` argument in `sgl.gen` is implemented by computing the [token-length normalized log probabilities](https://blog.eleuther.ai/multiple-choice-normalization/) of all choices and selecting the one with the highest probability.
- The `regex` argument in `sgl.gen` is implemented through autoregressive decoding with logit bias masking, according to the constraints set by the regex. It is compatible with `temperature=0` and `temperature != 0`.

## Benchmark And Performance
- Llama-7B on NVIDIA A10G, FP16, Tensor Parallelism=1
![llama_7b](assets/llama_7b.jpg)

- Mixtral-8x7B on NVIDIA A10G, FP16, Tensor Parallelism=8
![mixtral_8x7b](assets/mixtral_8x7b.jpg)

- Learn more about the above [results](docs/benchmark_results.md).
- Synthetic latency and throughput benchmark [scripts](https://github.com/sgl-project/sglang/tree/main/benchmark/latency_throughput).

## Roadmap
[Development Roadmap (2024 Q3)](https://github.com/sgl-project/sglang/issues/634)

## Citation And Acknowledgment
Please cite our paper, [SGLang: Efficient Execution of Structured Language Model Programs](https://arxiv.org/abs/2312.07104), if you find the project useful.
We also learned from the design and reused code from the following projects: [Guidance](https://github.com/guidance-ai/guidance), [vLLM](https://github.com/vllm-project/vllm), [LightLLM](https://github.com/ModelTC/lightllm), [FlashInfer](https://github.com/flashinfer-ai/flashinfer), [Outlines](https://github.com/outlines-dev/outlines), and [LMQL](https://github.com/eth-sri/lmql).
