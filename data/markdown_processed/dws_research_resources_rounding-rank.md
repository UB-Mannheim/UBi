---
title: Rounding Rank – Theory and Algorithms for Binary Matrix Factorization
source_url_de: https://www.uni-mannheim.de/dws/research/resources/rounding-rank/
category: Projekte
tags: ['Matrixfaktorisierung', 'Rundungsrang', 'Binär', 'Algorithmen', 'ICDM', 'Dimensionalitätsreduktion', 'Neumann', 'Gemulla']
language: en
---

# Supplementary Material: Rounding Rank Theory and Algorithms

This page provides supplementary material for the ICDM16 paper, "What You Will Gain By Rounding: Theory and Algorithms for Rounding Rank," authored by Stefan Neumann, Rainer Gemulla, and Pauli Miettinen.

## Abstract

When factorizing binary matrices, researchers face a choice: use expensive combinatorial methods that preserve the discrete nature of the data, or use continuous methods that are efficient but destroy the discrete structure. An alternative approach is to compute a continuous factorization and subsequently apply a rounding procedure to obtain a discrete representation.

This paper addresses fundamental questions regarding this process:

- What is gained by rounding?
- Does rounding yield lower reconstruction errors?
- Is it easy to find a low-rank matrix that rounds to a given binary matrix?
- Does the choice of rounding threshold matter?
- Does restricting factorizations to non-negative values change the outcome?

We introduce and study the concept of **rounding rank**. We demonstrate that rounding rank is related to linear classification, dimensionality reduction, and nested matrices. Furthermore, we report on an extensive experimental study comparing different algorithms for finding optimal factorizations under the rounding rank model.

## Publications

**What You Will Gain By Rounding: Theory and Algorithms for Rounding Rank**

- **Authors:** S. Neumann, R. Gemulla, P. Miettinen
- **Status:** To appear in ICDM, 2016
- **PDF:** [Download Paper](https://www.uni-mannheim.de/media/Einrichtungen/dws/Files_Research/neumann16rr.pdf)
- **Extended Version:** [arXiv Link](https://arxiv.org/abs/1609.05034)

## Resources

The following resources are available for reproducing the results:

- **Source Code and Synthetic Dataset Generators:** [Download tar.gz](https://www.uni-mannheim.de/media/Einrichtungen/dws/Files_Research/rounding_rank_code.tar.gz)
