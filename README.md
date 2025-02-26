# Youtube Comments Summarization using LLM model (T5)

This project utilizes a fine-tuned T5 model for text generation and processing. It includes Flask-based API endpoints and utility scripts for preprocessing and model loading.

## Project Structure

```
├── comment_summarization/       # Main project folder
│   ├── static/                 # Static files (CSS, JS, Images)
│   │   ├── styles.css          # Stylesheet
│   ├── templates/              # HTML templates
│   │   ├── index.html          # Main UI page
│   ├── utils/                  # Utility scripts
│   │   ├── __init__.py         # Init file for utils module
│   │   ├── api_call.py         # API request handling
│   │   ├── gpu_check.py        # GPU availability check
│   │   ├── model_load.py       # Model loading script
│   │   ├── preprocessing.py    # Data preprocessing utilities
│   ├── .env                    # Environment variables
│   ├── app.py                  # Flask application
│   ├── Pipfile                 # Dependencies (Pipenv)
│   ├── Pipfile.lock            # Locked dependencies
│   ├── requirements.txt        # Python package dependencies
```

## Installation & Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/fine_tuned_t5_review.git
   cd fine_tuned_t5_review
   ```

2. **Create a Virtual Environment** (Optional but recommended)
   ```bash
   pip install pipenv
   pipenv install
   ```

3. **Install Dependencies**
   Using `pip`:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**
   Create a `.env` file in the root directory and add any required environment variables.

5. **Run the Flask Application**
   ```bash
   python app.py
   ```
   The app should now be running at `http://127.0.0.1:5000/`.

## Usage
- Open the `index.html` file in your browser.
- Use the Flask API for text generation and processing.
- Modify `utils/` scripts to adapt the project as needed.

## Contributing
Feel free to fork this repository, submit issues, and make pull requests!

## License
This project is licensed under the MIT License.

