import streamlit as st
from get_description import get_meaning

# Define the test function
def test(query):
    # Replace this with your logic
    return f"You submitted: {query}"

# Streamlit UI
st.title("Dictionary📕")

# Input field for the query
user_query = st.text_input("Enter your query:")
context = ''
context = st.text_area("Enter your context(optional):")

# Submit button
if st.button("Submit"):
    if user_query:
        print('query submitted')
        # Call the test function with the user query
        response = get_meaning(user_query, context)
        # Display the response
        st.success(response)
    else:
        st.warning("Please enter a query before submitting.")
