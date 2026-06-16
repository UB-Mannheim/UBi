---
title: Forschungsresultate zur Aktivitäts- und Positionserkennung mit Wearable Devices
source_url_de: https://www.uni-mannheim.de/dws/research/projects/activity-recognition/results/
source_url_en: None
category: Projekte
tags: ['Aktivitätserkennung', 'Wearables', 'ADLs', 'Sensorik', 'Machine Learning', 'Smart-Home', 'Pervasives Computing']
language: de
---

# Forschungsresultate zur Aktivitäts- und Positionserkennung

Diese Seite fasst die experimentellen Ergebnisse aus verschiedenen Forschungsprojekten zur Aktivitäts- und Positionserkennung (Activity Recognition) zusammen, die Ambient Assisted Living (AAL) und Ubiquitous Computing unterstützen.

## POLARIS: Probabilistic and Ontological Activity Recognition in Smart-homes

*Recognition of activities of daily living (ADLs) is an enabling technology for several ubiquitous computing applications.*

**Überblick:**
Dieses Projekt untersucht die Erkennung von ADLs. Die Ergebnisse stammen aus der Veröffentlichung *POLARIS: Probabilistic and Ontological Activity Recognition in Smart-homes*. Die resultierenden Dateien enthalten die Testergebnisse für jeden einzelnen Patienten/Tag, dargestellt durch Präzision, Recall und F-Measure.

**Setup:**

