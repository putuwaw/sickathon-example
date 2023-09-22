# sickathon-example

![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![LICENSE](https://img.shields.io/github/license/putuwaw/sickathon-example?style=for-the-badge)
![BUILD](https://img.shields.io/github/actions/workflow/status/putuwaw/sickathon-example/streamlit.yml?style=for-the-badge)

## Features 🚀

This app provides a simple example of how to use Streamlit `st.experimental_connection` to connect to a data source like Google Sheets and SQL database.

## Prerequisites 📋

- Python 3.10 or higher
- Git and GitHub

## Installation 🛠

- Clone the repository:

```bash
git clone https://github.com/putuwaw/sickathon-example.git
```

- Create and activate virtual environment:

```bash
python -m venv venv
source venv/bin/activate
```

- Install the packages:

```bash
pip install -r requirements.txt
```

- Set up secret for experimental connection:

```bash
cp .streamlit/secret.example.toml .streamlit/secrets.toml
```

- Run the application:

```bash
streamlit run app.py
```

## License 📝

This project is licensed under the Apache-2.0 License. See the [LICENSE](LICENSE) file for details.
