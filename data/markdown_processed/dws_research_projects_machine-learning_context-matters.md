---
title: Improving Feature Stability during Upsampling – The Role of Spatial Context in Deep Learning
source_url_de: https://www.uni-mannheim.de/dws/research/projects/machine-learning/context-matters/
source_url_en: https://www.uni-mannheim.de/dws/research/projects/machine-learning/context-matters/
category: Projekte
tags: ['Upsampling', 'Spektralartefakte', 'Deep Learning', 'Konvolution', 'Bildrestaurierung', 'Kontext', 'LCTC', 'KI']
language: en
---

# Improving Feature Stability during Upsampling: The Importance of Spatial Context

This project investigates the stability and robustness of pixel-wise predictions during the upsampling phase in deep learning models, focusing on the role of spatial context.

## Project Details

**Accepted at:** ECCV 2024

**Researchers:**

- [Shashank Agnihotri](https://www.uni-mannheim.de/dws/people/researchers/phd-students/shashank/)
- [Julia Grabinski](https://www.uni-mannheim.de/dws/people/alumni/juliagrabinski/)
- [Prof. Dr.-Ing. Margret Keuper](https://www.uni-mannheim.de/dws/people/professors/prof-dr-ing-margret-keuper/)

**Resources:**

- [Paper (arXiv)](https://arxiv.org/pdf/2311.17524)
- [Slides for better understanding](link_to_slides)

## Abstract

Pixel-wise predictions are essential for tasks like image restoration, segmentation, or disparity estimation. Common models involve multi-stage data resampling: first reducing feature map resolution to aggregate information, and then increasing it to generate a high-resolution output.

Previous research has shown that resampling operations are susceptible to artifacts, such as aliasing. While downsampling aliases compromise prediction stability, the effect of aliases during upsampling has not been thoroughly discussed regarding prediction stability and robustness.

The challenges for correct upsampling differ significantly from downsampling:

- **Downsampling:** High frequencies cannot be correctly represented and must be removed to avoid aliases.
- **Upsampling:** The model must restore high frequencies that were lost in lower resolutions.

We find that the availability of large spatial context during upsampling allows for stable, high-quality pixel-wise predictions, even when fully learning all filter weights.

## Proposed Hypotheses

**Hypothesis 1 (H1): Large Context Transposed Convolutions (LCTC)**
Large kernels in transposed convolution operations provide more context, reduce spectral artifacts, and can therefore be leveraged by the network to facilitate better and more robust pixel-wise predictions.

**Hypothesis 2 (H2, Null Hypothesis):**
To leverage prediction context and reduce spectral artifacts, it is crucial to increase the size of the transposed convolution kernels (upsample using large filters). Increasing the size of normal (non-upsampling) decoder convolutions does not have this effect.

## Technical Background

### Visualizing Spectral Artifacts

Image restoration examples using [NAFNet](https://arxiv.org/abs/2204.04676) variants on the [GoPro dataset](https://openaccess.thecvf.com/content_cvpr_2017/papers/Nah_Deep_Multi-Scale_Convolutional_CVPR_2017_paper.pdf) demonstrate the issue. Prior art often uses upsampling techniques like [Pixel Shuffle](https://arxiv.org/abs/1609.05158) or small-filter [transposed convolution](https://arxiv.org/abs/1603.07285) (2x2 or 3x3). These methods lead to spectral artifacts.

When observed in the frequency domain, these artifacts manifest as repeating peaks. Based on sampling theoretic considerations, we propose **Large Context Transposed Convolutions (7x7 or larger)**, which significantly increase the model’s stability during upsampling, observable both in the restored image under attack and in the frequency spectrum.

### Causes and Mitigation of Spectral Artifacts

Various upsampling techniques are compared using an image from the [GoPro dataset](https://openaccess.thecvf.com/content_cvpr_2017/papers/Nah_Deep_Multi-Scale_Convolutional_CVPR_2017_paper.pdf) downsampled with 3x3 MaxPooling.

- **Bilinear interpolation:** Causes over-smoothing.
- **Bicubic interpolation:** Causes overestimation along image boundaries.
- **Pixel Shuffle / Nearest Neighbor:** Cause strong grid artifacts and discoloration.
- **Small kernel transposed convolutions:** Cause grid artifacts.
- **Increasing kernel size:** Leads to better upsampling results.

## Methodology

Our study focuses on the model decoder (shown in green in the architecture diagram). The backbone for the decoder commonly uses a [ResNet-like](https://arxiv.org/abs/1512.03385) structure, though we also utilized a [ConvNeXt-like](https://arxiv.org/abs/2201.03545) structure.

We investigate variants of different upsampling operations for fixed decoder blocks:

1. **Baseline Transposed Deconvolution (a):** Standard approach.
1. **LCTC (b):** Increased convolution kernel size.
1. **Parallel Path (c):** Increased convolution kernel with a second path using a small convolution kernel.

To test the null hypothesis (H2), we also ablate the increase of convolution kernel size in the decoder block (blue arrows), comparing the results against standard [ResNet-like](https://arxiv.org/abs/1512.03385) and [ConvNeXt-like](https://arxiv.org/abs/2201.03545) structures.

## Acknowledgements and Funding

Margret Keuper acknowledges funding by the [DFG Research Unit 5336 – Learning to Sense](https://www.learning2sense.de/).
Initial computations utilized the [OMNI cluster of University of Siegen](https://cluster.uni-siegen.de/?lang=en).
