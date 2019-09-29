# DGNN-PyTorch

An unofficial PyTorch implementation of the paper "Skeleton-Based Action Recognition with Directed Graph Neural Networks" in CVPR 2019.

- Paper: [PDF](http://openaccess.thecvf.com/content_CVPR_2019/papers/Shi_Skeleton-Based_Action_Recognition_With_Directed_Graph_Neural_Networks_CVPR_2019_paper.pdf)
- Code is based on 2s-AGCN: [GitHub](https://github.com/lshiwjx/2s-AGCN)


## Dependencies

- Python >= 3.5
- scipy >= 1.3.0
- numpy >= 1.16.4
- PyTorch >= 1.1.0
- tensorboardX >= 1.8   (For logging)


## Directory Structure

Most of the interesting stuff can be found in:
- `model/dgnn.py`: model definition of DGNN
- `data_gen/`: how raw datasets are processed into numpy tensors
- `graphs/directed_ntu_rgb_d.py`: graph definition for DGNN
- `feeders/feeder.py`: how datasets are read in
- `main.py`: general training/eval processes; graph freezing by disabling gradients; etc.


## reference
by kenziyuliu, flickr (CC BY-NC)
https://github.com/kenziyuliu/DGNN-PyTorch
