import streamlit as st
import pandas as pd
import pymysql

myconnection = pymysql.connect(host='127.0.0.1',user='root',passwd='Abhi09101997*',database='bus_data')
print(myconnection)
mycursor=myconnection.cursor(pymysql.cursors.SSCursor)

#SQL Connection
def get_db_connection():
    return pymysql.connect(host='127.0.0.1',user='root',passwd='Abhi09101997*',database='bus_data')


intro = st.sidebar.radio('Main Menu',['Home page','Check In for Bus Routes'])
if  'Home page'==intro:
    st.title('Welcome to My Webpage 🌍')
    st.subheader('Redbus Data Scraping')
    st.write('\n- This involves using an automated method to extract data from the Redbus website, such as bus routes, schedules, and pricing and store it in a database and using it for Analysis')

    st.write("#### Selenium: \n- This is a tool used for automating web browsers, which allows users to programmatically interact with a website and extract data")
    st.write("#### SQL: \n- This is a tool used for storing the collected data")
    st.write("#### Streamlit: \n- This is a tool used to build an interactive webpage")
    
    st.subheader('Objective of the Project')
    st.markdown("<br>", unsafe_allow_html=True) 
    st.write(""" Automate the collection of bus travel data from the Redbus website using Selenium. 
             This includes gathering detailed information such as:
                    \n- Bus routes
                    \n- Rating
                    \n- Schedules
                    \n- Ticket prices
                    \n- Seat availability""")
    
    st.write("Store the scraped data in a structured SQL database, making it easier to access, manage, and analyze.")

    st.write("""Develop a user-friendly Streamlit application to:
                    \n- Display the collected data in an interactive interface.
                    \n- Allow users to filter and analyze bus routes based on various criteria, such as bus type, route, price, ratings, and seat availability.""")
    st.markdown("<br>", unsafe_allow_html=True) 
    st.write("""##### In Summary: 
                \n- the project's goal is to streamline the process of collecting, filtering, and analyzing bus travel data, 
                offering an efficient tool for decision-making and enhancing user experiences in the transportation sector.""")
    
    st.markdown("<br>", unsafe_allow_html=True) 
    
    st.header("  Explore Bus Routes Across India 🚀:") 
    st.subheader("From Himachal Pradesh to Kerala, Discover Both Government and Private AC/Non-AC Options!")

    col1,col2,col3=st.columns(3,gap='small')
    col1.markdown("### States:\n- West Bengal\n- Punjab\n- Telangana")
    col2.markdown("### \n- Kerala\n- Rajasthan\n- Himachal Pradesh\n- Karnataka")
    col3.markdown("### \n- Chandigarh\n- North Bengal\n- Bihar")

    col4,col5=st.columns(2,gap='medium')
    col4.markdown("### Buses:\n- Goverment Buses\n- AC and Non-Ac")
    col5.markdown("### \n- Privite Buses\n- AC and Non-Ac")
    st.info('For Additional Bus information click Check In For Bus Routes')

