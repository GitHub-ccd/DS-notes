# Section 08 — Neural Networks

Forward and backpropagation, building networks with Keras, and an introduction to deep learning fundamentals.

## Notebooks

| Notebook | Topic |
|----------|-------|
| `01_introduction_to_keras_lab.ipynb` | Keras introduction lab |
| `02_introduction_to_keras.ipynb` | Tensors, tensor operations, Keras model building |
| `03_introduction_to_neural_networks_lab.ipynb` | Neural networks from scratch lab |
| `04_introduction_to_neural_networks.ipynb` | Forward propagation, backpropagation, network types |
| `05_neural_networks_section_intro.ipynb` | Section introduction |
| `06_neural_networks_section_recap.ipynb` | Section recap |

## 2026 Context

This section uses **Keras** (now `tf.keras` inside TensorFlow). Keras remains a solid high-level API for learning neural networks. However, **PyTorch** has become the dominant framework in research and is equally common in production — most new papers, HuggingFace models, and ML engineering roles use PyTorch.

| | Keras / TensorFlow | PyTorch |
|---|---|---|
| Style | High-level, declarative | Imperative (Pythonic) |
| Debugging | Harder (graph execution) | Easier (eager by default) |
| Research adoption | Declining | Dominant |
| HuggingFace | Supported | Primary backend |

Learn the concepts here with Keras, then transfer to PyTorch when working with HuggingFace models or reading research code. `pip install torch torchvision`