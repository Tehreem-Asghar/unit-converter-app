
import streamlit as st
import google.generativeai as genai
from datetime import datetime
import uuid
import time
import os
from dotenv import load_dotenv
# import genai  # Assuming you're using the genai library






load_dotenv()

# Set page configuration
st.set_page_config(
    page_title="Multi-Tool Application",
    page_icon="🤖",
    layout="wide"
)

# Initialize session state
if 'chats' not in st.session_state:
    st.session_state.chats = {}
if 'current_chat_id' not in st.session_state:
    st.session_state.current_chat_id = None
if 'chat_titles' not in st.session_state:
    st.session_state.chat_titles = {}
if 'error_count' not in st.session_state:
    st.session_state.error_count = 0


# chat_Key = os.getenv("CHAT_KEY") 
# Configure Gemini API          


chat_Key= st.secrets["api"]["key"]
genai.configure(api_key=chat_Key)

def chat_with_gemini(user_input):
    try:
        # Reset error count on successful API call
        st.session_state.error_count = 0
        
        model = genai.GenerativeModel("gemini-1.5-pro")
        prompt = f"""
         You are a helpful AI assistant. Answer all types of questions accurately.
        
        If the user asks anything related to 'who created you', 'who made you', or 'who is your developer',
        respond with: 'I was created by Tehreem Asghar. She is a student at Governor House and is enrolled in the GIAIC course, where she is studying Artificial Intelligence.'
        
        If the user asks 'why were you created?' or anything related,
        respond with: 'I was created to assist you by answering all kinds of questions and providing useful information.'
        
        If the user requests a response in a specific language, reply in that language.
        
        User: {user_input}
        """
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        # Increment error count
        st.session_state.error_count += 1
        
        # If quota exceeded (429 error)
        if "429" in str(e):
            if st.session_state.error_count >= 3:
                return "I'm currently experiencing high traffic. Please try again in a few minutes. 🙏"
            # Wait and retry
            time.sleep(2)
            return chat_with_gemini(user_input)
        
        return "I apologize, but I'm having trouble processing your request. Please try again. 🤔"

def create_new_chat():
    chat_id = str(uuid.uuid4())
    st.session_state.chats[chat_id] = []
    st.session_state.current_chat_id = chat_id
    st.session_state.chat_titles[chat_id] = "New Chat"
    return chat_id

def delete_chat(chat_id):
    if chat_id in st.session_state.chats:
        del st.session_state.chats[chat_id]
        del st.session_state.chat_titles[chat_id]
        if st.session_state.current_chat_id == chat_id:
            st.session_state.current_chat_id = None
        return True
    return False

def get_first_message_preview(messages):
    if messages:
        first_msg = messages[0]['content']
        return first_msg[:30] + "..." if len(first_msg) > 30 else first_msg
    return "Empty chat"

# Custom CSS for styling
st.markdown("""
<style>
    /* Creator attribution */
    .creator-info {
        position: fixed;
        bottom: 10px;
        right: 10px;
        background-color: rgba(255, 255, 255, 0.9);
        padding: 5px 10px;
        border-radius: 5px;
        font-size: 0.8em;
        z-index: 1000;
        color : green
          
    }
    
    /* Sidebar styling */
    .css-1d391kg {
        padding-top: 0;
    }
    
    /* Chat title styling */
    .chat-title {
        font-size: 1.1em;
        font-weight: bold;
        margin-bottom: 5px;
    }
    
    /* Chat session styling */
    .chat-session {
        position: relative;
        padding: 10px;
        margin: 5px 0;
        border: 1px solid #ddd;
        border-radius: 5px;
        background-color: white;
    }
    
    .chat-session:hover {
        background-color: #f0f2f6;
    }
    
    /* Delete button styling */
    .delete-btn {
        position: absolute;
        top: 5px;
        right: 5px;
        color: #ff4b4b;
        cursor: pointer;
        opacity: 0.7;
    }
    
    .delete-btn:hover {
        opacity: 1;
    }
    
    /* Message styling */
    .chat-message {
        padding: 0px;
        margin: 10px 0;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    .user-message {
        background-color: #e3f2fd;
        margin-left: 20%;
    }
    
    .bot-message {
        background-color: #f5f5f5;
        margin-right: 10%;
    }
    
    /* New chat button styling */
    .new-chat-btn {
        width: 100%;
        background-color: #ff4b4b !important;
        color: white !important;
        font-weight: bold !important;
        padding: 10px 20px !important;
        border-radius: 5px !important;
        margin-bottom: 20px !important;
    }
    
    /* Error message styling */
    .error-message {
        padding: 10px;
        border-radius: 5px;
        background-color: #ffe5e5;
        color: #ff4b4b;
        margin: 10px 0;
    }
            




 
    .stChatInput {
        position: fixed;
        bottom: 50px;
        width: 90%;
      
        padding: 10px;
        z-index: 999;
         /* border: 2px solid gray;  Border added with red color */
    }





</style>

<!-- Creator attribution -->
<div class="creator-info">
    Created by Tehreem Asghar
</div>
""", unsafe_allow_html=True)

