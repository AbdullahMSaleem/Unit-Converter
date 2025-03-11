import streamlit as st
from forex_python.converter import CurrencyRates

def convert_length(value, from_unit, to_unit):
    conversion_factors = {
        "Kilometre": 1000,
        "Metre": 1,
        "Centimetre": 0.01,
        "Millimetre": 0.001,
        "Mile": 1609.34,
        "Yard": 0.9144,
        "Foot": 0.3048,
        "Inch": 0.0254,
    }
    return value * (conversion_factors[from_unit] / conversion_factors[to_unit])

def convert_weight(value, from_unit, to_unit):
    conversion_factors = {
        "Kilogram": 1,
        "Gram": 0.001,
        "Milligram": 0.000001,
        "Pound": 0.453592,
        "Ounce": 0.0283495,
    }
    return value * (conversion_factors[from_unit] / conversion_factors[to_unit])

def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    elif from_unit == "Celsius" and to_unit == "Fahrenheit":
        return (value * 9/5) + 32
    elif from_unit == "Celsius" and to_unit == "Kelvin":
        return value + 273.15
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        return (value - 32) * 5/9
    elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
        return (value - 32) * 5/9 + 273.15
    elif from_unit == "Kelvin" and to_unit == "Celsius":
        return value - 273.15
    elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
        return (value - 273.15) * 9/5 + 32

def main():
    st.title("Unit Converter ⚡")
    st.write("One tap, endless conversions—no limits, just results!")
    
    category = st.selectbox("Select Category", ["Length", "Weight", "Temperature"])
    value = st.number_input("Enter Value", min_value=0.0, format="%.2f")
    
    if category == "Length":
        units = ["Kilometre", "Metre", "Centimetre", "Millimetre", "Mile", "Yard", "Foot", "Inch"]
        from_unit = st.selectbox("From", units)
        to_unit = st.selectbox("To", units)
        result = convert_length(value, from_unit, to_unit)
    
    elif category == "Weight":
        units = ["Kilogram", "Gram", "Milligram", "Pound", "Ounce"]
        from_unit = st.selectbox("From", units)
        to_unit = st.selectbox("To", units)
        result = convert_weight(value, from_unit, to_unit)
    
    elif category == "Temperature":
        units = ["Celsius", "Fahrenheit", "Kelvin"]
        from_unit = st.selectbox("From", units)
        to_unit = st.selectbox("To", units)
        result = convert_temperature(value, from_unit, to_unit)
    
    if st.button("Convert"):
        st.success(f"Converted Value: {result:.2f} {to_unit}")

if __name__ == "__main__":
    main()