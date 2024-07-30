# MCTSr: Mathematic as a Blackbox for LLM

## Envoirment

### Server
We need VLLM or other Openai compatible method.
```
pip install vllm
```
### Clients
We need Huggingface toolkit and Openai for inference.
```
pip install datasets transformers openai
```

## Usage

The script relies on Slurm, If you run it on non-slurm environments,

Just use VLLM to create a openai compatible server, and insert to 'server.csv'

```
IP,PORT,MODEL_NAME
```

If you run it on slurm environment, change the `partition name` to your own partition in `make_n_server.py`

then, you can run the `run_with_earlystopping.py` for datasets.

```
python run_with_earlystopping.py MODEL_NAME DATA_DIR_NAME
```

### Support Datasets

datasets were given by the first part of `DATA_DIR_NAME` arguments, like ` gsm8k-llama3-8b-new-mcts-8` for `gsm8k` , can selected in,

```
        'gsm8k-llama3-8b-new-mcts-8',
         'gsmhard-llama3-8b-new-mcts-8',
         'olympiadbench-llama3-8b-new-mcts-8',
         'GAIC-llama3-8b-new-mcts-8',
         'MATH-llama3-8b-new-mcts-8',
         'AIME-llama3-8b-mcts-2'
```

Using `run_olympics.py` to run all of them.

Alert: That would consume a long time.

## Citation
```
@misc{zhang2024accessing,
      title={Accessing GPT-4 level Mathematical Olympiad Solutions via Monte Carlo Tree Self-refine with LLaMa-3 8B}, 
      author={Di Zhang and Xiaoshui Huang and Dongzhan Zhou and Yuqiang Li and Wanli Ouyang},
      year={2024},
      eprint={2406.07394},
      archivePrefix={arXiv},
      primaryClass={id='cs.AI' full_name='Artificial Intelligence' is_active=True alt_name=None in_archive='cs' is_general=False description='Covers all areas of AI except Vision, Robotics, Machine Learning, Multiagent Systems, and Computation and Language (Natural Language Processing), which have separate subject areas. In particular, includes Expert Systems, Theorem Proving (although this may overlap with Logic in Computer Science), Knowledge Representation, Planning, and Uncertainty in AI. Roughly includes material in ACM Subject Classes I.2.0, I.2.1, I.2.3, I.2.4, I.2.8, and I.2.11.'}
}
```


## Disclaimer

This project was still in a very early stage for explore, pay attentions for the algorithm's output, and do not deploying it to real-world product without fully test.


## Read More

https://arxiv.org/abs/2406.07394

## Re-implementations

https://github.com/BrendanGraham14/mcts-llm

[Jupyter Notebook](https://github.com/trotsky1997/MathBlackBox/issues/2)
