import streamlit as st

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


# st.markdown(""" 
#  <style>
#     .stApp {
#         background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
#     }
            
#     .title-container {
#         text-align: center;
#         padding: 1rem;
#         color: blue;
#     }
            
#  </style>
#  """, unsafe_allow_html=True)


# Streamlit UI
st.markdown('<div><h2>✨ Advanced Unit Converter ✨</h2></div>' ,unsafe_allow_html=True)

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

# Add some explanation about the selected conversion type
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

st.write(conversion_explanations[conversion_type])