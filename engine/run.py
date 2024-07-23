from app import app
from app.model import RecommendationModel
from app.preprocess import load_data, preprocess_data
from threadpoolctl import threadpool_limits

if __name__ == '__main__':
    # Load and preprocess data
    events, item_properties = load_data()
    events, item_properties = preprocess_data(events, item_properties)

    # Train the model with threadpool limits
    with threadpool_limits(limits=1, user_api='blas'):
        model = RecommendationModel()
        model.train(events, item_properties)
        print("Model trained successfully")  # Debug statement

    # Attach the model to the app
    app.config['MODEL'] = model
    print("Model attached to app config")  # Debug statement

    # Run the app on a different port
    app.run(debug=True, host='0.0.0.0', port=5001)  # Change the port if 5000 is in use
