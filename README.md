# VectorMind AI – Text Embedding Application

## Project Overview

VectorMind AI is a simple text embedding application developed using Python and Streamlit. It uses a pre-trained Sentence Transformer model to convert text into numerical vector representations called embeddings.

The application provides an interactive interface where users can enter text and generate its corresponding embedding vector. It also displays the embedding dimension, making it easier to understand how text is represented numerically by an embedding model.

## Features

* Convert text into numerical embeddings.
* Use a pre-trained Sentence Transformer model.
* Display the embedding dimension.
* Display the generated embedding vector.
* Interactive Streamlit interface.
* Automatic model loading and caching.
* Simple and user-friendly design.

## Technologies Used

* Python
* Streamlit
* Sentence Transformers
* `all-MiniLM-L6-v2` Embedding Model

## Project Structure

```text
VectorMind-AI/
│
├── embedding.py
└── requirements.txt
```

## How It Works

1. The user enters text into the Streamlit application.
2. The Sentence Transformer model processes the input text.
3. The model converts the text into a numerical embedding.
4. The application calculates the embedding dimension.
5. The generated vector and its dimension are displayed on the screen.

## Embedding Model

The application uses:

```text
all-MiniLM-L6-v2
```

This model converts text into a **384-dimensional embedding vector**.

For example, a single input sentence is represented as a vector containing 384 numerical values.

## Example

Input:

```text
Artificial intelligence is useful in everyday life.
```

Output:

```text
Embedding Dimension: 384
```

The application also displays the generated numerical embedding vector.

## DEMO
## Screenshot

<img width="1920" height="1080" alt="Screenshot (133)" src="https://github.com/user-attachments/assets/f615545c-387d-4987-9b86-7bf00840bf4d" />

<img width="1920" height="1080" alt="Screenshot (134)" src="https://github.com/user-attachments/assets/a0b552b3-f4f5-48d2-82fd-d648b0bf3345" />

## Applications of Text Embeddings

Text embeddings are commonly used in:

* Semantic search
* Text similarity
* Recommendation systems
* Document retrieval
* Question answering systems
* Natural Language Processing applications

## Conclusion

VectorMind AI demonstrates how an embedding model can convert human language into numerical vector representations. Using Python, Streamlit, and the Sentence Transformers library, the project provides a simple and interactive way to understand text embeddings and their role in modern Natural Language Processing applications.
