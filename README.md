Youtube Comments Summarization using LLM model (T5)
This project utilizes a fine-tuned T5 model for text generation and processing. It includes Flask-based API endpoints and utility scripts for preprocessing and model loading.

Project Structure
├── fine_tuned_t5_review/       # Main project folder
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


Installation & Setup
Clone the Repository
git clone https://github.com/Codin-glitch/fine_tuned_t5_review.git
cd fine_tuned_t5_review

Create a Virtual Environment
pip install pipenv
pipenv install

Install Dependencies
Using pip:
pip install -r requirements.txt

Set Up Environment Variables
Create a .env file in the root directory and add any required environment variables.
Run the Flask Application
python app.py

The app should now be running at http://127.0.0.1:5000/.

Contributing
Feel free to fork this repository, submit issues, and make pull requests!

License
This project is licensed under the MIT License.