# ====================== UNIT CONVERTER ======================

# Conversion functions for each type
def length_conversion(value, from_unit, to_unit):
    units = {
        'Kilometer': 1000,
        'Meter': 1,
        'Centimeter': 0.01,
        'Millimeter': 0.001,
        'Mile': 1609.34,
        'Yard': 0.9144,
        'Foot': 0.3048,
        'Inch': 0.0254
    }
    return value * units[from_unit] / units[to_unit]

def area_conversion(value, from_unit, to_unit):
    units = {
        'Square Kilometer': 1000000,
        'Square Meter': 1,
        'Square Mile': 2589988.11,
        'Square Yard': 0.836127,
        'Square Foot': 0.092903,
        'Square Inch': 0.00064516,
        'Hectare': 10000,
        'Acre': 4046.86
    }
    return value * units[from_unit] / units[to_unit]

def data_transfer_rate_conversion(value, from_unit, to_unit):
    units = {
        'Bit per second': 1,
        'Kilobit per second': 1000,
        'Megabit per second': 1000000,
        'Gigabit per second': 1000000000,
        'Byte per second': 8,
        'Kilobyte per second': 8000,
        'Megabyte per second': 8000000,
        'Gigabyte per second': 8000000000
    }
    return value * units[from_unit] / units[to_unit]

def digital_storage_conversion(value, from_unit, to_unit):
    units = {
        'Bit': 1,
        'Byte': 8,
        'Kilobyte': 8 * 1024,
        'Megabyte': 8 * 1024**2,
        'Gigabyte': 8 * 1024**3,
        'Terabyte': 8 * 1024**4,
        'Petabyte': 8 * 1024**5
    }
    return value * units[from_unit] / units[to_unit]

def energy_conversion(value, from_unit, to_unit):
    units = {
        'Joule': 1,
        'Kilojoule': 1000,
        'Calorie': 4.184,
        'Kilocalorie': 4184,
        'Watt-hour': 3600,
        'Kilowatt-hour': 3600000,
        'Electron volt': 1.602177e-19,
        'British thermal unit': 1055.06
    }
    return value * units[from_unit] / units[to_unit]

def frequency_conversion(value, from_unit, to_unit):
    units = {
        'Hertz': 1,
        'Kilohertz': 1000,
        'Megahertz': 1000000,
        'Gigahertz': 1000000000
    }
    return value * units[from_unit] / units[to_unit]

def fuel_economy_conversion(value, from_unit, to_unit):
    units = {
        'Miles per gallon': 1,
        'Miles per gallon(Imperial)': 0.832674,
        'Kilometer per liter': 0.425144,
        'Liter per 100 kilometers': 235.215
    }
    
    # Special case for 'Liter per 100 kilometers' which is inversely related
    if from_unit == 'Liter per 100 kilometers' and to_unit != 'Liter per 100 kilometers':
        return units[to_unit] / (value / units['Liter per 100 kilometers'])
    elif to_unit == 'Liter per 100 kilometers' and from_unit != 'Liter per 100 kilometers':
        return units['Liter per 100 kilometers'] / (value * units[from_unit])
    else:
        return value * units[from_unit] / units[to_unit]

def mass_conversion(value, from_unit, to_unit):
    units = {
        'Kilogram': 1000,
        'Gram': 1,
        'Milligram': 0.001,
        'Metric ton': 1000000,
        'Pound': 453.592,
        'Ounce': 28.3495,
        'Carat': 0.2
    }
    return value * units[from_unit] / units[to_unit]

def plane_angle_conversion(value, from_unit, to_unit):
    units = {
        'Degree': 1,
        'Radian': 57.2958,
        'Gradian': 0.9,
        'Milliradian': 0.057296,
        'Minute of arc': 0.016667,
        'Second of arc': 0.000278
    }
    return value * units[from_unit] / units[to_unit]

