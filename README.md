## Summary

This repository consists of pre-processed data for the [VITON-HD](https://github.com/shadow2496/VITON-HD) model.

The model takes several items as input.

- Cloth Image
- Cloth Mask
- Person Image
- Person Image Mask (obtained from [CIHP_PGN](https://github.com/Engineering-Course/CIHP_PGN))
- Person Keypoints (obtained from [OpenPose](https://github.com/CMU-Perceptual-Computing-Lab/openpose))
- Person Keypoints (in json format)

For simplicity, we re-used the sample cloth images provided by [VITON-HD](https://github.com/shadow2496/VITON-HD).

## Execution Environemnt

All codes, except image rescaling and quantizing were performed on Google Colab due to computational limitations.

## Steps to reproduce

1. Resize the images to 768\*1024. It is recommended to scale the image to height 1024, keeping the same aspect ratio. Then, pad or crop image width instead of height. This will better fit the model. We do so with the [resize.py](./resize.py) script.

2. Parse the resized images to [OpenPose](https://github.com/CMU-Perceptual-Computing-Lab/openpose). A colab setup of OpenPose can be found [here](https://colab.research.google.com/github/tugstugi/dl-colab-notebooks/blob/master/notebooks/OpenPose.ipynb). The command to execute the code can also be found below.

```
# Generate Person Keypoints in json format (with hand and face points)

!cd openpose && ./build/examples/openpose/openpose.bin --image-dir ../img --write_json ./output/ --display 0 --hand --face --disable-blending --render_pose 0


# Generate Person Keypoints Images (with hand points only)

!cd openpose && ./build/examples/openpose/openpose.bin --image-dir ../img --display 0  --write_images ../out --hand --disable-blending
```

3. Parse the resized images to [CIHP_PGN](https://github.com/Engineering-Course/CIHP_PGN). The command to execute the code can be found below. This model needs some further pre-processing of the images. More information for the prepare_dataset.py can be found [here](https://github.com/Engineering-Course/CIHP_PGN/issues/38#issuecomment-560973424).

```
%tensorflow_version 1.x                 # Tensorflow v1 is used.
!python prepare_dataset.py input CIHP
!python test_pgn.py
```

4. After obtaining the Person Mask images from the Part Grouping Network, we have to do some processing. This is because, the image generated are in RGB form, while [VITON-HD](https://github.com/shadow2496/VITON-HD) requires image with color ranges 0 to 19. We perform quantizing with the [convert.py](./convert.py) script.

5. Finally, parse all the pre-processed images into [VITON-HD](https://github.com/shadow2496/VITON-HD). The command to execute the code can be found below.

```
!pip install opencv-python torchgeometry
!python test.py --name out
```

## Credits to

```
@inproceedings{choi2021viton,
  title={VITON-HD: High-Resolution Virtual Try-On via Misalignment-Aware Normalization},
  author={Choi, Seunghwan and Park, Sunghyun and Lee, Minsoo and Choo, Jaegul},
  booktitle={Proc. of the IEEE conference on computer vision and pattern recognition (CVPR)},
  year={2021}
}

@misc{https://doi.org/10.48550/arxiv.1808.00157,
  doi={10.48550/ARXIV.1808.00157},
  url={https://arxiv.org/abs/1808.00157},
  author={Gong, Ke and Liang, Xiaodan and Li, Yicheng and Chen, Yimin and Yang, Ming and Lin, Liang},
  keywords={Computer Vision and Pattern Recognition (cs.CV), FOS: Computer and information sciences, FOS: Computer and information sciences},
  title={Instance-level Human Parsing via Part Grouping Network},
  publisher={arXiv},
  year={2018},
  copyright={arXiv.org perpetual, non-exclusive license}
}

@article{8765346,
  author = {Z. {Cao} and G. {Hidalgo Martinez} and T. {Simon} and S. {Wei} and Y. A. {Sheikh}},
  journal = {IEEE Transactions on Pattern Analysis and Machine Intelligence},
  title = {OpenPose: Realtime Multi-Person 2D Pose Estimation using Part Affinity Fields},
  year = {2019}
}

@inproceedings{simon2017hand,
  author = {Tomas Simon and Hanbyul Joo and Iain Matthews and Yaser Sheikh},
  booktitle = {CVPR},
  title = {Hand Keypoint Detection in Single Images using Multiview Bootstrapping},
  year = {2017}
}

@inproceedings{cao2017realtime,
  author = {Zhe Cao and Tomas Simon and Shih-En Wei and Yaser Sheikh},
  booktitle = {CVPR},
  title = {Realtime Multi-Person 2D Pose Estimation using Part Affinity Fields},
  year = {2017}
}

@inproceedings{wei2016cpm,
  author = {Shih-En Wei and Varun Ramakrishna and Takeo Kanade and Yaser Sheikh},
  booktitle = {CVPR},
  title = {Convolutional pose machines},
  year = {2016}
}
```
