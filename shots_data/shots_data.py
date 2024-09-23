import time
import pandas as pd
from nba_api.stats.endpoints import commonallplayers, shotchartdetail
    
def get_active_players(season_year):
    """
    Fetch active players' IDs for the specified season.
    """
    all_players = commonallplayers.CommonAllPlayers(is_only_current_season=0)
    players_df = all_players.get_data_frames()[0]
    
    # Convert 'FROM_YEAR' and 'TO_YEAR' columns to numeric for filtering
    players_df['FROM_YEAR'] = pd.to_numeric(players_df['FROM_YEAR'], errors='coerce')
    players_df['TO_YEAR'] = pd.to_numeric(players_df['TO_YEAR'], errors='coerce')

    # Filter to get players who were active during the specified season (2023-2024)
    active_players_df = players_df[(players_df['FROM_YEAR'] <= season_year) & (players_df['TO_YEAR'] >= season_year)]
    
    return active_players_df[['PERSON_ID', 'DISPLAY_FIRST_LAST']]

def get_player_shotchart(player_id, season):
    """
    Fetch shot chart data for a specific player in the specified season.
    """
    shot_chart = shotchartdetail.ShotChartDetail(
        team_id=0,
        player_id=player_id,
        season_type_all_star='Regular Season',
        season_nullable=season,
        context_measure_simple='FGA'
    )
    # Get the shot chart data
    shot_data = shot_chart.get_data_frames()[0]
    return shot_data

def fetch_shot_data_for_2023_2024():
    """
    Fetch shot chart data for all active players in the 2023-2024 season.
    """
    season_year = 2023  # For the 2023-2024 season
    season_str = f'{season_year}-{str(season_year + 1)[-2:]}'
    print(f'Fetching data for the {season_str} season...')

    all_shot_data = pd.DataFrame()

    # Get active players for the 2023-2024 season
    players_df = get_active_players(season_year)

    # Loop through active players in that season
    for index, row in players_df.iterrows():
        player_id = row['PERSON_ID']
        player_name = row['DISPLAY_FIRST_LAST']
        print(f'Fetching shots for {player_name} in the {season_str} season...')

        try:
            shot_data = get_player_shotchart(player_id, season_str)
            if not shot_data.empty:
                shot_data['PLAYER_ID'] = player_id
                shot_data['PLAYER_NAME'] = player_name
                shot_data['SEASON'] = season_str
                all_shot_data = pd.concat([all_shot_data, shot_data], ignore_index=True)
        except Exception as e:
            print(f'Error fetching data for {player_name} in season {season_str}: {e}')

        # Avoid hitting API rate limits
        time.sleep(1)

    return all_shot_data

# Fetch shot chart data for the 2023-24 season
shot_data_2023_24 = fetch_shot_data_for_2023_2024()

# Save to a CSV or Excel file
shot_data_2023_24.to_csv('nba_shot_data_2023_2024.csv', index=False)
