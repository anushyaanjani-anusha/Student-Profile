import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Student Profile Application",
    page_icon="🎓",
    layout="centered"
)
st.markdown("""
<style>
.stApp {
    background-color: #171717;
}
</style>
""", unsafe_allow_html=True)
st.title("🎓 Student Profile Application")
st.caption("lauched by ANUSHA A")
name = st.text_area("Student Name", placeholder="Enter your name")

roll = st.text_area("USN / Roll no.", placeholder="Enter your USN")

department = st.text_area("Department", placeholder="Enter your department")
year = st.radio(
    "Current Year",
    ["1st Year", "2nd Year", "3rd Year", "4th Year"]
)
if st.button("View My Profile"):

    if name and roll and department:

        st.success("Profile Created Successfully!")

        st.subheader("🎓 Student Profile Details")

        st.write("**Student Name:**", name)
        st.write("**USN / Roll No.:**", roll)
        st.write("**Department:**", department)
        st.write("**Current Year:**", year)

    else:
        st.warning("Please fill all the details!")


       