else:
    def get_state_names():
        myconnection = get_db_connection()
        mycursor=myconnection.cursor(pymysql.cursors.SSCursor)
        mycursor.execute('SELECT DISTINCT state_name FROM bus_routes')    
        state_names = [row[0] for row in mycursor.fetchall()]
        mycursor.close()
        myconnection.close()
        return state_names

    def get_route_names_by_state(selected_state):
        myconnection = get_db_connection()
        mycursor = myconnection.cursor(pymysql.cursors.SSCursor)
        mycursor.execute('SELECT DISTINCT route_name FROM bus_routes WHERE state_name = %s', (selected_state))
        route_names = [row[0] for row in mycursor.fetchall()]
        mycursor.close()
        myconnection.close()
        return route_names
    
    def get_bustype():
        myconnection = get_db_connection()
        mycursor=myconnection.cursor(pymysql.cursors.SSCursor)
        mycursor.execute('SELECT DISTINCT bustype FROM bus_routes')
        bustype = [row[0] for row in mycursor.fetchall()]
        mycursor.close()
        myconnection.close()
        return bustype
    
    def get_rating():
        myconnection = get_db_connection()
        mycursor=myconnection.cursor(pymysql.cursors.SSCursor)
        mycursor.execute('SELECT DISTINCT star_rating FROM bus_routes WHERE star_rating ORDER BY star_rating')
        star_rating = [float(row[0]) for row in mycursor.fetchall()]
        mycursor.close()
        myconnection.close()
        return star_rating
    
    def get_min_rating():
        myconnection = get_db_connection()
        mycursor = myconnection.cursor(pymysql.cursors.SSCursor)
        mycursor.execute('SELECT MIN(star_rating) FROM bus_routes')  # Get the minimum price directly
        min_rating = float(mycursor.fetchone()[0])  # Convert to float
        mycursor.close()
        myconnection.close()
        return min_rating

    def get_max_ratinge():
        myconnection = get_db_connection()
        mycursor = myconnection.cursor(pymysql.cursors.SSCursor)
        mycursor.execute('SELECT MAX(star_rating) FROM bus_routes')  # Get the maximum price directly
        max_ratinge = float(mycursor.fetchone()[0])  # Convert to float
        mycursor.close()
        myconnection.close()
        return max_ratinge
    
    def get_departing_time():
        myconnection = get_db_connection()
        mycursor=myconnection.cursor(pymysql.cursors.SSCursor)
        mycursor.execute('SELECT DISTINCT departing_time FROM bus_routes WHERE departing_time ORDER BY departing_time')
        departing_time = [row[0] for row in mycursor.fetchall()]
        mycursor.close()
        myconnection.close()
        return departing_time

    def get_price():
        myconnection = get_db_connection()
        mycursor = myconnection.cursor(pymysql.cursors.SSCursor)
        mycursor.execute('SELECT DISTINCT price FROM bus_routes WHERE price ORDER BY price')
        price = [float(row[0]) for row in mycursor.fetchall()]  # Convert to float
        mycursor.close()
        myconnection.close()
        return price

    def get_min_price():
        myconnection = get_db_connection()
        mycursor = myconnection.cursor(pymysql.cursors.SSCursor)
        mycursor.execute('SELECT MIN(price) FROM bus_routes')  # Get the minimum price directly
        min_price = float(mycursor.fetchone()[0])  # Convert to float
        mycursor.close()
        myconnection.close()
        return min_price

    def get_max_price():
        myconnection = get_db_connection()
        mycursor = myconnection.cursor(pymysql.cursors.SSCursor)
        mycursor.execute('SELECT MAX(price) FROM bus_routes')  # Get the maximum price directly
        max_price = float(mycursor.fetchone()[0])  # Convert to float
        mycursor.close()
        myconnection.close()
        return max_price

    def get_ac_type():
        myconnection = get_db_connection()
        mycursor=myconnection.cursor(pymysql.cursors.SSCursor)
        mycursor.execute('SELECT DISTINCT ac_type FROM bus_routes')    
        ac_type = [row[0] for row in mycursor.fetchall()]
        mycursor.close()
        myconnection.close()
        return ac_type
    
    def get_seat_type():
        myconnection = get_db_connection()
        mycursor=myconnection.cursor(pymysql.cursors.SSCursor)
        mycursor.execute('SELECT DISTINCT seat_type FROM bus_routes')    
        seat_type = [row[0] for row in mycursor.fetchall()]
        mycursor.close()
        myconnection.close()
        return seat_type
    
    
    state_names = get_state_names()
    bustype = get_bustype()
    star_rating = get_rating()
    departing_time = get_departing_time()
    price = get_price()
    ac_type = get_ac_type()
    seat_type = get_seat_type()
    

    min_price = min(price)
    max_price = max(price)

    min_rating = min(star_rating)
    max_rating = max(star_rating)

    # Display selection dropdown
    col1, col2, col3 = st.columns(3,gap='medium')
    with col1:
        selected_state = st.selectbox("Select the State", state_names)
    with col2:
        route_names = get_route_names_by_state(selected_state)
        selected_route = st.selectbox("Select the Route", route_names)
    with col3:
        selected_price = st.slider('Bus Fare Range',min_value=min_price,max_value=max_price,value=(min_price, max_price),step=500.00)
    
    st.markdown("<br>", unsafe_allow_html=True) 

    col4, col5, col6 = st.columns(3,gap='large')
    with col4:
        selected_rating = st.slider('Rating',min_value=min_rating,max_value=max_rating,value=(min_rating, max_rating),step=1.0)
    with col5:
        selected_ac = st.radio("Type A/C or NON A/C", ac_type)
    with col6:
        selected_seat = st.radio("Select Seat Sleeper or Seater", seat_type)
   
    st.markdown("<br>", unsafe_allow_html=True) 

    col7, col8, col9 = st.columns([4,1,1])
    with col7:
        st.subheader('Available Routes for above selection')
    with col8:
        selected_start_departing_time = st.selectbox("Departing Time From", departing_time)
    with col9:
        selected_end_departing_time = st.selectbox("Departing Time To", departing_time)
    
    
    query = """
        SELECT * FROM bus_routes
        WHERE state_name = %s
        AND route_name = %s
        AND star_rating BETWEEN %s AND %s
        AND departing_time BETWEEN %s AND %s
        AND price BETWEEN %s AND %s
        AND ac_type = %s
        AND seat_type = %s
        """

    mycursor.execute(query, (selected_state,selected_route, selected_rating[0], 
                             selected_rating[1], selected_start_departing_time, 
                             selected_end_departing_time, selected_price[0], selected_price[1],selected_ac,selected_seat))
    data = mycursor.fetchall()


    if data:
        df = pd.DataFrame(data)
        df.columns=['id','route_name','route_link','busname',
                     'bustype','departing_time','duration','reaching_time',
                     'star_rating','price','seats_available', 'state_name', 'ac_type', 'seat_type']
        # df['departing_time']=df['departing_time'].astype(str)
        # df['departing_time']=pd.to_datetime(df['departing_time']).dt.time
        df['departing_time'] = pd.to_timedelta(df['departing_time']).dt.components['hours'].astype(str) + ":" + \
                    pd.to_timedelta(df['departing_time']).dt.components['minutes'].astype(str).str.zfill(2) + ":" + \
                    pd.to_timedelta(df['departing_time']).dt.components['seconds'].astype(str).str.zfill(2)
        df['reaching_time'] = pd.to_timedelta(df['reaching_time']).dt.components['hours'].astype(str) + ":" + \
                    pd.to_timedelta(df['reaching_time']).dt.components['minutes'].astype(str).str.zfill(2) + ":" + \
                    pd.to_timedelta(df['reaching_time']).dt.components['seconds'].astype(str).str.zfill(2)
        st.dataframe(df)
        st.success('🎉 Available Routes 🎉')
    else:
        st.error(" ! SORRY ! No Buses 🚍 found for the selected State, Route, Rating or Timing.")
        st.info('Select Different Options and Try Again')
