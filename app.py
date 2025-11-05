import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import numpy as np
import cv2
from PIL import Image
from keras.models import load_model
from keras.preprocessing.image import load_img, img_to_array

# Set page configuration
st.set_page_config(page_title="Health Assistant",
                   layout="wide",
                   page_icon="🧑‍⚕️")

    
# getting the working directory of the main.py
working_dir = os.path.dirname(os.path.abspath(__file__))

# loading the saved models

diabetes_model = pickle.load(open(f'{working_dir}/saved_models/diabetes_model.sav', 'rb'))

heart_disease_model = pickle.load(open(f'{working_dir}/saved_models/heart_disease_model.sav', 'rb'))

parkinsons_model = pickle.load(open(f'{working_dir}/saved_models/parkinsons_model.sav', 'rb'))

carotid_artery_model = load_model(f'{working_dir}/saved_models/carotid_artery_model.h5')

# sidebar for navigation
with st.sidebar:
    selected = option_menu('Smart Disease Detection Hub',

                           ['Carotid Artery Diagnosis','Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Prediction'],
                           menu_icon='hospital-fill',
                           icons=['camera','activity', 'heart', 'person'],
                           default_index=0)


# Diabetes Prediction Page
if selected == 'Diabetes Prediction':

    # page title
    st.title('Diabetes Prediction')

    # getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')

    with col2:
        Glucose = st.text_input('Glucose Level')

    with col3:
        BloodPressure = st.text_input('Blood Pressure value')

    with col1:
        SkinThickness = st.text_input('Skin Thickness value')

    with col2:
        Insulin = st.text_input('Insulin Level')

    with col3:
        BMI = st.text_input('BMI value')

    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')

    with col2:
        Age = st.text_input('Age of the Person')


    # code for Prediction
    diab_diagnosis = ''

    # creating a button for Prediction

    if st.button('Diabetes Test Result'):

        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
                      BMI, DiabetesPedigreeFunction, Age]

        user_input = [float(x) for x in user_input]

        diab_prediction = diabetes_model.predict([user_input])

        if diab_prediction[0] == 1:
            diab_diagnosis = 'The person is diabetic'
        else:
            diab_diagnosis = 'The person is not diabetic'

    st.success(diab_diagnosis)

# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':

    # page title
    st.title('Heart Disease Prediction')

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')

    with col2:
        sex = st.text_input('Sex')

    with col3:
        cp = st.text_input('Chest Pain types')

    with col1:
        trestbps = st.text_input('Resting Blood Pressure')

    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')

    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')

    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')

    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')

    with col3:
        exang = st.text_input('Exercise Induced Angina')

    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')

    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')

    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')

    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

    # code for Prediction
    heart_diagnosis = ''

    # creating a button for Prediction

    if st.button('Heart Disease Test Result'):

        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

        user_input = [float(x) for x in user_input]

        heart_prediction = heart_disease_model.predict([user_input])

        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person is having heart disease'
        else:
            heart_diagnosis = 'The person does not have any heart disease'

    st.success(heart_diagnosis)

# Parkinson's Prediction Page
if selected == "Parkinsons Prediction":

    # page title
    st.title("Parkinson's Disease Prediction")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')

    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')

    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')

    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')

    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')

    with col1:
        RAP = st.text_input('MDVP:RAP')

    with col2:
        PPQ = st.text_input('MDVP:PPQ')

    with col3:
        DDP = st.text_input('Jitter:DDP')

    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')

    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')

    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')

    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')

    with col3:
        APQ = st.text_input('MDVP:APQ')

    with col4:
        DDA = st.text_input('Shimmer:DDA')

    with col5:
        NHR = st.text_input('NHR')

    with col1:
        HNR = st.text_input('HNR')

    with col2:
        RPDE = st.text_input('RPDE')

    with col3:
        DFA = st.text_input('DFA')

    with col4:
        spread1 = st.text_input('spread1')

    with col5:
        spread2 = st.text_input('spread2')

    with col1:
        D2 = st.text_input('D2')

    with col2:
        PPE = st.text_input('PPE')

    # code for Prediction
    parkinsons_diagnosis = ''

    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):

        user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs,
                      RAP, PPQ, DDP,Shimmer, Shimmer_dB, APQ3, APQ5,
                      APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]

        user_input = [float(x) for x in user_input]

        parkinsons_prediction = parkinsons_model.predict([user_input])

        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease"

    st.success(parkinsons_diagnosis)

