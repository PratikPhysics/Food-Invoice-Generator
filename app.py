import streamlit as st
from fpdf import FPDF
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
        # Create Invoice PDF
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", "B", 16)

        # Header
        pdf.cell(200, 10, txt="Food Palace Invoice", ln=True, align="C")
        pdf.set_font("Arial", "", 12)
        pdf.cell(200, 10, txt=f"Date: {datetime.date.today()}", ln=True, align="C")

        pdf.ln(10)
        pdf.cell(200, 10, txt=f"Customer Name: {name}", ln=True)
        pdf.cell(200, 10, txt="--------------------------------------", ln=True)

        # Food items
        pdf.cell(200, 10, txt="Ordered Items:", ln=True)
        for item in food_items:
            pdf.cell(200, 10, txt=f" - {item}", ln=True)

        pdf.ln(5)
        pdf.cell(200, 10, txt=f"Total Amount: ₹{amount:.2f}", ln=True)
        pdf.ln(5)
        pdf.cell(200, 10, txt="Thank you for dining with us! 🍴", ln=True, align="C")

        # Save and show download button
        file_path = "invoice.pdf"
        pdf.output(file_path)
        
        with open(file_path, "rb") as f:
            st.download_button(
                label="⬇️ Download Invoice as PDF",
                data=f,
                file_name=f"Invoice_{name.replace(' ', '_')}.pdf",
                mime="application/pdf"
            )

        st.success("✅ Invoice generated successfully!")

