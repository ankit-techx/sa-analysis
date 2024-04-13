import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load CSV file
@st.cache_data
def load_data(filename):
    return pd.read_csv(filename)

# Function to generate pie chart
def generate_pie_chart(df, product):
    product_row = df[df['Pr1'] == product]
    product_row = product_row.drop(columns=['Pr1'])  # Remove product column
    top_10 = product_row.sum().nlargest(10)  # Get top 10 values
    labels = top_10.index
    sizes = top_10.values
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    st.pyplot(fig)

# Main function
def main():
    st.title('Product Data Visualization')
    
    # Adding logo
    logo = "unnamed.png"
    st.image(logo, caption='', use_column_width=True)

    filename = "3_Months_output.csv"  # Path to CSV file
    try:
        df = load_data(filename)
    except Exception as e:
        st.error(f"Error: {e}")
        return

    products = df['Pr1'].unique()
    selected_product = st.selectbox('Select Product', products)
    if st.button('Generate Pie Chart'):
        generate_pie_chart(df, selected_product)

if __name__ == "__main__":
    main()
