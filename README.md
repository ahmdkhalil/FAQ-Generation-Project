# FAQ Generation Project

A web-based tool designed to streamline the FAQ creation process by using Natural Language Processing (NLP) and clustering techniques. This project helps organizations automate the generation of FAQs from large datasets, making it easier to address common inquiries.

## Table of Contents
* [About](https://github.com/ahmdkhalil/FAQ-Generation-Project?tab=readme-ov-file#about)
* [Features](https://github.com/ahmdkhalil/FAQ-Generation-Project?tab=readme-ov-file#features)
* [Project Structure](https://github.com/ahmdkhalil/FAQ-Generation-Project?tab=readme-ov-file#porject-strucutre)
* [Setup](https://github.com/ahmdkhalil/FAQ-Generation-Project?tab=readme-ov-file#setup)
* [Usage](https://github.com/ahmdkhalil/FAQ-Generation-Project?tab=readme-ov-filed#usage)
* [Technologies](https://github.com/ahmdkhalil/FAQ-Generation-Project?tab=readme-ov-file#technologies)

## About
The FAQ Generation Project uses clustering algorithms to identify common questions from input data, creating concise, relevant FAQs that organizations can use across platforms. This tool aims to improve customer support efficiency and reduce manual effort in FAQ management.

## Features
* Clustering-based FAQ Generation: Identifies patterns and generates FAQs based on common questions and keywords.
* Real-time Data Update: Supports monthly data updates to refine FAQ suggestions continuously.
* User Feedback Mechanism: Allows evaluators to provide feedback on generated FAQs for continuous improvement. (future updates)
* Web Application: Built with Flask for ease of deployment and interaction.

## Project Structure
```
├── app/                    # Flask app files
│   ├── templates/          # HTML templates
│   └── static/             # Static assets such as CSS, JS, images
├── data/                   # Sample datasets for FAQ generation (removed)
├── models/                 # Pre-trained clustering and NLP models
├── scripts/                # Scripts for data processing and model training
├── tests/                  # Unit tests for various project components
└── README.md               # Project documentation
```

## Setup
1. Clone the repository
```
git clone https://github.com/ahmdkhalil/FAQ-Generation-Project.git
cd faq-generation
```

2. Set up a virtual environment
```
python3 -m venv env
source env/bin/activate
```

3. Install dependencies
```
pip install -r requirements.txt
```

4. Run the app
```
python app.py
```

## Usage
1. **Upload Dataset**: Upload your dataset containing customer inquiries or Q&A logs.
2. **Generate FAQs**: Use the interface to process the data and generate FAQs.
3. **Review and Refine**: View the generated FAQs and adjust clustering settings if needed.
4. **Provide Feedback**: Reviewers can provide feedback on FAQ accuracy to improve model performance. (future improvements)

## Technologies
* Python: Programming language
* Flask / Streamlit: Web framework for deployment
* Scikit-Learn: Clustering algorithms
* NLTK / SpaCy: NLP libraries for preprocessing and text analysis

