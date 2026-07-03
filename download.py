import os

destination_folder = r"C:\Users\ashup\OneDrive\Desktop\Credit Risk Model\datasets"
# kabure/german-credit-data-with-risk
os.system(
    f'kaggle datasets download -d kabure/german-credit-data-with-risk -p "{destination_folder}" --unzip'
)