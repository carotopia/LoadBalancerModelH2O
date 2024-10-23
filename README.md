# Project: DDoS Detection using H2O and Random Forest

This project uses **H2O** to train a Random Forest model to detect DDoS attacks in a network traffic dataset.

## Prerequisites

Before running the script, make sure you have the following prerequisites installed:

1. **Java 8 or higher**: H2O requires a Java installation.

   - You can check if you have Java installed by running in the terminal:
     ```bash
     java -version
     ```
   - If you don’t have Java installed, you can download it [here](https://www.oracle.com/java/technologies/javase-jdk8-downloads.html).

2. **H2O**: H2O is a machine learning platform that can be installed via `pip`.

   - Install H2O with the following command:
     ```bash
     pip install h2o
     ```

## Dataset

The dataset used for this project is part of the **CICIDS 2019 DDoS** dataset. Due to its large size, it is not included in the repository. You can download the file from the following link:

[Download dataset](https://www.unb.ca/cic/datasets/ddos-2019.html)

Once downloaded, place the file `Friday-WorkingHours-Afternoon-DDos_cleaned.csv` in your desired directory.

## Usage Instructions

1. **Install dependencies**: After installing Java and H2O, ensure you have a Python environment set up.

   - If you don’t have a virtual environment set up, you can create and activate one as follows:
     ```bash
     python -m venv venv
     source venv/bin/activate  # On Linux/MacOS
     venv\Scripts\activate  # On Windows
     ```

2. **Run the script**:

   - The script loads the dataset, trains a Random Forest model, and saves it to a specified path. You can run it by executing the Python script in your terminal:
     ```bash
     python your_script_name.py
     ```

   Make sure to update the path in the script where the dataset is located if needed.

## Script Overview

The script follows these steps:

1. **Initialize H2O**:
   ```python
   h2o.init()
