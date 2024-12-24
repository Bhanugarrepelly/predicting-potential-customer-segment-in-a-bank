import streamlit as st
import pickle
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
scaler=pickle.load(open('scl.pkl','rb'))


st.set_page_config(layout="wide")
st.header("Predicting Deposits")
xg=pickle.load(open('xg.pkl','rb'))
scaler2=StandardScaler()
def main():
    st.title("Fill the details")
    st.write("Enter values for the parameters below:")

    # Number of columns for the table layout (adjust as needed)
    num_columns = 4

    # Create a list to store the parameter names
    parameters = ["age","default","balance","housing","loan","contact","day","month","duration","campaign","pdays","previous","poutcome_failure","poutcome_other","poutcome_success","education_primary","education_secondary","education_tertiary","marital_divorced","marital_married","marital_single","job_admin","job_clue-collar","job_entrepreneur","job_housemaid","job_management","job_retired","job_self-employed","job_services","job_student","job_technician","job_unemployed"]

    # Create a dictionary to hold the user inputs
    inputs = {}
    inputs1=[]

    scaled_cols = ['age','balance','duration','pdays']
    
    for row_start in range(0, len(parameters), num_columns):
        cols = st.columns(num_columns)
        for col, param in zip(cols, parameters[row_start:row_start + num_columns]):
        # Take input and validate as integer
            user_input = col.text_input(param)
            if user_input.strip(): #ensure string is not empty
                try:
                    inputs1.append(user_input)
                    inputs[param]=user_input                   
                
                except ValueError:
                    col.error(f"Invalid input for {param}. Please enter a valid integer.")
            else:
                col.error(f"Input for {param} cannot be empty.")


    for i in range(len(inputs1)):
        if i<=11:
            inputs1[i]=int(inputs1[i])
        else:
            if inputs1[i]=="True":
                inputs1[i]=True
            else:
                inputs1[i]=False


    if st.button("Submit"):
        #st.write("Here are the values you entered:")
        

        df3=np.asarray(inputs1)
        df4=df3.reshape(1,-1)
        #st.write(df4.shape)
        #df5=scaler.fit_transform(df4)
        if xg.predict(df4):
            st.write("The user tends to deposit in the bank")
        else:
            st.write("The user is not willing to deposit in the bank")
    


if __name__ == "__main__":
    main()