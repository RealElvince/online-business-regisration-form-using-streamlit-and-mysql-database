#   Useful libraries for this project
import streamlit as st
import mysql.connector

# Establish database connection
mydb = mysql.connector.connect(
    host="localhost",
    user='root',
    port='3306',
    password='',
    database='business_db'
)
# cursor for executing SQL queries
my_cursor = mydb.cursor()
# configure web layout
st.set_page_config(page_title="county business registration form", page_icon="chart_with_upwards_trend",
                   layout="wide")
with st.container():
    st.title('Kenya Counties Business Registration form.')
    st.subheader('If you want to register your business ,please fill in the form below.')
    st.markdown("<b>Please provide all the details to register with us!</b>", unsafe_allow_html=True)
    st.markdown("---", unsafe_allow_html=True)
    with st.form("form_one", clear_on_submit=True):
        business_owner = st.text_input("Business Owner's full names:")
        business_name = st.text_input("Enter your business name:")
        phone_number = st.text_input("Contact")
        email_address = st.text_input("Email")
        kra_pin = st.text_input("KRA pin", max_chars=11)
        physical_address = st.text_input("Physical Address")
        county = st.text_input("County")
        town = st.text_input("Town")
        business_type = st.selectbox("Select business type:",
                                     options=["Sole proprietorship", "Partnership", "Corporation", "S corporation",
                                              "Online Business", "Retail Business"])
        on_click = st.form_submit_button('submit')

        # form button functionality on_click
        if on_click:
            # query insert into database
            sql = "insert into business_table(business_owner,business_name,contact,email,kra_pin,physical_address,county,town,business_type) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            val = (business_owner, business_name,phone_number, email_address, kra_pin, physical_address, county, town,
                   business_type)

            # use my_cursor to execute sql query into mysql database
            my_cursor.execute(sql,val)
            mydb.commit()
            st.success(
                f"Dear {business_owner},your application has been sent to our database,we will contact you soon and guide on your on registration fee payment. Thank you!")
