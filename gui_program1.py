import tkinter as tk
from tkinter import ttk, messagebox
from PIL import ImageTk, Image
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression

# Load and preprocess the dataset
df = pd.read_csv('insurance.csv')

# Ensure that the classes are properly defined and used in the encoders
df['sex'] = df['sex'].str.title()
sex_encoder = LabelEncoder()
sex_encoder.classes_ = np.array(['Female', 'Male'])  # Specify possible classes in alphabetical order
df['sex'] = sex_encoder.transform(df['sex'])

df['smoker'] = df['smoker'].str.title()
smoker_encoder = LabelEncoder()
smoker_encoder.classes_ = np.array(['No', 'Yes'])  # Specify possible classes in alphabetical order
df['smoker'] = smoker_encoder.transform(df['smoker'])

df['region'] = df['region'].str.lower()
region_encoder = LabelEncoder()
region_encoder.classes_ = np.array(['northeast', 'northwest', 'southeast', 'southwest'])  # Specify possible classes in alphabetical order
df['region'] = region_encoder.transform(df['region'])

# Prepare independent and dependent variables
X = df[["age", "sex", "bmi", "children", "smoker", "region"]]
y = df["charges"]

# Train the Linear Regression model
model = LinearRegression()
model.fit(X, y)

# Create the main application window
root = tk.Tk()

# Function to display the information provided by the user and make a prediction
def submit_form():
    # Retrieve input values from the GUI
    name = name_input.get()
    gender = gender_combobox.get().capitalize()  # Ensure 'Male' or 'Female'
    age = int(age_input.get())
    bmi = float(bmi_input.get())
    children = int(noofchildren_input.get())
    smoker = Smoker_combobox.get().capitalize()  # Ensure 'Yes' or 'No'
    region = region_combobox.get().lower()  # Ensure lowercase values

    # Encode categorical inputs
    try:
        gender_encoded = sex_encoder.transform([gender])[0]
        smoker_encoded = smoker_encoder.transform([smoker])[0]
        region_encoded = region_encoder.transform([region])[0]
    except ValueError as e:
        messagebox.showerror("Error", f"Invalid input value: {e}")
        return

    # Create a DataFrame for the new input
    new_data = pd.DataFrame({
        "age": [age],
        "sex": [gender_encoded],
        "bmi": [bmi],
        "children": [children],
        "smoker": [smoker_encoded],
        "region": [region_encoded]
    })

    # Make a prediction
    predicted_charge = model.predict(new_data)[0]

    # Display the information and prediction
    info = (f"Name: {name}\n"
            f"Gender: {gender}\n"
            f"Age: {age}\n"
            f"BMI: {bmi}\n"
            f"No. of Children: {children}\n"
            f"Smoker: {smoker}\n"
            f"Region: {region}\n"
            f"Predicted Insurance Charge: ${predicted_charge:.2f}")
    
    messagebox.showinfo("Submitted Information", info)

# Set up the GUI
root.title('Insurance Charge Predictor')
root.geometry('500x950')
root.configure(background='#0096DC')

# Logo
img = Image.open('logo.png')
resized_img = img.resize((100, 100))
img = ImageTk.PhotoImage(resized_img)
img_label = tk.Label(root, image=img, bg='#0096DC')
img_label.pack(pady=(10, 10))

# Titles and Labels
text_label = tk.Label(root, text='Insurance Charge Predictor', fg='White', bg='#0096DC')
text_label.pack()
text_label.config(font=('Cursive', 20))

text_label = tk.Label(root, text='Enter Details Properly', fg='White', bg='#0096DC')
text_label.pack()
text_label.config(font=('Cursive', 12))

# Name
name_label = tk.Label(root, text='Name', fg='White', bg='#0096DC')
name_label.pack(pady=(20, 5))
name_label.config(font=('Cursive', 10))
name_input = tk.Entry(root, width=50)
name_input.pack(ipady=6, pady=(1, 15))

# Gender
gender_label = tk.Label(root, text='Gender', fg='White', bg='#0096DC')
gender_label.pack(pady=(15, 5))
gender_label.config(font=('Cursive', 10))
gender_combobox = ttk.Combobox(root, width=20, values=('Male', 'Female'), state='readonly')
gender_combobox.pack()
gender_combobox.config(font=('Cursive', 10))

# Age
age_label = tk.Label(root, text='Age', fg='White', bg='#0096DC')
age_label.pack(pady=(20, 5))
age_label.config(font=('Cursive', 10))
age_input = tk.Entry(root, width=50)
age_input.pack(ipady=6, pady=(1, 15))

# BMI
bmi_label = tk.Label(root, text='Body Mass Index (BMI)', fg='White', bg='#0096DC')
bmi_label.pack(pady=(20, 5))
bmi_label.config(font=('Cursive', 10))
bmi_input = tk.Entry(root, width=50)
bmi_input.pack(ipady=6, pady=(1, 15))

# No. of Children
noofchildren_label = tk.Label(root, text='No. Of Children You Have', fg='White', bg='#0096DC')
noofchildren_label.pack(pady=(5, 5))
noofchildren_label.config(font=('Cursive', 10))
noofchildren_input = tk.Entry(root, width=50)
noofchildren_input.pack(ipady=6, pady=(1, 15))

# Smoker
Smoker_label = tk.Label(root, text='Smoker', fg='White', bg='#0096DC')
Smoker_label.pack(pady=(10, 5))
Smoker_label.config(font=('Cursive', 10))
Smoker_combobox = ttk.Combobox(root, width=20, values=('Yes', 'No'), state='readonly')
Smoker_combobox.pack()
Smoker_combobox.config(font=('Cursive', 10))

# Region
region_label = tk.Label(root, text='Region', fg='White', bg='#0096DC')
region_label.pack(pady=(15, 5))
region_label.config(font=('Cursive', 10))
region_combobox = ttk.Combobox(root, width=20, values=('northeast', 'northwest', 'southeast', 'southwest'), state='readonly')
region_combobox.pack()
region_combobox.config(font=('Cursive', 10))

# Submit Button
submit_button = tk.Button(root, text="Submit", command=submit_form, bg='White', fg='black', width=15, height=2)
submit_button.pack(pady=(10, 20))
submit_button.config(font=('Cursive', 10))

root.mainloop()
