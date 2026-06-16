---
title: Seminar on Solving Complex Tasks using Large Language Models (CS715)
source_url_de: None
source_url_en: https://www.uni-mannheim.de/dws/teaching/course-details/courses-for-master-candidates/cs-715-seminar-on-solving-complex-tasks-using-large-language-models/
category: Services
tags: ['LLM', 'RAG', 'Agent', 'Seminar', 'Datenwissenschaft', 'KI', 'NLP', 'Forschung']
language: en
---

# Seminar CS715: Solving Complex Tasks using Large Language Models

This seminar focuses on **LLM agents** and **Retrieval Augmented Generation (RAG)**. The curriculum is structured around two main types of topics:

- **Experimental Topics**: These aim to verify the utility of specific approaches by applying them to tasks beyond those used in the original research papers.
- **Literature Topics**: These require summarizing the state-of-the-art concerning a specific application of LLMs or LLM-based agents and comparing various approaches using a systematic set of criteria.

## Organization and Prerequisites

The seminar is organized by:

- [Prof. Dr. Christian Bizer](https://www.uni-mannheim.de/dws/people/professors/prof-dr-christian-bizer/)
- [Gastprofessor Dr. Ralph Peeters](https://www.uni-mannheim.de/dws/people/professors/dr-ralph-peeters/)
- [Aaron Steiner](https://www.uni-mannheim.de/dws/people/researchers/phd-students/aaron-steiner/)

It is available for master and bachelor students in the Data Science, Social Data Science, and Business Informatics programs.

**Resources:**

- [Slide Set from Kickoff Meeting (PDF, 2 MB)](https://www.uni-mannheim.de/media/Einrichtungen/dws/Files_Teaching/Seminar_CS715/Seminar-Solving-Complex-Tasks-with-LLMs-Intro-FSS2026.pdf)

## Learning Goals

Upon completion of the seminar, students will be able to:

- Read, understand, and explore scientific literature.
- Critically summarize the state-of-the-art concerning their assigned topic.
- For experimental topics, experimentally verify the utility of prompt engineering or agent-based methods.
- Deliver a presentation about their topic (prior to the final report submission).

## Seminar Schedule

1. **Registration**: Register via the centrally-coordinated seminar registration in Portal2.
1. **Topic Selection**: After acceptance, submit three preferred topics via the [Google Form](https://forms.gle/BkXGPp2zx8ECP6rM6). Topics will be assigned based on preferences.
1. **Kickoff Meeting**: Attend the meeting on **February 25th** (3 pm; Seminarraum 211 (B 6, 30–32 Bauteil E-F)). This meeting will cover general requirements for reports and presentations.
1. **Mentorship**: Students will be assigned a mentor for guidance and one-to-one meetings throughout the semester.
1. **Work Period**: Work is conducted individually, involving literature exploration, performing experiments (note: LLM API costs are not reimbursed), creating a presentation, and writing a report.
1. **Presentation**: Deliver the presentation in a block seminar on **May 4th, 2026**.
1. **Submission**: Write and submit the seminar thesis by **July 3rd, 2026**.

## Seminar Topics (FSS2026)

### Retrieval-Augmented Generation (RAG)

**1. Experimental Topic: Wikipedia Article Generation Using Web-RAG**

- Zhang, J. et al., 2025. WIKIGENBENCH: Exploring full-length Wikipedia generation under real-world scenario. *Proceedings of the 31st International Conference on Computational Linguistics*, pp. 5191-5210.
- Yang, Z., et al., 2025. WikiAutoGen: Towards Multi-Modal Wikipedia-Style Article Generation. *arXiv preprint arXiv:2503.19065*.
- Reeves, N. and Simperl, E., 2025. Machines in the Margins: A Systematic Review of Automated Content Generation for Wikipedia. *Proceedings of the ACM on Human-Computer Interaction*, 9(7), pp.1–30.

**2. Experimental Topic: Verifying Scientific Claims using Web-RAG Agents**

- Wadden, D. et al., 2020. Fact or Fiction: Verifying Scientific Claims. *Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP)*, pages 7534–7550.
- Dmonte et al. 2024. Claim Verification in the Age of Large Language Models: A Survey. *arXiv:2408.14317*.
- Asai, A., He, J., Shao, R. et al. Synthesizing scientific literature with retrieval-augmented language models. *Nature*(2026).

**3. Experimental Topic: Related Work Section Generation using Web-RAG**

- Zhengliang Shi, Z. et al. 2023. Towards a Unified Framework for Reference Retrieval and Related Work Generation. *Findings of the Association for Computational Linguistics: EMNLP 2023*, pages 5785–5799.
- Zhang, Z. et al. 2025. Mixture of Knowledge Minigraph Agents for Literature Review Generation. *Proceedings of the AAAI Conference on Artificial Intelligence*, Vol. 39, No. 24, pp. 26012-26020.
- Luo, Z., et al., 2025. Llm4sr: A survey on large language models for scientific research. *arXiv preprint arXiv:2501.04306*.
- Asai, A., He, J., Shao, R. et al. Synthesizing scientific literature with retrieval-augmented language models. *Nature*(2026).

**4. Experimental Topic: RAG-Driven Data Cleaning with PyDI**

- Ahmad, M.S. et al., 2023. RetClean: Retrieval-based Data Cleaning using Foundation Models and Data Lakes. *arXiv preprint arXiv:2303.16909*.
- Chen, M. et al., 2025. Empowering Tabular Data Preparation with Language Models: Why and How?. *arXiv preprint arXiv:2508.01556*.
- [PyDI Repository](https://github.com/wbsg-uni-mannheim/PyDI)

### LLM Agents

**5. Experimental Topic: LLMs (Agents) for Data Normalization**

- Brinkmann, A., Baumann, N. and Bizer, C., 2024. Using LLMs for the Extraction and Normalization of Product Attribute Values. *Advances in Databases and Information Systems (ADBIS 2024)*. Lecture Notes in Computer Science, vol 14918. Springer, Cham, pp.217–230.
- Chen, M. et al., 2025. Empowering Tabular Data Preparation with Language Models: Why and How?. *arXiv preprint arXiv:2508.01556*.
- [PyDI Repository](https://github.com/wbsg-uni-mannheim/PyDI)

**6. Experimental Topic: Small vs. Large LLMs for Training Data Generation for Entity Matching**

- Zhang, Z. et al., 2025. A Deep Dive Into Cross-Dataset Entity Matching with Large and Small Language Models. *Proceedings of the 28th International Conference on Extending Database Technology*.
- Tan, Z. et al., 2024. Large Language Models for Data Annotation and Synthesis: A Survey. *Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing*, pp. 930–957.
- [MatchGPT Repository](https://github.com/wbsg-uni-mannheim/MatchGPT/tree/main/LLMForEM)

**7. Literature Topic: Query Answering over Data Lakes containing Structured Data and Documents**

- Li, Z. et al., 2025. DocDB: A Database for Unstructured Document Analysis. *Proceedings of the VLDB Endowment*, 18(12), pp.5387-5390.
- Shankar, S. et al., 2025. DocETL: Agentic Query Rewriting and Evaluation for Complex Document Processing. *Proceedings of the VLDB Endowment*, 18(9), pp.3035-3048.
- Sun, Z. et al., 2025. QUEST: Query Optimization in Unstructured Document Analysis. *Proceedings of the VLDB Endowment*, 18(11), pp.4560-4573.

**8. Experimental Topic: Reducing the Resource Consumption of LLM Agents**

- Du, S. et al., 2025. A Survey on the Optimization of Large Language Model-based Agents. *arXiv preprint arXiv:2503.12434*.
- Zhang, Q. et al., 2025. Agentic Plan Caching: Test-Time Memory for Fast and Cost-Efficient LLM Agents. *The Thirty-ninth Annual Conference on Neural Information Processing Systems*.

**9. Experimental Topic: Resource-efficient Agentic Plan Caching for Entity Matching**

- Zhang, Q. et al., 2025. Agentic Plan Caching: Test-Time Memory for Fast and Cost-Efficient LLM Agents. *The Thirty-ninth Annual Conference on Neural Information Processing Systems*.
- Peeters, R. et al., 2025. Entity Matching using Large Language Models. *Proceedings of the 28th International Conference on Extending Database Technology*.
- [PyDI Repository](https://github.com/wbsg-uni-mannheim/PyDI)

**10. Experimental Topic: Effectiveness and Efficiency of Data Serialization Formats for LLMs**

- Yang, J. et al., 2025. StructEval: Benchmarking LLMs' Capabilities to Generate Structural Outputs. *arXiv preprint arXiv:2505.20139*.
- TOON Format, 2024. Token-Oriented Object Notation. Available at: [https://github.com/toon-format/toon](https://github.com/toon-format/toon)
- ZON Format, 2024. Zero Overhead Notation. Available at: [https://github.com/ZON-Format/ZON](https://github.com/ZON-Format/ZON)
- *Comparison formats include: JSON, XML, Markup Tables, etc.*

**11. Experimental Topic: Descriptive Agent Trajectory Mining: What did the agent do?**

- Mohammadi, M. et al., 2025. Evaluation and Benchmarking of LLM Agents: A Survey. *Proceedings of the 31st ACM SIGKDD Conference on Knowledge Discovery and Data Mining (KDD 2025)*.
- Ou, T. et al., 2025. AgentDiagnose: An Open Toolkit for Diagnosing LLM Agent Trajectories. *Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing*.
- Peeters, R. et al., 2025. WebMall--A Multi-Shop Benchmark for Evaluating Web Agents. *arXiv preprint arXiv:2508.13024*.
- van der Aalst, W., 2016. Process Mining – Data Science in Action. Springer.

**12. Experimental Topic: Diagnostic Agent Trajectory Mining: How do agents fail?**

- Mohammadi, M. et al., 2025. Evaluation and Benchmarking of LLM Agents: A Survey. *Proceedings of the 31st ACM SIGKDD Conference on Knowledge Discovery and Data Mining (KDD 2025)*.
- Zhu, et el., 2025. Where do LLM agents fails and how can they learn from failures? *arXiv:2509.25370*.
- Peeters, R. et al., 2025. WebMall--A Multi-Shop Benchmark for Evaluating Web Agents. *arXiv preprint arXiv:2508.13024*.
- van der Aalst, W., 2016. Process Mining – Data Science in Action. Springer.

## Recommended Reading

The following survey articles and tutorials provide excellent starting points for gaining an overview of the seminar topics:

- **Autonomous Agents**: Wang, et al.: [A Survey on Large Language Model based Autonomous Agents](https://arxiv.org/abs/2308.11432). *arXiv:2308.11432, 2024*.
- **GUI Automation**: Sager et al.: [AI Agents for Computer Use: A Review of Instruction-based Computer Control, GUI Automation, and Operator Assistants](https://arxiv.org/abs/2501.16150). *arXiv:2501.16150, 2025*.
- **LLM Overview**: Zhao, et al.: [A survey of Large Language Models](https://arxiv.org/abs/2303.18223). *arXiv:2303.18223, 2024*.
