# awesome-hallucination-detection

[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/EdinburghNLP/awesome-hallucination-detection) [![License: Apache 2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

## Citing this repository

```
@misc{MinerviniAHD2024,
  author = {Pasquale Minervini and others},
  title = {awesome-hallucination-detection},
  year = {2024},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/EdinburghNLP/awesome-hallucination-detection}}
}
```

## Papers and Summaries

### [HallusionBench: An Advanced Diagnostic Suite for Entangled Language Hallucination and Visual Illusion in Large Vision-Language Models](https://arxiv.org/pdf/2310.14566.pdf)
- **Metrics:**  Accuracy.
- **Datasets:** HallusionBench
- **Comments:** This benchmark presents significant challenges to advanced large visual-language models (LVLMs), such as GPT-4V(Vision), Gemini Pro Vision, Claude 3, and LLaVA-1.5, by emphasizing nuanced understanding and interpretation of visual data. This paper introduces a novel structure for these visual questions designed to establish control groups. This structure is able to conduct a quantitative analysis of the models' response tendencies, logical consistency, and various failure modes.

### [Unified Hallucination Detection for Multimodal Large Language Models](https://arxiv.org/pdf/2402.03190)
- **Metrics:**  Accuracy, F1/Precision/Recall.
- **Datasets:** MHaluBench
- **Framework:** UniHD
- **Comments:** This paper proposes a more unified problem setting for hallucination detection in MLLMs, unveils a meta-evaluation benchmark MHaluBench that encompasses various hallucination categories and multimodal tasks, and introduces UNIHD, a unified framework for the detection of hallucinations in content produced by MLLMs.

### [FactCHD: Benchmarking Fact-Conflicting Hallucination Detection](https://arxiv.org/pdf/2310.12086)
- **Metrics:**  F1 of detection, Match of explanation
- **Datasets:** FactCHD
- **Highlights:** This paper introduces the FACTCHD benchmark, which focuses on detecting fact-conflicting hallucinations. FACTCHD integrates factual knowledge from multiple domains, encompassing a wide range of fact patterns, including raw facts, multi-hop reasoning, comparison, and set operations. Its distinguishing feature lies in its goal to combine evidence chains rooted in factual information, enabling persuasive reasoning in predicting the factuality or non-factuality of a claim.

### [Attention Satisfies: A Constraint-Satisfaction Lens on Factual Errors of Language Models](https://arxiv.org/abs/2309.15098)
- **Metrics:** AUROC, risk-coverage curve operating points
- **Datasets:** CounterFact, factual queries generated from Wikidata
- **Comments:** This paper models factual queries as constraint-satisfaction problems and finds that attention to constraint tokens significantly correlates with factual correctness/hallucinations.

### [TRUE: Re-Evaluating Factual Consistency Evaluation](https://arxiv.org/abs/2204.04991)
- **Metrics:** AUROC, across multiple datasets and evaluation methods
- **Datasets:** PAWS, XSum, QAGS, FRANK, SummEval, BEGIN, Q^2, DialFact, FEVER, VitaminC

### [TrueTeacher: Learning Factual Consistency Evaluation with Large Language Models](https://arxiv.org/abs/2305.11171)
- **Metrics:** AUROC, across multiple datasets and evaluation methods
- **Datasets:** XSum, QAGS, FRANK, SummEval

### [SAC$`^3`$: Reliable Hallucination Detection in Black-Box Language Models via Semantic-aware Cross-check Consistency](https://arxiv.org/abs/2311.01740)
- **Metrics:** Accuracy and AUROC: classification QA and open-domain QA
- **Datasets:** Prime number and senator search from Snowball Hallucination, HotpotQA and Nq-open QA

### [Elastic Weight Removal for Faithful and Abstractive Dialogue Generation](https://arxiv.org/abs/2303.17574)
- **Metrics:** Faithfulness between predicted response and ground-truth knowledge (Tab. 1) -- Critic, Q², BERT F1, F1.
- **Datasets:** Wizard-of-Wikipedia (WoW), the DSTC9 and DSTC11 extensions of MultiWoZ 2.1, FaithDial -- a de-hallucinated subset of WoW.

### [Trusting Your Evidence: Hallucinate Less with Context-aware Decoding](https://arxiv.org/abs/2305.14739)
- **Metrics:** Factual consistency of summaries: BERT-Precision and FactKB. MemoTrap and NQ-Swap: Exact Match.
- **Datasets:** Summarisation: CNN-DM, XSUM. Knowledge Conflicts: MemoTrap, NQ-Swap.

### [When Not to Trust Language Models: Investigating Effectiveness of Parametric and Non-Parametric Memories](https://arxiv.org/abs/2212.10511)
- **Metrics:** Exact Match/Accuracy.
- **Datasets:** QA datasets with long-tail entities: PopQA, EntityQuestions; NQ.

### [Retrieval Augmentation Reduces Hallucination in Conversation](https://arxiv.org/abs/2104.07567)
- **Metrics:** Generation: Perplexity, Unigram Overlap (F1), BLEU-4, ROUGE-L. Overlap between generation and knowledge on which the human grounded during dataset collection: Knowledge F1; only consider words that are infrequent in the dataset when calculating F1: Rare F1.
- **Datasets:** Wow, CMU Document Grounded Conversations (CMU_DoG). Knowledge source: KiLT Wikipedia dump.

### [Just Ask for Calibration: Strategies for Eliciting Calibrated Confidence Scores from Language Models Fine-Tuned with Human Feedback](https://arxiv.org/abs/2305.14975)
- **Metrics:** Expected Calibration Error (ECE) with temperature scaling (ECE-t); accuracy@coverage and coverage@accuracy.
- **Datasets:** Question Answering datasets assessing factual knowledge: TriviaQA, SciQ, TruthfulQA.

### [How Language Model Hallucinations Can Snowball](https://arxiv.org/abs/2305.13534)
- **Metrics:** Percentage of Wrong Answers (Hallucinations) and cases where "the model knows it's wrong" (Snowballed Hallucinations).
- **Datasets:** Primality Testing, Senator Search, Graph Connectivity.

### [Improving Language Models with Advantage-based Offline Policy Gradients](https://arxiv.org/abs/2305.14718)
- **Metrics:** Faithfulness evaluation for Knowledge-Grounded response generation on FaithDial -- FaithCritic, CoLA (Fluency), Dialog Engagement, Length-penalised TF-IDF Diversity. 
- **Datasets:** Faithful Knowledge-Grounded Dialog: FaithDial, a more faithful subset of WoW.

### [Generating with Confidence: Uncertainty Quantification for Black-box Large Language Models](https://arxiv.org/abs/2305.19187)
- **Metrics:** AUROC, AUARC, Uncertainty and Confidence metrics (NumSet, Deg, EigV).
- **Datasets:** CoQA (Open-book Conversational QA dataset), TriviaQA and Natural Questions (Closed-book QA).

### [Contextualized Sequence Likelihood: Enhanced Confidence Scores for Natural Language Generation](https://arxiv.org/abs/2406.01806)
- **Metrics:** AUROC, AUARC; Improved sequence likelihood (log probability of generated sequence) used in Confidence or Uncertainty computation.
- **Datasets:** CoQA (Open-book Conversational QA dataset), TriviaQA and Natural Questions (Closed-book QA).

### [FaithDial: A Faithful Benchmark for Information-Seeking Dialogue](https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00529/114373/FaithDial-A-Faithful-Benchmark-for-Information)
- **Metrics:** Metrics measure either the degree of hallucination of generated responses wrt to some given knowledge or their overlap with gold faithful responses: Critic, Q² (F1, NLI), BERTScore, F1, BLEU, ROUGE.
- **Datasets:** FaithDial, WoW.

### [Neural Path Hunter: Reducing Hallucination in Dialogue Systems via Path Grounding](https://arxiv.org/abs/2104.08455)
- **Metrics:** FeQA, a faithfulness metric; Critic, a hallucination critic; BLEU.
- **Datasets:** OpenDialKG, a dataset that provides open-ended dialogue responses grounded on paths from a KG.

### [HaluEval: A Large-Scale Hallucination Evaluation Benchmark](https://arxiv.org/abs/2305.11747)
- **Metrics:** Accuracy: QA, Dialogue, Summarisation.
- **Datasets:** HaluEval, a collection of generated and human-annotated hallucinated samples for evaluating the performance of LLMs in recognising hallucinations.

### [Self-contradictory Hallucinations of Large Language Models: Evaluation, Detection and Mitigation](https://arxiv.org/abs/2305.15852)
- **Metrics:** After generating sentence pairs, it measures precision, recall, and F1 score in detection tasks.
- **Datasets:** 12 selected topics from Wikipedia.

### [Mitigating Language Model Hallucination with Interactive Question-Knowledge Alignment](https://arxiv.org/abs/2305.13669)
- **Metrics:** *Coverage*: a binary metric that determines whether all the correct gold answer values are included in the generated value. *Hallucination*: a binary indicator that assesses the presence of generated values that do not exist in the question values and gold grounding values. *User Simulator*: user simulator as an "oracle" language model with access to attribution information about the target answer.
- **Datasets:** FuzzyQA, a dataset based on HybridDialogue and MuSiQue where complex questions were simplified using ChatGPT.

### [Check Your Facts and Try Again: Improving Large Language Models with External Knowledge and Automated Feedback](https://arxiv.org/abs/2302.12813)
- **Metrics:** KF1, BLEU, ROUGE, chrF, METEOR, BERTScore, BARTScore, BLEURT, Avg length.
- **Datasets:** News Chat: DSTC7 Track 2 was repurposed as an evaluation corpus for news conversation. Customer Service: uses DSTC11 Track 5 as a showcase in a conversational customer service scenario, expanding upon DSTC9 Track 1 by incorporating subjective information.

### [SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models](https://arxiv.org/abs/2303.08896)
- **Metrics:** Sentence-level Hallucination Detection (AUC-PR), and Passage-level Hallucination Detection (Pearson and Spearman's correlation coefficients).
- **Datasets:** Generated Wikipedia articles from WikiBio, with annotated hallucinations.

### [The Internal State of an LLM Knows When it's Lying](https://arxiv.org/abs/2304.13734)
- **Metrics:** Per-topic and average accuracy.
- **Datasets:** The True-False Dataset contains true and false statements covering several topics -- Cities, Inventions, Chemical Elements, Animals, Companies, and Scientific Facts.

### [Chain of Knowledge: A Framework for Grounding Large Language Models with Structured Knowledge Bases](https://arxiv.org/abs/2305.13269)
- **Metrics:** Exact Match.
- **Datasets:** FEVER, Adversarial HotpotQA.

### [Halo: Estimation and Reduction of Hallucinations in Open-Source Weak Large Language Models](https://arxiv.org/abs/2308.11764)
- **Metrics:** HaloCheck and SelfCheckGPT scores; consistency, factuality.
- **Datasets:** Generated and reviewed questions in the NBA domain.

### [A Stitch in Time Saves Nine: Detecting and Mitigating Hallucinations of LLMs by Validating Low-Confidence Generation](https://arxiv.org/abs/2307.03987)
- **Metrics:** Precision and Recall when detecting Sentence-level and Concept-level Hallucinations.
- **Datasets:** ChatGPT-generated paragraphs spanning 150 topics from diverse domains.

### [Sources of Hallucination by Large Language Models on Inference Tasks](https://arxiv.org/abs/2305.14552)
- **Metrics:** Directional Levy/Holt precision and recall with entity insertions and replacements.
- **Datasets:** Levy/Holt dataset, containing premise-hypothesis pairs with a task formatted as *Given [premise P], is it true that [hypothesis H]?*, where the model is evaluated with random premises.

### [Hallucinations in Large Multilingual Translation Models](https://arxiv.org/abs/2303.16104)
- **Metrics:** Rate to which MT system produces hallucinations under perturbation (Language Pair fraction, rate).
- **Datasets:** Flores-101, WMT, TICO.

### [Citation: A Key to Building Responsible and Accountable Large Language Models](https://arxiv.org/abs/2307.02185)
- **Metrics:** N/A
- **Datasets:** N/A

### [Zero-Resource Hallucination Prevention for Large Language Models](https://arxiv.org/abs/2309.02654)
- **Metrics:** Hallucinatory instruction classification: AUC, ACC, F1, PEA.
- **Datasets:** Concept-7, which focuses on classifying potential hallucinatory instructions.

### [RARR: Researching and Revising What Language Models Say, Using Language Models](https://arxiv.org/abs/2210.08726)
- **Metrics:** Attributable to Identified Sources (AIS) scores before and after editing.
- **Datasets:** Generated statements by creating task inputs from three datasets and prompting different models to produce long-form outputs which may contain hallucinations -- Factoid statements, Reasoning chains, and Knowledge-intensive dialogues.

### [Q²: Evaluating Factual Consistency in Knowledge-Grounded Dialogues via Question Generation and Question Answering](https://arxiv.org/abs/2104.08202)
- **Metrics:** Q² is a metric itself, and it is compared with F1 token-level overlap, Precision and Recall, Q² w/o NLI, E2E NLI, Overlap, BERTScore, and BLEU.
- **Datasets:** WoW which contains dialogues in which a bot needs to respond to user inputs in a knowledgeable way; Topical-Chat, a human-human knowledge-grounded conversation dataset; Dialogue NLI, a dataset based on the Persona-Chat dialogue task consisting of premise-hypothesis pairs.

### [Do We Know What We Don’t Know? Studying Unanswerable Questions beyond SQuAD 2.0](https://aclanthology.org/2021.findings-emnlp.385.pdf)
- **Metrics:** EM on All, "Has answer", and "IDK"
- **Datasets:** MNLI, SQuAD 2.0, ACE-whQA.

### [Chain-of-Verification Reduces Hallucination in Large Language Models](https://arxiv.org/abs/2309.11495)
- **Metrics:** Wikidata and Wiki-Category List: test precision, average number of positive and negative (hallucination) entities for list-based questions; MultiSpanQA: F1, Precision, Recall; Longform generation of biographies: FactScore.
- **Datasets:** Wikidata, Wiki-Category List, MultiSpanQA, Longform Generation of Biographies.

### [Detecting and Mitigating Hallucinations in Multilingual Summarisation](https://arxiv.org/abs/2305.13632)
- **Metrics:** mFACT, a novel multilingual faithful metric developed from four English faithfulness metrics: DAE, QAFactEval, ENFS%, and EntFA.
- **Datasets:** XL-Sum, a multilingual summarisation dataset.

### [Hallucinated but Factual! Inspecting the Factuality of Hallucinations in Abstractive Summarization](https://aclanthology.org/2022.acl-long.236/)
- **Metrics:** XEnt: Hallucination (Accuracy, F1), Factuality (Accuracy, F1), ROUGE, % of novel n-gram, Faithfulness (%ENFS, FEQA, DAE), EntFA (% Factual Ent., % Factual Hal.)
- **Datasets:** A novel dataset, XEnt, for analysing entity hallucination and factuality in abstractive summarisation, consisting of 800 summaries generated by BART and annotated. MEnt, a set of factuality and hallucination annotations for XSum.
- **Comments:** Tab. 2 outlines several types of hallucinations (e.g., factual, non-factual, intrinsic).

### [Enabling Large Language Models to Generate Text with Citations](https://arxiv.org/abs/2305.14627)
- **Metrics:** Fluency (MAUVE), Correctness (EM recall for ASQA, recall-5 for QAMPARI, claim recall for ELI5), Citation quality (citation recall, citation precision).
- **Datasets:** QA datasets such that 1) they contain factual questions in which references are important, 2) questions require long-text answers covering multiple aspects, and 3) answering the questions requires synthesising multiple sources: ASQA, QAMPARI, ELI5.

