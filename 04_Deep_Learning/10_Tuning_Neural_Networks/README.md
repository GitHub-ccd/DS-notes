# Section 10 — Tuning Neural Networks

Regularisation (L1/L2, dropout), batch normalisation, and end-to-end hyperparameter tuning.

## Notebooks

| Notebook | Topic |
|----------|-------|
| `01_tuning_neural_networks_from_start_to_finish_lab.ipynb` | End-to-end tuning lab |
| `02_tuning_neural_networks_intro.ipynb` | Section introduction |
| `03_tuning_neural_networks_recap.ipynb` | Section recap |
| `04_tuning_neural_networks_with_normalization_lab.ipynb` | Normalisation lab |
| `05_tuning_neural_networks_with_normalization.ipynb` | Batch normalisation — stabilising activations across layers |
| `06_tuning_neural_networks_with_regularization_lab.ipynb` | Regularisation lab |
| `07_tuning_neural_networks_with_regularization.ipynb` | L1/L2 weight regularisation and dropout |

## 2026 Context

The regularisation and normalisation concepts here apply in PyTorch exactly as in Keras. Modern additions worth knowing:

- **Learning rate schedulers** (`torch.optim.lr_scheduler`, Keras `ReduceLROnPlateau`) — decaying or cycling the learning rate often outperforms a fixed rate
- **Gradient clipping** — important for RNNs and Transformers to prevent exploding gradients
- **Hyperparameter search** — `keras-tuner`, **Optuna** (framework-agnostic, widely used), or Ray Tune for large-scale search
- **Layer normalisation** (LayerNorm) — preferred over BatchNorm in Transformer architectures