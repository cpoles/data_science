def transform(legacy_data):
    dics = [{}.fromkeys(v, k) for k, v in legacy_data.items()]
    data = {}
    for dic in dics:
        data.update(dic)

    data = dict(sorted(data.items()))
    return {k.lower(): v for k, v in data.items()}
