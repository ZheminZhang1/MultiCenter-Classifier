# MultiCenter-Classifier
This is an official implementation for ["Generating Multi-Center Classifier via Conditional Gaussian Distribution"](https://arxiv.org/pdf/2401.15942.pdf). This code is modified from [Swin Transformer](https://github.com/microsoft/Swin-Transformer). 

The core code for the ResNet50 model is in MCC-ResNet50/models/ResNet50.py and MCC-ResNet50/main.py.
The core code for the Swin-T model is in MCC-Swin_T/models/swin_transformer.py and MCC-Swin_T/main.py.

# Requirements

Refer to [Swin Transformer get_started](https://github.com/microsoft/Swin-Transformer/blob/main/get_started.md). 

# Train

to train `Multi-Center Classifier` with 2 GPU (A100) on a single node for 150 epochs, a single GPU batch-size=512, run:

```bash
torchrun --nproc_per_node 2 --master_port 12345  main.py --cfg configs/swin/swin_tiny_patch4_window7_224.yaml --batch-size 512
```

# Acknowledgement

This repository is built using the [Swin Transformer](https://github.com/microsoft/Swin-Transformer) repository and the [timm](https://github.com/huggingface/pytorch-image-models) library.
