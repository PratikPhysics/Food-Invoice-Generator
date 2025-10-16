import streamlit as st
import datetime

st.set_page_config(page_title="Food Invoice Generator", page_icon="🍽️")

st.title("🍽️ Food Invoice Generator")

# Fixed price list (you can customize this)
menu = {
    "Pizza": 250,
    "Burger": 120,
    "Pasta": 180,
    "Sandwich": 100,
    "Coffee": 80,
    "Juice": 60,
    "Salad": 90,
    "Dessert": 150
}

# Customer info
name = st.text_input("Customer Name")

# Select food items
selected_items = st.multiselect("Select Food Items", list(menu.keys()))

quantities = {}
total_amount = 0

# Quantity inputs for each selected item
if selected_items:
    st.subheader("🧾 Order Details")
    for item in selected_items:
        col1, col2, col3 = st.columns([3, 1, 2])
        with col1:
            st.write(f"**{item}** (₹{menu[item]} each)")
        with col2:
            qty = st.number_input(f"Qty ({item})", min_value=1, value=1, step=1, key=item)
        quantities[item] = qty
        with col3:
            item_total = menu[item] * qty
            st.write(f"= ₹{item_total}")
            total_amount += item_total

# Generate invoice
if st.button("Generate Invoice"):
    if not name or not selected_items:
        st.warning("⚠️ Please enter customer name and select at least one item.")
    else:
        st.success("✅ Invoice generated successfully!")
        st.markdown("---")
        st.markdown("### 🧾 **Food Palace Invoice**")
        st.markdown(f"**Date:** {datetime.date.today().strftime('%d-%m-%Y')}")
        st.markdown(f"**Customer Name:** {name}")
        st.markdown("---")

        st.markdown("#### Ordered Items:")
        for item in selected_items:
            st.markdown(f"- {item} × {quantities[item]} = ₹{menu[item] * quantities[item]}")

        st.markdown("---")
        st.markdown(f"### 💰 **Total Amount: ₹{total_amount:.2f}**")
        st.markdown("Thank you for dining with us! 🍴")
