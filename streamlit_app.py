import streamlit as st

# Roman/Classical Aesthetic Styling
st.markdown("""
    <style>
    /* Parchment background */
    .stApp {
        background: linear-gradient(to bottom, #FFF8E7, #F5E6D3);
    }

    /* Classical typography for title */
    h1 {
        font-family: 'Georgia', serif;
        color: #8B0000;
        text-align: center;
        font-size: 3em;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        margin-bottom: 0;
    }

    /* Subtitle styling */
    h3 {
        font-family: 'Georgia', serif;
        color: #4E342E;
        text-align: center;
    }

    /* Styled button */
    .stButton>button {
        background-color: #8B0000;
        color: #FFF8E7;
        border: 2px solid #D4AF37;
        font-family: 'Georgia', serif;
        padding: 0.5rem 2rem;
        font-size: 1.1em;
        transition: all 0.3s;
    }

    .stButton>button:hover {
        background-color: #A52A2A;
        border-color: #FFD700;
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }

    /* Input styling */
    .stTextInput input, .stNumberInput input {
        background-color: #FFFEF0;
        border: 2px solid #D4AF37;
        color: #3E2723;
        font-family: 'Georgia', serif;
    }

    /* Radio buttons */
    .stRadio > label {
        font-family: 'Georgia', serif;
        color: #3E2723 !important;
        font-weight: bold;
    }

    /* Labels - all form labels */
    label, .stRadio label, .stTextInput label, .stNumberInput label, .stTextArea label {
        font-family: 'Georgia', serif !important;
        color: #3E2723 !important;
        font-weight: 500 !important;
    }

    /* Radio button options - comprehensive targeting */
    .stRadio div[role="radiogroup"] label,
    .stRadio div[role="radiogroup"] label p,
    .stRadio div[role="radiogroup"] label span,
    .stRadio div[data-baseweb="radio"] label,
    .stRadio div[data-baseweb="radio"] span,
    .stRadio label p,
    .stRadio span,
    .stRadio * {
        color: #3E2723 !important;
    }

    /* Additional radio button styling */
    [data-testid="stRadio"] * {
        color: #3E2723 !important;
    }

    /* Markdown text */
    .stMarkdown {
        font-family: 'Georgia', serif;
        color: #3E2723;
    }

    /* Divider */
    hr {
        border: 1px solid #D4AF37;
    }
    </style>
""", unsafe_allow_html=True)

# Elegant Caesar Cipher Function
def caesar_cipher(text, shift, decode=False):
    """
    Elegant Caesar cipher using character arithmetic and modulo operator.

    Benefits:
    - O(n) time complexity (single pass)
    - Preserves original case (upper/lower)
    - Preserves all non-alphabetic characters
    - Automatic wrapping with modulo
    """
    if decode:
        shift = -shift

    result = []
    for char in text:
        if char.isalpha():
            # Determine base (uppercase 'A' or lowercase 'a')
            start = ord('A') if char.isupper() else ord('a')
            # Shift within 26-letter range using modulo for automatic wrapping
            shifted = (ord(char) - start + shift) % 26
            result.append(chr(start + shifted))
        else:
            # Preserve spaces, punctuation, numbers, etc.
            result.append(char)

    return ''.join(result)

# App Title with Roman decorations
st.markdown("# Caesar Cipher")
st.markdown("### _\"Veni, Vidi, Vici\"_")
st.markdown("*A cipher used by Julius Caesar to protect military messages in ancient Rome*")
st.markdown("---")

# Input Section
col1, col2 = st.columns(2)

with col1:
    choice = st.radio("Choose Mode:", ["Encode", "Decode"])

with col2:
    key = st.number_input("Shift Key (0-25):", min_value=0, max_value=25, value=3)

message = st.text_area("Enter Your Message:", height=100, placeholder="Type your message here...")

# Action Button
if st.button("Transform Message"):
    if message:
        # Apply cipher
        is_decode = (choice == "Decode")
        result = caesar_cipher(message, key, decode=is_decode)

        # Display result in styled container
        st.markdown("---")
        if choice == "Encode":
            st.markdown("### 🔒 Encrypted Message:")
        else:
            st.markdown("### 🔓 Decrypted Message:")

        # Styled result box
        st.markdown(f"""
            <div style="
                background-color: #FFFEF0;
                border: 3px solid #D4AF37;
                border-radius: 10px;
                padding: 20px;
                margin: 10px 0;
                font-family: 'Courier New', monospace;
                color: #3E2723;
                font-size: 1.2em;
                box-shadow: 0 4px 6px rgba(0,0,0,0.1);
                word-wrap: break-word;
            ">
                {result}
            </div>
        """, unsafe_allow_html=True)
    else:
        st.warning("⚠️ Please enter a message to transform.")

# Footer with historical context
st.markdown("---")
st.markdown("""
<div style="text-align: center; font-family: Georgia, serif; color: #4E342E; font-size: 0.9em;">
    <p><b>How it works:</b> Each letter is shifted by the key value in the alphabet.<br>
    For example, with key=3: A→D, B→E, C→F, ..., X→A, Y→B, Z→C</p>
    <p style="font-style: italic; margin-top: 10px;">
    "The shift cipher was used by Julius Caesar around 58 BC to send secret messages to his generals."
    </p>
</div>
""", unsafe_allow_html=True)
