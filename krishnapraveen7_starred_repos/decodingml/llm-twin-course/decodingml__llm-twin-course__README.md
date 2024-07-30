<div align="center">
    <h2>LLM Twin Course: Building Your Production-Ready AI Replica</h2>
    <h1>An End-to-End Framework for Production-Ready LLM & RAG Systems by Building Your LLM Twin</h1>
    <h3>From data gathering to productionizing LLMs using LLMOps good practices.</h3>
    <i>by <a href="https://github.com/iusztinpaul">Paul Iusztin</a>, <a href="https://github.com/alexandruvesa">Alexandru Vesa</a> and <a href="https://github.com/Joywalker">Alexandru Razvant</a></i>
</div>

</br>

<p align="center">
  <img src="media/cover.png" alt="Your image description">
</p>

</br>

## Why is this course different?

*By finishing the **"LLM Twin: Building Your Production-Ready AI Replica"** free course, you will learn how to design, train, and deploy a production-ready LLM twin of yourself powered by LLMs, vector DBs, and LLMOps good practices.*

> Why should you care? 🫵
> 
> → **No more isolated scripts or Notebooks!** Learn production ML by building and deploying an end-to-end production-grade LLM system.


## What will you learn to build by the end of this course?

You will **learn** how to **architect** and **build a real-world LLM system** from **start** to **finish** - from **data collection** to **deployment**.

You will also **learn** to **leverage MLOps best practices**, such as experiment trackers, model registries, prompt monitoring, and versioning.

**The end goal?** Build and deploy your own LLM twin.

**What is an LLM Twin?** It is an AI character that learns to write like somebody by incorporating its style and personality into an LLM.

## The architecture of the LLM twin is split into 4 Python microservices:

### The data collection pipeline

