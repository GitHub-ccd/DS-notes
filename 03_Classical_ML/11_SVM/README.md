# Section 11 — Support Vector Machines

Maximum-margin classifiers, the kernel trick, and SVM in scikit-learn.

## Notebooks

| Notebook | Topic |
|----------|-------|
| `01_building_an_svm_from_scratch_lab.ipynb` | Linear SVM from scratch lab |
| `02_building_an_svm_using_scikit_learn_lab.ipynb` | SVM with scikit-learn lab |
| `03_introduction_to_support_vector_machines.ipynb` | Maximum-margin hyperplane, support vectors, soft margin (C parameter) |
| `04_kernels_in_scikit_learn_lab.ipynb` | Kernel functions lab |
| `05_svm_intro.ipynb` | Section introduction |
| `06_svm_recap.ipynb` | Section recap |
| `07_the_kernel_trick.ipynb` | Projecting to higher dimensions implicitly — RBF, polynomial, sigmoid kernels |

## 2026 Context

SVMs are less dominant than they were pre-2015. Gradient-boosted trees and neural networks outperform them on most tabular and image tasks. They remain useful for small-to-medium datasets with clear margin separation and in high-dimensional sparse spaces (e.g. text classification with TF-IDF). For SHAP explanations on SVM predictions, use `shap.KernelExplainer` (model-agnostic, slower than TreeExplainer).