### [A Token-level Reference-free Hallucination Detection Benchmark for Free-form Text Generation](https://arxiv.org/abs/2104.08704)
- **Metrics:** Acc, G-Mean, BSS, AUC, Not Hallucination (P, R, F1), Hallucination (P, R, F1).
- **Datasets:** HaDes (HAllucination DEtection dataSet), a novel token-level reference-free annotated hallucination detection dataset obtained by perturbing a large number of text segments extracted from the English Wikipedia and verified with crowd-sourced annotations.
- **Comments:** Fig. 3 outlines several hallucination types (domain-specific knowledge, commonsense knowledge, incoherence or improper collocation, unrelated to central topic, conflict with preceding context, conflict with succeeding context, ..)

### [Generating Benchmarks for Factuality Evaluation of Language Models](https://arxiv.org/abs/2307.06908)
- **Metrics:** Percentage of examples it assigns the highest probability to the factual completion.
- **Datasets:** Wiki-FACTOR and News-FACTOR: two novel factuality evaluation benchmarks for LLMs, based on Wikipedia and News articles. Each example consists of a prefix, a factual completion and three similar but non-factual alternatives.
- **Comments:** The paper introduces a framework for automatically generating such datasets from a given corpus, detailed in Section 3.

### [Do Language Models Know When They're Hallucinating References?](https://arxiv.org/abs/2305.18248)
- **Metrics:** Hallucination rate (H%, out of 1000 generated titles)
- **Datasets:** Generated (true and hallucinated) references on topics from the ACM Computing Classification System.

