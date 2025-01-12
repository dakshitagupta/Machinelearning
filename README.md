# Hindi Fake News Detection System

## Project Overview
The **Hindi Fake News Detection System** is designed to identify and prevent the spread of fake news in the Hindi language. This system leverages advanced **Natural Language Processing (NLP)** techniques and **Machine Learning (ML)** models to classify news as genuine or fake. It aims to enhance the integrity of online information by providing a reliable tool for fake news detection.

## Features
- **Multilingual Support**: Focuses on fake news detection in Hindi, addressing a critical gap in non-English language tools.
- **Machine Learning Algorithms**: Utilizes both the Naive Bayes algorithm and the LSTM (Long Short-Term Memory) model for accurate classification.
- **Streamlit User Interface**: Provides a user-friendly web interface for interaction.
- **Data Preprocessing**: Includes tokenization, stopword removal, and stemming tailored for the Hindi language.

## Technologies Used
- **Programming Language**: Python
- **Libraries and Frameworks**:
  - **NLP**: NLTK, SpaCy
  - **Machine Learning**: Scikit-learn, TensorFlow
  - **Data Analysis**: Pandas, NumPy
  - **Visualization**: Matplotlib, Seaborn
  - **Web Framework**: Streamlit

## Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/hindi-fake-news-detection.git
   cd hindi-fake-news-detection
   ```
2. **Set Up a Virtual Environment**:
   ```bash
   python -m venv env
   source env/bin/activate   # On Windows: env\Scripts\activate
   ```
3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. **Run the Application**:
   ```bash
   streamlit run app.py
   ```
2. **Upload Dataset**: Provide the news dataset in Hindi for analysis.
3. **Get Results**: View the classification of news articles as real or fake along with probability scores.

## Project Workflow
1. **Data Collection**: Gather Hindi news articles from various online sources.
2. **Preprocessing**:
   - Tokenization and stopword removal.
   - Text normalization specific to Hindi language rules.
3. **Model Training**:
   - Train the Naive Bayes and LSTM models on preprocessed data.
   - Evaluate performance using metrics like accuracy and F1 score.
4. **User Interface**:
   - Allow users to input news text and receive classification results.

## Dataset
The project uses a labeled dataset of Hindi news articles for training and evaluation. Ensure the dataset is properly formatted and cleaned before use.

## Contribution
Contributions are welcome! Feel free to fork the repository and submit pull requests.
