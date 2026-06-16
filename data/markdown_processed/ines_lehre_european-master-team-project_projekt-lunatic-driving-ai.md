---
title: Lunatic Driving AI – Benchmark for Automated Test Case Generation
source_url_de: None
source_url_en: https://www.uni-mannheim.de/en/ines/lehre/european-master-team-project/projekt-lunatic-driving-ai-1/
category: Projekte
tags: ['Automatisierte Testfälle', 'KI', 'Fahrsimulation', 'Benchmark', 'Software-Testing', 'Machine Learning', 'Edge Cases', 'autonomes Fahren']
language: en
---

# Lunatic Driving AI Project Overview

The field of software testing has been revolutionized by significant strides in **Automated Test Case Generation (ATCG)**. This technique is crucial for optimizing software testing, moving away from the traditionally manual and labor-intensive process of test case creation.

### The Role of AI in Testing

The advent of ATCG has dramatically increased speed, consistency, and overall effectiveness in testing processes. Recent trends highlight the integration of AI and Machine Learning techniques, particularly through **Search-Based Software Testing (SBST)**. This allows testers to generate test cases that cover rare edge cases, which are difficult to identify manually. Furthermore, AI introduces predictive analysis, helping prioritize test scenarios based on bug probability.

### Project Goal: Benchmark Environment

A major challenge in this field is the evaluation and comparison of different testing approaches. The goal of this project is to create a comprehensive **benchmark testing environment** designed to evaluate machine-generated sets of test cases and their coverage of the input space.

### Core Component: The Customizable Driving AI

The central element of the project is a completely customizable driving AI. This AI must simulate a wide range of driving behaviors, including:

- **Safe Operation:** Driving in a good and safe manner, adhering to speed limits, safety distances, traffic lights, and respecting other vehicles and pedestrians.
- **Error Simulation:** Being able to perform subtle or drastic driving mistakes and safety violations across a broad variety of scenarios.
- **Lunatic Behavior:** The capability to act as a complete menace to society.

### Technical Specifications

**Programming Language:**
While the choice is up to the team, **Python** or **C++** are recommended, given that the underlying simulation environment (Carla) is written in C++ and offers a versatile Python API.

**AI Model:**
The approach is flexible, but a **rule-based approach** is recommended. This is because it can be significantly harder to build adjustable settings into a neural network or a reinforcement learning-based AI.

**Frameworks:**
Teams are free to use any framework, library, or open-source solution, provided they maintain reasonable licenses.