### [Why Does ChatGPT Fall Short in Providing Truthful Answers?](https://arxiv.org/abs/2304.10513)
- **Metrics:** #Correct and #Wrong answers, and different type of failure counts: Comprehension, Factualness, Specificity, Inference.
- **Datasets:** HotpotQA, BoolQ
- **Comments:** This has a nice taxonomy on different error types -- e.g., *comprehension*, *factualness*, *specifity*, *inference*.

### [LM vs LM: Detecting Factual Errors via Cross Examination](https://arxiv.org/abs/2305.13281)
- **Metrics:** Precision, Recall, F1 (under different cross-examination strategies: AYS, IDK, Confidence-Based, IC-IDK)
- **Datasets:** TriviaQA, NQ, PopQA

### [RHO (ρ): Reducing Hallucination in Open-domain Dialogues with Knowledge Grounding](https://arxiv.org/abs/2212.01588)
- **Metrics:** BLEU, ROUGE-L; FeQA, QuestEval, EntityCoverage (Precision, Recall, F1) to estimate the hallucination degree -- FrQA and QuestEval are QA-based metrics for evaluating the faithfulness of the output in the generation task.
- **Datasets:** OpenDialKG

### [FActScore: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation](https://arxiv.org/abs/2305.14251)
- **Metrics:** %Supported statements across varying frequency levels of human entities.
- **Datasets:** People biographies generated from LLMs, where human annotators break them into supporting facts.

