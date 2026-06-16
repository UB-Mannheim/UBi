---
title: Projekt – Effizientes Fine-Tuning großer Sprachmodelle (LLMs)
source_url_de: None
source_url_en: https://www.uni-mannheim.de/en/ines/teaching/european-master-team-project/project-efficient-fine-tuning-of-large-language-models/
category: Projekte
tags: ['LLMs', 'Fine-Tuning', 'KI', 'NLP', 'Master', 'Projekt', 'Künstliche Intelligenz']
language: en
---

# Project: Efficient Fine-Tuning of Large Language Models (LLMs)

This document provides an overview of the European Master Team Project focused on optimizing the fine-tuning process for Large Language Models (LLMs).

## 💡 Project Overview

The project addresses the critical need for efficient and resource-optimized methods to adapt massive pre-trained language models to specific, domain-restricted tasks. Fine-tuning LLMs is computationally expensive, making efficient techniques essential for practical application.

- **Goal:** To implement and evaluate advanced parameter-efficient fine-tuning (PEFT) methods.
- **Context:** European Master Team Project, focusing on cutting-edge research in Natural Language Processing (NLP) and Artificial Intelligence (AI).

## 🔬 Methodology and Techniques

The core of the project involves exploring and comparing various state-of-the-art techniques that reduce the computational overhead associated with full model retraining.

### Parameter-Efficient Fine-Tuning (PEFT)

Instead of updating all billions of parameters in the base LLM, PEFT methods only train a small subset of new, specialized parameters. Key techniques explored include:

- **LoRA (Low-Rank Adaptation):** Injecting trainable low-rank matrices into the model layers. This significantly reduces the number of trainable parameters while maintaining high performance.
- **Prompt Tuning:** Optimizing only the input prompt embeddings rather than the model weights themselves.
- **Adapter Layers:** Inserting small, trainable modules between the layers of the pre-trained model.

### Evaluation Metrics

The project evaluates the effectiveness of these methods based on:

1. **Performance:** Accuracy and task-specific performance (e.g., classification, summarization).
1. **Efficiency:** Computational cost (GPU memory usage) and training time compared to full fine-tuning.

## 🎓 Learning Outcomes

Participants gain hands-on experience with:

- Advanced deep learning frameworks (e.g., PyTorch, Hugging Face Transformers).
- The theoretical underpinnings of transformer architectures.
- The practical deployment of cutting-edge AI models in a collaborative, international team setting.

______________________________________________________________________

**[Source Link]** For more details on the project structure and academic requirements, please visit the official course page: [European Master Team Project Details](https://www.uni-mannheim.de/en/ines/teaching/european-master-team-project/project-efficient-fine-tuning-of-large-language-models/)
