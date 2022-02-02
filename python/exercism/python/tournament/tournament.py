

def create_stats_dict() -> dict:
    stats = ["MP", "W", "L", "D", "P"]
    return {}.fromkeys(stats, 0)

def create_teams_dict(results:list) -> dict:
    teams_dict = {}
    for result in results:
        home, away, _, _ = get_team_result(result)
        if (home, away) not in teams_dict.keys():
            teams_dict[home] = create_stats_dict()
            teams_dict[away] = create_stats_dict()
    return teams_dict

def extract_features(stats:dict) -> tuple:
    mp = stats['MP']
    w = stats['W']
    l = stats['L']
    d = stats['D']
    p = stats['P']
    return mp, w, d, l, p

def update_stats(result:str, stats:dict):
    stats['MP'] += 1
    if result == 'W':
        stats['W'] += 1
    elif result == 'D':
        stats['D'] += 1
    elif result == 'L':
        stats['L'] += 1
    stats['P'] = calculate_points(stats)


def create_headings() -> str:
    return f'{"Team":<31}| {"MP":>2} | {"W":>2} | {"D":>2} | {"L":>2} | {"P":>2}'

def team_stats_print(team:str, 
                    mp:str, 
                    w:str, 
                    d:str, 
                    l:str, 
                    p:str) -> str:
    return f'{team:<31}| {mp:>2} | {w:>2} | {d:>2} | {l:>2} | {p:>2}' 

def result_to_abbr(result:str) -> tuple:
    if result == 'win':
        return 'W', 'L'
    elif result == 'loss':
        return 'L', 'W'
    elif result == 'draw':
        return 'D', 'D'
    else:
        raise ValueError('Invalid result.')

def get_team_result(match:str) -> tuple:
    home, away, home_res = match.split(';')
    home_res, away_res = result_to_abbr(home_res)
    return home, away, home_res, away_res

def calculate_points(stats:dict) -> int:
    return stats['W'] * 3 + stats['D']


def tally(rows):
    teams_dic = create_teams_dict(rows)

    for row in rows:
        home, away, home_res, away_res = get_team_result(row)
        update_stats(home_res, teams_dic[home])
        update_stats(away_res, teams_dic[away])

    by_points_and_team = lambda x: (-x[1]['P'], x[0])

    sorted_dict = sorted(teams_dic.items(), key=by_points_and_team)

    table = [create_headings()]
    for team, stats in sorted_dict:
        mp, w, d, l, p = extract_features(stats)
        table.append(team_stats_print(team, mp, w, d, l, p))
    
    return table


if __name__ == '__main__':
    results = [
            "Courageous Californians;Devastating Donkeys;win",
            "Allegoric Alaskans;Blithering Badgers;win",
            "Devastating Donkeys;Allegoric Alaskans;loss",
            "Courageous Californians;Blithering Badgers;win",
            "Blithering Badgers;Devastating Donkeys;draw",
            "Allegoric Alaskans;Courageous Californians;draw",
        ]
    
    test_table = [
            "Team                           | MP |  W |  D |  L |  P",
            "Allegoric Alaskans             |  3 |  2 |  1 |  0 |  7",
            "Courageous Californians        |  3 |  2 |  1 |  0 |  7",
            "Blithering Badgers             |  3 |  0 |  1 |  2 |  1",
            "Devastating Donkeys            |  3 |  0 |  1 |  2 |  1",
        ]
    teams_dic = create_teams_dict(results)

    for result in results:
        home, away, home_res, away_res = get_team_result(result)
        update_stats(home_res, teams_dic[home])
        update_stats(away_res, teams_dic[away])

    by_points_and_team = lambda x: (-x[1]['P'], x[0])

    sorted_dict = sorted(teams_dic.items(), key=by_points_and_team)

    table = [create_headings()]
    for team, stats in sorted_dict:
        mp, w, d, l, p = extract_features(stats)
        table.append(team_stats_print(team, mp, w, d, l, p))

    print(all([True for l, l1 in zip(table, test_table) if l == l1]))

    print(test_table)
    print(table)