### [ExpertQA: Expert-Curated Questions and Attributed Answers](https://arxiv.org/abs/2309.07852)
- **Metrics:** zero-shot (P, R, F1) and fine-tuned (P, R, F1) of AutoAIS labels; FActScore F1 scores on reference factuality labels; AutoAIS (Attributable to Identified Sources) scores.
- **Datasets:** Expert-curated questions across multiple fields (e.g., Anthropology, Architecture, Biology, Chemistry, Engineering & Technology, Healthcare/Medicine; see Tab. 1 for a sample) organised by Question Type (e.g., Directed question with single unambiguous answer, open-ended potentially ambiguous question, summarisation of information of a topic, advice or suggestion on how to approach a problem; see Tab. 2)

### [DoLa: Decoding by Contrasting Layers Improves Factuality in Large Language Models](https://arxiv.org/abs/2309.03883)
- **Metrics:** TruthffulQA: MC1, MC2, MC3 scores; FACTOR: News, Wiki; these were multiple-choice results. Open-ended generation: for TruthfulQA, they use %Truth, %Info, %Truth*Info, %Reject; for CoT tasks (StrategyQA and GSM8K) they go with accuracy.
- **Datasets:** TruthfulQA, FACTOR (news/wiki), StrategyQA, GSM8K

### [FreshLLMs: Refreshing Large Language Models with Search Engine Augmentation](https://arxiv.org/abs/2310.03214)
- **Metrics:** Accuracy (Strict, Relaxed on Fast-changing questions, Slow-changing questions, Never-changing questions, False-premise questions involve knowledge before 2022 and since 2022, 1-hop and multi-hop questions, and Overall).
- **Datasets:** FreshQA, a new QA benchmark with 600 questions covering a wide spectrum of question and answer types.

