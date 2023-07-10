import streamlit as st
import pickle
import streamlit_option_menu as option_manue


# dibatese_model = pickle.load(open(r"C:\Users\Dell\Desktop\New folder\model.pkl","rb"))

# with st.sidebar:
    
#     selected = option_manue('Dibatese Pridiction system',
#                  ["Dibatese Prediction using ML",
#                   "Model 1","Model 2"],defult_index = 0)

                 
import streamlit as st
import pickle

# Load the diabetes model from the pickle file
diabetes_model = pickle.load(open(r"C:\Users\Dell\Desktop\New folder\model.pkl","rb"))

# Create a sidebar with the option menu
with st.sidebar:
    selected = st.selectbox('Diabetes Prediction System',
                            ["Diabetes Prediction using ML",
                             "Model 1", "Model 2"], index=0)

# Main application
if selected == ("Diabetes Prediction using ML"):
    st.title("Dibatese Pridiction using ML")

    # excessive_thurst = st.text("Did you feel excessive thirst? \t (yes/no)")
    # urinationn = st.text("Are you experiencing frequent urination? (yes/no)")
    #  st.title('Diabetes Prediction using ML')
    
    
    # getting the input data from the user
    col1, col2 = st.columns(2)
    
    with col1:
        excessive_thurst = st.text_input('Did you feel excessive thirst ? (yes/no)')
    
    if excessive_thurst.lower() == "yes":
        excessive_thurst = 1
    elif excessive_thurst == "no":
        excessive_thurst = 0
    else:
        pass
    
        
    with col2:
        urination = st.text_input('Are you experiencing frequent urination ? (yes/no)')
    
    if urination.lower() == "yes":
        urination = 1
    elif urination == "no":
        urination = 0


    with col1:
        fatigue = st.text_input('Do you often feel fatigued or weak ? (yes/no)')

    if fatigue.lower() == "yes":
        fatigue = 1
    elif fatigue == "no":
        fatigue = 0


    
    with col2:
        glucose = st.text_input('Are you currently taking any medications that may affect blood sugar levels? (yes/no)')

    if glucose.lower() == "yes":
        glucose = 1    
    elif glucose == "no":
        glucose = 0


    with col1:
        vision_b = st.text_input('Have you noticed any vision problem or blurred vision ? (yes/no)')


    if vision_b.lower() == "yes":
        vision_b = 1
    elif vision_b == "no":
        vision_b = 0

    with col2:
        numbness = st.text_input('Are you experiencing any tingling or numbness in your extremities? (yes/no)')


    if numbness.lower() == "yes":
        numbness = 1
    elif numbness == "no":
        numbness = 0

    with col1:
        healing = st.text_input('Have you noticed slow healing of wounds or infections ? (yes/no)')


    if healing.lower() == "yes":
        healing = 1
    elif healing == "no":
        healing = 0

    with col2:
        genitics = st.text_input("Does any one in your family hav history of  diabetes ? (yes/no)")


    if genitics.lower() == "yes":
        genitics = 1
    elif genitics == "no":
        genitics = 0
    with col1:
        Age = st.text_input('Age of the Person')



    # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[excessive_thurst, urination, fatigue, glucose, vision_b, numbness , healing,genitics, Age]])
        
        if (diab_prediction[0] == 1):
          diab_diagnosis = ('The person is diabetic')
        else:
          diab_diagnosis = 'The person is not diabetic'
    st.success(diab_diagnosis)










elif selected == "Model 1":
    st.title("My Next Model")
    pass
elif selected == "Model 2":
    st.title("page not found")
    pass

elif selected == "Model 1":
    st.title("page not")
    pass
elif selected == "Model 2":
    # Your code for Model 2 goes here
    pass