- **MLNnc Solver:** [show](https://www.uni-mannheim.de/media/Einrichtungen/dws/Files_Research/Projects/sensor/results/riboni2016unsupervised/mln/casas.mln) (Ontology: unchanged compared to D. Riboni et al. 2016)

**Datasets:**

### WSU CASAS Dataset

- **Publikation:** [http://dx.doi.org/10.1109/MC.2012.328](http://dx.doi.org/10.1109/MC.2012.328)
- **MLNnc Model:** [show](https://www.uni-mannheim.de/media/Einrichtungen/dws/Files_Research/Projects/sensor/results/riboni2016unsupervised/mln/casas.mln)
  | #1 | - | - | coming soon |

### SmartFaber Dataset

- **Publikation:** [http://dx.doi.org/10.1109/PERCOMW.2015.7134060](http://dx.doi.org/10.1109/PERCOMW.2015.7134060)
- **MLNnc Model:** [show](https://www.uni-mannheim.de/media/Einrichtungen/dws/Files_Research/Projects/sensor/results/riboni2016unsupervised/mln/smartfaber.mln)
  | #1 | - | - | coming soon |

______________________________________________________________________

## Modeling and Reasoning with ProbLog: An Application in Recognizing Complex Activities

*Smart-home activity recognition is an enabling tool for a wide range of ambient assisted living applications.*

**Überblick:**
Dieses Projekt zielt darauf ab, die Einschränkungen von überwachtem Lernen und wissensbasiertem Reasoning zu überwinden, indem deren Stärken kombiniert werden. Die Ergebnisse stammen aus der Veröffentlichung *Modeling and Reasoning with ProbLog: An Application in Recognizing Complex Activities*.

**Setup:**

- **ProbLog Online Editor:** [show](https://dtai.cs.kuleuven.be/problog/editor.html)

**ProbLog Modelle:**
| #1 | Minimal ProbLog Model (Figure 1) | Download | \<1 |
| #2 | Final ProbLog Model (Running Example) | Download | \<1 |

*Kooperation zwischen der [University of Milano](https://www.unimi.it/ENG/) und der [University of Mannheim](http://dws.informatik.uni-mannheim.de/)*

______________________________________________________________________

## Hips Do Lie! A Position-Aware Mobile Fall Detection System (2018)

*Ambient Assisted Living using mobile device sensors is an active area of research in pervasive computing.*

**Überblick:**
Das Ziel ist die Implementierung eines selbstadaptiven, pervasiven Sturzerkennungsansatzes, der für reale Lebenssituationen geeignet ist. Die Ergebnisse stammen aus der Veröffentlichung *Hips Do Lie! A Position-Aware Mobile Fall Detection System*. Die resultierenden Dateien enthalten die individuellen (nicht aggregierten) Ergebnisse.

**Datasets:**
Die Datensätze, die in den Experimenten berücksichtigt wurden, sind:

- MMSys
- UMA
- MiBShar
- SisFall

Weitere Informationen zu den Datensätzen finden Sie [hier (DataSets)](https://www.uni-mannheim.de/media/Einrichtungen/dws/Files_Research/Projects/sensor/results/krupitzer2018hips/readme_raw_data.txt) und [hier (Traces)](https://www.uni-mannheim.de/media/Einrichtungen/dws/Files_Research/Projects/sensor/results/krupitzer2018hips/traces/readme_traces.txt).

**Ergebnisse:**

**Fall Detection**
| #1 | Fall Detection | ReadMe | Table III-VI | show |
| #2 | Positioning | ReadMe | Table VII | show |
| #3 | Fullstack (FallDetection) | ReadMe | Table VIII | show |
| #4 | Fullstack (Positioning) | ReadMe | Table IX | show |
| #5 | Clustering | ReadMe | - | show |

**Additional Results (F-measure)**
| #1 | F0.5, F1, and F2 | Table IV | show |
| #2 | F0.5, F1, and F2 | Table V | show |
| #3 | F0.5, F1, and F2 | Table VII | show |
| #4 | F0.5, F1, and F2 | Table VIII | show |
| #5 | F0.5, F1, and F2 | Table IX | show |

*Kooperation zwischen der [Chair of Information Systems II](https://becker.bwl.uni-mannheim.de/home) und der [Chair of Artificial Intelligence](http://dws.informatik.uni-mannheim.de/en/research/artificial-intelligence-prof-stuckenschmidt/)*

______________________________________________________________________

## Online Personalization of Cross-Subjects based Activity Recognition Models on Wearable Devices (2017)

*Human activity recognition using wearable devices is an active area of research in pervasive computing.*

**Überblick:**
Dieses Projekt zielt auf Patienten und Senioren ab, die keine subjektspezifischen Daten sammeln können. Der Fokus liegt auf der Entwicklung von Cross-Subjects-basierten Erkennungsmodellen. Die Ergebnisse stammen aus der Veröffentlichung *Online Personalization of Cross-Subjects based Activity Recognition Models on Wearable Devices*. Die Ergebnisse enthalten die Testergebnisse (Precision, Recall, F-measure) für jeden einzelnen Probanden, sind aber nicht aggregiert.

**Hinweis:**
Alle Experimente wurden mit Random Forest als Klassifikator durchgeführt. Es wurden zwei Versionen betrachtet: Online- und Offline-Lernen.

**Preprocessed Accerleration Data (Windows)**
| #1 | Single sensor setup, separated by position and subject | Download | ~120 |
| #2 | Two-part setup, separated by combination and subject | Download | ~690 |
| #3 | Three-part setup, separated by combination and subject | Download | ~1600 |
| #4 | Four-part setup, separated by combination and subject | Download | ~2100 |
| #5 | Five-part setup, separated by combination and subject | Download | ~1600 |
| #6 | Six-part setup, separated by combination and subject | Download | ~640 |

**Cross-Subjects Activity Recognition (Section VI, Part A)**
| #1 | Randomy, One Accelerometer, Offline learning | Table II | show | ~1 |
| #2 | Randomy, Two Accelerometer, Offline learning | Table II/III/IV | show | ~2 |
| #3 | Randomy, Three Accelerometer, Offline learning | Table II | show | ~3 |
| #4 | Randomy, Four Accelerometer, Offline learning | Table II | show | ~3 |
| #5 | Randomy, Five Accelerometer, Offline learning | Table II | show | ~2 |
| #6 | Randomy, Six Accelerometer, Offline learning | Table II | show | ~1 |
| #7 | L1O, One Accelerometer, Offline learning | Table II | show | \<1 |
| #8 | L1O, Two Accelerometer, Offline learning | Table II/III/IV | show | \<1 |
| #9 | L1O, Three Accelerometer, Offline learning | Table II | show | \<1 |
| #10 | L1O, Four Accelerometer, Offline learning | Table II | show | \<1 |
| #11 | L1O, Five Accelerometer, Offline learning | Table II | show | \<1 |
| #12 | L1O, Six Accelerometer, Offline learning | Table II | show | \<1 |
| #13 | Our approach, One Accelerometer, Offline learning | Table II | show | \<1 |
| #14 | Our approach, Two Accelerometer, Offline learning | Table II/III/IV | show | \<1 |
| #15 | Our approach, Three Accelerometer, Offline learning | Table II | show | \<1 |
| #16 | Our approach, Four Accelerometer, Offline learning | Table II | show | \<1 |
| #17 | Our approach, Five Accelerometer, Offline learning | Table II | show | \<1 |
| #18 | Our approach, Six Accelerometer, Offline learning | Table II | show | \<1 |
| #19 | Subject-Specific, One Accelerometer, Offline learning | - | show | \<1 |
| #20 | Subject-Specific, Two Accelerometer, Offline learning | - | show | \<1 |

**Personalization: Online and Active Learning (Section VI, Part B)**
| #1 | Our approach, One Accelerometer, Online Learning | - | show | \<1 |
| #2 | Our approach + User-Feedback, One Accelerometer, Online Learning | - | show | ~1 |
| #3 | Our approach + User-Feedback + Smoothing, One Accelerometer, Online Learning | - | show | ~1 |
| #4 | Our approach, Two Accelerometer, Online Learning | Table V/VI | show | \<1 |
| #5 | Our approach + Smoothing, Two Accelerometer, Online Learning | Table V/VI | show | ~2 |
| #6 | Our approach + User-Feedback, Two Accelerometer, Online Learning | Table V/VI | show | ~2 |
| #7 | Our approach + User-Feedback + Smoothing, Two Accelerometer, Online Learning | Table V/VI/VII/VIII, Figure 4 | show | ~2 |
| #8 | Our approach + User-Feedback + Smoothing (varying confidence threshold), Two Accelerometer, Online Learning | Figure 5 | show | ~23 |
| #9 | Our approach + User-Feedback + Smoothing (varying number of trees), Two Accelerometer, Online Learning | Figure 6 | show | ~27 |
| #10 | Subject-Specific, One Accelerometer, Online Learning | - | show | ~1 |
| #11 | Subject-Specific, Two Accelerometer, Online Learning | - | show | ~2 |

______________________________________________________________________

## Position-Aware Activity Recognition with Wearable Devices (2017)

*Reliable human activity recognition with wearable devices enables the development of human-centric pervasive applications.*

**Überblick:**
Das Ziel ist die Entwicklung eines robusten, wearable-basierten Aktivitätserkennungssystems für reale Situationen. Der Fokus liegt auf der Erkennung der Position des Wearables am Körper. Die Ergebnisse stammen aus der Veröffentlichung *Position-Aware Activity Recognition with Wearable Devices*. Die resultierenden Dateien enthalten die Testergebnisse (F-Measure, Confusion Matrix, ...) für jeden einzelnen Probanden.

**Hinweis:**
Dieses Projekt ist eine Erweiterung.

**Subject-Specific Activity Recognition (Section 5.2)**
| #1 | Single Sensor | Figure V | show | ~20 |
| #2 | Two-part setup (all combinations) | - | show | ~60 |
| #3 | Three-part setup (all combinations) | - | show | ~100 |

**Cross-Subjects Activity Recognition (Section 5.4)**
| #1 | Dynamic Activity Recognition (Randomly, One accelormeter) | Table 10, 11 | show | \<1 |
| #2 | Dynamic Activity Recognition (L1O, One accelormeter) | Table 10, 11 | show | \<1 |
| #3 | Dynamic Activity Recognition (Top-Pairs, One accelormeter) | Table 10, 11 | show | \<1 |
| #4 | Dynamic Activity Recognition (Physical, One accelormeter) | Table 10, 11 | show | \<1 |
| #5 | Activity Recognition (Physical, One accelormeter) | Table 12 | show | \<1 |
| #6 | Activity Recognition (Physical, One accelormeter, including gravity feature for static activities) | Table 12 | show | \<1 |
| #7 | Activity Recognition (Physical, Two accelormeter, Only waist combinations) | Table 12, 13 | show | \<1 |
| #8 | Activity Recognition (Physical, Two accelormeter, Only waist combinations, including gravity feature for static activities) | Table 12, 13 | show | \<1 |
| #9 | Position Recognition (Randomly, One accelormeter) | Table 12, 13 | show | \<1 |
| #10 | Position Recognition (L1O, One accelormeter) | Table 12, 13 | show | \<1 |
| #11 | Position Recognition (Top-Pairs, One accelormeter) | Table 12, 13 | show | \<1 |
| #12 | Position Recognition (Physical, One accelormeter) | Table 12, 13 | show | \<1 |

______________________________________________________________________

## Self-Tracking Reloaded: Applying Process Mining to Personalized Health Care from Labeled Sensor Data (2016)

*Using current devices such as smart-phones and smart-watches, an individual can easily record detailed data from her daily life.*

**Überblick:**
Das Projekt beschäftigt sich mit der Förderung der personalisierten Gesundheitsversorgung. Die Ergebnisse stammen aus der Veröffentlichung *Self-Tracking Reloaded: Applying Process Mining to Personalized Health Care from Labeled Sensor Data*. Die Seite liefert zusätzliche Materialien, einschließlich personaler Prozesskarten und Trace Alignment Clustering-Ergebnisse.

**Hinweis:**
Die XES-Dateien stammen von anderen Forschern. Der ursprüngliche Datensatz „Activity Log UCI“ wurde von [Ordóñez et al.](https://dx.doi.org/10.3390/s130505460) erstellt.

**Personal Processes (Fuzzy Model)**
| #1 | Main personal activity for all users during the working days (frequency) | 6.2 | show (PDF, 5 kB) |
| #2 | Main personal activity for all users during the weekend days (frequency) | 6.2 | show (PDF, 5 kB) |
| #3 | Main personal activity for all users during the working days (duration) | 6.2 | show (PDF, 5 kB) |
| #4 | Main personal activity for all users during the weekend days (duration) | 6.2 | show (PDF, 6 kB) |

**Personal Process Models (XES)**
| #1 | Activity Log UCI Detailed (during the week) | 6.2 | show |
| #2 | Activity Log UCI Detailed (Weekend) | 6.2 | show |
| #3 | hh102 (during the week) | 6.2 | show |
| #4 | hh102 (Weekend) | 6.2 | show |
| #5 | hh104 (during the week) | 6.2 | show |
| #6 | hh104 (Weekend) | 6.2 | show |
| #7 | hh110 (during the week) | 6.2 | show |
| #8 | hh110 (Weekend) | 6.2 | show |

**Trace Alignment**
| #1 | Clustered Traces, Subject 1 (based on our data set) | 7 | show |

______________________________________________________________________

## Unsupervised Recognition of Interleaved Activities of Daily Living through Ontological and Probabilistic Reasoning

*Recognition of activities of daily living (ADLs) is an enabling technology for several ubiquitous computing applications.*

**Überblick:**
Dieses Projekt adressiert das Problem der Datenerfassung für ADLs. Die Ergebnisse stammen aus der Veröffentlichung *Unsupervised Recognition of Interleaved Activities of Daily Living through Ontological and Probabilistic Reasoning*. Die resultierenden Dateien enthalten die Testergebnisse für jeden einzelnen Patienten/Tag, einschließlich sensor- und instanzbasierter Ergebnisse.

**Setup:**

- **MLNnc Solver:** [show](http://executor.informatik.uni-mannheim.de/systems/n-rockit/)
- **Ontology:** [show](https://www.uni-mannheim.de/media/Einrichtungen/dws/Files_Research/Projects/sensor/results/riboni2016unsupervised/ont/adlont.owl)

**Datasets:**

### WSU CASAS Dataset

- **MLNnc Model:** [show](https://www.uni-mannheim.de/media/Einrichtungen/dws/Files_Research/Projects/sensor/results/riboni2016unsupervised/mln/casas.mln)
- **Probabilities (Ontology-based):** [show](https://www.uni-mannheim.de/media/Einrichtungen/dws/Files_Research/Projects/sensor/results/riboni2016unsupervised/ont/priorprobontology.kb)
- **Dataset (External Link):** [show](https://www.uni-mannheim.de/media/Einrichtungen/dws/Files_Research/Projects/sensor/results/riboni2016unsupervised/ont/priorprobontology.kb)
  | #1 | Probabilities derived from our ontology | Table II,III | show |
  | #2 | Probabilities derived from the data set | Table II,III | show |

### SmartFaber Dataset

- **MLNnc Model:** [show](https://www.uni-mannheim.de/media/Einrichtungen/dws/Files_Research/Projects/sensor/results/riboni2016unsupervised/mln/smartfaber.mln)
- **Probabilities (Ontology-based):** Comming soon
- **Dataset:** Not publicly available due to data privacy
  | #1 | Probabilities derived from our ontology | Table IV,V | show |
  | #2 | Probabilities derived from the data set | Table IV,V | show |

______________________________________________________________________

## On-body Localization of Wearable Devices: An Investigation of Position-Aware Activity Recognition (2016)

*Human activity recognition using mobile device sensors is an active area of research in pervasive computing.*

**Überblick:**
Dieses Projekt zielt darauf ab, Aktivitätserkennungsansätze zu implementieren, die für reale Situationen geeignet sind, indem der Fokus auf der Erkennung der Position des Mobilgeräts am Körper liegt. Die Ergebnisse stammen aus der Veröffentlichung *On-body Localization of Wearable Devices: An Investigation of Position-Aware Activity Recognition*. Die resultierenden Dateien enthalten die Testergebnisse für jeden einzelnen Probanden (nicht aggregiert).

**Ergebnisse nach Klassifikator:**

**Random Forest**
| #1 | Position Detection (all activities) | Table II | show |
| #2 | Position Detection (only static activities) | Table III | show |
| #3 | Position Detection (only static activities) incl. gravity feature | Table IV | show |
| #4 | Position Detection (only dynamic activities) | Table III | show |
| #5 | Position Detection (activity-level dependend) | Table VI | see #3,#4 |
| #6 | Activity Recognition (single classifier, all activities) | Table VII,VIII | show |
| #7 | Activity Recognition (assumption: position is known for sure, all activities) | - | show |
| #8 | Activity Recognition (based on the position detection result of RF, incl. all mistakes) | Table IX,X | show |
| #9 | Distinction between static and dynamic activity (all activities) | Table V | show |

**Naive Bayes**
| #1 | Position Detection (all activities) | Table II | show |
| #2 | Position Detection (only static activities) | Table III | show |
| #3 | Position Detection (only static activities) incl. gravity feature | Table IV | show |
| #4 | Position Detection (only dynamic activities) | Table III | show |
| #5 | Position Detection (activity-level dependend) | Table VI | see #3,#4 |
| #6 | Activity Recognition (single classifier, all activities) | Table VII,VIII | show |
| #7 | Activity Recognition (assumption: position is known for sure, all activities) | - | show |
| #8 | Activity Recognition (based on the position detection result of RF, incl. all mistakes) | Table IX,X | show |
| #9 | Distinction between static and dynamic activity (all activities) | Table V | show |

**Artificial Neural Network**
| #1 | Position Detection (all activities) | Table II | show |
| #2 | Position Detection (only static activities) | Table III | show |
| #3 | Position Detection (only static activities) incl. gravity feature | Table IV | show |
| #4 | Position Detection (only dynamic activities) | Table III | show |
| #5 | Position Detection (activity-level dependend) | Table VI | see #3,#4 |
| #6 | Activity Recognition (single classifier, all activities) | Table VII,VIII | show |
| #7 | Activity Recognition (assumption: position is known for sure, all activities) | - | show |
| #8 | Activity Recognition (based on the position detection result of RF, incl. all mistakes) | Table IX,X | show |
| #9 | Distinction between static and dynamic activity (all activities) | Table V | show |

**Decision Tree**
| #1 | Position Detection (all activities) | Table II | show |
| #2 | Position Detection (only static activities) | Table III | show |
| #3 | Position Detection (only static activities) incl. gravity feature | Table IV | show |
| #4 | Position Detection (only dynamic activities) | Table III | show |
| #5 | Position Detection (activity-level dependend) | Table VI | see #3,#4 |
| #6 | Activity Recognition (single classifier, all activities) | Table VII,VIII | show |
| #7 | Activity Recognition (assumption: position is known for sure, all activities) | - | show |
| #8 | Activity Recognition (based on the position detection result of RF, incl. all mistakes) | Table IX,X | show |
| #9 | Distinction between static and dynamic activity (all activities) | Table V | show |

**k-Nearest-Neighbor**
| #1 | Position Detection (all activities) | Table II | show |
| #2 | Position Detection (only static activities) | Table III | show |
| #3 | Position Detection (only static activities) incl. gravity feature | Table IV | show |
| #4 | Position Detection (only dynamic activities) | Table III | show |
| #5 | Position Detection (activity-level dependend) | Table VI | see #3,#4 |
| #6 | Activity Recognition (single classifier, all activities) | Table VII,VIII | show |
| #7 | Activity Recognition (assumption: position is known for sure, all activities) | - | show |
| #8 | Activity Recognition (based on the position detection result of RF, incl. all mistakes) | Table IX,X | show |
| #9 | Distinction between static and dynamic activity (all activities) | Table V | show |

**Support Vector Machine**
| #1 | Position Detection (all activities) | Table II | show |
| #2 | Position Detection (only static activities) | Table III | show |
| #3 | Position Detection (only static activities) incl. gravity feature | Table IV | show |
| #4 | Position Detection (only dynamic activities) | Table III | show |
| #5 | Position Detection (activity-level dependend) | Table VI | see #3,#4 |
| #6 | Activity Recognition (single classifier, all activities) | Table VII,VIII | show |
| #7 | Activity Recognition (assumption: position is known for sure, all activities) | - | show |
| #8 | Activity Recognition (based on the position detection result of RF, incl. all mistakes) | Table IX,X | show |
| #9 | Distinction between static and dynamic activity (all activities) | Table V | show |
