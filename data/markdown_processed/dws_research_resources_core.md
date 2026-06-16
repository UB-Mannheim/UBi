---
title: CORE – Context-Aware Open Relation Extraction with Factorization Machines
source_url_de: https://www.uni-mannheim.de/dws/research/resources/core/
category: Medien
tags: ['Relationsextraktion', 'Kontext', 'NLP', 'Maschinelles_Lernen', 'Factorization_Machines', 'EMNLP', 'CORE', 'Petroni']
language: en
---

# CORE: Context-Aware Open Relation Extraction with Factorization Machines

This page provides supplementary material for the paper **[CORE: Context-Aware Open Relation Extraction with Factorization Machines](https://www.uni-mannheim.de/media/Einrichtungen/dws/Files_Research/petroni15core.pdf)** by Fabio Petroni, Luciano del Corro, and Rainer Gemulla, which was published at the 2015 Conference on Empirical Methods on Natural Language Processing (EMNLP).

## Abstract

We propose **CORE**, a novel matrix factorization model designed for open relation extraction. Our model leverages contextual information and is built upon factorization machines. CORE integrates facts from various sources—such as knowledge bases or open information extractors—along with the specific context in which these facts were observed.

We argue that integrating contextual information (e.g., metadata about extraction sources, lexical context, or type information) significantly improves prediction performance. For instance, open information extractors may produce extractions that are unspecific or ambiguous when removed from their original context.

Our experimental study on a large real-world dataset demonstrates that CORE achieves significantly better prediction performance than state-of-the-art approaches when contextual information is available.

## Supplementary Material

- **Source Code:** The source code for the CORE model is available on GitHub: [https://github.com/fabiopetroni/CORE](https://github.com/fabiopetroni/CORE)
