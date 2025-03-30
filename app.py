import streamlit as st
import random

def main():
    st.title("Eid Mubarak Wishes Generator")

    # User input for names

    st.write("### Enter Names")
    your_name = st.text_input ("your name")
    friend_name = st.text_input ("Friend's Name")

    # Generate wishes
    if st.button("Generate Wishes"):
        wishes = [
            
            f"Wishing you a blessed Eid, {friend_name}! May Allah shower you with peace and prosperity. - {your_name}",
            f"To my dear friend {friend_name}, Eid Mubarak! May your day be filled with love, laughter, and all your favourite foods. - {your_name}",
            f"Eid Mubarak,{friend_name}! May this special occasion bring happiness and success to your life. -{your_name}"
        ]
        #Display Wishes
        st.write("### Eid Mubarak Wishes") 
        st.write(random.choice(wishes))

        import random

        if __name__=="__main__":
            main()
