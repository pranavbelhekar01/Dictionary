
# 📚 Advanced English Dictionary Agent

Checkout app [here](https://advance-dictionary.streamlit.app/)

## 🌟 Overview

This is an **advanced dictionary agent** designed to provide comprehensive insights into the English language. Unlike a simple dictionary, this tool offers definitions, grammatical forms, usage examples, pronunciation guidance, formality levels, word intensity comparisons, and much more. The agent also suggests alternative words and appropriate scenarios for usage, helping users choose the perfect word for any context.

## ✨ Features

- 📖 **Word Definition**: Get the full meaning of any word in simple terms.
- 📝 **Grammatical Forms**: Discover various forms of the word (noun, adjective, verb, adverb) with sentences showing how to use each form.
- 🔊 **Pronunciation Guide**: Learn how to pronounce the word correctly with phonetic spelling and tips.
- 🏛️ **Formality Level**: Understand if the word is formal or casual, and see formal and informal alternatives.
- 🎯 **Usage Scenarios**: View specific scenarios where the word should be used, along with suggestions of when not to use it.
- 💡 **Word Intensity**: Compare words with varying levels of intensity and emotional impact (e.g., injured vs. catastrophic).
- 🔄 **Synonyms & Antonyms**: Get a list of synonyms and antonyms with brief meanings to understand the nuances between them.
- 🧠 **Contextual Suggestions**: Users can provide a {context} (optional) to get suggestions tailored to a specific situation, improving the relevance of the word usage.

## 💻 How to Use

1. **Input**: Enter any English word you'd like to explore. Optionally, you can provide a {context} to refine the suggestions (e.g., "In a workplace setting to describe performance").
2. **Output**: The dictionary agent will return:
   - Definition of the word.
   - Grammatical forms (adjective, verb, noun, etc.) with example sentences.
   - Pronunciation guide with phonetic spelling.
   - Formality level and usage scenarios (formal/casual versions).
   - Scenarios where the word is appropriate, and alternatives where it isn’t.
   - Synonyms and antonyms, including brief meanings.
   - Suggestions for words with different intensity levels, helping you select the most appropriate one.

## 🚀 Deployment

This dictionary agent is built on **Streamlit**, providing an interactive web application that is easy to use and navigate.

### ⚙️ Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone <repository_url>
   ```
2. **Install dependencies**:
   Make sure you have `Streamlit` and any other necessary libraries installed. You can install them using:
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the Streamlit app**:
   ```bash
   streamlit run app.py
   ```
4. **Access the app**: Once the app is running, you can access it via `localhost` in your browser.

### 🔎 Additional Notes

- **Contextual Queries**: While providing a word query, you can also pass an optional context to get more refined suggestions based on your situation.
- If no context is provided, the dictionary agent will offer general word suggestions and usage.

## 🛠️ Future Enhancements

- 🌐 **Multilingual Support**: Adding support for multiple languages to expand beyond English.
- 📊 **Integration with Thesaurus APIs**: For a broader range of synonyms and usage examples.
- 🗣️ **User Feedback System**: Allow users to provide feedback on the suggestions for continuous improvement.

