# Study Helper

Welcome to the **Study Helper**! This application is designed to assist students and researchers by providing quick access to relevant web links and downloadable PDFs related to their queries. It is built using Streamlit and Google's Custom Search JSON API.

## Features

- **Chatbot Page**: Enter your question to get related links and definitions from the web.
- **PDFs Page**: Search for specific queries and get downloadable PDF links.

## Installation

### Prerequisites

- Python 3.6 or later
- Streamlit
- Requests

### Setup

1. **Clone the repository**:
    ```sh
    git clone https://github.com/your-username/study-helper.git
    cd study-helper
    ```

2. **Install the required packages**:
    ```sh
    pip install -r requirements.txt
    ```

3. **Create a `.env` file** in the root directory and add your Google API key and Custom Search Engine ID:
    ```
    GOOGLE_API_KEY=your_api_key
    CUSTOM_SEARCH_ENGINE_ID=your_cx_id
    ```

## Usage

1. **Run the Streamlit app**:
    ```sh
    streamlit run study_chatbot.py
    ```

2. **Open your web browser**:
    Go to `http://localhost:8501` to access the Study Helper app.

## Project Structure

- `study_chatbot.py`: Main application script.

- `.env`: Environment variables file containing API keys (not included in the repository).



## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes. For major changes, please open an issue first to discuss what you would like to change.

1. **Fork the repository**.
2. **Create a new branch** (`git checkout -b feature-branch`).
3. **Commit your changes** (`git commit -am 'Add new feature'`).
4. **Push to the branch** (`git push origin feature-branch`).
5. **Create a new Pull Request**.

## License

This project is licensed under the MIT License.

## Acknowledgments

- [Streamlit](https://www.streamlit.io/)
- [Google Custom Search JSON API](https://developers.google.com/custom-search/v1/overview)

