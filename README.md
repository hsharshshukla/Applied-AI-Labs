# Applied AI Labs

Hands-on implementations and experiments across Machine Learning, NLP, vector databases, and Generative AI.

## Overview

Applied AI Labs is a collection of practical exercises and small applications created while exploring the foundations and application layer of modern AI systems.

The repository covers the progression from text preprocessing and traditional machine-learning concepts to embeddings, vector databases, LLM APIs, multimodal use cases, and chatbot integrations.

This repository is intentionally a **lab / experimentation repository**, not a single production application.

## Areas Covered

### NLP & Machine Learning

- Text preprocessing
- Text representation
- Bag of Words / vector-based representations
- Word embeddings
- Text classification
- Sentiment-oriented datasets and experiments

### Vector Databases

Hands-on experiments with:

- Pinecone
- ChromaDB
- embeddings
- semantic retrieval concepts

### Generative AI

Experiments include:

- OpenAI API integration
- text generation
- image generation
- audio transcription / translation
- chatbot workflows
- multimodal application concepts

### Integrations

Small applications and integrations include:

- Flask-based AI applications
- Telegram chatbot integration
- file-upload workflows
- Hugging Face experiments

## Repository Structure

The repository contains notebook-based experiments alongside small Python applications.

Typical areas include:

```text
Applied-AI-Labs/
│
├── NLP / Text Representation
├── Text Preprocessing
├── Text Classification
├── Pinecone Experiments
├── ChromaDB Experiments
├── Hugging Face Experiments
├── Audio Translation
├── Image Generation
└── Telegram Chatbot
```

## Technology

### Languages
- Python

### AI / ML
- Machine Learning
- NLP
- Embeddings
- Generative AI
- LLM APIs

### Libraries / Platforms
- OpenAI
- Hugging Face
- Pinecone
- ChromaDB
- Pandas
- Flask

### Integrations
- Telegram Bot API
- Audio / speech processing
- Image-generation APIs

## What This Repository Demonstrates

This repository is useful as evidence of breadth across the AI stack:

```text
Text Processing
      │
      ▼
Machine Learning / NLP
      │
      ▼
Embeddings
      │
      ▼
Vector Databases
      │
      ▼
Generative AI / LLM APIs
      │
      ▼
Small AI Applications & Integrations
```

The objective was to move from conceptual understanding toward hands-on implementation.

## Project Status

**Experimental / learning lab**

Some implementations were created with earlier versions of libraries and APIs and may require updates before running in a current environment.

The repository is retained as part of my technical portfolio because it shows the progression of my hands-on work across ML, NLP, vector search, and Generative AI.

## Security

API keys, tokens, credentials, and environment-specific secrets should never be committed to source control.

Use environment variables or a local `.env` file excluded through `.gitignore`.

Example:

```text
OPENAI_API_KEY=your_key_here
TELEGRAM_BOT_TOKEN=your_token_here
```

## Current Direction

My more recent work extends these concepts into:

- Retrieval-Augmented Generation (RAG)
- backend AI platforms
- vector retrieval architecture
- AI agents
- enterprise knowledge systems
- system design and production-oriented AI applications

See **Neura-RAG** for a more integrated RAG application.
