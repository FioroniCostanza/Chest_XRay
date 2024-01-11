# Classifying Chest X-Ray Images Using CNN Architectures
The project aims to harness the power of Convolutional Neural Networks (CNNs) to classify chest X-ray images for various diseases. Utilizing advanced deep learning models, specifically DenseNet-121 and ResNet-50, the project seeks to improve the accuracy and efficiency of diagnosing chest-related diseases from X-ray images. These models are known for their effectiveness in image classification tasks. The project involves training and fine-tuning these models on a comprehensive dataset of chest X-ray images, aiming to establish a reliable, automated system for early and accurate disease detection in the medical imaging field.

## Dataset
The dataset for this project is a comprehensive amalgamation of three distinct datasets from Kaggle, enriched to form a new dataset with 18 classes:
- **Chest X-ray – 17 Diseases**: This dataset includes X-rays in both JPEG and DCM formats, organized into 17 folders named after specific diseases or conditions [1].
- **Chest X-Ray Images (Pneumonia)** Comprising 5863 X-ray images in JPEG format, this dataset categorizes images as either depicting pneumonia or being normal [2].
- **Tuberculosis (TB) Chest X-ray Database** Contains chest X-ray images of normal individuals (3500) and patients diagnosed with Tuberculosis [3].

From these datasets, a novel dataset was curated, improving the scope of the project to encompass 18 disease categories.

## Technologies Used
The project utilizes a range of technologies and tools for its implementation. Key technologies include:
- **TensorFlow and Keras**: For building and training the CNN models.
- **Google Colab**: Used for leveraging GPU acceleration during model training.
- **Nvidia-smi library**: Employed to speed up the training process.

## Setup

### Cloning the repository
Run this command to download the repository:`git clone https://github.com/FioroniCostanza/Chest_XRay.git`

### Dependencies
To Install the necessary libraries you just need to run their installation commands, like:
```
pip install tensorflow
pip install keras
```
already provided in this file `Xray_chest.ipynb`.

## Repository File Descriptions

### Preprocessing Scripts
The following files are used for preprocessing the dataset, ensuring it is clean and standardized for analysis:
- `black_border.py`: Script to remove black borders from images.
- `white_border.py`: Script to remove white borders from images.
- `white_boxes.py`: Script to remove white boxes from images.

### Main Project Notebook
- `Xray_chest.ipynb`: This Jupyter notebook contains the core of the project. It includes data loading, model building with CNN architectures (DenseNet-121 and ResNet-50), training, evaluation, and results presentation. All major analyses and findings of the project are documented here.

## References
1. ”Chest X-ray – 17 Diseases” Kaggle.com. [Online]. Available: https://www.kaggle.com/datasets/trainingdatapro/chest- xray- 17- diseases
2. ”Chest X-Ray Images (Pneumonia)”, Kaggle.com. [Online]. Available: https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia
3. ”Tuberculosis (TB) Chest X-ray Database”, Kaggle.com.[Online]. Available: https://www.kaggle.com/datasets/tawsifurrahman/ tuberculosis- tb- chest- xray- dataset
