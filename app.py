import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load product names from text file
def load_product_names(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file.readlines()]

# Load CSV file based on selected time period
@st.cache_resource
def load_data(filename):
    return pd.read_csv(filename)

# Function to generate pie chart
def generate_pie_chart(df, product, time_period):
    product_row = df[df['Product 1'] == product]
    product_row = product_row.drop(columns=['Product 1'])  # Remove product column
    top_10 = product_row.sum().nlargest(10)  # Get top 10 values
    labels = top_10.index
    sizes = top_10.values
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    st.pyplot(fig)
    st.markdown(f"**Pie Chart Description**: The pie chart displays the distribution of sales for the selected product (**{product}**) among the top 10 most bought products after it, within the **{time_period}** time period.")

# Main function
def main():
    st.title('Product Data Visualization')

    # Adding logo
    logo = "unnamed.png"
    st.image(logo, caption='', use_column_width=True)
    
    st.sidebar.markdown('## Data Selection')
    st.sidebar.markdown('Select the time period and product for analysis.')

    time_period = st.sidebar.selectbox('Select Time Period', ['3 Months', '6 Months', '1 Year'], help="Choose the duration for which you want to analyze the product data.")

    # Load CSV file based on time period
    if time_period == '3 Months':
        filename = "new_3_months_output.csv"
    elif time_period == '6 Months':
        filename = "new_6_months_output.csv"
    else:
        filename = "new_1_year_output.csv"

    try:
        df = load_data(filename)
    except Exception as e:
        st.error(f"Error: {e}")
        return

    product_names = load_product_names("productname.txt")  # Load product names from text file
    selected_product = st.sidebar.selectbox('Select Product', product_names, help="Choose a specific product for which you want to visualize the sales data.")
    if st.sidebar.button('Generate Pie Chart'):
        generate_pie_chart(df, selected_product, time_period)

if __name__ == "__main__":
    main()
