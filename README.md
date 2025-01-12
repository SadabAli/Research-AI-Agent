# Research Agentic AI

This project is a powerful AI-powered research assistant built using the Phi framework. It uses advanced tools like DuckDuckGo and Newspaper4k to fetch and analyze data from the web, generating high-quality research articles.

## Features

- **Advanced AI Model**: Powered by the Gemini model (`gemini-2.0-flash-exp`) for robust natural language understanding.
- **Web Search and Analysis**: Integrates DuckDuckGo for web searches and Newspaper4k for article scraping and analysis.
- **Markdown Output**: Provides research articles in Markdown format, ready for use in publications.
- **Error Handling**: Includes robust error handling for a seamless user experience.
- **Customizable Agents**: Fully customizable agent with detailed instructions for specific tasks.

## Requirements

To run this project, ensure you have the following installed:

- Python 3.8+
- [Phi Framework](https://github.com/phi-ai)
- Flask
- `dotenv`
- Required Python libraries (see `requirements.txt`)

## Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/SadabAli/Research-AI-Agent.git
    cd research-agentic-ai
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up your environment variables:
    - Create a `.env` file in the root directory:
      ```
      PHI_API_KEY=your_phi_api_key
      GOOGLE_API_KEY=your_google_api_key
      ```
    - Replace `your_phi_api_key` and `your_google_api_key` with valid API keys.

## Usage

1. Start the application:
    ```bash
    python Reaserch_AI_Agent.py
    ```

2. Access the application in your browser at:
    ```
    http://localhost:7777
    ```

3. Enter your research query in the input box and let the agent generate an article.

## Example

To research the reasons behind the Los Angeles fire:
1. Enter the query: `What are the reasons behind the Los Angeles fire?`
2. The agent will search for relevant articles, analyze the content, and generate a detailed summary.

## UI Screenshot

Below is a screenshot of the application in action:
![Screenshot 2025-01-12 201838](https://github.com/user-attachments/assets/abee15cf-7fad-467d-8345-7ef43e594dc3)
![Uploading Screenshot 2025-01-12 201852.png…]()



## Debugging

If you encounter issues:
- Check the logs for detailed error messages.
- Ensure the environment variables are correctly set.
- Run the agent standalone for testing:
    ```python
    result = Research_Agentic_AI.run("Your query here")
    print(result)
    ```

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for suggestions or bug fixes.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- [Phi Framework](https://github.com/phi-ai) for providing the tools to build this application.
- Open-source contributors for supporting the libraries used in this project.
