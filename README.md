
# LLM Application Using LCEL

This project demonstrates a simple application utilizing the **LangChain Expression Language (LCEL)** to perform basic arithmetic operations. It serves as an introductory example for developers interested in leveraging LCEL for building applications powered by Large Language Models (LLMs).

## Features

- Performs basic arithmetic operations: addition, subtraction, multiplication, and division.
- Utilizes LCEL for chaining prompts and model responses.
- Interactive web interface accessible via a browser.

## Prerequisites

- [Poetry](https://python-poetry.org/docs/#installation) for dependency management

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/adi9358/LLM-application-using-LCEL.git
   cd LLM-application-using-LCEL
   ```

2. **Install dependencies using Poetry:**

   ```bash
   pip install poetry
   poetry install
   ```

## Running the Application

1. **Activate the virtual environment:**

   ```bash
   poetry shell
   ```

2. **Start the application server:**

   ```bash
   python serve.py
   ```

3. **Access the application:**

   Open your web browser and navigate to [http://localhost:8000/chain/playground/](http://localhost:8000/chain/playground/) to interact with the calculator.

## Project Structure

```
├── client.py           # Client-side logic for interacting with the application
├── serve.py            # Sets up the FastAPI server and routes
├── requirements.txt    # Project dependencies
├── .env.example        # Example environment variables
├── render.yaml         # Configuration for deployment (e.g., Render.com)
├── LICENSE             # Apache 2.0 License
└── README.md           # Project documentation
```

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, feel free to open an issue or submit a pull request.

## License

This project is licensed under the Apache 2.0 License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [LangChain](https://github.com/langchain-ai/langchain) for providing the LCEL framework.
- [FastAPI](https://fastapi.tiangolo.com/) for the web framework used in this application.
