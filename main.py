import streamlit as st

tab1, tab2, tab3 = st.tabs(["About", "Hobbies", "Contact"])

with tab1:  #Inside the first tab.
    col1, col2 = st.columns([0.3, 0.7])
    with col1:
        st.image("mypic.png", width=200)
        st.subheader("Akshay Sharma :sunglasses:")

    with col2:
        st.write(
            "Hello, I am Akshay, a robotics trainer and content developer :robot_face: . My parents find it challenging to manage and track their expenses. So, I created a website  to help them in tracking and managing their expenses. You can use this website to manage and track your expenses as well. I hope you all like it."
        )

with tab2:  #Inside the second tab.
    st.write(
        "I love coding robots :computer: and playing PC games in my free time :performing_arts:. Also, i love travelling:sunrise_over_mountains:."
    )

with tab3:  #Inside the third tab.
    st.write("Email : akshay.s@moonpreneur.com")
    st.write("Website : https://akshay.home.blog/")
