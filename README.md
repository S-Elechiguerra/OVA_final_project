
![OVA](https://github.com/user-attachments/assets/fa50cc72-3867-438b-9844-718ec5900789)

# Breast Cancer Predictor Model and Virtual Assistant for Oncologists: OVA
Prevalence: Breast cancer is one of the most common cancers among women worldwide, with an estimated 2.3 million new cases diagnosed in 2020.

Survival Rate: Early detection significantly improves survival rates. The 5-year relative survival rate for localized breast cancer is 99%.

Risk Factors: Major risk factors include age, genetic predisposition, lifestyle factors, and hormonal influences.

Preventive Measures: Regular screening, maintaining a healthy diet, regular exercise, and avoiding smoking can reduce the risk of developing breast cancer.

Innovation: Advances in technology, such as AI and machine learning, are revolutionizing cancer detection and treatment, making personalized medicine more accessible and effective.

# Overview
This project combines machine learning and artificial intelligence to assist oncologists in predicting breast cancer and providing personalized patient recommendations. The core component is a predictive model that analyzes patient data to forecast the likelihood of breast cancer. Complementing this model is a chatbot, which facilitates smooth communication between oncologists and their patients, offering guidance and tailored advice.


## Project Components
# Data Set:
Dataset Information
Additional Information

Samples arrive periodically as Dr. Wolberg reports his clinical cases. The database therefore reflects this chronological grouping of the data. This grouping information appears immediately below, having been removed from the data itself:

Group 1: 367 instances (January 1989)
Group 2:  70 instances (October 1989)
Group 3:  31 instances (February 1990)
Group 4:  17 instances (April 1990)
Group 5:  48 instances (August 1990)
Group 6:  49 instances (Updated January 1991)
Group 7:  31 instances (June 1991)
Group 8:  86 instances (November 1991)
-----------------------------------------
Total:   699 points (as of the donated datbase on 15 July 1992)

Note that the results summarized above in Past Usage refer to a dataset of size 369, while Group 1 has only 367 instances.  This is because it originally contained 369 instances; 2 were removed.  The following statements summarizes changes to the original Group 1's set of data:

#####  Group 1 : 367 points: 200B 167M (January 1989)

#####  Revised Jan 10, 1991: Replaced zero bare nuclei in 1080185 & 1187805

#####  Revised Nov 22,1991: Removed 765878,4,5,9,7,10,10,10,3,8,1 no record
#####                  : Removed 484201,2,7,8,8,4,3,10,3,4,1 zero epithelial
#####                  : Changed 0 to 1 in field 6 of sample 1219406
#####                  : Changed 0 to 1 in field 8 of following sample:
#####                  : 1182404,2,3,1,1,1,2,0,1,1,1

# Predictive Model:

The model employs statistical features and other significant measures derived from medical data and screening.
![1](https://github.com/user-attachments/assets/b3bc4927-6ed7-4daa-a7a5-2d2baf9e5493)

![2](https://github.com/user-attachments/assets/1687570f-d45d-4b7f-b992-ca7ef8f68862)



By applying techniques like GridSearchCV for hyperparameter tuning, the model achieves high accuracy in predicting tumour malignancy.

It uses Logistic Regression and SVC models to ensure robust performance across different datasets.


![my_plot_presentation](https://github.com/user-attachments/assets/06be56cb-c513-499b-9a0a-a438897df03d)


# Integration:

Our Virtual Assistant and Predictor Model provide real-time predictions and detailed health advice, making it easier for oncologists to communicate critical information to patients.
Patients receive tailored recommendations based on their prediction outcomes, enhancing their understanding and management of their health.

# Promptly Virtual Assistant:

It ensures the application is easily deployable and consistent across various environments.
This guarantees that the Virtual Assistant runs smoothly regardless of the underlying infrastructure.

# Technical Highlights:

Feature Engineering: The model uses carefully selected features that have significant predictive power for breast cancer.
Cross-Validation: This technique ensures that the model generalizes well to unseen data, enhancing its reliability.
Health Recommendations: Based on the prediction, the system provides actionable health advice, covering topics like treatment options, lifestyle changes, and preventive measures.

This project not only aims to improve diagnostic accuracy but also seeks to enhance patient care through intelligent automation and personalized health communication. By integrating cutting-edge AI with practical healthcare applications, it represents a significant step forward in the fight against breast cancer.

# Links
## Presentation
https://www.canva.com/design/DAGUa7EntuQ/x3sfyCBmkENSouaHTyMviA/view?utm_content=DAGUa7EntuQ&utm_campaign=designshare&utm_medium=link&utm_source=editor

## website
https://ovassist.wordpress.com/
