# Formspring Data Text Classification
This is an attempt to improve the prediction of cyberbullying using text analysis. I have used formspring data (https://www.kaggle.com/swetaagrawal/formspring-data-for-cyberbullying-detection) as the input text data. 

The data cleaning, stemming, etc is done uisng the script "extract.py". This is a highly imbalanced classificatin with ~6 % cases of cyberbullying. Currently the best ML classification is done by the script "predict.py", which stands at:
 Accuracy: 0.95201	Precision: 0.73585	Recall: 0.45349	F1: 0.56115	F2: 0.49118
