---
title: Frameworks for Activity Recognition
source_url_de: https://www.uni-mannheim.de/dws/research/projects/activity-recognition/frameworks/
source_url_en: https://www.uni-mannheim.de/dws/research/projects/activity-recognition/frameworks/
category: Services
tags: ['Framework', 'Sensor', 'Feature', 'Machine Learning', 'Activity Recognition', 'Online', 'Java']
language: en
---

# Frameworks for Activity Recognition

This section details the technical frameworks developed for activity recognition research.

## Sensor Feature Factory

[https://www.uni-mannheim.de/dws/research/projects/activity-recognition/frameworks/features/](https://www.uni-mannheim.de/dws/research/projects/activity-recognition/frameworks/features/)

This framework is designed for processing recorded acceleration sensor data. It computes necessary features, such as energy or entropy.

**Key Features:**

- Supports multi-threading.
- Allows specification of various settings (e.g., concerning windows).
- Optimized for speed and runnable on Android devices.

## Online Random Forest Classifier

[https://www.uni-mannheim.de/dws/research/projects/activity-recognition/frameworks/onlineforest/](https://www.uni-mannheim.de/dws/research/projects/activity-recognition/frameworks/onlineforest/)

This is a Java implementation of the online random forest classifier.

**Functionality:**
Online machine learning enables the continuous updating of an existing classification model without requiring the processed data to be kept available or knowing all data a-priori.

**Requirements:**

- Supports threading.
- Requires at least Java 1.7 (compatible with Android).
