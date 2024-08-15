# -INSURANCE-CHARGE-PREDICTOR
![python_pro](https://github.com/user-attachments/assets/da32ff1f-198e-4061-9bf2-3c6028a94e58)
## Project Description

This project is a GUI-based application that predicts insurance charges based on user input. It utilizes a Linear Regression model trained on a dataset of insurance charges along with various factors that affect them.

### Files Used in the Project

1. **Insurance.csv**: The dataset used to train the Linear Regression model.
2. **Logo.png**: The logo image used in the GUI.
3. **Main.py**: The Python script containing the code for the GUI and the Linear Regression model.
4. **Requirements.txt**: A list of the required Python packages and their versions.

### Project Features

- **GUI Creation**: Developed using Tkinter.
- **Data Processing**: Handled with Pandas and NumPy.
- **Machine Learning**: Implemented using Scikit-learn (Sklearn).
- **Image Handling**: Managed with PIL (Pillow).

## Key Sections

### Imports the Necessary Libraries

- **For GUI**: 
  - `tkinter` (TK)
  - `PIL` (Pillow)
  
- **For Data Handling**: 
  - `pandas`
  - `numpy`
  
- **For Machine Learning**: 
  - `scikit-learn` (Sklearn)

### Data Loading and Processing

- The dataset (`Insurance.csv`) is loaded using Pandas.
- Categorical variables (such as sex, smoking status, and region) are encoded using `LabelEncoder` to convert them into a numerical format suitable for model training.

### Model Training

- Features such as age, sex, BMI, children, smoking status, and region are used to train a Linear Regression model.

### GUI Setup

- The `tkinter` library is used to create a form where users can input their details (e.g., name, gender, age, BMI, number of children, smoker status, region).
- **Prediction Function (`submit_form`)**:
  - Retrieves user input from the GUI.
  - Encodes categorical inputs to match the model's expectations.
  - Uses the trained model to predict insurance charges.
  - Displays the predicted charge along with the user's input details in a message box.

### Dataset: `Insurance.csv`

- **Purpose**: Stores the dataset used for training the machine learning model.

## Key Calculations

### Label Encoding

- **Purpose**: Converts categorical variables like sex, smoker, and region into numerical values for use by the machine learning model.
- **Example**:
  ```python
  df['sex'] = sex_encoder.transform(df['sex'])
