# Setup
import pandas as pd
import streamlit as st
import tensorflow as tf
from tensorflow import keras


# Load Model
model = keras.models.load_model('model.keras')

# Load Data
df = pd.read_csv('mushroom.csv')

# Interface

# title and heading
with st.container():

    # img and title
    img_col, title_col = st.columns([.5, 1.5], vertical_alignment='center')

    with img_col:
        st.image('images/logo.png', width=150)

    with title_col:
        st.write('# 🫴🏻🍄:rainbow[Eat or Yeet]🫳🏻🍄')
        st.write('**:blue[Eat or Yeet] is a deep learning classification model, which detects a mushroom whether the mushroom is edible or poisonous.**')

# output
out = st.container(border=True)
col1, col2, col3, col4 = out.columns(4)

def output(prediction):
    
    if prediction[0][0] < 0.5:
        col1.image('images/poisonous_mushroom.jpg', width=150)
        col2.image('images/poisonous_mushroom.jpg', width=150)
        col3.image('images/poisonous_mushroom.jpg', width=150)
        col4.image('images/poisonous_mushroom.jpg', width=150)
        out.write('**:red[Poisonous Mushroom]**')
    else:
        col1.image('images/edible_mushroom.jpg', width=150)
        col2.image('images/edible_mushroom.jpg', width=150)
        col3.image('images/edible_mushroom.jpg', width=150)
        col4.image('images/edible_mushroom.jpg', width=150)
        out.write('**:blue[Edible Mushroom]**')
    return out


# Inputs
with st.container():

    # create columns for inputs
    input1, input2, input3, input4, input5 = st.columns(5)

    with input1:
        cap_shape = st.selectbox('**:green[cap shape]**', options=df['cap-shape'].unique())
    with input2:
        cap_surface = st.selectbox('**:green[cap surface]**', options=df['cap-surface'].unique())
    with input3:
        cap_color = st.selectbox('**:green[cap color]**', options=df['cap-color'].unique())
    with input4:
        bruises = st.selectbox('**:green[bruises]**', options=df['bruises'].unique())
    with input5:
        odor = st.selectbox('**:green[odor]**', options=df['odor'].unique())

    input6, input7, input8, input9, input10 = st.columns(5)

    with input6:
        gill_attachment = st.selectbox('**:green[gill attachment]**', options=df['gill-attachment'].unique())
    with input7:
        gill_spacing = st.selectbox('**:green[gill spacing]**', options=df['gill-spacing'].unique())
    with input8:
        gill_size = st.selectbox('**:green[gill size]**', options=df['gill-size'].unique())
    with input9:
        gill_color = st.selectbox('**:green[gill color]**', options=df['gill-color'].unique())
    with input10:
        stalk_shape = st.selectbox('**:green[stalk shape]**', options=df['stalk-shape'].unique())

    input11, input12, input13, input14, input15 = st.columns(5)

    with input11:
        stalk_root = st.selectbox('**:green[stalk root]**', options=df['stalk-root'].unique())
    with input12:
        stalk_surface_above_ring = st.selectbox('**:green[surface above ring]**', options=df['stalk-surface-above-ring'].unique())
    with input13:
        stalk_surface_below_ring = st.selectbox('**:green[surface below ring]**', options=df['stalk-surface-below-ring'].unique())
    with input14:
        stalk_color_above_ring = st.selectbox('**:green[color above ring]**', options=df['stalk-color-above-ring'].unique())
    with input15:
        stalk_color_below_ring = st.selectbox('**:green[color below ring]**', options=df['stalk-color-below-ring'].unique())

    input16, input17, input18, input19, input20 = st.columns(5)

    with input16:
        veil_type = st.selectbox('**:green[veil type]**', options=df['veil-type'].unique())
    with input17:
        veil_color = st.selectbox('**:green[veil color]**', options=df['veil-color'].unique())
    with input18:
        ring_number = st.selectbox('**:green[ring number]**', options=df['ring-number'].unique())
    with input19:
        ring_type = st.selectbox('**:green[ring type]**', options=df['ring-type'].unique())
    with input20:
        spore_print_color = st.selectbox('**:green[spore print color]**', options=df['spore-print-color'].unique())

    input21, input22, *x = st.columns(5)

    with input21:
        population = st.selectbox('**:green[population]**', options=df['population'].unique())
    with input22:
        habitat = st.selectbox('**:green[habitat]**', options=df['habitat'].unique())
    
    sample = {
        'cap-shape':[cap_shape], 'cap-surface':[cap_surface], 'cap-color':[cap_color], 'bruises':[bruises], 'odor':[odor], 
        'gill-attachment':[gill_attachment], 'gill-spacing':[gill_spacing], 'gill-size':[gill_size], 'gill-color':[gill_color], 
        'stalk-shape':[stalk_shape], 'stalk-root':[stalk_root], 'stalk-surface-above-ring':[stalk_surface_above_ring], 
        'stalk-surface-below-ring':[stalk_surface_below_ring], 'stalk-color-above-ring':[stalk_color_above_ring],
        'stalk-color-below-ring':[stalk_color_below_ring], 'veil-type':[veil_type], 'veil-color':[veil_color], 'ring-number':[ring_number],
        'ring-type':[ring_type], 'spore-print-color':[spore_print_color], 'population':[population], 'habitat':[habitat]
    }
    input_dict = {
        name: keras.ops.convert_to_tensor([value]) for name, value in sample.items()
        }

    prediction = model.predict(input_dict)
    output(prediction)

# Container for sharing contents
with st.container():
     # five more cols for linking app with other platforms
    youtube_col, hfspace_col, madee_col, repo_col, linkedIn_col = st.columns([1,1.2,1.08,1,1], gap='small')

    # Youtube link
    with youtube_col:
        st.link_button('**VIDEO**', icon=':material/slideshow:', url='https://youtu.be/cDHW8Ige2ng', help='YOUTUBE')
    
    # Hugging Face Space link
    with hfspace_col:
        st.link_button('**HF SPACE**', icon=':material/sentiment_satisfied:', url='https://huggingface.co/spaces/madhav-pani/Mushroom_Classifier/tree/main', help='HUGGING FACE SPACE')

    # Madee Link
    with madee_col:
        st.button('**MADEE**', icon=':material/flight:', disabled=True, help='MADEE')

    # Repository Link
    with repo_col:
        st.link_button('**REPO**', icon=':material/code_blocks:', url='https://github.com/madhavpani/Mushroom_Classifier', help='GITHUB REPOSITORY')

    # LinkedIn link
    with linkedIn_col:
        st.link_button('**CONNECT**', icon=':material/connect_without_contact:', url='https://www.linkedin.com/in/madhavpani', help='LINKEDIN')
   
