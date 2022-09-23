def transform(legacy_data):
    return {letter.lower(): key for key, value in legacy_data.items() for letter in value}
