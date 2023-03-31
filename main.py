import streamlit as st
import pandas as pd
import datetime
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from streamlit_option_menu import option_menu
from PIL import Image
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
        import folium
        from streamlit_folium import folium_static
        shape_tuple = [[23.250265289120904, 77.40540829355803], [23.250107568377107, 77.40497914011564], [23.24987098691169, 77.40454998667326], [23.249397822721765, 77.40394917185392], [23.249634405026583, 77.40296211893644], [23.250068138162035, 77.40188923533049], [23.25014699858056, 77.40124550516691], [23.25006813816203, 77.40030136759368], [23.250738450233026, 77.39922848398771], [23.250975030159537, 77.39828434641447], [23.25046243978831, 77.3976406162509], [23.249910417185077, 77.39802685434904], [23.249358392296827, 77.39879933054533], [23.249042948477634, 77.39957180674162], [23.248688073289212, 77.40017262156096], [23.248490919998734, 77.40068760569181], [23.248057181733795, 77.40128842051116], [23.247584011108767, 77.40214672739592], [23.247307994135603, 77.40261879618254], [23.247071407703988, 77.40334835703459], [23.2469136831831, 77.40407791788664], [23.246598233581782, 77.4051508014926], [23.245888469251092, 77.40480747873869], [23.245415290932417, 77.40429249460783], [23.245060406091877, 77.40356293375578], [23.244390065483675, 77.40274754221525], [23.244035177915574, 77.40214672739592], [23.24344369653732, 77.40150299723234], [23.242852212536526, 77.40154591257658], [23.243049374161522, 77.40227547342865], [23.243443696537323, 77.40283337290373], [23.24360142516129, 77.40334835703459], [23.24387744980447, 77.40407791788664], [23.244390065483675, 77.40472164805021], [23.244666088495027, 77.40523663218109], [23.24490267919301, 77.40588036234465], [23.24569131182231, 77.40635243113127], [23.246203920530995, 77.40738239939299], [23.246203920530995, 77.40798321421232], [23.24608562638846, 77.40849819834318], [23.247426287194042, 77.40858402903166], [23.248214904902426, 77.40901318247404], [23.248964087406257, 77.40944233591642], [23.25006813816203, 77.41000023539152], [23.250608695872465, 77.41072979624357], [23.250805846032197, 77.41012898142424], [23.25139729476258, 77.41060105021086], [23.25171273301285, 77.41111603434172], [23.251633873520237, 77.4121030872592], [23.25151558419388, 77.41287556345549], [23.251160715585222, 77.41381970102873], [23.25147615439511, 77.41377678568449], [23.252028170516947, 77.41364803965178], [23.252580184353608, 77.41326180155363], [23.252974478552105, 77.4126609867343], [23.253329342333874, 77.41177199151964], [23.25376306345126, 77.41155741479845], [23.25407849610504, 77.41108534601183], [23.25415735415188, 77.41065619256945], [23.254630501453526, 77.40958330896349], [23.25447278587288, 77.4090254094884], [23.254196783157816, 77.40889666345568], [23.253684205171215, 77.40859625604601], [23.253171625214122, 77.40812418725939], [23.252737902172907, 77.40773794916124], [23.252383036817132, 77.40726588037462], [23.25194931121088, 77.40675089624376], [23.251633873520237, 77.40615008142443], [23.251279005226362, 77.40567801263781], [23.250529835726965, 77.40584967401476], [23.250265289120904, 77.40540829355803]]

        # Create a Folium map
        m = folium.Map(location=[23.250265289120904, 77.40540829355803], zoom_start=15)

        # Add a marker to the map
        #folium.Marker([42.363600, -71.099500], popup="My Marker").add_to(m)

        # Add a polygon to the map using the shape tuple
        folium.Polygon(locations=shape_tuple, color='blue', fill_opacity=0.3).add_to(m)

        # Render the map in Streamlit
        folium_static(m)
    elif chart_select == 'Sarangpani lake' :
        df = pd.read_csv('SarangpaniLakefinal.csv')
        st.subheader('Sarangpani lake')
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
