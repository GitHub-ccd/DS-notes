# Section 12 — Convolutional Neural Networks

Convolutional layers, pooling, data augmentation, building CNNs with Keras, and visualising activations.

## Notebooks

| Notebook | Topic |
|----------|-------|
| `01_cnn_introduction.ipynb` | Section introduction |
| `02_convolutional_neural_networks.ipynb` | Convolutions, filters, pooling — the CNN building blocks |
| `03_convolutional_neural_networks_codealong.ipynb` | Building a CNN end-to-end with Keras and `ImageDataGenerator` |
| `04_building_a_cnn_from_scratch.ipynb` | Building a CNN from scratch on chest X-ray data |
| `05_visualizing_activation_functions_lab.ipynb` | Visualising activation functions lab |
| `06_visualizing_intermediate_activations.ipynb` | Visualising what each layer learns |
| `07_cnn_recap.ipynb` | Section recap |

## 2026 Context

CNNs remain the standard for tasks where spatial locality matters and dataset size is insufficient for transformers. However, **Vision Transformers (ViT)** now match or beat CNNs on image classification benchmarks when sufficient data is available.

- **Custom CNNs** (as built here) — good for learning; rarely built from scratch in production
- **Pretrained CNNs** (ResNet, EfficientNet, ConvNeXt) — the standard starting point for image tasks via `torchvision.models` or HuggingFace; see Section 13
- **Vision Transformers (ViT, CLIP)** — use when you have large datasets or need image-text alignment

In PyTorch: `torchvision.models` provides pretrained ResNet, EfficientNet, and ViT. HuggingFace `transformers` provides ViT, CLIP, and DINO.