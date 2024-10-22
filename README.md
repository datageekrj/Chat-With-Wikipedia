# 🧑‍💻 Chat with Wikipedia Application

Welcome to the **Chat with Wikipedia** web application! This application allows users to interact with Wikipedia in a chat format. Simply enter the title of a Wikipedia page, and you can ask questions about that page directly, and the app will return relevant information in a conversational way. This project leverages the power of **Flask**, **Wikipedia API**, and **Google Generative AI** for delivering dynamic, user-friendly chats. 🤖

## 🚀 Features

- **Wikipedia Search**: Enter the title of a Wikipedia page and get the content for a more detailed, conversational experience.
- **Conversational AI**: You can ask questions about a Wikipedia page in a chat, and the app will respond using Google’s Generative AI.
- **Syntax Highlighting**: The app supports syntax highlighting for code blocks using **highlight.js**.
- **Markdown Support**: Chat responses are parsed with **Markdown** for rich text formatting.

## 🛠️ Tech Stack

Here is a breakdown of the technologies used in this application:

### Frontend
- **HTML5**: The structure of the webpage.
- **CSS3**: Styling the app for a modern, user-friendly experience.
- **JavaScript (Vanilla)**: Adds interactivity to the chat interface.
- **highlight.js**: Provides syntax highlighting for code snippets.
- **Google Fonts**: Uses the **Roboto** font for a clean and modern look.
- **Marked.js**: Converts Markdown text to HTML in chat messages.

### Backend
- **Flask (Python)**: The core web framework for handling requests and routing.
- **Wikipedia API**: Used to fetch text from Wikipedia based on the page title entered by the user.
- **Google Generative AI**: The conversational AI that answers user questions about Wikipedia pages.
- **wikipedia-api**: Python library to fetch page content from Wikipedia.

### APIs Used
1. **Wikipedia API**: Fetches the content of a Wikipedia page based on the title provided by the user.
2. **Google Generative AI API**: Used for answering user questions about Wikipedia page content in a conversational style.

## ⚙️ Installation Guide

Follow these steps to install and run the application on your local machine. 🎯

### Prerequisites
- Python 3.x
- Flask (`pip install Flask`)
- Wikipedia API (`pip install wikipedia-api`)
- Google Generative AI Python Client (`pip install google-generativeai`)

### Steps

1. **Clone the Repository**
   ```bash
   git clone [https://github.com/your-repo/chat-wikipedia.git](https://github.com/datageekrj/Chat-With-Wikipedia.git)
   cd chat-wikipedia
   ```

2. **Install Dependencies**
   Make sure you have all the required Python packages installed:
   ```bash
   pip install -r requirements.txt
   ```

3. **Setup API Keys**
   You’ll need to provide an API key for **Google Generative AI**. Here’s how:
   - Create a `api_key.json` file in the root of the project with the following structure:
     ```json
     {
       "key": "YOUR_GOOGLE_GENERATIVE_AI_API_KEY"
     }
     ```

4. **Run the Flask App**
   Start the Flask server by running the following command:
   ```bash
   python app.py
   ```

5. **Access the App**
   Once the server is running, open your browser and navigate to:
   ```
   http://127.0.0.1:5000
   ```

## 💻 How It Works

### 1. **Enter a Wikipedia Title**
   - On the homepage, type in the title of a Wikipedia page in the input box and click "Chat With Wiki." This sends a request to fetch the page content using the Wikipedia API.

### 2. **Start a Chat**
   - Once the page content is fetched, a chat window appears where you can ask questions about the Wikipedia content.
   
### 3. **Conversational Responses**
   - The chat uses Google Generative AI to provide natural language responses to your questions, making it feel like you're chatting with Wikipedia itself!

### 4. **Check Another Page**
   - Want to ask about another Wikipedia page? Click the "Another Wikipedia Page" button to start over!

## 📸 YouTube Demo
Here’s a sneak peek of the app in action: https://youtu.be/1mxTvmpDV-I

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🎉 Contributions
Contributions are welcome! Feel free to submit a Pull Request or open an Issue to discuss any improvements.

Enjoy chatting with Wikipedia! 🧠🌐
