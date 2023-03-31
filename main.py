import streamlit as st
import pandas as pd
import datetime
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from streamlit_option_menu import option_menu
from PIL import Image
import folium
from streamlit_folium import folium_static
st.set_page_config(layout="wide")


@st.cache_data
def load_data(path):
    data = pd.read_csv(path)
    df1 = data.filter(
        [
            "Chlorophyll",
            "Dissolved Oxygen",
            "Dissolved Oxygen Matter",
            "Salinty",
            "Temperature",
            "Turbidity",
            "pH",
            "Suspended Matter",
        ]
    )
    data["Date"] = pd.to_datetime(data["Date"], errors="coerce")
    data["Date"] = pd.to_datetime(data["Date"]).dt.date
    data["Year"] = pd.to_datetime(data["Date"]).dt.strftime("%Y")
    data["Month"] = pd.to_datetime(data["Date"]).dt.strftime("%m")
    data["Day"] = pd.to_datetime(data["Date"]).dt.strftime("%d")
    # data=data.set_index("Date")
    return data, df1

with open("styles.css", "r") as source_style:
 st.markdown(f"<style>{source_style.read()}</style>", 
             unsafe_allow_html = True)

st.title("Water Quality Monitoring")

header_project = st.container()
data_collection = st.container()
data_analysis = st.container()



data_df, df1 = load_data("merged_data.csv")

with st.sidebar:
    selected = option_menu(
        menu_title="Main Menu",
        options=[
            "Project",
            "Data Collection",            
            "Interactive Data Analysis",
            "Data Analysis Findings",
        ],
        default_index=0,
    )


if selected == "Project":

    with header_project:
        st.title("Water Quality Monitoring in Lendyia Lake Bhopal")
        introduction_str=""" Water is a very crucial resource for all the living beings on Earth. Therefore, it is necessary to 
monitor water quality to ensure that it is safe for consumption and does not pose any harm to the 
environment. Water quality monitoring is done on the basis of various parameters. These 
parameters include Temperature, Turbidity, Chlorophyll-a (Chl-a), Blue-green algae 
Phycocyanin, Dissolved oxygen concentration, Specific conductivity, Fluorescent dissolved 
organic matter (FDOM) and Pollution sediments.  In the current world scenario there are many 
ways to monitor water quality. One of these ways is using Satellite Imagery and GIS techniques. 
Satellite imagery is a powerful tool for monitoring water quality as it provides a broad and 
detailed view of the region. It can capture data on water temperature, color, and clarity, which 
are essential indicators of water quality. Moreover, satellite imagery can provide data on the 
extent of contamination and the source of pollution. GIS techniques can be used to analyze and 
interpret the satellite data to identify areas of concern and develop appropriate strategies to 
address them. \n
 Bhopal region, located in the central part of India, is well known for its beautiful lakes. It is also 
called “The City of Lakes”.  However, due to rapid urbanization and industrialization, the water 
quality of the region is deteriorating at an alarming rate. The aftereffects of Bhopal Gas Tragedy 
still show significances in determining various water quality parameters. In this article we will 
see the measures taken by our Project in monitoring the water quality in Bhopal region using 
Satellite Imagery and GIS techniques. \n
In this article, we  will discuss the data visualization and analysis of Lendyia Lake. Lendyia 
Lake is a significant source of freshwater for the region, and its water quality is vital to maintain 
the ecological balance. In this analysis, we examine the various parameters of water quality in the lake
and identify the areas that require treatment.
"""
        st.text(introduction_str            
        )


if selected == "Data Collection":
    with data_collection:
        st.title("Data Collection")
        st.text(
            """ In the first week of the project, we conducted research on different types of APIs for 
collecting water quality data in Bhopal. After careful consideration, we chose the 
Google Earth Engine API for our data collection. \n
In the second week, we started collecting data using the Google Earth Engine API, 
using Sentinel 2A and Landsat 8 satellite imagery to collect data on various water 
quality parameters, including chlorophyll, turbidity, salinity, pH, dissolved oxygen, 
dissolved organic matter, and suspended matter."""
        )

