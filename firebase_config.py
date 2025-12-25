import firebase_admin
from firebase_admin import credentials, firestore
import streamlit as st
import json
import os

if not firebase_admin._apps:
    if "FIREBASE_KEY" in st.secrets:
        # Modo Streamlit Cloud
        cred_dict = json.loads(st.secrets["FIREBASE_KEY"])
        cred = credentials.Certificate(cred_dict)
    else:
        # Modo local
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        KEY_PATH = os.path.join(BASE_DIR, "firebase_key.json")
        cred = credentials.Certificate(KEY_PATH)

    firebase_admin.initialize_app(cred)

db = firestore.client()