### [Beyond Factuality: A Comprehensive Evaluation of Large Language Models as Knowledge Generators](https://arxiv.org/abs/2310.07289)
- **Metrics:** Factuality, Relevance, Coherence, Informativeness, Helpfulness and Validity.
- **Datasets:** Natural Questions, Wizard of Wikipedia.

### [Complex Claim Verification with Evidence Retrieved in the Wild](https://arxiv.org/abs/2305.11859)
- **Metrics:** Accuracy, MAE, Macro-F1, soft accuracy.
- **Datasets:** ClaimDecomp, which contains 1200 complex claims from PolitiFactL each claim is labeled with one of the six veracity labels, a justification paragraph written by expect fact-checkers, and subquestions annotated by prior work.

### [FELM: Benchmarking Factuality Evaluation of Large Language Models](https://arxiv.org/abs/2310.00741)
- **Metrics:** Accuracy, F1/Precision/Recall.
- **Datasets:** Reasoning, Math, Writing/Rec, Science/Tech, World Knowledge: GSM8K, ChatGPT, MATH, TruthfulQA, Quora, MMLU/hc3.

### [Evaluating Hallucinations in Chinese Large Language Models](https://arxiv.org/abs/2310.03368)
- **Metrics:** Humand and GPT-4 evaluations.
- **Datasets:** HalluQA (which they propose), and mention TruthfulQA, ChineseFactEval, HaluEval.