# Carotid Artery Diagnosis Page
if selected == "Carotid Artery Diagnosis":
    st.title("Carotid Artery Diagnosis")

    # Image upload functionality
    uploaded_file = st.file_uploader("Upload an Ultrasound Image of the Carotid Artery", type=["jpg", "jpeg", "png", "bmp", "tiff"])

    # If an image is uploaded, display it
    if uploaded_file is not None:
        # Load and resize the image to a more manageable size
        image = Image.open(uploaded_file)
        image = image.resize((800, 600))  # Resize to a suitable size for display
        st.image(image, caption="Uploaded Image")

        # Button for prediction
        if st.button("Analyze Carotid Artery"):
            # Step 1: Load and Preprocess New Images for Prediction
            def load_and_preprocess_image(img_path, img_size=(128, 128)):
                img = load_img(img_path, target_size=img_size)
                img = img_to_array(img) / 255.0  # Normalize to [0,1]
                return np.expand_dims(img, axis=0)  # Add batch dimension

            # Step 2: Predicting on a New Image
            new_image_path = uploaded_file  # Image path
            new_image = load_and_preprocess_image(new_image_path)

            # Step 3: Make Predictions
            predicted_mask = carotid_artery_model.predict(new_image)

            # Step 4: Post-process the Output
            predicted_mask = np.squeeze(predicted_mask)  # Remove batch dimension
            predicted_mask = (predicted_mask * 255).astype(np.uint8)  # Convert to 0-255 range

            # Ensure the predicted_mask is binary (0 or 255)
            _, binary_mask = cv2.threshold(predicted_mask, 127, 255, cv2.THRESH_BINARY)

            # Step 5: Find the Boundary of the Predicted Mask
            def find_mask_boundary(mask):
                if mask.ndim == 3:  # If mask is 3D (e.g., RGB)
                    mask = cv2.cvtColor(mask, cv2.COLOR_RGB2GRAY)  # Convert to grayscale
                _, binary_mask = cv2.threshold(mask, 127, 255, cv2.THRESH_BINARY)
                # Find contours
                contours, _ = cv2.findContours(binary_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
                # Create an empty image for the boundary
                boundary_image = np.zeros_like(mask)
                # Draw contours on the boundary image in red
                cv2.drawContours(boundary_image, contours, -1, (255, 0, 0), thickness=2)  # Red boundary (BGR format)
                return boundary_image

            # Get the mask boundary
            mask_boundary = find_mask_boundary(predicted_mask)

            # Step 6: Overlay the Mask and Boundary on the Original Image
            def overlay_mask_and_boundary(original_image_path, predicted_mask, mask_boundary):
                # Load and convert the original image to a NumPy array
                original_image = img_to_array(load_img(original_image_path)) / 255.0  # Normalize to [0, 1]
                # Resize predicted mask and mask boundary to match original image size
                original_height, original_width, _ = original_image.shape
                predicted_mask_resized = cv2.resize(predicted_mask, (original_width, original_height))
                mask_boundary_resized = cv2.resize(mask_boundary, (original_width, original_height))
                # Create an overlay by blending the original image and mask boundary
                overlay = original_image.copy()
                overlay[mask_boundary_resized > 0] = [1, 0, 0]  # Set boundary pixels to red
                return overlay, original_image

            # Create the overlay
            overlay_image, original_image = overlay_mask_and_boundary(new_image_path, predicted_mask, mask_boundary)

            # Step 7: Extract the Image Segment Enclosed by the Mask
            def extract_segment(original_image, binary_mask):
                # Resize the binary mask to match the original image dimensions
                original_height, original_width, _ = original_image.shape
                binary_mask_resized = cv2.resize(binary_mask, (original_width, original_height))
                # Create an empty image to hold the segmented region
                segmented_image = np.zeros_like(original_image)
                # Apply the binary mask to the original image
                segmented_image[binary_mask_resized > 0] = original_image[binary_mask_resized > 0]
                return segmented_image

            # Extract the image segment that is enclosed by the mask boundary
            segmented_image = extract_segment(original_image, binary_mask)

            col1, col2, col3 = st.columns(3)

            # Display the results

            # Define a fixed width and height for the images to ensure they align
            image_width = 709  # Adjust the width as needed
            image_height = 749  # Adjust the height as needed

            # Resize the images to the desired size
            image = image.resize((image_width, image_height))
            

            with col1:
                st.subheader("Original Ultrasound Image ")
                st.image(image, caption="Original Ultrasound Image")
            
            with col2:
                st.subheader("Predicted Mask with Boundary")
                st.image(overlay_image, caption="Predicted Mask with Boundary")
            
            with col3:
                st.subheader("Extracted Segmented Region")
                st.image(segmented_image, caption="Segmented Region")

            st.success("Carotid Artery Analysis Completed")