if selected =='Data Analysis Findings':
	st.header("Water Quality Index and Parameters Identification")
	str_text_body = """ 
	There are several water quality parameters available, but the team has chosen the following 8 important 
parameters to monitor water quality.\n

1-pH:One of the most crucial indicators of water quality is pH. The pH scale determines how basic or acidic a 
solution is. \n
2- Salinity: The quantity of dissolved salts in water is known as salinity.
Water that is cloudy or hazy due to numerous tiny particles that are often unseen to the unaided eye is said to 
be turbid. Water quality is typically impacted by suspended sediments, such as clay, dirt, and silt particles, 
which frequently enter the water from disturbed locations.\n

3- Temperature: The aquatic system is significantly influenced by water temperature, which also affects the habitat's 
suitability for supporting aquatic life. Lower oxygen solubility in warmer water restricts the amount of oxygen
available.\n

4- Chlorophyll: A popular indicator of water quality and eutrophication level is chlorophyll-a.
The concentration of phytoplankton is determined by the amount of chlorophyll present in a water sample. 
Greater concentrations, which often occur when high algal production is sustained, indicate poorer water quality.\n


5- Suspended matter: Fine particles make up suspended matter, which is in suspension. Plankton, tiny pieces of plant matter,
and minerals are among those that naturally occur in river water, whilst others are a result of human activity
(organic and inorganic matter). Water can become more turbid due to suspended materials, harming the ecology 
of rivers and streams.\n

6- Dissolved oxygen (DO) is a gaseous form of molecular oxygen (O2) that comes from the environment. 
The concentrations of dissolved oxygen in water are influenced by salinity and temperature. 
Temperature and salinity have an opposite relationship with oxygen solubility in water;
as these two variables rise, so does DO.\n
7- The organic matter percentage in solution that passes through a 0.45 m filter is referred to as
"dissolved organic matter" (DOM). The mass of other elements, such as nitrogen, oxygen, and hydrogen,
that are present in organic material is also included in DOM. The total mass of the dissolved organic matter
is referred to here as DOM. \n

This figure shows paramters values for safe and danger zone. \n
"""
	st.text(str_text_body)
	image = Image.open('Parameter-Thresholds.png')
	st.image(image)

	st.header("Findings")
	st.subheader('Per-year Findins')
	str_findings= """
1- pH level had outlier in 2019, 2022. However it could be concluded that each year the distribution ranges changes
2- Turbidity had outliers values since 2019, however the disrtibution didn't change across the years
3- Temperautre had outliersin every-year. However we have no information in 2022.
 In covid year the disribution of temperatures varies. However before and  after 2020 the temperatures variation across years is not large
4- Salinty had large number of outliers in 2019. However distribution and ranges across year varies.
5- Disssolved oxygen matter is the most consisent features across years. There are small number of outliers
6- Dissolved oxygen had outliers since 2019. However the disrtibution across years are quit similar.
"""
	st.text(str_findings)
	st.subheader('Per-Month Findins')
	str_findings= """
1- Chrolophyll values across year pe-month ar not so good except for 2022 fisrt month has bad zone values. 
2- Dissloved oxygen for 20220 values where in bad zone and begging of2021. Hoever the rest are in good zone values
3- Dissolved oxygen matters for 2019,2018 the values where in bad zone ranges. However, 
for 2020,2021,2022 for first 2 months andlast 3 months the values where in good zone range however
from month 3-9 the values are too high
4- Salinty values are between 0-1 for most year hence, lies whithin bad zone values
5- Trubidity values are less than 0 for all months hence lies within good zone 
6- pH values are in good zone ranges for all years and months
"""
	st.text(str_findings)
	st.subheader('Overall Conclusion')
	str_findings="""
Our data collection efforts yielded a rich dataset of water quality parameters for Lendyia lake in the Bhopal region.
We found that chlorophyll levels varied widely showing high levels of chlorophyll, indicating high levels of algae and other aquatic plants. 
Turbidity levels were generally within the acceptable range.
pH levels were generally within the acceptable range.
Dissolved oxygen levels were generally within the acceptable range as well, however there were some outliers.
For the dissolved oxygen matters: Mmre than **50%** of the values lie in **need treatment zone**.
Overall, the data provides a comprehensive view of water quality in the Bhopal region and can be
used to inform future efforts to monitor and manage water resources in the area.
"""
	st.text(str_findings)
	st.subheader('Conclusion')
	str_conclusino="""
In conclusion, monitoring water quality using satellite imagery, GIS techniques, and 
machine learning is crucial to ensure safe water consumption and protect the 
environment. These technologies provide a broad and detailed view of the region, 
which is essential for developing appropriate strategies to address water quality 
issues. The project's findings and recommendations can inform stakeholders to 
implement effective and sustainable monitoring programs to ensure the long-term 
	"""
	st.text(str_conclusino)




