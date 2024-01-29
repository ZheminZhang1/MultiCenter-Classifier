# MultiCenter-Classifier
This is an official implementation for "Generating Multi-Center Classifier via Conditional Gaussian Distribution". This code is modified from [Swin Transformer](https://github.com/microsoft/Swin-Transformer). 

The core code for the ResNet50 model is in MCC-ResNet50/models/ResNet50.py and MCC-ResNet50/main.py.

# Requirements

Refer to [Swin Transformer get_started](https://github.com/microsoft/Swin-Transformer/blob/main/get_started.md). 

# Train

to train `Multi-Center Classifier` with 2 GPU on a single node for 150 epochs, run:

```bash
torchrun --nproc_per_node 2 --master_port 12345  main.py --cfg configs/swin/swin_tiny_patch4_window7_224.yaml --batch-size 512
```