- Crawl your digital data from various social media platforms.
- Clean, normalize and load the data to a [Mongo NoSQL DB](https://www.mongodb.com/) through a series of ETL pipelines.
- Send database changes to a [RabbitMQ](https://www.rabbitmq.com/) queue using the CDC pattern.
- ☁️ Deployed on [AWS](https://aws.amazon.com/).

### The feature pipeline

- Consume messages from a queue through a [Bytewax](https://github.com/bytewax/bytewax?utm_source=github&utm_medium=decodingml&utm_campaign=2024_q1) streaming pipeline.
- Every message will be cleaned, chunked, embedded (using [Superlinked](https://github.com/superlinked/superlinked-alpha?utm_source=community&utm_medium=github&utm_campaign=oscourse), and loaded into a [Qdrant](https://qdrant.tech/?utm_source=decodingml&utm_medium=referral&utm_campaign=llm-course) vector DB in real-time.
- ☁️ Deployed on [AWS](https://aws.amazon.com/).

### The training pipeline
- Create a custom dataset based on your digital data.
- Fine-tune an LLM using QLoRA.
- Use [Comet ML's](https://www.comet.com/signup/?utm_source=decoding_ml&utm_medium=partner&utm_content=github) experiment tracker to monitor the experiments.
- Evaluate and save the best model to [Comet's](https://www.comet.com/signup/?utm_source=decoding_ml&utm_medium=partner&utm_content=github) model registry.
- ☁️ Deployed on [Qwak](https://www.qwak.com/lp/end-to-end-mlops/?utm_source=github&utm_medium=referral&utm_campaign=decodingml).

### The inference pipeline
- Load and quantize the fine-tuned LLM from [Comet's](https://www.comet.com/signup/?utm_source=decoding_ml&utm_medium=partner&utm_content=github) model registry.
- Deploy it as a REST API.
- Enhance the prompts using RAG.
- Generate content using your LLM twin.
- Monitor the LLM using [Comet's](https://www.comet.com/signup/?framework=llm&utm_source=decoding_ml&utm_medium=partner&utm_content=github) prompt monitoring dashboard.
- ☁️ Deployed on [Qwak](https://www.qwak.com/lp/end-to-end-mlops/?utm_source=github&utm_medium=referral&utm_campaign=decodingml).

</br>

<p align="center">
  <img src="media/architecture.png" alt="Your image description">
</p>

</br>

Along the 4 microservices, you will learn to integrate 3 serverless tools:

* [Comet ML](https://www.comet.com/signup/?utm_source=decoding_ml&utm_medium=partner&utm_content=github) as your ML Platform;
* [Qdrant](https://qdrant.tech/?utm_source=decodingml&utm_medium=referral&utm_campaign=llm-course) as your vector DB;
* [Qwak](https://www.qwak.com/lp/end-to-end-mlops/?utm_source=github&utm_medium=referral&utm_campaign=decodingml) as your ML infrastructure;

## Who is this for?

**Audience:** MLE, DE, DS, or SWE who want to learn to engineer production-ready LLM systems using LLMOps good principles.

**Level:** intermediate

**Prerequisites:** basic knowledge of Python, ML, and the cloud

## How will you learn?

The course contains **11 hands-on written lessons** and the **open-source code** you can access on GitHub.

You can read everything and try out the code at your own pace. 

## Costs?
The **articles** and **code** are **completely free**. They will always remain free.

If you plan to run the code while reading it, you have to know that we use several cloud tools that might generate additional costs.

**Pay as you go** 
- [AWS](https://aws.amazon.com/) offers accessible plans to new joiners.
    - For a new first-time account, you could get up to 300$ in free credits which are valid for 6 months. For more, consult the [AWS Offerings](https://aws.amazon.com/free/offers/) page.
- [Qwak](https://www.qwak.com/lp/end-to-end-mlops/?utm_source=github&utm_medium=referral&utm_campaign=decodingml) has a QPU based pricing plan. Here's what you need to know:
    - A QPU stands for Qwak Processing Unit, and is the equivalent of 4vCPU-16GB.
    - Qwak offers up to 100QPU/month for free for up to one year after registration.
    - After that, a policy of 1.2$/QPU is applied as a pay-as-you-go tactic.
    - To find more about Qwak pricing, consult [Qwak Pricing Page](https://www.qwak.com/pricing?utm_source=github&utm_medium=referral&utm_campaign=decodingml)
    - To find more about Qwak Compute Instances, consult [Qwak Instances Page](https://docs.qwak.com/docs/instance-sizes?utm_source=github&utm_medium=referral&utm_campaign=decodingml)

**Freemium** (Free-of-Charge)
- [Qdrant](https://qdrant.tech/?utm_source=decodingml&utm_medium=referral&utm_campaign=llm-course)
- [Comet ML](https://www.comet.com/signup/?utm_source=decoding_ml&utm_medium=partner&utm_content=github)

## Lessons

> [!IMPORTANT]
> **To understand the entire code step-by-step, check out our articles ↓**
> 
> `The course is split into 11 lessons. Every Medium article will be its own lesson.`

### System Design
1. [An End-to-End Framework for Production-Ready LLM Systems by Building Your LLM Twin](https://medium.com/decodingml/an-end-to-end-framework-for-production-ready-llm-systems-by-building-your-llm-twin-2cc6bb01141f)

### Data Engineering: Gather & store the data for your LLM twin
2. [The Importance of Data Pipelines in the Era of Generative AI](https://medium.com/decodingml/the-importance-of-data-pipelines-in-the-era-of-generative-ai-673e1505a861)
3. [Change Data Capture: Enabling Event-Driven Architectures](https://medium.com/decodingml/the-3nd-out-of-11-lessons-of-the-llm-twin-free-course-ba82752dad5a)

### Feature Pipeline: prepare data for LLM fine-tuning & RAG
4. [SOTA Python Streaming Pipelines for Fine-tuning LLMs and RAG — in Real-Time!](https://medium.com/decodingml/sota-python-streaming-pipelines-for-fine-tuning-llms-and-rag-in-real-time-82eb07795b87)
5. [The 4 Advanced RAG Algorithms You Must Know to Implement](https://medium.com/decodingml/the-4-advanced-rag-algorithms-you-must-know-to-implement-5d0c7f1199d2)

### Training Pipeline: fine-tune your LLM twin
6. [The Role of Feature Stores in Fine-Tuning LLMs: From raw data to instruction dataset](https://medium.com/decodingml/the-role-of-feature-stores-in-fine-tuning-llms-22bd60afd4b9)
7. [How to fine-tune LLMs on custom datasets at Scale using Qwak and CometML](https://medium.com/decodingml/how-to-fine-tune-llms-on-custom-datasets-at-scale-using-qwak-and-cometml-12216a777c34)
8. [Best Practices when evaluating fine-tuned LLMs](https://medium.com/decodingml/best-practices-when-evaluating-fine-tuned-llms-47f02f5164c2)

### Inference Pipeline: serve your LLM twin
9. [Architect scalable and cost-effective LLM & RAG inference pipelines](https://medium.com/decodingml/architect-scalable-and-cost-effective-llm-rag-inference-pipelines-73b94ef82a99)
10. [How to evaluate your RAG using RAGAs Framework](https://medium.com/decodingml/how-to-evaluate-your-rag-using-ragas-framework-18d2325453ae)

### Grand Finale
11. [The LLM-Twin Free Course on Production-Ready RAG applications](https://medium.com/decodingml/the-llm-twin-free-course-on-production-ready-rag-pipelines-c96472f4e8c8)
12. Ending Notes (TBD)

## Meet your teachers!
The course is created under the [Decoding ML](https://decodingml.substack.com/) umbrella by:

<table>
  <tr>
    <td><a href="https://github.com/iusztinpaul" target="_blank"><img src="https://github.com/iusztinpaul.png" width="100" style="border-radius:50%;"/></a></td>
    <td>
      <strong>Paul Iusztin</strong><br />
      <i>Senior ML & MLOps Engineer</i>
    </td>
  </tr>
  <tr>
    <td><a href="https://github.com/alexandruvesa" target="_blank"><img src="https://github.com/alexandruvesa.png" width="100" style="border-radius:50%;"/></a></td>
    <td>
      <strong>Alexandru Vesa</strong><br />
      <i>Senior AI Engineer</i>
    </td>
  </tr>
  <tr>
    <td><a href="https://github.com/Joywalker" target="_blank"><img src="https://github.com/Joywalker.png" width="100" style="border-radius:50%;"/></a></td>
    <td>
      <strong>Răzvanț Alexandru</strong><br />
      <i>Senior ML Engineer</i>
    </td>
  </tr>
</table>

## License

This course is an open-source project released under the MIT license. Thus, as long you distribute our LICENSE and acknowledge our work, you can safely clone or fork this project and use it as a source of inspiration for whatever you want (e.g., university projects, college degree projects, personal projects, etc.).

## 🏆 Contribution

A big "Thank you 🙏" to all our contributors! This course is possible only because of their efforts.

<p align="center">
    <a href="https://github.com/decodingml/llm-twin-course/graphs/contributors">
      <img src="https://contrib.rocks/image?repo=decodingml/llm-twin-course" />
    </a>
</p>
