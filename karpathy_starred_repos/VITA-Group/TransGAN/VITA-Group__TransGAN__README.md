# TransGAN: Two Pure Transformers Can Make One Strong GAN, and That Can Scale Up
Code used for [TransGAN: Two Pure Transformers Can Make One Strong GAN, and That Can Scale Up](https://arxiv.org/abs/2102.07074). 

## Implementation
- [ ] checkpoint gradient using torch.utils.checkpoint
- [ ] 16bit precision training
- [x] Distributed Training (Faster!)
- [x] IS/FID Evaluation
- [x] Gradient Accumulation
- [x] Stronger Data Augmentation
- [x] Self-Modulation

## Guidance
#### Cifar training script
```
python exp/cifar_train.py
```
I disabled the evaluation during training job as it causes strange bug. Please launch another evaluation job simultaneously by copying the `path` to [test script](https://github.com/VITA-Group/TransGAN/blob/a13640fbf4699d651c1a9da0fd936f260f5f096d/exps/cifar_test.py#L58).
#### Cifar test
First download the [cifar checkpoint](https://drive.google.com/file/d/149I8kPnNOypp_4tU_27s7OAVdBR_ZR2Z/view?usp=sharing) and put it on `./cifar_checkpoint`. Then run the following script.
```
python exp/cifar_test.py
```

## Main Pipeline
![Main Pipeline](assets/TransGAN_1.png)

## Representative Visual Results
![Cifar Visual Results](assets/cifar_visual.png)
![Visual Results](assets/teaser_examples.jpg)


README waits for updated
## Acknowledgement
Codebase from [AutoGAN](https://github.com/VITA-Group/AutoGAN), [pytorch-image-models](https://github.com/rwightman/pytorch-image-models)

## Citation
if you find this repo is helpful, please cite
```
@article{jiang2021transgan,
  title={Transgan: Two pure transformers can make one strong gan, and that can scale up},
  author={Jiang, Yifan and Chang, Shiyu and Wang, Zhangyang},
  journal={Advances in Neural Information Processing Systems},
  volume={34},
  year={2021}
}
```
