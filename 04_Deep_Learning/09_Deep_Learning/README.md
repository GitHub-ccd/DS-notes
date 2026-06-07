# Section 09 — Deep Learning

Deeper networks, activation functions, and image classification with multi-layer perceptrons.

## Notebooks

| Notebook | Topic |
|----------|-------|
| `03_deeper_neural_networks_lab.ipynb` | Deeper networks lab |
| `04_deeper_neural_networks.ipynb` | Activation functions — sigmoid, tanh, ReLU, leaky ReLU |
| `05_image_classification_with_mlps_lab.ipynb` | MNIST image classification lab |
| `06_image_classification_with_mlps.ipynb` | Multi-layer perceptrons for image classification |

## 2026 Context

MLPs (fully connected networks) are the foundation covered here. For images, **CNNs** supersede MLPs — see Section 12 (Convolutional Neural Networks). For sequences and language, **Transformers** have replaced both RNNs and MLPs — see Module 05. In PyTorch, the equivalent of a Keras `Sequential` model is `torch.nn.Sequential` or a custom `nn.Module` subclass.