def pressure_conversion(value, from_unit, to_unit):
    units = {
        'Pascal': 1,
        'Kilopascal': 1000,
        'Bar': 100000,
        'Pound per square inch': 6894.76,
        'Atmosphere': 101325
    }
    return value * units[from_unit] / units[to_unit]

def speed_conversion(value, from_unit, to_unit):
    units = {
        'Meter per second': 1,
        'Kilometer per hour': 0.277778,
        'Mile per hour': 0.44704,
        'Knot': 0.514444,
        'Foot per second': 0.3048
    }
    return value * units[from_unit] / units[to_unit]

def time_conversion(value, from_unit, to_unit):
    units = {
        'Second': 1,
        'Minute': 60,
        'Hour': 3600,
        'Day': 86400,
        'Week': 604800,
        'Month': 2629746,
        'Year': 31556952
    }
    return value * units[from_unit] / units[to_unit]

def volume_conversion(value, from_unit, to_unit):
    units = {
        'Cubic meter': 1000,
        'Cubic centimeter': 0.001,
        'Liter': 1,
        'Milliliter': 0.001,
        'Gallon': 3.78541,
        'Quart': 0.946353,
        'Pint': 0.473176,
        'Cup': 0.236588
    }
    return value * units[from_unit] / units[to_unit]

# Dictionary mapping conversion types to their units and conversion functions
CONVERSION_TYPES = {
    'Length': {
        'units': ['Kilometer', 'Meter', 'Centimeter', 'Millimeter', 'Mile', 'Yard', 'Foot', 'Inch'],
        'function': length_conversion
    },
    'Area': {
        'units': ['Square Kilometer', 'Square Meter', 'Square Mile', 'Square Yard', 'Square Foot', 'Square Inch', 'Hectare', 'Acre'],
        'function': area_conversion
    },
    'Data Transfer Rate': {
        'units': ['Bit per second', 'Kilobit per second', 'Megabit per second', 'Gigabit per second', 
                 'Byte per second', 'Kilobyte per second', 'Megabyte per second', 'Gigabyte per second'],
        'function': data_transfer_rate_conversion
    },
    'Digital Storage': {
        'units': ['Bit', 'Byte', 'Kilobyte', 'Megabyte', 'Gigabyte', 'Terabyte', 'Petabyte'],
        'function': digital_storage_conversion
    },
    'Energy': {
        'units': ['Joule', 'Kilojoule', 'Calorie', 'Kilocalorie', 'Watt-hour', 'Kilowatt-hour', 
                 'Electron volt', 'British thermal unit'],
        'function': energy_conversion
    },
    'Frequency': {
        'units': ['Hertz', 'Kilohertz', 'Megahertz', 'Gigahertz'],
        'function': frequency_conversion
    },
    'Fuel Economy': {
        'units': ['Miles per gallon', 'Miles per gallon(Imperial)', 'Kilometer per liter', 'Liter per 100 kilometers'],
        'function': fuel_economy_conversion
    },
    'Mass': {
        'units': ['Kilogram', 'Gram', 'Milligram', 'Metric ton', 'Pound', 'Ounce', 'Carat'],
        'function': mass_conversion
    },
    'Plane Angle': {
        'units': ['Degree', 'Radian', 'Gradian', 'Milliradian', 'Minute of arc', 'Second of arc'],
        'function': plane_angle_conversion
    },
    'Pressure': {
        'units': ['Pascal', 'Kilopascal', 'Bar', 'Pound per square inch', 'Atmosphere'],
        'function': pressure_conversion
    },
    'Speed': {
        'units': ['Meter per second', 'Kilometer per hour', 'Mile per hour', 'Knot', 'Foot per second'],
        'function': speed_conversion
    },
    'Time': {
        'units': ['Second', 'Minute', 'Hour', 'Day', 'Week', 'Month', 'Year'],
        'function': time_conversion
    },
    'Volume': {
        'units': ['Cubic meter', 'Cubic centimeter', 'Liter', 'Milliliter', 'Gallon', 'Quart', 'Pint', 'Cup'],
        'function': volume_conversion
    }
}

# Conversion explanations
conversion_explanations = {
    'Length': 'Convert between different units of length or distance.',
    'Area': 'Convert between different units of area or surface measurement.',
    'Data Transfer Rate': 'Convert between different units of data transfer speed.',
    'Digital Storage': 'Convert between different units of digital data storage.',
    'Energy': 'Convert between different units of energy and work.',
    'Frequency': 'Convert between different units of frequency or rate of occurrence.',
    'Fuel Economy': 'Convert between different units of fuel consumption.',
    'Mass': 'Convert between different units of mass or weight.',
    'Plane Angle': 'Convert between different units of angular measurement.',
    'Pressure': 'Convert between different units of pressure or force per unit area.',
    'Speed': 'Convert between different units of speed or velocity.',
    'Time': 'Convert between different units of time.',
    'Volume': 'Convert between different units of volume or capacity.'
}

