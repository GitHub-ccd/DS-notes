# Section 13 — Transfer Learning

Feature extraction and fine-tuning pretrained networks for image classification.

## Notebooks

| Notebook | Topic |
|----------|-------|
| `01_transfer_learning_intro.ipynb` | Section introduction |
| `02_using_pretrained_networks.ipynb` | VGG-19 on ImageNet — feature extraction vs fine-tuning |
| `03_using_pretrained_networks_codealong.ipynb` | Freezing and unfreezing layers in Keras |
| `04_image_classification_lab.ipynb` | Image classification with transfer learning lab |
| `05_transfer_learning_recap.ipynb` | Section recap |

## 2026 Context

Transfer learning is now **the default approach** for almost all deep learning tasks — training from scratch is rarely justified unless you have hundreds of millions of training examples. The freeze-then-fine-tune pattern here applies equally to modern foundation models:

- **Images:** `torchvision.models` (ResNet, EfficientNet, ViT) or HuggingFace `transformers` (`ViTForImageClassification`)
- **Text:** HuggingFace `AutoModelForSequenceClassification` with BERT/RoBERTa — freeze the base, fine-tune the classification head
- **Multimodal:** CLIP (OpenAI) — jointly trained on image and text, excellent zero-shot classifier

For parameter-efficient fine-tuning of large models (billions of parameters), see **LoRA** and **QLoRA** in Module 05 Section 06.