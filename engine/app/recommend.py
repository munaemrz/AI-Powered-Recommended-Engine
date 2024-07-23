from flask import request, jsonify, current_app
from app import app


@app.route('/recommend', methods=['GET'])
def recommend():
    user_id = request.args.get('user_id', type=int)

    # Access the model from the app context
    model = current_app.config.get('MODEL')
    print(f"Model retrieved from app config: {model}")  # Debug statement

    # Check if the model is properly instantiated
    if model is None:
        print("Model is None")  # Debug statement
        return jsonify({'error': 'Model not initialized'}), 500

    # Get recommendations
    try:
        recommendations = model.recommend(user_id)
        print(f"Recommendations for user {user_id}: {recommendations}")  # Debug statement
        return jsonify(recommendations)
    except Exception as e:
        print(f"Error during recommendation: {e}")  # Debug statement
        return jsonify({'error': str(e)}), 500
