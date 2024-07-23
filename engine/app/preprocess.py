import pandas as pd


def load_data(chunk_size=10000):
    events = pd.read_csv('data/events.csv', chunksize=chunk_size)
    item_properties1 = pd.read_csv('data/item_properties_part1.csv', chunksize=chunk_size)
    item_properties2 = pd.read_csv('data/item_properties_part2.csv', chunksize=chunk_size)

    item_properties_chunks = []
    for chunk in item_properties1:
        item_properties_chunks.append(chunk)
    for chunk in item_properties2:
        item_properties_chunks.append(chunk)

    item_properties = pd.concat(item_properties_chunks)

    return list(events), item_properties


def preprocess_data(events, item_properties):
    processed_events = []
    for chunk in events:
        if isinstance(chunk, pd.DataFrame):
            print(f"Processing chunk: {chunk.head()}")  # Debug statement
            chunk.fillna(0, inplace=True)
            processed_events.append(chunk)
        else:
            print(f"Encountered non-DataFrame chunk: {type(chunk)}")  # Debug statement
    events = pd.concat(processed_events)

    item_properties.fillna(0, inplace=True)
    return events, item_properties
