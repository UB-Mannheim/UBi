---
title: Multilevel Measurement Models Workshop – Bayesian Approaches
source_url_de: https://www.uni-mannheim.de/smip-summerschool/workshops/multilevel-measurement-models/
category: Services
tags: ['Multilevel', 'Messmodelle', 'Bayes', 'MCMC', 'Stan', 'R', 'Latent Variable', 'Statistik']
language: en
---

# Multilevel Measurement Models Workshop

**Instructors:** Lesa Hoffman (University of Iowa) & Jonathan Templin (University of Iowa)

This workshop focuses on utilizing latent variable measurement models for research designs involving multiple levels of sampling. The estimation methods covered are Bayesian Markov Chain Monte Carlo (MCMC).

### Workshop Scope and Applicability

While the examples presented will feature outcomes from persons nested within clusters, the models are applicable to a wider range of multilevel designs (e.g., occasions nested in persons).

The course provides traditional lectures alongside curated examples demonstrating model estimation using R software. All instructional sessions (instructor screen plus audio) will be recorded for future participant use.

### Course Schedule and Topics

The workshop is structured to build knowledge progressively, assuming no extensive prior familiarity with latent variable measurement models, multilevel models, or Bayesian MCMC estimation.

- **Day 1: Single-Level Models and MCMC Introduction**
  - Introduction to single-level latent variable measurement models (all in slope–intercept form).
  - Coverage includes confirmatory factor analysis for continuous responses and item response theory models for binary and ordinal responses.
  - Introduction to MCMC estimation.
- **Day 2: Multilevel Models**
  - Focus on hierarchical linear models (mixed-effects models) for predicting continuous observed outcomes for persons nested in clusters.
  - Includes three-level models for predicting categorical item responses from persons nested in clusters.
- **Days 3 & 4: Advanced Models**
  - Extension of multilevel models to include latent variable measurement models with level-specific discrimination parameters.

### Technical Requirements and Materials

**Prerequisites:**
No prior experience with Stan is assumed.

**Software:**
The course uses Stan software run through R (using CMDStanR).

**Optional Setup:**
Participants who wish to follow along live with examples in Stan are requested to install the `cmdstanr` interface to Stan by following the “Getting Started with CmdStanR” vignette at [mc-stan.org/cmdstanr/articles/cmdstanr.html](https://mc-stan.org/cmdstanr/articles/cmdstanr.html).

*Note: Running Stan during the workshop is optional, as complete examples of syntax and output will be provided as part of the course materials.*

**Course Materials:**
[https://jonathantemplin.github.io/MultilevelMeasurementModels2025/](https://jonathantemplin.github.io/MultilevelMeasurementModels2025/)
