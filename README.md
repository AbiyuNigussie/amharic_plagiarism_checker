# Plagiarism Checker

A plagiarism detection tool designed for Amharic text. This project uses Natural Language Processing (NLP) techniques to identify potential plagiarism in Amharic language documents. The tool compares text input against a variety of sources to determine the level of similarity and provides a percentage-based report of potential copied content. The project is built with **Flask** to serve as a web application, making it easy to access and use.

## Features

- Detects plagiarism in Amharic text.
- Supports the use of various NLP methods to compare texts.
- Provides a plagiarism score based on text similarity.
- Web-based interface powered by Flask for easy interaction.
- Allows users to submit Amharic text via web forms for plagiarism checking.

## NLP Methods Used

This project utilizes the following NLP methods to preprocess Amharic text for plagiarism detection:

1. **Punctuation Removal**: Removes all punctuation marks to focus on the words in the text, ensuring that only meaningful content is compared during plagiarism checks.
2. **Tokenization**: Breaks the text into individual tokens (words or phrases) to make comparison and analysis easier. This is an essential step for most NLP applications.

3. **Stopword Removal**: Eliminates common stopwords (such as "and," "the," etc.) that do not contribute significantly to the meaning of the text. Removing these helps to focus on the more substantial content during plagiarism detection.

## Installation

To use this project, follow the steps below:

1. Clone the repository:

   ```bash
   git clone https://github.com/AbiyuNigussie/amharic_plagiarism_checker.git
   ```

2. Navigate to the project directory:

   ```bash
   cd amharic_plagiarism_checker
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Running the Flask Server

1. Start the Flask server:

   ```bash
   python app.py
   ```

2. This will start the web server, usually accessible at `http://127.0.0.1:5000/`.

3. Open the web browser and navigate to the address to interact with the plagiarism checker.

## Web Interface Usage

1. **Upload Text for Plagiarism Check**: On the homepage, you can paste your Amharic text into the upload box or upload a file containing the text.

2. **View Results**: Once submitted, the server will process the text, apply the NLP methods, and return the plagiarism score.

## Project Structure

- `app.py`: The main Flask application that serves the web interface plagiarism detection.
- `plagiarism_checker.py`: Contains the core logic for plagiarism detection, using NLP methods.
- `preprocess.py`: Contains functions for text preprocessing, including punctuation removal, tokenization, and stopword removal.
- `templates/`: Contains HTML templates for rendering the web interface.
- `static/`: Stores static files such as CSS and JavaScript for the web interface.
- `requirements.txt`: A list of dependencies for the project.
- `README.md`: Documentation for the project.

## Contributors

- [**Abiyu Nigussie**](https://github.com/AbiyuNigussie)
- [**Yonathan Girmachew**](https://github.com/yonatan1611)
- **Lealem Mekuria**
- **Mohammed Elamin**
- **Dagim Sisay**
- **Yishak Daniel**

## Contributing

We welcome contributions to improve this project. If you have suggestions or have fixed an issue, please feel free to submit a pull request!

### Steps to contribute:

1. Fork the repository
2. Create a new branch (`git checkout -b feature-name`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add new feature'`)
5. Push to the branch (`git push origin feature-name`)
6. Create a new Pull Request

## Acknowledgements

- Special thanks to all contributors and the community for support in developing this tool.

---