# Create main tabs
tab1, tab2 = st.tabs(["Unit Converter", "Gemini AI Chatbot"])

# Unit Converter Tab
with tab1:
    st.markdown('<div><h2>✨ Advanced Unit Converter ✨</h2></div>', unsafe_allow_html=True)
    
    # Select conversion type
    conversion_type = st.selectbox('Select Conversion Type', list(CONVERSION_TYPES.keys()))
    
    # Get the selected conversion type's details
    current_converter = CONVERSION_TYPES[conversion_type]
    
    # Input value
    value = st.number_input('Enter Value', value=0.0)
    
    # Select units
    col1, col2 = st.columns(2)
    with col1:
        from_unit = st.selectbox('From Unit', current_converter['units'])
    with col2:
        to_unit = st.selectbox('To Unit', current_converter['units'])
    
    # Calculate and display result
    if st.button('Convert'):
        st.balloons()
        result = current_converter['function'](value, from_unit, to_unit)
        st.success(f'{value} {from_unit} = {result:.6f} {to_unit}')
    
    # Add helpful information
    st.info(f'This converter supports {len(current_converter["units"])} different units for {conversion_type} conversion.')
    
    # Add a divider
    st.divider()
    
    # Add explanation about the selected conversion type
    st.write(conversion_explanations[conversion_type])

# Chatbot Tab
with tab2:
    # Sidebar for chat history
    with st.sidebar:
        st.title("💬 Chat History")
        
        # New Chat button
        if st.button("+ New Chat", key="new_chat", help="Start a new chat session", use_container_width=True):
            create_new_chat()
        
        st.divider()
        
        # Display chat sessions
        if st.session_state.chats:
            for chat_id, messages in st.session_state.chats.items():
                # Create a unique key for each button
                button_key = f"chat_session_{chat_id}"
                delete_key = f"delete_{chat_id}"
                
                # Get chat title
                chat_title = st.session_state.chat_titles.get(chat_id, "Untitled Chat")
                
                # Create a container for the chat session
                col1, col2 = st.columns([6, 1])
                
                with col1:
                    if st.button(
                        f"📝 {chat_title}\n\n{get_first_message_preview(messages)}",
                        key=button_key,
                        help="Click to view this chat",
                        use_container_width=True
                    ):
                        st.session_state.current_chat_id = chat_id
                        st.rerun()
                
                with col2:
                    if st.button("🗑️", key=delete_key, help="Delete this chat"):
                        if delete_chat(chat_id):
                            st.success("Chat deleted!")
                            st.rerun()
                
                st.divider()
        else:
            st.info("No chat history yet. Start a new chat!")
    
    # Main chat area
    if not st.session_state.current_chat_id:
        create_new_chat()
    
    # Display current chat
    st.title("💬 Gemini AI Chatbot")
    
    # Display messages in current chat
    current_messages = st.session_state.chats.get(st.session_state.current_chat_id, [])
    
    # Chat display area with some bottom padding for input box
    chat_container = st.container()
    with chat_container:
        for message in current_messages:
            with st.chat_message(message["role"]):
                st.write(message["content"])
                st.caption(message.get("timestamp", ""))
    




    # Chat input
    if prompt := st.chat_input("Type your message here..."):
        if prompt.strip():
            # Add user message
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            # Update chat title with first message if it's empty
            if not current_messages:
                st.session_state.chat_titles[st.session_state.current_chat_id] = prompt[:30]
            
            # Add message to current chat
            st.session_state.chats[st.session_state.current_chat_id].append({
                "role": "user",
                "content": prompt,
                "timestamp": timestamp
            })
            
            # Display user message
            with st.chat_message("user"):
                st.write(prompt)
                st.caption(timestamp)
            
            # Get and display assistant response
            with st.chat_message("assistant"):
                with st.spinner("Thinking..."):
                    response = chat_with_gemini(prompt)
                    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    
                    # Add assistant message to current chat
                    st.session_state.chats[st.session_state.current_chat_id].append({
                        "role": "assistant",
                        "content": response,
                        "timestamp": timestamp
                    })
                    
                    st.write(response)
                    st.caption(timestamp)
            
            # Rerun to update the sidebar
            st.rerun()