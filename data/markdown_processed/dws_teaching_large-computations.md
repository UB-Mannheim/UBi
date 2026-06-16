---
title: Compute Resources for Students at the University of Mannheim
source_url_de: None
source_url_en: https://www.uni-mannheim.de/dws/teaching/large-computations/
category: Services
tags: ['Rechenleistung', 'Student', 'HPC', 'GPU', 'Cluster', 'Datenverarbeitung', 'bwCloud', 'UniMannheim']
language: en
---

# Compute Resources for Students

This page provides an overview of the compute resources available to students at the University of Mannheim for performing large-scale computations, such as for team projects or master theses.

**Recommendation:** Please attempt to run your computation on your private machine first. Only utilize the resources listed below if this proves unfeasible.

## 💻 Large-Scale Data Processing (HPC)

If your project requires processing large amounts of data or involves time-consuming computations, the **bwHPC** is available for use.

- **bwUniCluster:** Students can use the [bwUniCluster](https://wiki.bwhpc.de/e/BwUniCluster2.0/Hardware_and_Architecture). This resource is available free of charge, requiring only a short project description.
- **Details:** Available nodes and their hardware configurations are listed on the [bwUniCluster wiki](https://wiki.bwhpc.de/e/BwUniCluster2.0/Hardware_and_Architecture).

## 🚀 GPU Computations

The bwUniCluster also provides several machines equipped with NVIDIA GPUs, enabling computation using CUDA.

- **General GPU Usage:** Information regarding the use of GPUs can be found at the [bwUniCluster-Wiki](https://wiki.bwhpc.de/e/BwUniCluster2.0/Slurm#GPU_jobs).
- **JupyterLab Integration:** There is also an option to use the GPUs within a JupyterLab environment via [bwUniCluster-JupyterLab](https://wiki.bwhpc.de/e/BwUniCluster2.0/Jupyter).

## 🖥️ Dedicated Linux Machine (bwCloud)

If you need to develop an application that must be put online, or if you simply require a dedicated Linux machine for specific tasks, you can use [bwCloud](https://www.bw-cloud.org/en/first_steps). This service is accessible to students.

- **Limitation:** Please note that GPUs cannot currently be used in [bwCloud](https://www.bw-cloud.org/en/first_steps).

## ⚠️ Alternative Requirements (Local Hardware)

If neither bwHPC nor bwCloud meets your specific needs, you may consider using local hardware.

**Important:** This should be treated as the last fallback option, as these resources are quite limited. For further guidance, please consult your supervisor or professor.
