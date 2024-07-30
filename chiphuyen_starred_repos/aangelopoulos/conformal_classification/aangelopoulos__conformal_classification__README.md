# [conformal_classification](https://github.com/aangelopoulos/conformal_classification)

<p align="center"><img width=25% src="https://github.com/aangelopoulos/conformal-classification/blob/master/media/logo_conformal_compat.svg"></p>
<p align="center"><img width=50% src="https://github.com/aangelopoulos/conformal-classification/blob/master/media/text_conformal.svg"></p>

<p align="center">
    <a style="text-decoration:none !important;" href="https://arxiv.org/abs/2009.14193" alt="arXiv"> <img src="https://img.shields.io/badge/paper-arXiv-red" /> </a>
    <a style="text-decoration:none !important;" href="https://people.eecs.berkeley.edu/%7Eangelopoulos/blog/posts/conformal-classification/" alt="website"> <img src="https://img.shields.io/badge/website-Berkeley-yellow" /> </a>
    <a style="text-decoration:none !important;" href="https://docs.conda.io/en/latest/miniconda.html" alt="package management"> <img src="https://img.shields.io/badge/conda-env-green" /> </a>
    <a style="text-decoration:none !important;" href="https://opensource.org/licenses/MIT" alt="License"> <img src="https://img.shields.io/badge/license-MIT-blue.svg" /> </a>
    <a href="https://colab.research.google.com/github/aangelopoulos/conformal_classification/blob/master/example.ipynb" target="_parent"><img src="https://camo.githubusercontent.com/52feade06f2fecbf006889a904d221e6a730c194/68747470733a2f2f636f6c61622e72657365617263682e676f6f676c652e636f6d2f6173736574732f636f6c61622d62616467652e737667" alt="Open In Colab" data-canonical-src="https://colab.research.google.com/assets/colab-badge.svg"></a>

</p>

## Paper 
[Uncertainty Sets for Image Classifiers using Conformal Prediction](https://arxiv.org/abs/2009.14193)
```
@article{angelopoulos2020sets,
  title={Uncertainty Sets for Image Classifiers using Conformal Prediction},
  author={Angelopoulos, Anastasios N and Bates, Stephen and Malik, Jitendra and Jordan, Michael I},
  journal={arXiv preprint arXiv:2009.14193},
  year={2020}
}
```

## Basic Overview

<p>
    This codebase modifies any PyTorch classifier to output a <i>predictive set</i> which provably contains the true class with a probability you specify.
    It uses a method called Regularized Adaptive Prediction Sets (RAPS), which we introduce in our accompanying paper.
    The procedure is as simple and fast as Platt scaling, but provides a formal finite-sample coverage guarantee for every model and dataset.
</p>

<figure>
<img src="https://github.com/aangelopoulos/conformal-classification/blob/master/media/figure_sets.svg" alt="Set-valued classifier." style="display: block; width=1000%">
<figcaption>
    <b>Prediction set examples on Imagenet.</b> we show three examples of the class <tt>fox squirrel</tt> along with 95% prediction sets generated by our method to illustrate how set size changes based on the difficulty of a test-time image.
</figcaption>
</figure>

<br>

## Google Colab
We have written a Colab which allows you to explore `RAPS` and conformal classification.
You don't have to install anything to run the Colab.
The notebook will lead you through constructing predictive sets from a pretrained model.
You can also visualize examples from ImageNet along with their corresponding `RAPS` sets and play with the regularization parameters.

You can access the Colab by clicking the shield below.

<p align="center">

<a href="https://colab.research.google.com/github/aangelopoulos/conformal_classification/blob/master/example.ipynb" target="_parent"><img src="https://camo.githubusercontent.com/52feade06f2fecbf006889a904d221e6a730c194/68747470733a2f2f636f6c61622e72657365617263682e676f6f676c652e636f6d2f6173736574732f636f6c61622d62616467652e737667" alt="Open In Colab" data-canonical-src="https://colab.research.google.com/assets/colab-badge.svg"></a>

</p>

## Usage
If you'd like to use our code in your own projects and reproduce our experiments, we provide the tools below.
Note that although our codebase isn't a package, it's easy to use it like a package, and we do so in the Colab notebook above.

From the root directory, install the dependencies and run our example by executing:
```
git clone https://github.com/aangelopoulos/conformal-classification
cd conformal-classification
conda env create -f environment.yml
conda activate conformal
python example.py 'path/to/imagenet/val/'
```
Look inside `example.py` for a minimal example that modifies a pretrained classifier to output 90% prediction sets.

If you'd like to use our codebase on **your own model**, first place this at the top of your file:
```
from conformal.py import *
from utils.py import *
```
Then create a holdout set for conformal calibration using a line like: 

[`calib, val = random_split(mydataset, [num_calib,total-num_calib])` ](https://github.com/aangelopoulos/conformal-classification/blob/cb2267a0fd127c27f61a7cd74f9519f6f2509e82/example.py#L38)

Finally, you can create the model 

[`model = ConformalModel(model, calib_loader, alpha=0.1, lamda_criterion='size')`](https://github.com/aangelopoulos/conformal-classification/blob/cb2267a0fd127c27f61a7cd74f9519f6f2509e82/example.py#L52)

The `ConformalModel` object takes a boolean flag `randomized`. When `randomized=True`, at test-time, the sets will not be randomized.  This will lead to conservative coverage, but deterministic behavior.

The `ConformalModel` object takes a second boolean flag `allow_zero_sets`. When `allow_zero_sets=True`, at test-time, sets of size zero are disallowed.  This will lead to conservative coverage, but no zero-size sets.

See the discussion below for picking `alpha`, `kreg`, and `lamda` manually.

## Reproducing Our Results
The output of `example.py` should be:
```
Begin Platt scaling.
Computing logits for model (only happens once).
100%|███████████████████████████████████████| 79/79 [02:24<00:00,  1.83s/it]
Optimal T=1.1976691484451294
Model calibrated and conformalized! Now evaluate over remaining data.
N: 40000 | Time: 1.686 (2.396) | Cvg@1: 0.766 (0.782) | Cvg@5: 0.969 (0.941) | Cvg@RAPS: 0.891 (0.914) | Size@RAPS: 2.953 (2.982)
Complete!
```
The values in parentheses are running averages. The preceding values are only for the most recent batch. The timing values will be different on your system, but the rest of the numbers should be exactly the same. The progress bar may print over many lines if your terminal window is small. 

The expected outputs of the experiments are stored in `experiments/outputs`, and they are exactly identical to the results reported in our paper. You can reproduce the results by executing the python scripts in './experiments/' after you have installed our dependencies. For Table 2, we used the `matched-frequencies` version of ImageNet-V2. 

## Picking `alpha`, `kreg`, and `lamda`

`alpha` is the maximum proportion of errors you are willing to tolerate. The target coverage is therefore `1-alpha`. A smaller `alpha` will usually lead to larger sets, since the desired coverage is more stringent.

We have included two optimal procedures for picking 'kreg' and 'lamda'.
If you want sets with small size, set 'lamda_criterion=\'size\''.
If you want sets that approximate conditional coverage, set 'lamda_criterion=\'adaptiveness\''.

## License
<a href="https://opensource.org/licenses/MIT" alt="License">MIT License</a>