import streamlit as st
import pandas as pd
import joblib

# Load the model (cached so it doesn't reload every time)
@st.cache_resource
def load_model():
    return joblib.load('transaction_model.pkl')

# Load the model
model = load_model()

# Custom CSS to adjust image height
st.markdown(
    """
    <style>
    .banner-img img {
        height: 250px;   
        width: 1600px;   
        object-fit: cover;
        border-radius: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Header image
st.markdown(
    '<div class="banner-img">'
    '<img src="https://www.transaction.technology/uploads/images/_ecb2_images/gallery_feature_76/POS%20Retail.jpg" />'
    '</div>',
    unsafe_allow_html=True
)

# App title
st.title("Retail Transaction Total Amount Predictor")

# Sidebar for inputs
st.sidebar.header("Enter Transaction Details")
quantity = st.sidebar.number_input("Quantity", min_value=1, max_value=10, value=5)
price = st.sidebar.number_input("Price ($)", min_value=0.0, max_value=100.0, value=50.0)

# Prediction button
if st.sidebar.button("Predict Total Amount"):
    # Prepare input data
    input_data = pd.DataFrame({
        'Quantity': [quantity],
        'Price': [price]
    })
    # Make prediction
    prediction = model.predict(input_data)[0]

    # Display prediction
    st.subheader("Prediction Result")
    st.write(f"**Predicted Total Amount:** ${prediction:.2f}")
    
    # Optional: Show feature importance or other insights
    st.subheader("Model Insights")
    st.write("This model uses Linear Regression to predict Total Amount based on Quantity and Price, accounting for typical discount patterns from the training data.")

# Instructions section
with st.expander("How to Use"):
    st.write("""
    1. Enter the quantity of items purchased.
    2. Enter the unit price per item.
    3. Click 'Predict Total Amount' to get the estimated total after discount.
    
    The model is trained on historical retail data and provides predictions for bulk or single transactions.
    """)

# Footer
st.markdown("---")

st.markdown("Model: Linear Regression on Retail Transactions")
