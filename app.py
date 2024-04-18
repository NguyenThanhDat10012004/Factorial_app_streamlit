import streamlit as st
from factorial import fact

def main():
    st.title("Factorial test") 
    number = st.number_input("Enter a number", min_value = 1, max_value = 900)

    if st.button("Calculate"):
        result = fact(number)
        st.write(f"The result of {number} is {result}")
        st.balloons()
if __name__ == "__main__":
    main()
