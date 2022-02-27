import numpy as np
import pickle
import pandas as pd
import streamlit as st 
from PIL import Image


pickle_in = open("classifier.pkl","rb")
classifier=pickle.load(pickle_in)

#@app.route('/')
def welcome():
    return "Welcome All"

#@app.route('/predict',methods=["Get"])
def predict_win(Client_Category,Solution_Type,Sector, Location,Deal_Cost,VPManager):
    
    """Let's predict win of deals for IT Consulting Firm 
    This is using docstrings for specifications.
    ---
    parameters:  
      - name: Client_Category
        in: query
        type: number
        required: true
      - name: Solution_Type
        in: query
        type: number
        required: true
        name: Sector
        in: query
        type: number
        required: true
      - name: Location
        in: query
        type: number
        required: true
      - name: Deal_Cost
        in: query
        type: number
        required: true
        name: VPManager
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values
        
    """
   
    prediction=classifier.predict([[Client_Category,Solution_Type,Sector,Location,Deal_Cost,VPManager]])
    print(prediction)
    return prediction



def main():
    st.title("Win Prediction of Bids")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Win Prediction ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    Client_Category = st.text_input("Client_Category_Code")
    Solution_Type = st.text_input("Solution_Type_Code")
    Sector = st.text_input("Sector_Code")
    Location = st.text_input("Location_Code")
    Deal_Cost = st.text_input("Deal_Cost")
    VPManager = st.text_input("VP_Manager_Code")
    result=""
    if st.button("Predict"):
        result=predict_win(Client_Category,Solution_Type,Sector, Location,Deal_Cost,VPManager)
        if result == 0:
            st.text("According to this prediction, you are going to 'Loose' this bid.")
        else:
            st.text("According to this prediction, you are going to 'Win' this bid.")    
    st.success('The output is {}'.format(result))
    

    if st.button("About ML App"):
        st.text("IT firms bids for project by designing and proposing solutions to their clients. These bids often differ from each other in terms sector of the client, solution to be delivered, technology to be used and the scope of the project. The bid value can reach up to millions of dollars, which leads to highly competitive processes. Even a marginal improvement in the win rate can result into a substantial revenue addition for the firm. By predicting the probability of winning a Bid, the engagement teams can prioritize the pipeline of opportunities to staff the most attractive options first. With the probability of winning known in advance, deal engagement manager can ensure that for the most profitable bids there are resources available.")
        st.text("Built with Streamlit")


    if st.button("Input Dictionary"):
        st.text("Client_Category_Code : Code of Client category for which IT Firm is going to make project") 
        st.text("Solution_Type_Code : Code of solution which is demanded by client") 
        st.text("Sector_Code : Code of sector from which client is belongs to")    
        st.text("Location_Code : Code of location for which client has asked the solution")
        st.text("Deal_Cost : Initial deal cost of the project")
        st.text("VP_Manager_Code : Code of VP + Manager combination who are going to take care of deal")

    if st.button("About Author"):
        st.text("Name : Gautham R") 
        
if __name__=='__main__':
    main()