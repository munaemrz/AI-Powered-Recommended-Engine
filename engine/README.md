# E-commerce Recommendation System

## Overview
This repository contains an AI-powered recommendation engine for an e-commerce platform. The engine provides personalized product recommendations to users based on their browsing and purchase history.

# download data from below url
https://www.kaggle.com/datasets/retailrocket/ecommerce-dataset?select=events.csv
https://www.kaggle.com/datasets/retailrocket/ecommerce-dataset?select=item_properties_part1.csv
https://www.kaggle.com/datasets/retailrocket/ecommerce-dataset?select=item_properties_part2.csv
and add in data folder under engine

## File Structure
- `data/`: Contains user, product, and transaction data.
- `models/`: Contains different recommendation models.
- `notebooks/`: Contains data preprocessing notebook.
- `main.py`: Flask application to serve the recommendation engine.
- `requirements.txt`: Required Python packages.
- `README.md`: Instructions on how to run the project.

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/munaemrz/AI-Powered-Recommended-Engine
   cd engine
   
2. **To run the app**
   python run.py

3. **Access the Recommendation Endpoint** 

   Open your web browser and navigate to:
   http://127.0.0.1:5001/recommend?user_id=<user_id>

4. **To retrain the model with new data**
   you can run the retrain.py script:
   python app/retrain.py


**Additional Notes**
# Ensure that your firewall or security settings allow traffic on port 5001.
# If you encounter any issues, ensure that the virtual environment is activated and that all required packages are installed.
# Adjust the configuration files as necessary to fit your specific use case and environment.

**Contact**
# For any questions or issues, please contact **munaem.rudab@live.com**.
