
import streamlit as st

st.set_page_config(
    page_title="SmartInquiry",
    page_icon="💬",
    layout="centered"
)

st.title("💬 SmartInquiry")
st.subheader("Customer Inquiry Classification & Draft Replies")

st.write(
    "Enter a customer inquiry below. "
    "The system will help organize the request "
    "and prepare a draft for human review."
)

with st.form("inquiry_form"):
    customer_name = st.text_input("Customer Name")
    customer_email = st.text_input("Customer Email")
    order_id = st.text_input("Order ID (optional)")

    inquiry_message = st.text_area(
        "Customer Inquiry",
        placeholder="Example: Where is my order?",
        height=150
    )

    submitted = st.form_submit_button("Submit Inquiry")

if submitted:
    if not inquiry_message.strip():
        st.error("Please enter a customer inquiry.")
    else:
        st.success("Inquiry received successfully!")

        st.subheader("Submitted Information")
        st.write("Customer:", customer_name or "Not provided")
        st.write("Email:", customer_email or "Not provided")
        st.write("Order ID:", order_id or "Not provided")
        st.write("Inquiry:", inquiry_message)

        st.info(
            "Next step: classification and draft generation "
            "will be added in a later milestone. "
            "No reply has been sent."
        )
