import streamlit as st
import Get_Data
import pandas as pd
import json
import smap
import clone
import DataBase

def run_once():
    if not st.session_state.get('has_run', False):
        st.session_state['has_run'] = True
        clone.Clone()
        DataBase.main()

run_once() 




st.title("Data Visualization")
col1, col2, col3, col4 = st.columns(4)

data = col1.radio("Data",["Transaction", "User"])
year = col2.radio("Year",["2018","2019","2020","2021","2022"])
month = col3.radio("Month",["Q1(Jan - Mar)","Q2(Apr - Jun)","Q3(Jul - Sep)","Q4(Oct - Dec)"])
l=[]

if (data == "User"):
    l = ['appOpens', 'registeredUsers']
    
if (data == "Transaction"):
    l=["count","amount"]
s = col4.radio("Available Data to View in Map",l)

dfa = Get_Data.GetData(data,year,month,"A")
dfm = Get_Data.GetData(data,year,month,"M")
dft = Get_Data.GetData(data,year,month,"T")

dfa = json.loads(dfa)
dfm = json.loads(dfm)
dft = json.loads(dft)

#For Aggregated
df_a = pd.DataFrame()


if (data == "Transaction"):
    transaction_data = dfa['data']['transactionData']

    # Initialize empty lists for columns
    names = []
    counts = []
    amounts = []
    # Loop through transaction data and extract desired columns
    for transaction in transaction_data:
        name = transaction['name']
        for payment in transaction['paymentInstruments']:
            count = payment['count']
            amount = payment['amount']
            names.append(name)
            counts.append(count)
            amounts.append(amount)
            # Create DataFram
            df_a = pd.DataFrame({'name': names, 'count': counts, 'amount': amounts})
            
if (data == "User"):
    df_a1 = pd.json_normalize(dfa['data']['aggregated'])
    df_a = pd.DataFrame(df_a1)

#For Mapping
df = pd.DataFrame()

if (data == "Transaction"):
    hover_data = dfm['data']['hoverDataList']
    df = pd.json_normalize(hover_data, record_path='metric', meta=['name'], errors='ignore')
    

elif (data == "User"):
    json_data = json.dumps(dfm['data']['hoverData'])
    df = pd.read_json(json_data, orient='index')
    df = df.reset_index()
    df = df.rename(columns={df.columns[0]: 'name'})
    cols = df.columns.tolist()

st.title("Aggregated Data")
st.write(df_a)
st.title("Top 10")
col1, col2 = st.columns(2)

st.title("Data Visualization in Map")
smap.Map(df,s,data)

#For Top
df_t = pd.DataFrame()
name = col1.radio("Select the Data", ['states', 'districts', 'pincodes'])
if(data == "Transaction"):
    df_t = pd.json_normalize(dft['data'][name])
    df_t = df_t.drop(columns='metric.type')
    if (name == 'pincodes'):
        df_t = df_t.rename(columns={'entityName' : 'Pin Code','metric.count': 'Count', 'metric.amount': 'Amount'})
    else:
        df_t = df_t.rename(columns={'entityName' : 'EntityName','metric.count': 'Count', 'metric.amount': 'Amount'})

    
elif(data == "User"):
    df_t = pd.json_normalize(dft['data'][name])
    if (name == 'pincodes'):
        df_t = df_t.rename(columns={'entityName' : 'Pin Code','name': 'Name', 'registeredUsers': 'RegisteredUsers'})
    else:
        df_t = df_t.rename(columns={'entityName' : 'EntityName','name': 'Name', 'registeredUsers': 'RegisteredUsers'})

with col2:
    st.write("Top 10 "+name)
    st.write(df_t)
