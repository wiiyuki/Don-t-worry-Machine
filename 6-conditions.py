import streamlit as st
st.title('Don\'t worry Machine')

problem_index=st.text_input('Do you have a problem?(enter yes or no)').lower()
if problem_index:
    if problem_index == 'yes':
        do_index = st.text_input('Can you do something about?(enter yes or no)').lower()
        if do_index:
            if do_index == 'yes':
                st.success("Then don't worry!")
            else:
                st.success("Then don't worry!")
    else:
        st.success("Then don't worry!")
