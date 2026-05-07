# Section 07 — NLP (Legacy NLTK + Modern Transformers)

Regular expressions, NLTK, word vectorisation, text classification, and an introduction to the modern HuggingFace NLP stack.

## Notebooks

| Notebook | Topic |
|----------|-------|
| `01_context_free_grammars_and_POS_tagging.ipynb` | Parts of speech, parse trees, context-free grammars |
| `02_context_free_grammars_codealong.ipynb` | CFG codealong |
| `03_corpus_statistics_lab.ipynb` | Corpus statistics lab |
| `04_feature_engineering_for_text_data.ipynb` | Feature engineering — n-grams, vocabulary, character features |
| `05_introduction_to_nltk.ipynb` | NLTK — tokenisation, stemming, lemmatisation, stopwords |
| `06_introduction_to_regular_expressions.ipynb` | Regular expressions — fully current for text preprocessing |
| `07_nlp_and_word_vectorization.ipynb` | Bag-of-words and TF-IDF — sparse text representations |
| `08_nlp_section_intro.ipynb` | Section introduction |
| `09_nlp_section_recap.ipynb` | Section recap |
| `10_regular_expressions_codealong.ipynb` | Regular expressions codealong |
| `11_text_classification_lab.ipynb` | Text classification lab |
| `12_text_classification.ipynb` | TF-IDF + logistic regression / Naive Bayes pipeline |
| `13_word_vectorization_lab.ipynb` | Word vectorisation lab |
| `14_transformers_huggingface.ipynb` | HuggingFace `transformers` — the 2026 NLP entry point |

## 2026 Context

> **Legacy note:** Notebooks 01–13 cover NLTK-based NLP — tokenisation, POS tagging, TF-IDF, bag-of-words, context-free grammars. These are foundational concepts worth understanding, but NLTK is no longer the primary production NLP tool. The field has moved to transformer-based models via the HuggingFace ecosystem.

`14_transformers_huggingface.ipynb` is the 2026 starting point: `pipeline` API for sentiment analysis, NER, and zero-shot classification; fine-tuning DistilBERT; sentence embeddings with `sentence-transformers`; production NLP with `spaCy`. For deeper coverage see Module 05 Sections 01 and 02.