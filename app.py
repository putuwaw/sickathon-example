import streamlit as st
from st_pages import Page, show_pages

st.set_page_config(
    page_title="Sickathon | Example App",
    page_icon=":balloon:",
)

show_pages(
    [
        Page("app.py", "Home", ":house:"),
        Page("pages/gsheets.py", "Google Sheets", ":memo:"),
        Page("pages/sql.py", "SQL", ":floppy_disk:"),
        Page("pages/extra.py", "Extra", ":sparkles:")
    ]
)

st.title("Sickathon Example App")

'''
### Prerequisites
Before you start, make sure you have installed [Git](https://git-scm.com/) and [Python](https://www.python.org/).

### Setup
Before starting, you need to install some packages. But first we need to create a virtual environment.
```bash
python -m venv venv
```
After that, activate the virtual environment.
```bash
source venv/bin/activate
```
Then, install the packages.
```bash 
pip install validators==0.20.0 streamlit mysqlclient matplotlib sqlalchemy git+https://github.com/streamlit/gsheets-connection st-pages
```
Now, you ready to go!

'''