### [On Faithfulness and Factuality in Abstractive Summarization](https://arxiv.org/abs/2305.11747)
- **Metrics:** ROUGE, BERTScore; human assessment (identify hallucinatory spans, and whether it's intrinsic or extrinsic) -- *intrinsic hallucinations* are manipulations of the information in the input document, while *extrinsic hallucinations* are information not directly inferable from the input document. Humans were asked to annotate intrinsic and extrinsic hallucinations.
- **Datasets:** XSum.

### [QuestEval: Summarization Asks for Fact-based Evaluation](https://arxiv.org/abs/2103.12693)
- **Metrics:** QuestEval (proposed in this work), for testing for *consistency*, *coherence*, *fluency*, and *relevance*. ROUGE, BLUE, METEOR, BERTScore. SummaQA, QAGS.
- **Datasets:** SummEval, QAGS-XSUM, SQuAD-v2.

### [QAFactEval: Improved QA-Based Factual Consistency Evaluation for Summarization](https://arxiv.org/abs/2112.08542)
- **Metrics:** QAFactEval (proposed in this work), measuring answer selection, question generation, question answering, answer overlap, and filtering/answerability.
- **Datasets:** SummaC, a collection of benchmarks for binary factual consistency evaluation; CGS, correct and incorrect sentences from CNN/DailyMail; XSF; Polytope; FactCC; SummEval; FRANK; QAGs.

### [Fast and Accurate Factual Inconsistency Detection Over Long Documents](https://arxiv.org/abs/2310.13189)
- **Metrics:** SCALE (new metric proposed in this work). Compared with Q², ANLI, SummaC, F1, BLEURT, QuestEval, BARTScore, BERTScore (Table 3). 
- **Datasets:** TRUE benchmark and ScreenEval, new dataset proposed in this work to assess the factual inconsistency in long-form dialogues (52 documents from SummScreen).

### [Understanding Factuality in Abstractive Summarization with FRANK: A Benchmark for Factuality Metrics](https://arxiv.org/abs/2104.13346)
- **Metrics:** BERTScore, FEQA, QGFS, DAE, FactCC
- **Datasets:** Proposed a new dataset FRANK: human annotated factual errors for CNN/DM and XSum dataset

### [TRUE: Re-evaluating Factual Consistency Evaluation](https://aclanthology.org/2022.dialdoc-1.19/)
- **Metrics:** Q², ANLI, SummaC, BLEURT, QuestEval, FactCC, BARTScore, BERTScore
- **Datasets:** Consolidation of 11 different human annotated datasets for fctual consistency.

### [The Curious Case of Hallucinatory (Un)answerability: Finding Truths in the Hidden States of Over-Confident Large Language Models](https://aclanthology.org/2023.emnlp-main.220/)
- **Metrics:** (classification) F-1, Exact Match, (token) F-1
- **Datasets:** SQuAD, Natural Questions, MuSiQue
- **Comments:** This paper models explores LLMs' handling of (un)answerable questions in a closed-book setting, namely answering a question based on a given passage, where the passage doesn't have the answer. The paper shows that despite LLMs' tendency to hallucinate contextual answers, rather than state that they cannot answer the question, they possess internal understanding of the question's (un)answerability.

### [Do Androids Know They're Only Dreaming of Electric Sheep?](https://arxiv.org/abs/2312.17249)
- **Metrics:** (Hallucination detection) Response-level F1, Span-level Partial Credit Match F1
- **Datasets:** Organically generated and synthetically edited CNN DailyMail, ConvFEVER, and E2E, labeled span-wise for hallucinations
- **Comments:** Language models know when they're hallucinating, and we can train probes on LLM hidden states during decoding to reliably detect them. 

### [Correction with Backtracking Reduces Hallucination in Summarization](https://arxiv.org/abs/2310.16176)
- **Metrics:** AlignScore, FactCC, BS-Fact, ROUGE-L
- **Datasets:** CNN/DM, XSum, Newsroom

### [Fine-grained Hallucination Detection and Editing for Language Models](https://arxiv.org/abs/2401.06855)
- **Metrics:** Precision, Recall, F1.
- **Datasets:** Custom fine-grained hallucination detection/editing dataset for various types of (factual) hallucinations: Entity, Relation, Contradictory, Invented, Subjective, Unverifiable.

### [LLMs as Factual Reasoners: Insights from Existing Benchmarks and Beyond](https://arxiv.org/abs/2305.14540)
- **Metrics:** Accuracy for various error types -- positive examples, date swap, entity swap, negated sentences, number swap, pronoun swap.
- **Datasets:** They propose SummEdits, a 10-domain inconsistency detection benchmark.

### [Evaluating the Factual Consistency of Abstractive Text Summarization](https://arxiv.org/abs/1910.12840)
- **Metrics:** They propose FactCC, a metric that measures the factual consistency of abstractive text summarization (intuition: a summary is factually consistent if it contains the same facts as the source document)
- **Datasets:** CNN/DM for generating training data; MNLI and FEVER for training models. Human-based experiments for evaluation on claims about CNN/DM articles.

### [SummaC: Re-Visiting NLI-based Models for Inconsistency Detection in Summarization](https://arxiv.org/abs/2111.09525)
- **Metrics:** Each dataset comes with its metrics (e.g., CoGenSumm uses a reranking-based measure; XSumFaith, SummEval, and FRANK propose several metrics and analyse how they correlate with human annotations; etc.) -- for SummaC, authors propose using balanced accuracy.
- **Datasets:** They propose SummaC (Summary Consistency), a benchmark consisting of six large inconsistency detection datasets: CoGenSumm, XSumFaith, Polytope, FactCC, SummEval, and FRANK.

### [On the Origin of Hallucinations in Conversational Models: Is it the Datasets or the Models?](https://arxiv.org/abs/2204.07931)
- **Metrics:** Expert and non-expert annotations: Partial Hallucination, Entailment, Hallucination, Uncoop, Generic (each of these categories has more fine-grained sub-classes -- see e.g., Fig. 2) -- annotations follow the BEGIN and VRM taxonomies.
- **Datasets:** Knowledge-grounded conversational benchmarks: Wizard of Wikipedia (WoW), CMU-DoG, and TopicalChat -- datasets consisting of dialogues between two speakers where the goal is to communicate information about particular topics while speakers are presented with a knowledge snippet relevant to the current turn.

### [Teaching Language Models to Hallucinate Less with Synthetic Tasks](https://arxiv.org/abs/2310.06827)
- **Metrics:** Hallucination rate in several settings (original, with optimised system message, with full LLM weights, with synthetic data, or with mixtures of synthetic and reference data); BLEU, ROUGE-1, ROUGE-2, ROUGE-L.
- **Datasets:** Search-and-retrieve (MS MARCO), meeting summarisation (QMSum), automated clinical report generation (ACI-Bench).

### [Faithfulness-Aware Decoding Strategies for Abstractive Summarization](https://arxiv.org/abs/2303.03278)
- **Metrics:** ROUGE-L, BERTScore, BS-Fact, FactCC, DAE, QuestEval
- **Datasets:** CNN/DM, XSum

### [KL-Divergence Guided Temperature Sampling](https://arxiv.org/abs/2306.01286)
- **Metrics:** Conversational QA: models fine-tuned on MNLI, SNLI, FEVER, PAWS, ScTail, and VitaminC. Summarisation: models fine-tuned on ANLI and XNLI.
- **Datasets:** Question Rewriting in Conversational Context (QReCC), XLSum.

### [Investigating Hallucinations in Pruned Large Language Models for Abstractive Summarization](https://arxiv.org/abs/2311.09335)
- **Metrics:** Hallucination Risk Metrics (HaRiM+), SummaC, SummaCzs, SummaCconv, Hallucination Risk Ratio (HRR)
- **Datasets:** FactCC, Polytope, SummEval, Legal Contracts, RCT

### [Entity-Based Knowledge Conflicts in Question Answering](https://arxiv.org/abs/2109.05052)
- **Metrics:** EM, Memorisation ratio.
- **Datasets:** NQ Dev with Answer Overlap (AO) and No Answer Overlap (NAO), NewsQA.

### [TruthX: Alleviating Hallucinations by Editing Large Language Models in Truthful Space](https://arxiv.org/abs/2402.17811)
- **Metrics:** MC1/MC2/MC3 scores for TruthffulQA multiple-choice task; %Truth, %Info, %Truth*Info for TruthffulQA open-ended generation task; Choice accuracy for Natural Questions, TriviaQA and FACTOR (news, expert, wiki).
- **Datasets:** TruthfulQA, Natural Questions, TriviaQA, FACTOR (news, expert, wiki)

### [Question Decomposition Improves the Faithfulness of Model-Generated Reasoning](https://arxiv.org/abs/2307.11768)
- **Metrics:** Accuracy, Final Answer Truncation Sensitivity, Final Answer Corruption Sensitivity, Biased-Context Accuracy Change.
- **Datasets:** HotpotQA, OpenbookQA, StrategyQA, TruthfulQA.

### [Self-contradictory Hallucinations of Large Language Models: Evaluation, Detection and Mitigation](https://arxiv.org/abs/2305.15852)
- **Metrics:** For detection: Precision, Recall, F1. For Mitigation: Ratio of self-contradiction removed, Ratio of informative facts retained, perplexity increased.
- **Datasets:** Custom Open-domain Text Generation dataset, LLM-generated encyclopedic text descriptions for Wikipedia entities, PopQA.





## Domain-specific Entries

### [Med-HALT: Medical Domain Hallucination Test for Large Language Models](https://arxiv.org/abs/2307.15343)
- **Metrics:** Reasoning Hallucination Tests (False Confidence Tests, None of the Above Tests, Fake Questions Tests), Memory Hallucination Tests (Abstract-to-Link Tests, PMID-to-Title Tests, Title-to-Link Tests, Link-to-Title Tests); Accuracy, Pointwise Score.
- **Datasets:** Med-HALT: MEDMCQA, Headqa, Medqa USMILE, Medqa (Taiwan), Pubmed.

### [Retrieval-Based Prompt Selection for Code-Related Few-Shot Learning](https://people.ece.ubc.ca/amesbah/resources/papers/cedar-icse23.pdf)
- **Metrics:** Accuracy, Accuracy plausible match
- **Datasets:** ATLAS dataset, TFix dataset
- **Comments:**: Published at ICSE 2023



## Overviews, Surveys, and Shared Tasks

- [Mitigating LLM Hallucinations: a multifaceted approach](https://amatriain.net/blog/hallucinations)
- [Siren’s Song in the AI Ocean: A Survey on Hallucination in Large Language Models](https://arxiv.org/abs/2309.01219)
- [Survey of Hallucination in Natural Language Generation](https://arxiv.org/abs/2202.03629)
- [A Survey of Hallucination in Large Foundation Models](https://arxiv.org/abs/2309.05922)
- [A Survey on Hallucination in Large Language Models: Principles, Taxonomy, Challenges, and Open Questions](https://github.com/LuckyyySTA/Awesome-LLM-hallucination)
    - Paper available [here](https://arxiv.org/abs/2311.05232)
    - Two main categories: *factuality hallucinations* and *faithfulness hallucinations*. Factuality hallucinations emphasise the discrepancy between generated content and verifiable real-world facts, typically manifesting as factual inconsistencies or fabrications. Faithfulness hallucinations refer to the divergence of generated content from user instructions or the context provided by the input, as well as self-consistency within generated content.
- [LLM Powered Autonomous Agents](https://lilianweng.github.io/posts/2023-06-23-agent/)
- [SemEval-2024 Task-6 - SHROOM, a Shared-task on Hallucinations and Related Observable Overgeneration Mistakes](https://helsinki-nlp.github.io/shroom/)
- [llm-hallucination-survey](https://github.com/HillZhang1999/llm-hallucination-survey)
- [How Do Large Language Models Capture the Ever-changing World Knowledge? A Review of Recent Advances](https://arxiv.org/abs/2310.07343)
- [The Dawn After the Dark: An Empirical Study on Factuality Hallucination in Large Language Models](https://arxiv.org/abs/2401.03205)

![Taxonomy from Huang et al.](figures/huang_taxonomy.png "Taxonomy")

## Taxonomies

[Survey of Hallucination in Natural Language Generation](https://arxiv.org/abs/2202.03629) classifies metrics in *Statistical* (ROUGE, BLEU, PARENT, Knowledge F1, ..) and *Model-based* metrics. The latter are further structured in the following classes:
- **Information-Extraction (IE)-based**: retrieve an answer from a knowledge source and compare it with the generated answer -- there might be problems due to the error propagation from the IE model.
- **QA-based**: measure the overlap/consistency between generation and source reference, based on the intuition that similar answers will be generated from the same question if the generation is factually consistent with the source reference. Used to evaluate hallucinations in summarisation, dialogue, and data2text generation. Composed of a *question generation* model and a *question answering* model.
- **Natural Language Inference (NLI)-based**: based on the idea that only the source knowledge reference should entail the entirety of the information in faithful and hallucination-free generation.

[A Survey of Hallucination in “Large” Foundation Models](https://arxiv.org/abs/2309.05922) surveys papers flagging them for *detection*, *mitigation*, *tasks*, *datasets*, and *evaluation metrics*. Regarding hallucinations in text, it categorises papers by *LLMs*, *Multilingual LLMs*, and *Domain-specific LLMs*.

[The Dawn After the Dark: An Empirical Study on Factuality Hallucination in Large Language Models](https://arxiv.org/abs/2401.03205) proposed a taxonomy of different types of hallucinations: Entity-error Hallucination, Relation-error Hallucination, Incompleteness Hallucination, Outdatedness Hallucination, Overclaim Hallucination, Unverifiability Hallucination.

## Measuring Hallucinations in LLMs
- [AnyScale - Llama 2 is about as factually accurate as GPT-4 for summaries and is 30X cheaper](https://www.anyscale.com/blog/llama-2-is-about-as-factually-accurate-as-gpt-4-for-summaries-and-is-30x-cheaper)
- [Arthur.ai - Hallucination Experiment](https://www.arthur.ai/gap-articles/hallucination-experiment)
- [Vectara - Cut the Bull…. Detecting Hallucinations in Large Language Models](https://vectara.com/cut-the-bull-detecting-hallucinations-in-large-language-models/)
- [Vectara LLM Hallucination Leaderboard](https://github.com/vectara/hallucination-leaderboard)
- [TofuEval: Evaluating Hallucinations of LLMs on Topic-Focused Dialogue Summarization](https://arxiv.org/abs/2402.13249)

## Open Source Models for Measuring Hallucinations
- [AlignScore Code and Model - GutHub](https://github.com/yuh-zha/AlignScore)
- [Google True Teacher Model - HuggingFace](https://huggingface.co/google/t5_11b_trueteacher_and_anli)
- [Hallucination Evaluation Model - HuggingFace](https://huggingface.co/vectara/hallucination_evaluation_model)
- [Summac Code and Model - GitHub](https://github.com/tingofurro/summac)
- [SCALE Code and Model - GutHub](https://github.com/asappresearch/scale-score)

## Definitions and Notes

### Extrinsic and Intrinsic Hallucinations

[Neural Path Hunter](https://arxiv.org/abs/2104.08455) defines as *extrinsic hallucination* as an utterance that brings a new span of text that does not correspond
to a valid triple in a KG, and as *intrinsic hallucination* as an utterance that misuses either the subject or object in a KG triple such that there is no direct path between the two entities. [Survey of Hallucination in Natural Language Generation](https://arxiv.org/abs/2202.03629) defines as *extrinsic hallucination* a case where  the generated output that cannot be verified from the source content, and as an *intrinsic hallucination* a case where the generated output contradicts the source content.
