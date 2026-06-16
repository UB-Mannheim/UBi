---
title: CosPGD – Efficient White-Box Adversarial Attack for Pixel-Wise Prediction Tasks
source_url_de: https://www.uni-mannheim.de/dws/research/projects/machine-learning/cospgd/
source_url_en: https://www.uni-mannheim.de/dws/research/projects/machine-learning/cospgd/
category: Projekte
tags: ['adversarial attack', 'semantische segmentierung', 'pixel-weise', 'machine learning', 'robustheit', 'PGD', 'CosPGD']
language: en
---

# CosPGD: An Efficient White-Box Adversarial Attack for Pixel-Wise Prediction Tasks

This project introduces CosPGD, a novel and efficient adversarial attack designed for pixel-wise prediction tasks, such as semantic segmentation and optical flow estimation.

## 💡 Overview

While neural networks achieve high accuracy, their lack of robustness to minor input perturbations is a major hurdle for deployment. Traditional adversarial attacks, like Projected Gradient Descent (PGD), are effective but often focus on isolated point-wise predictions. This can lead to optimization instability and reduced efficiency when trying to balance the attack across the entire image domain.

**CosPGD** addresses this by encouraging more balanced errors across the entire image domain while significantly increasing the attack's overall efficiency. It achieves this by leveraging a simple, fully differentiable alignment score computed between any pixel-wise prediction and its target.

**Applications:**
CosPGD provides efficient evaluations of model robustness for:

- Semantic Segmentation
- Regression Models (e.g., optical flow, disparity estimation, image restoration)

CosPGD has been shown to outperform previous state-of-the-art (SotA) attacks in semantic segmentation.

## 🔗 Useful Resources

- **Paper:** [CosPGD: an efficient white-box adversarial attack for pixel-wise prediction tasks](https://arxiv.org/abs/2302.02213)
- **Code:** [CosPGD code with Sample implementation](https://github.com/shashankskagnihotri/cospgd)
- **Integration:** [CosPGD integrated with mmsegmentation](https://github.com/shashankskagnihotri/adv_mmsegmentation)
- **Presentation:** [Slides for better understanding (PDF)](https://www.uni-mannheim.de/media/Einrichtungen/dws/Files_Research/Machine_Learning/Projects/cospgd_presentation_ICML2024_slides_upload.pdf)

## 🔬 Technical Demonstrations

### 1. Prediction Alignment Scaling (Gradient Analysis)

When analyzing the change in pixel-wise image gradients over attack iterations on DeepLabV3 for semantic segmentation on PASCAL VOC 2012, CosPGD demonstrated superior stability compared to PGD and Seg[PGD].

- **Stability:** CosPGD showed fewer changes in gradient direction over attack iterations, indicating greater optimization stability during the attack process.

### 2. Semantic Segmentation Demo

CosPGD was tested against SegFormer using the ADE20K dataset with different $\\ell\_\\infty$ bounded $\\epsilon$ values, comparing it against Seg[PGD] and PGD as untargeted attacks.

- **Result:** CosPGD outperformed all other tested attacks across various $\\epsilon$ values and attack iterations.

### 3. Optical Flow Estimation Demo

The method was compared against PGD as a targeted $\\ell\_\\infty$-norm constrained 40-iteration attack on RAFT using the Sintel (clean) validation dataset.

## 🧑‍🔬 Research Team

The project was presented at ICML 2024 and involves the following researchers:

- **Shashank Agnihotri:** [Link to profile](https://www.uni-mannheim.de/dws/people/researchers/phd-students/shashank/)
- **Steffen Jung:** [Link to profile](https://jung.vision/)
- **Prof. Dr.-Ing. Margret Keuper:** [Link to profile](https://www.uni-mannheim.de/dws/people/professors/prof-dr-ing-margret-keuper/)

## 🏢 Acknowledgements

- **Funding:** Steffen Jung and Margret Keuper acknowledge funding by the [DFG Research Unit 5336 – Learning to Sense](https://www.learning2sense.de/).
- **Computational Resources:** The [OMNI cluster of University of Siegen](https://cluster.uni-siegen.de/?lang=en) was used for initial computations.