if selected == "Interactive Data Analysis":


    st.sidebar.subheader("Visualisation Settings")

    # add a select widget to the sidebar
    chart_select = st.sidebar.selectbox(
        label = "Select the Lake",
        options = ['Hathaikheda dam', 'Sarangpani lake', 'Upper lake']
    )
    if chart_select == 'Hathaikheda dam':
        df = pd.read_csv('Hathaikheda.csv')
        st.subheader('Hathaikheda dam')
        
        shape_tuple = [[23.276159781091796, 77.48381495776124], [23.275981245796764, 77.48359275012776], [23.275902400663092, 77.48316359668537], [23.275606730996113, 77.48333525806233], [23.275429328880875, 77.4835283771114], [23.275035101112213, 77.48348546176716], [23.274995678271157, 77.48324942737385], [23.27456202624964, 77.4839789882259], [23.27420721900009, 77.48374295383259], [23.273734141197263, 77.48339963107868], [23.27333990841148, 77.48202634006306], [23.273537024950212, 77.48425793796345], [23.273300485068734, 77.48524499088093], [23.273162503277234, 77.48616767078205], [23.272176914895812, 77.48786282687946], [23.272019220078107, 77.48932194858357], [23.272019220078107, 77.49069523959919], [23.270718230709516, 77.49168229251667], [23.270245140516476, 77.49288392215534], [23.270402837434148, 77.49348473697468], [23.269678267622574, 77.49371020641799], [23.26928402283434, 77.49276606884474], [23.268574379275776, 77.49285189953322], [23.267806444763416, 77.49248135600928], [23.267451619521786, 77.49175179515723], [23.266741966203956, 77.49192345653418], [23.265992883601633, 77.49123681102637], [23.26528322251516, 77.4914943030918], [23.264691835389545, 77.49085057292822], [23.264337001854468, 77.49115098033789], [23.264179297757845, 77.49188054118994], [23.262996511084673, 77.49196637187842], [23.263390774475408, 77.49278176341895], [23.26410044563953, 77.49312508617285], [23.264415853832798, 77.49278176341895], [23.26528322251516, 77.4929534247959], [23.26587460701633, 77.49415505443457], [23.2662688618924, 77.49445546184424], [23.266111160081945, 77.49501336131934], [23.26630828731585, 77.49535668407324], [23.266347712727633, 77.49582875285986], [23.266544839611605, 77.49660122905615], [23.265559202275632, 77.49668705974463], [23.26516494529999, 77.49582875285986], [23.264691835389545, 77.49595749889258], [23.263982167374618, 77.49570000682715], [23.263785036699794, 77.49509919200781], [23.262681099532323, 77.49574292217139], [23.269265160829594, 77.50084984813574], [23.269895952020086, 77.50127900157813], [23.274547944814806, 77.49939072643164], [23.275178710991543, 77.49973404918555], [23.27541524753774, 77.50012028728369], [23.27600658706548, 77.4999057105625], [23.275809474181273, 77.49917614971045], [23.27608543213749, 77.49883282695654], [23.277303103570617, 77.49905442493679], [23.277657902573278, 77.49832486408474], [23.277579058432142, 77.49780987995388], [23.27817038835291, 77.49755238788845], [23.27686945906157, 77.49729489582302], [23.276554080349985, 77.49669408100368], [23.277224259219434, 77.49579285877468], [23.277894434716618, 77.4957070280862], [23.277539636344073, 77.49523495929958], [23.27686945906157, 77.49540662067653], [23.2764752355554, 77.49523495929958], [23.276435813140612, 77.49454831379177], [23.27592332068646, 77.49506329792263], [23.275292558035876, 77.49416207569362], [23.275253135271036, 77.49360417621853], [23.27434640845934, 77.49476289051296], [23.273557945345097, 77.4948058058572], [23.27320313542108, 77.49411916034938], [23.273873331150828, 77.49308919208767], [23.273597368611647, 77.49248837726833], [23.274228139289725, 77.49171590107204], [23.274858906980878, 77.491887562449], [23.274977175590436, 77.49094342487575], [23.27572620767904, 77.49064301746608], [23.274109870015103, 77.48939847248317], [23.27340025216221, 77.48926972645046], [23.273518522066873, 77.48669480579616], [23.273833907965955, 77.48613690632106], [23.274819484087697, 77.48545026081325], [23.27548967168506, 77.48510693805935]]

        # Create a Folium map
        m = folium.Map(location=[23.276159781091796, 77.48381495776124], zoom_start=15)

        # Add a marker to the map
        #folium.Marker([42.363600, -71.099500], popup="My Marker").add_to(m)

        # Add a polygon to the map using the shape tuple
        folium.Polygon(locations=shape_tuple, color='blue', fill_opacity=0.3).add_to(m)

        # Render the map in Streamlit
        folium_static(m)
    elif chart_select == 'Sarangpani lake' :
        df = pd.read_csv('SarangpaniLakefinal.csv')
        st.subheader('Sarangpani lake')

        shape_tuple = [[23.244997616477278, 77.47025211456], [23.244248411693995, 77.4703594029206], [23.244061109840693, 77.47089584472357], [23.24396252981228, 77.4707027256745], [23.243775227557578, 77.47074564101874], [23.243647073231774, 77.47029502990424], [23.243499202702868, 77.47043450477301], [23.243440054445415, 77.47086365821539], [23.24331189979763, 77.47074564101874], [23.243035873984248, 77.47107823493658], [23.243213319215556, 77.47135718467413], [23.242986583600327, 77.47164686324774], [23.2428781446916, 77.47203310134589], [23.24237538132672, 77.47211893203436], [23.242188076843604, 77.4725588143128], [23.241902190546604, 77.47259100082098], [23.242188076843604, 77.47295578124701], [23.243400622259205, 77.47293432357489], [23.24357806700535, 77.47263391616522], [23.243785085577528, 77.47251589896857], [23.24409068383501, 77.47215111854254], [23.24450471906707, 77.47203310134589], [23.244997616477278, 77.47100313308417], [23.245165201181862, 77.47038086059271], [23.244997616477278, 77.47025211456]]

        # Create a Folium map
        m = folium.Map(location=[23.244997616477278, 77.47025211456], zoom_start=15)

        # Add a marker to the map
        #folium.Marker([42.363600, -71.099500], popup="My Marker").add_to(m)

        # Add a polygon to the map using the shape tuple
        folium.Polygon(locations=shape_tuple, color='blue', fill_opacity=0.3).add_to(m)

        # Render the map in Streamlit
        folium_static(m)
    elif chart_select == 'Upper lake' :
        df = pd.read_csv('UPLake.csv')
        st.subheader('Upper Lake')

    # add a checkbox to show/hide dataset
    show_data = st.sidebar.checkbox("Show dataset")

    if show_data:
        st.write(df.head())

    global numeric_columns
    try:
        numeric_columns  = list(df.select_dtypes(['float','int' ]).columns)
    except Exception as e:
        print(e)
        

    # add a select widget to the sidebar
    chart_select = st.sidebar.selectbox(
        label = "Select the Chart Type",
        options = ['Scatterplots', 'Lineplots', 'Histogram', 'Boxplot']
    )

    if chart_select == 'Scatterplots':
        st.sidebar.subheader('Scatterplot Settings')
        try:
            x_values = st.sidebar.selectbox('X axis', options = numeric_columns)
            y_values = st.sidebar.selectbox('Y axis', options = numeric_columns)
            plot = px.scatter(data_frame = df, x = x_values, y = y_values)
            st.plotly_chart(plot)
        except Exception as e:
            print(e)

    if chart_select == 'Lineplots':
        st.sidebar.subheader('Lineplots Settings')
        try:
            x_values = st.sidebar.selectbox('X axis', options = numeric_columns)
            y_values = st.sidebar.selectbox('Y axis', options = numeric_columns)
            plot = px.area(data_frame = df, x = x_values, y = y_values)
            st.plotly_chart(plot)
        except Exception as e:
            print(e)

    if chart_select == 'Boxplot':
        st.sidebar.subheader('Boxplot Settings')
        try:
            x_values = st.sidebar.selectbox('X axis', options = numeric_columns)
            y_values = st.sidebar.selectbox('Y axis', options = numeric_columns)
            plot = px.box(data_frame = df, x = x_values, y = y_values)
            st.plotly_chart(plot)
        except Exception as e:
            print(e)

    if chart_select == 'Histogram':
        st.sidebar.subheader('Histogram Settings')
        try:
            x_values = st.sidebar.selectbox('Select the variable to plot histogram', options = numeric_columns)
            bins = st.sidebar.slider("Select the number of bins", min_value=5, max_value=50, value=20, step=1)
            plot = px.histogram(data_frame = df, x = x_values, nbins=bins)
            st.plotly_chart(plot)
        except Exception as e:
            print(e)
