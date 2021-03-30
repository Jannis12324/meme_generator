# Project Overview
This project sets up a flask web application that either randomly
generates memes (An image with text and a quote author) or lets the user 
type in text and the author.
# Set up
# Running the program
# Roles & Responsibilities of submodules
The `QuoteEngine` submodule handels the ingestion and creation of quote objects.
The Ingestor class takes a file path and automatically chooses the fitting Ingestor
subclass to read the quotes and return a list of quote objects.

The `MemeEngine` loads the image, resizes if necessary, adds the quote and
saves the meme under the specified path.

# Dependencies
click==7.1.2  
Flask==1.1.2  
itsdangerous==1.1.0  
Jinja2==2.11.3  
lxml==4.6.3  
MarkupSafe==1.1.1  
numpy==1.20.1  
pandas==1.2.3  
Pillow==8.1.2  
pydocstyle==6.0.0  
python-dateutil==2.8.1  
python-docx==0.8.10  
pytz==2021.1  
six==1.15.0  
snowballstemmer==2.1.0  
Werkzeug==1.0.1  

# Examples