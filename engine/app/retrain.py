import schedule
import time

from app.model import RecommendationModel
from app.preprocess import load_data, preprocess_data


def retrain_model():
    # Load and preprocess data
    events, item_properties = load_data()
    events, item_properties = preprocess_data(events, item_properties)

    # Retrain model
    model = RecommendationModel()
    model.train(events, item_properties)


# Schedule retraining
schedule.every().day.at("00:00").do(retrain_model)

while True:
    schedule.run_pending()
    time.sleep(1)
