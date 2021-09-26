import streamlit as st
from multiapp import MultiApp
from apps import project_db, cartoonizer # import your app modules here
import base64

app = MultiApp()

main_bg = r"C:\Users\HP\Desktop\project_sem4\final.jpg"
main_bg_ext = "jpg"

side_bg = r"C:\Users\HP\Desktop\project_sem4\final.jpg"
side_bg_ext = "jpg"

st.markdown(
    f"""
    <style>
    .reportview-container {{
        background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()})
    }}
   .sidebar .sidebar-content {{
        background: url(data:image/{side_bg_ext};base64,{base64.b64encode(open(side_bg, "rb").read()).decode()})
    }}
    
    </style>
    """,
    unsafe_allow_html=True
)
# Add all your application here
app.add_app("Home", project_db.app)
app.add_app("cartoonize using python image processing", cartoonizer.app)

# The main app
app.run()
