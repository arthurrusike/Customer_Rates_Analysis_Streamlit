import pandas as pd
import numpy as np
import openpyxl
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="Customer Rates and Invoicing Analysis", page_icon="📊", layout="wide",
                   initial_sidebar_state="expanded")

with st.sidebar:
    st.title("Analytics Dashboard")
    uploaded_file = st.file_uploader('Upload Customer Rates File', type=['xlsx', 'xlsm'])
    st.markdown('---------------------')

# Main Dashboard
invoice_rates = pd.read_excel(uploaded_file, sheet_name="InvoiceRates")

# Main Dashboard
if uploaded_file:
    cost_centres = invoice_rates.Cost_Center.unique()
    workday_Customer_names = invoice_rates.WorkdayCustomer_Name.unique()
    select_Option1, select_Option2 = st.columns(2)

    with select_Option1:
        selected_cost_centre = st.selectbox("Cost Centre :", cost_centres, index=2)
        select_workday_customers = invoice_rates[
            invoice_rates.Cost_Center == selected_cost_centre].WorkdayCustomer_Name.unique()
        select_CC_data = invoice_rates[invoice_rates.Cost_Center == selected_cost_centre]

    with select_Option2:
        if selected_cost_centre:
            select_customer = st.selectbox("Select Customer : ", select_workday_customers, index=1)
        else:
            select_customer = st.selectbox("Select Customer : ", workday_Customer_names, index=1)

st.divider()

tab1, tab2, tab3, tab4 = st.tabs(["📈 Details", "🥇 Rankings", "🗺️ Map", "ℹ️ About"])

with tab1:
    Workday_Sales_Item_Name = invoice_rates.Workday_Sales_Item_Name.unique()
    selected_customer = invoice_rates[(invoice_rates.WorkdayCustomer_Name == select_customer)
                                      & (invoice_rates.Cost_Center == selected_cost_centre)]

    Revenue_Category = selected_customer.Revenue_Category.unique()

    selected_customer_pivot = pd.pivot_table(selected_customer,
                                             values=["Quantity", "LineAmount"],
                                             index=["Revenue_Category", "Workday_Sales_Item_Name"],
                                             aggfunc="sum")
    selected_customer_pivot["Avg Rate"] = selected_customer_pivot.LineAmount / selected_customer_pivot.Quantity

    col1, col2 = st.columns(2)

    with col1:
        st.dataframe(selected_customer_pivot)

    with col2:
        selected_graph = st.selectbox("Display :", ["Revenue", "Volumes"], index=0)
        graph_values = selected_graph

        if selected_graph == "Revenue":
            graph_values = "LineAmount"
        else:
            graph_values = "Quantity"

        fig = px.pie(selected_customer_pivot, values=selected_customer_pivot[graph_values],
                     names=Revenue_Category,
                     title=f'{selected_graph} View',
                     height=300, width=200)
        fig.update_layout(margin=dict(l=20, r=20, t=30, b=0), )
        st.plotly_chart(fig, use_container_width=True)

st.divider()

with tab2:
    storage_holding = select_CC_data[select_CC_data['Revenue_Category'] == 'Storage - Renewal']
    select_CC_data['pallet_thru_put'] = [(select_CC_data['Revenue_Category'] == 'Handling - Initial') &
                                   (select_CC_data['Revenue_Category'] == 'Handling - Initial')]
    # fig2 = go.Figure()
    # fig2.add_trace(go.Bar(x = storage_revenue ))
    pass

print(storage_revenue.columns)