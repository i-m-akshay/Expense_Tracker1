import streamlit as st

tab1, tab2, tab3 = st.tabs(["About", "Hobbies", "Contact"])

with tab1:  #Inside the first tab.
    col1, col2 = st.columns([0.3, 0.7])
    with col1:
        st.image("mypic.png", width=200)
        st.subheader("Ayesha Shariff :sunglasses:")

    with col2:
        st.write(
            "Hello, I am Akshay, a computer teacher and content developer :computer: . My parents find it challenging to manage and track their expenses. So, I created a website  to help them in tracking and managing their expenses. You can use this website to manage and track your expenses as well. I hope you all like it."
        )

with tab2:  #Inside the second tab.
    st.write(
        "I love solving math :triangular_ruler: problems and watching ANIME and reading manga sometimes :performing_arts: to learn about different things. Also, i love 3d house plan designing and travelling:sunrise_over_mountains:."
    )

with tab3:  #Inside the third tab.
    st.write("Email : ayeshacse.ai@gmail.com")
    st.write("Website : https://ayeshacse.home.blog/")
