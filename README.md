# Emoji Message Encoder

This is a very simple and fun Flask web application that encodes and decodes messages using emoji sequences. Hide your messages in plain sight by transforming text into a string of random emojis with hidden data!

## Table of Contents

- [Emoji Message Encoder](#emoji-message-encoder)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Demo](#demo)
  - [Installation](#installation)
  - [Usage](#usage)

## Features

- **Encode Messages:** Transform a plain text message into a seemingly random sequence of emojis.
- **Decode Messages:** Reveal the hidden message from an emoji sequence.
- **Web Interface:** A sleek, responsive UI built with HTML, CSS, and JavaScript.

## Demo

Check out the live version of the app on [Vercel](https://emoji-message-encoder.vercel.app/).

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/Umid0vic/emoji_message_encoder.git
   cd emoji_message_encoder
   ```

2. **(Optional) Create and Activate a Virtual Environment:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install Dependencies:**

   The project requires Flask and a pinned version of MarkupSafe:

   ```bash
   pip install -r requirements.txt
   ```

   _Note:_ The **requirements.txt** file includes:
   ```
   Flask==1.1.4
   MarkupSafe==2.0.1
   ```

## Usage

1. **Run the App Locally:**

   ```bash
   python app.py
   ```

   Open your browser and go to [http://localhost:5000](http://localhost:5000) to see the app in action.


Enjoy encoding your secret messages with emojis!