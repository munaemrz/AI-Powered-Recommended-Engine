import pandas as pd
from scipy.sparse import csr_matrix
from implicit.als import AlternatingLeastSquares
from sklearn.metrics.pairwise import cosine_similarity
from threadpoolctl import threadpool_limits


class RecommendationModel:
    def __init__(self):
        self.als_model = None
        self.item_similarity = None
        self.user_item_matrix = None

    def train(self, events, item_properties):
        with threadpool_limits(limits=1, user_api='blas'):
            # Process data in chunks
            user_item_data = []
            for chunk in events:
                if isinstance(chunk, pd.DataFrame):
                    print(f"Chunk before processing: {chunk.head()}")  # Debug statement
                    chunk['event'] = 1  # Assuming all events are binary (interaction or no interaction)
                    user_item_data.append(chunk)
                else:
                    print("Encountered non-DataFrame chunk:", type(chunk))  # Debug statement

            if not user_item_data:
                print("No valid DataFrame chunks to concatenate.")
                return

            user_item_df = pd.concat(user_item_data)
            user_item_matrix = csr_matrix((user_item_df['event'], (user_item_df['visitorid'], user_item_df['itemid'])))

            # Train ALS model
            self.als_model = AlternatingLeastSquares(factors=50)
            self.als_model.fit(user_item_matrix)

            # Handle duplicates in item_properties before pivoting
            item_properties = item_properties.groupby(['itemid', 'property']).first().reset_index()

            # Compute item similarity matrix
            item_features = item_properties.pivot(index='itemid', columns='property', values='value')

            # Convert all values to numeric, coercing errors to NaN
            item_features = item_features.apply(pd.to_numeric, errors='coerce')

            # Fill NaN values with 0
            item_features = item_features.fillna(0)

            # Ensure item_features is a sparse matrix
            item_features_sparse = csr_matrix(item_features.values)

            self.item_similarity = cosine_similarity(item_features_sparse)
            self.user_item_matrix = user_item_matrix

    def recommend(self, user_id, num_recommendations=10):
        user_recommendations = self.als_model.recommend(user_id, self.user_item_matrix[user_id])
        similar_items = self.item_similarity[user_recommendations]
        hybrid_recs = self.combine_recommendations(user_recommendations, similar_items)
        return hybrid_recs[:num_recommendations]

    def combine_recommendations(self, user_recommendations, similar_items):
        # Combine and rank recommendations (example logic)
        return user_recommendations
