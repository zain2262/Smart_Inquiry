import streamlit as st

st.set_page_config(
    page_title="SmartInquiry",
    page_icon="💬",
    layout="centered"
)


# Classification Function
def classify_inquiry(message):
    message = message.lower().strip()

    pricing_keywords = [
        "price", "pricing", "cost", "quote", "quotation",
        "charges", "how much", "payment", "refund"
    ]

    order_keywords = [
        "order", "delivery", "shipment", "tracking",
        "parcel", "dispatch", "shipping", "where is my"
    ]

    support_keywords = [
        "issue", "problem", "error", "not working",
        "broken", "help", "technical support",
        "unable to", "complaint"
    ]

    pricing_match = any(
        keyword in message for keyword in pricing_keywords
    )

    order_match = any(
        keyword in message for keyword in order_keywords
    )

    support_match = any(
        keyword in message for keyword in support_keywords
    )

    matched_categories = sum([
        pricing_match,
        order_match,
        support_match
    ])

    if matched_categories > 1:
        return (
            "Other/Uncertain",
            "Multiple categories detected. Human review required."
        )

    if pricing_match:
        return "Pricing", "Pricing-related inquiry detected."

    if order_match:
        return "Order", "Order-related inquiry detected."

    if support_match:
        return "Support", "Support-related inquiry detected."

    return (
        "Other/Uncertain",
        "No clear category detected. Human review required."
    )


# Application Interface
st.title("💬 SmartInquiry")

st.subheader("Customer Inquiry Classification & Draft Replies")

st.write(
    "Enter a customer inquiry below. "
    "The system will classify the request "
    "and identify inquiries requiring human review."
)

st.divider()


# Customer Input Form
with st.form("inquiry_form"):

    st.subheader("Customer Information")

    customer_name = st.text_input("Customer Name")

    customer_email = st.text_input("Customer Email")

    order_id = st.text_input("Order ID (optional)")

    inquiry_message = st.text_area(
        "Customer Inquiry",
        placeholder="Example: Where is my order?",
        height=150
    )

    submitted = st.form_submit_button(
        "Classify Inquiry",
        use_container_width=True
    )


# Process Inquiry
if submitted:

    if not inquiry_message.strip():

        st.error("Please enter a customer inquiry.")

    else:

        category, reason = classify_inquiry(inquiry_message)

        st.divider()

        st.header("Classification Results")

        st.success("Inquiry received successfully!")

        st.subheader("Customer Information")

        st.write("Customer:", customer_name or "Not provided")
        st.write("Email:", customer_email or "Not provided")
        st.write("Order ID:", order_id or "Not provided")

        st.subheader("Detected Category")

        st.write("Category:", category)
        st.write("Reason:", reason)

        if category == "Other/Uncertain":

            st.warning(
                "Human review is required before proceeding."
            )

        else:

            st.success(
                f"Inquiry classified as {category}."
            )

        st.subheader("Original Customer Message")

        st.write(inquiry_message)

        st.info(
            "No reply has been generated or sent. "
            "Reply drafting will be implemented on Day 3."
        )


# Footer
st.divider()

st.caption(
    "SmartInquiry | Internship Week 01 | Day 2"
)