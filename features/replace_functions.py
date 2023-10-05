import re

def findall_update_querys(query):
    return re.findall('UPDATE [^;]*;', query)

def combine_querys(querys):
    return "\n".join(querys)

def get_username(query):
    # e.g.
    # params query: string as query paramaters
    # return username='jinken@town.kotoura.tottori.jp': string
    username = re.search("username='[^']*'", query).group()
    return username

def replace_id_to_username(query, username):
    replaced_query = re.sub("id=[0-9]*", username, query)
    return replaced_query

def replace_all_id_to_username(update_query_set):
    querys = []
    for update_query in update_query_set:
        querys.append(replace_id_to_username(update_query, get_username(update_query)))
        
    return querys

def replace_by_rules(query, rules, lgcode):
    selected_rules = rules[rules['自治体コード'] == lgcode].T
    for rule in selected_rules.itertuples():
        query = query.replace(rule[0], str(rule[1]))
        
    return query

def update_query_translator(querys, rules, lgcode):
    update_querys = findall_update_querys(querys)
    replaced_username_querys = replace_all_id_to_username(update_querys)

    combined_querys = combine_querys(replaced_username_querys)

    
    applied_replaced_rules_query = replace_by_rules(combined_querys, rules=rules, lgcode=lgcode)
    return applied_replaced_rules_query