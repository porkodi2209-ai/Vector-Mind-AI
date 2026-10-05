import streamlit as st
from sentence_transformers import SentenceTransformer

st.set_page_config(page_title="VectorMind AI")

st.title("VectorMind AI")
st.write("Convert text into numerical embeddings using an embedding model.")

@st.cache_resource
def load_model():
    return SentenceTransformer("all-MiniLM-L6-v2")

model = load_model()

text = st.text_area(
    "Enter your text",
    placeholder="Example: Artificial intelligence is changing technology."
)

if st.button("Generate Embedding"):
    if text.strip():
        embedding = model.encode(text)

        st.success("Embedding generated successfully!")

        st.write("Embedding Dimension:", len(embedding))

        st.subheader("Embedding Vector")
        st.write(embedding)

    else:
        st.warning("Please enter some text.")