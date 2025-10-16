import streamlit as st
import datetime

# App Title
st.title("🍽️ Food Invoice Generator")

# Input fields
name = st.text_input("Customer Name")
amount = st.number_input("Total Amount (₹)", min_value=0.0, step=0.5)

# Food item selection
food_items = st.multiselect(
    "Select Food Items",
    ["Pizza", "Burger", "Pasta", "Sandwich", "Coffee", "Juice", "Salad", "Dessert"]
)

# Generate Invoice Button
if st.button("Generate Invoice"):
    if not name or not food_items or amount <= 0:
        st.warning("⚠️ Please fill all fields properly.")
    else:
        st.success("✅ Invoice generated successfully!")
        st.markdown("---")
        st.markdown("### 🧾 **Food Palace Invoice**")
        st.markdown(f"**Date:** {datetime.date.today().strftime('%d-%m-%Y')}")
        st.markdown(f"**Customer Name:** {name}")
        st.markdown("**Ordered Items:**")

        for item in food_items:
            st.markdown(f"- {item}")

        st.markdown(f"### 💰 Total Amount: ₹{amount:.2f}")
        st.markdown("---")
        st.markdown("Thank you for dining with us! 🍴")

