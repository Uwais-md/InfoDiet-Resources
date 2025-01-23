
# Dataset Generation and Model Finetuning

This folder contains all the entities required to generate the dataset. All the python scripts are ready to be executed. The data is then saved to respective JSON file.


## Execution

1. Follow this step for generating random values of entities

```bash
# execute cmd script for entities

# For Ubuntu or Mac
cd entities
bash generate.sh

# For Windows
cd entities
generate.bat
```

2. Follow this step for mergin all the entities in single JSON file.

```python
# execute user-data.py file
python user-data.py
```
    
3. Execute the Jupyter Notebook called "text-creation.ipynb"
* This notebook utilizes Google Gemini 1.5 Flash model to generate the text, tokens, and ner tags for the dataset.
* Use Google Gemini's API key to generate the dataset.
* The generated data will be stored in respective json and csv file (texts.json and texts.csv)

4. Execute the Jupyter Notebook called "csv_to_hf_dataset.ipynb"
* This file imports the texts.csv file and converts the data into a Hugging Face compatible dataset.
* The dataset will be stored as "pii_ner_dataset" folder.

5. Model Finetuning and Data Tokenization is done using ModernBERT Base Model.
* Data_Tokenization_and_Finetuning_Modernbert_Base.ipynb
* Execute this Notebook to apply Tokenization to the dataset.
* This notebook Finetunes the ModernBERT Base model and saves the Finetuned Model in the present directory.

6. Code for utilizing finetuned version of Model is mentioned at the bottom of Data_Tokenization_and_Finetuning_Modernbert_Base.ipynb Notebook.

#### Kindly go through all the files for better understanding. Reach out to me for any doubts and clearance.

#### Currently Focusing on Effective and Balanced Dataset creation for the models