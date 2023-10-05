def read_query(filename='PREVIOUS_mapinfos.groovy'):
    with open(filename, 'r', encoding='utf-8') as f:
        query = f.read()
    
    return query

def save_query(query, filename='TRANSLATED_mapinfo.groovy'):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(query)