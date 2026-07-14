# Chinthaka Chatbot

A simple web-based chatbot interface powered by OpenRouter AI, featuring a clean dark mode design and ChatGPT-style formatting.

## Features

- **Interactive Chat Interface**: Send messages and receive AI responses in real-time
- **Markdown Formatting**: Supports code blocks, bold, italic, lists, and links in responses
- **Responsive Design**: Works on desktop and mobile devices
- **Dark Theme**: Modern dark mode UI with Tailwind CSS
- **Auto-resizing Input**: Textarea expands as you type
- **Typing Indicator**: Shows when the AI is generating a response

## Setup

1. Download or clone this repository
2. Open `index.html` in your web browser
3. Replace the placeholder API key in the JavaScript code with your actual OpenRouter API key (get one from [openrouter.ai](https://openrouter.ai))

## Usage

- Type your message in the input field
- Press Enter to send (Shift+Enter for new line)
- The AI will respond with formatted text
- Scroll through the chat history as needed

## Technologies Used

- **Frontend**: HTML5, Tailwind CSS, Vanilla JavaScript
- **AI API**: OpenRouter (using Nvidia Nemotron model)
- **Styling**: Custom CSS for scrollbars and code blocks

## Security Note

The API key is currently embedded in the client-side code for demonstration purposes. For production use, implement proper server-side API handling to keep keys secure.

## License

This project is for educational purposes. Check OpenRouter's terms of service for API usage.
