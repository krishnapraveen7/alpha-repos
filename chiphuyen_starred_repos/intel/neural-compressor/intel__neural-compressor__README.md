# [neural-compressor](https://github.com/intel/neural-compressor)

<div align="center">

Intel® Neural Compressor
===========================
<h3> An open-source Python library supporting popular model compression techniques on all mainstream deep learning frameworks (TensorFlow, PyTorch, ONNX Runtime, and MXNet)</h3>

[![python](https://img.shields.io/badge/python-3.8%2B-blue)](https://github.com/intel/neural-compressor)
[![version](https://img.shields.io/badge/release-2.6-green)](https://github.com/intel/neural-compressor/releases)
[![license](https://img.shields.io/badge/license-Apache%202-blue)](https://github.com/intel/neural-compressor/blob/master/LICENSE)
[![coverage](https://img.shields.io/badge/coverage-85%25-green)](https://github.com/intel/neural-compressor)
[![Downloads](https://static.pepy.tech/personalized-badge/neural-compressor?period=total&units=international_system&left_color=grey&right_color=green&left_text=downloads)](https://pepy.tech/project/neural-compressor)

[Architecture](./docs/source/design.md#architecture)&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;[Workflow](./docs/source/design.md#workflow)&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;[LLMs Recipes](./docs/source/llm_recipes.md)&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;[Results](./docs/source/validated_model_list.md)&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;[Documentations](https://intel.github.io/neural-compressor)

---
<div align="left">

Intel® Neural Compressor aims to provide popular model compression techniques such as quantization, pruning (sparsity), distillation, and neural architecture search on mainstream frameworks such as [TensorFlow](https://www.tensorflow.org/), [PyTorch](https://pytorch.org/), [ONNX Runtime](https://onnxruntime.ai/), and [MXNet](https://mxnet.apache.org/),
as well as Intel extensions such as [Intel Extension for TensorFlow](https://github.com/intel/intel-extension-for-tensorflow) and [Intel Extension for PyTorch](https://github.com/intel/intel-extension-for-pytorch).
In particular, the tool provides the key features, typical examples, and open collaborations as below:

* Support a wide range of Intel hardware such as [Intel Gaudi Al Accelerators](https://www.intel.com/content/www/us/en/products/details/processors/ai-accelerators/gaudi-overview.html), [Intel Core Ultra Processors](https://www.intel.com/content/www/us/en/products/details/processors/core-ultra.html), [Intel Xeon Scalable Processors](https://www.intel.com/content/www/us/en/products/details/processors/xeon/scalable.html), [Intel Xeon CPU Max Series](https://www.intel.com/content/www/us/en/products/details/processors/xeon/max-series.html), [Intel Data Center GPU Flex Series](https://www.intel.com/content/www/us/en/products/details/discrete-gpus/data-center-gpu/flex-series.html), and [Intel Data Center GPU Max Series](https://www.intel.com/content/www/us/en/products/details/discrete-gpus/data-center-gpu/max-series.html) with extensive testing; 
support AMD CPU, ARM CPU, and NVidia GPU through ONNX Runtime with limited testing; support NVidia GPU for some WOQ algorithms like AutoRound and HQQ. 

* Validate popular LLMs such as [LLama2](/examples/pytorch/nlp/huggingface_models/language-modeling/quantization/llm), [Falcon](/examples/pytorch/nlp/huggingface_models/language-modeling/quantization/llm), [GPT-J](/examples/pytorch/nlp/huggingface_models/language-modeling/quantization/llm), [Bloom](/examples/pytorch/nlp/huggingface_models/language-modeling/quantization/llm), [OPT](/examples/pytorch/nlp/huggingface_models/language-modeling/quantization/llm), and more than 10,000 broad models such as [Stable Diffusion](/examples/pytorch/nlp/huggingface_models/text-to-image/quantization), [BERT-Large](/examples/pytorch/nlp/huggingface_models/text-classification/quantization/ptq_static/fx), and [ResNet50](/examples/pytorch/image_recognition/torchvision_models/quantization/ptq/cpu/fx) from popular model hubs such as [Hugging Face](https://huggingface.co/), [Torch Vision](https://pytorch.org/vision/stable/index.html), and [ONNX Model Zoo](https://github.com/onnx/models#models), with automatic [accuracy-driven](/docs/source/design.md#workflow) quantization strategies

* Collaborate with cloud marketplaces such as [Google Cloud Platform](https://console.cloud.google.com/marketplace/product/bitnami-launchpad/inc-tensorflow-intel?project=verdant-sensor-286207), [Amazon Web Services](https://aws.amazon.com/marketplace/pp/prodview-yjyh2xmggbmga#pdp-support), and [Azure](https://azuremarketplace.microsoft.com/en-us/marketplace/apps/bitnami.inc-tensorflow-intel), software platforms such as [Alibaba Cloud](https://www.intel.com/content/www/us/en/developer/articles/technical/quantize-ai-by-oneapi-analytics-on-alibaba-cloud.html), [Tencent TACO](https://new.qq.com/rain/a/20221202A00B9S00) and [Microsoft Olive](https://github.com/microsoft/Olive), and open AI ecosystem such as [Hugging Face](https://huggingface.co/blog/intel), [PyTorch](https://pytorch.org/tutorials/recipes/intel_neural_compressor_for_pytorch.html), [ONNX](https://github.com/onnx/models#models), [ONNX Runtime](https://github.com/microsoft/onnxruntime), and [Lightning AI](https://github.com/Lightning-AI/lightning/blob/master/docs/source-pytorch/advanced/post_training_quantization.rst)

## What's New
* [2024/07] From 3.0 release, framework extension API is recommended to be used for quantization.
* [2024/07] Performance optimizations and usability improvements on [client-side](https://github.com/intel/neural-compressor/blob/master/docs/source/3x/client_quant.md).

## Installation
### Install Framework
#### Install torch for CPU
```Shell
pip install torch --index-url https://download.pytorch.org/whl/cpu
```
#### Use Docker Image with torch installed for HPU
https://docs.habana.ai/en/latest/Installation_Guide/Bare_Metal_Fresh_OS.html#bare-metal-fresh-os-single-click 

#### Install torch/intel_extension_for_pytorch for Intel GPU
https://intel.github.io/intel-extension-for-pytorch/index.html#installation 

#### Install torch for other platform
https://pytorch.org/get-started/locally

#### Install tensorflow
```Shell
pip install tensorflow
```

### Install from pypi
```Shell
# Install 2.X API + Framework extension API + PyTorch dependency
pip install neural-compressor[pt]
# Install 2.X API + Framework extension API + TensorFlow dependency
pip install neural-compressor[tf]
```
> **Note**:
> Further installation methods can be found under [Installation Guide](https://github.com/intel/neural-compressor/blob/master/docs/source/installation_guide.md). check out our [FAQ](https://github.com/intel/neural-compressor/blob/master/docs/source/faq.md) for more details.

## Getting Started

Setting up the environment:
```bash
pip install "neural-compressor>=2.3" "transformers>=4.34.0" torch torchvision
```
After successfully installing these packages, try your first quantization program.

### Weight-Only Quantization (LLMs)
Following example code demonstrates Weight-Only Quantization on LLMs, it supports Intel CPU, Intel Gaudi2 AI Accelerator, Nvidia GPU, best device will be selected automatically.

To try on Intel Gaudi2, docker image with Gaudi Software Stack is recommended, please refer to following script for environment setup. More details can be found in [Gaudi Guide](https://docs.habana.ai/en/latest/Installation_Guide/Bare_Metal_Fresh_OS.html#launch-docker-image-that-was-built).
```bash
# Run a container with an interactive shell
docker run -it --runtime=habana -e HABANA_VISIBLE_DEVICES=all -e OMPI_MCA_btl_vader_single_copy_mechanism=none --cap-add=sys_nice --net=host --ipc=host vault.habana.ai/gaudi-docker/1.14.0/ubuntu22.04/habanalabs/pytorch-installer-2.1.1:latest

# Install the optimum-habana
pip install --upgrade-strategy eager optimum[habana]

# Install INC/auto_round
pip install neural-compressor auto_round
```
Run the example:
```python
from transformers import AutoModel, AutoTokenizer

from neural_compressor.config import PostTrainingQuantConfig
from neural_compressor.quantization import fit
from neural_compressor.adaptor.torch_utils.auto_round import get_dataloader

model_name = "EleutherAI/gpt-neo-125m"
float_model = AutoModel.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
dataloader = get_dataloader(tokenizer, seqlen=2048)

woq_conf = PostTrainingQuantConfig(
    approach="weight_only",
    op_type_dict={
        ".*": {  # match all ops
            "weight": {
                "dtype": "int",
                "bits": 4,
                "algorithm": "AUTOROUND",
            },
        }
    },
)
quantized_model = fit(model=float_model, conf=woq_conf, calib_dataloader=dataloader)
```
**Note:**

To try INT4 model inference, please directly use [Intel Extension for Transformers](https://github.com/intel/intel-extension-for-transformers), which leverages Intel Neural Compressor for model quantization.

### Static Quantization (Non-LLMs)

```python
from torchvision import models

from neural_compressor.config import PostTrainingQuantConfig
from neural_compressor.data import DataLoader, Datasets
from neural_compressor.quantization import fit

float_model = models.resnet18()
dataset = Datasets("pytorch")["dummy"](shape=(1, 3, 224, 224))
calib_dataloader = DataLoader(framework="pytorch", dataset=dataset)
static_quant_conf = PostTrainingQuantConfig()
quantized_model = fit(model=float_model, conf=static_quant_conf, calib_dataloader=calib_dataloader)
```

## Documentation

<table class="docutils">
  <thead>
  <tr>
    <th colspan="8">Overview</th>
  </tr>
  </thead>
  <tbody>
    <tr>
      <td colspan="2" align="center"><a href="./docs/source/3x/design.md#architecture">Architecture</a></td>
      <td colspan="2" align="center"><a href="./docs/source/3x/design.md#workflow">Workflow</a></td>
      <td colspan="2" align="center"><a href="https://intel.github.io/neural-compressor/latest/docs/source/api-doc/apis.html">APIs</a></td>
      <td colspan="1" align="center"><a href="./docs/source/3x/llm_recipes.md">LLMs Recipes</a></td>
      <td colspan="1" align="center">Examples</td>
    </tr>
  </tbody>
  <thead>
    <tr>
      <th colspan="8">PyTorch Extension APIs</th>
    </tr>
  </thead>
  <tbody>
    <tr>
        <td colspan="2" align="center"><a href="./docs/source/3x/PyTorch.md">Overview</a></td>
        <td colspan="2" align="center"><a href="./docs/source/3x/PT_StaticQuant.md">Static Quantization</a></td>
        <td colspan="2" align="center"><a href="./docs/source/3x/PT_DynamicQuant.md">Dynamic Quantization</a></td>
        <td colspan="2" align="center"><a href="./docs/source/3x/PT_SmoothQuant.md">Smooth Quantization</a></td>
    </tr>
    <tr>
        <td colspan="4" align="center"><a href="./docs/source/3x/PT_WeightOnlyQuant.md">Weight-Only Quantization</a></td>
        <td colspan="2" align="center"><a href="./docs/source/3x/PT_MXQuant.md">MX Quantization</a></td>
        <td colspan="2" align="center"><a href="./docs/source/3x/PT_MixedPrecision.md">Mixed Precision</a></td>
    </tr>
  </tbody>
  <thead>
      <tr>
        <th colspan="8">Tensorflow Extension APIs</th>
      </tr>
  </thead>
  <tbody>
      <tr>
          <td colspan="3" align="center"><a href="./docs/source/3x/TensorFlow.md">Overview</a></td>
          <td colspan="3" align="center"><a href="./docs/source/3x/TF_Quant.md">Static Quantization</a></td>
          <td colspan="2" align="center"><a href="./docs/source/3x/TF_SQ.md">Smooth Quantization</a></td>
      </tr>
  </tbody>
  <thead>
      <tr>
        <th colspan="8">Other Modules</th>
      </tr>
  </thead>
  <tbody>
      <tr>
          <td colspan="4" align="center"><a href="./docs/source/3x/autotune.md">Auto Tune</a></td>
          <td colspan="4" align="center"><a href="./docs/source/3x/benchmark.md">Benchmark</a></td>
      </tr>
  </tbody>
</table>

> **Note**:
> From 3.0 release, we recommend to use 3.X API. Compression techniques during training such as QAT, Pruning, Distillation only available in [2.X API](https://github.com/intel/neural-compressor/blob/master/docs/source/2x_user_guide.md) currently.

## Selected Publications/Events
* Blog by Intel: [Neural Compressor: Boosting AI Model Efficiency](https://community.intel.com/t5/Blogs/Tech-Innovation/Artificial-Intelligence-AI/Neural-Compressor-Boosting-AI-Model-Efficiency/post/1604740) (June 2024)
* Blog by Intel: [Optimization of Intel AI Solutions for Alibaba Cloud’s Qwen2 Large Language Models](https://www.intel.com/content/www/us/en/developer/articles/technical/intel-ai-solutions-accelerate-alibaba-qwen2-llms.html) (June 2024)
* Blog by Intel: [Accelerate Meta* Llama 3 with Intel AI Solutions](https://www.intel.com/content/www/us/en/developer/articles/technical/accelerate-meta-llama3-with-intel-ai-solutions.html) (Apr 2024)
* EMNLP'2023 (Under Review): [TEQ: Trainable Equivalent Transformation for Quantization of LLMs](https://openreview.net/forum?id=iaI8xEINAf&referrer=%5BAuthor%20Console%5D) (Sep 2023)
* arXiv: [Efficient Post-training Quantization with FP8 Formats](https://arxiv.org/abs/2309.14592) (Sep 2023)
* arXiv: [Optimize Weight Rounding via Signed Gradient Descent for the Quantization of LLMs](https://arxiv.org/abs/2309.05516) (Sep 2023)

> **Note**:
> View [Full Publication List](https://github.com/intel/neural-compressor/blob/master/docs/source/publication_list.md).

## Additional Content

* [Release Information](./docs/source/releases_info.md)
* [Contribution Guidelines](./docs/source/CONTRIBUTING.md)
* [Legal Information](./docs/source/legal_information.md)
* [Security Policy](SECURITY.md)

## Communication
- [GitHub Issues](https://github.com/intel/neural-compressor/issues): mainly for bug reports, new feature requests, question asking, etc.
- [Email](mailto:inc.maintainers@intel.com): welcome to raise any interesting research ideas on model compression techniques by email for collaborations.
- [Discord Channel](https://discord.com/invite/Wxk3J3ZJkU): join the discord channel for more flexible technical discussion.
- [WeChat group](/docs/source/imgs/wechat_group.jpg): scan the QA code to join the technical discussion.
