# Update - 25th July 2018
I have made the repository workable on higher image dimensions. 

To use it


1) Make 4 folders FRAMES, DEBLUR_FRAMES, PATCHES and deblurPATCHES.
2) Put your blurry image in FRAMES and name it as frame1.jpg.
3) Run vidpatchipy.py.  This will patch the image into patches of size 512 X 512 and saves them in PATCHES.
4) Run deblur_image.py. This will deblur the patches in PATCHES and stores the deblurred patches in deblurPATCHES.
5) Run vidjoiner.py. This will join the patches to form the final image and saves it in DEBLUR_FRAMES.

The default patch size is 512 X 512. This can be changed easily by making changes in shaper.py, vidpatchipy.py and vidjoiner.py
# ***

# What is this repo ?

This repository is a Keras implementation of [Deblur GAN](https://arxiv.org/pdf/1711.07064.pdf). You can find a tutorial on how it works on [Medium](https://blog.sicara.com/keras-generative-adversarial-networks-image-deblurring-45e3ab6977b5).

# Installation

```
virtualenv venv -p python3
. venv/bin/activate
pip install -r requirements.txt
```

# Dataset

Get the [GOPRO dataset](https://drive.google.com/file/d/1H0PIXvJH4c40pk7ou6nAwoxuR4Qh_Sa2/view?usp=sharing), and extract it in the `deblur-gan` directory. The directory name should be `GOPRO_Large`.

Use:
```
python organize_gopro_dataset.py --dir_in=GOPRO_Large --dir_out=images
```


# Training

```
python train.py --n_images=512 --batch_size=16
```

Use `python train.py --help` for all options

# Testing

```
python test.py
```

Use `python test.py --help` for all options
```
