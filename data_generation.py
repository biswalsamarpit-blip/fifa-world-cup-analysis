import pandas as pd
import numpy as np
import random

def generate_world_cup_summary():
    """
    Generates a DataFrame containing summary statistics for historical FIFA World Cups.
    """
    data = {
        'Year': [1930, 1934, 1938, 1950, 1954, 1958, 1962, 1966, 1970, 1974, 
                 1978, 1982, 1986, 1990, 1994, 1998, 2002, 2006, 2010, 2014, 2018, 2022],
        'HostCountry': ['Uruguay', 'Italy', 'France', 'Brazil', 'Switzerland', 'Sweden', 
                        'Chile', 'England', 'Mexico', 'Germany', 'Argentina', 'Spain', 
                        'Mexico', 'Italy', 'USA', 'France', 'Korea/Japan', 'Germany', 
                        'South Africa', 'Brazil', 'Russia', 'Qatar'],
        'Winner': ['Uruguay', 'Italy', 'Italy', 'Uruguay', 'West Germany', 'Brazil', 
                   'Brazil', 'England', 'Brazil', 'West Germany', 'Argentina', 'Italy', 
                   'Argentina', 'West Germany', 'Brazil', 'France', 'Brazil', 'Italy', 
                   'Spain', 'Germany', 'France', 'Argentina'],
        'RunnersUp': ['Argentina', 'Czechoslovakia', 'Hungary', 'Brazil', 'Hungary', 'Sweden', 
                      'Czechoslovakia', 'West Germany', 'Italy', 'Netherlands', 'Netherlands', 'West Germany', 
                      'West Germany', 'Argentina', 'Italy', 'Brazil', 'Germany', 'France', 
                      'Netherlands', 'Argentina', 'Croatia', 'France'],
        'GoalsScored': [70, 70, 84, 88, 140, 126, 89, 89, 95, 97, 102, 146, 132, 115, 141, 171, 161, 147, 145, 171, 169, 172],
        'QualifiedTeams': [13, 16, 15, 13, 16, 16, 16, 16, 16, 16, 16, 24, 24, 24, 24, 32, 32, 32, 32, 32, 32, 32],
        'MatchesPlayed': [18, 17, 18, 22, 26, 35, 32, 32, 32, 38, 38, 52, 52, 52, 52, 64, 64, 64, 64, 64, 64, 64],
        'Attendance': [590549, 363000, 375700, 1045246, 768607, 819810, 893172, 1563135, 1603975, 1865753, 
                       1545791, 2109723, 2394031, 2516215, 3587538, 2785100, 2705197, 3359439, 3178856, 3429873, 3031768, 3404252]
    }
    return pd.DataFrame(data)

def generate_historical_finals():
    """
    Generates a DataFrame containing match details of historical World Cup finals.
    """
    data = {
        'Year': [1930, 1934, 1938, 1950, 1954, 1958, 1962, 1966, 1970, 1974, 
                 1978, 1982, 1986, 1990, 1994, 1998, 2002, 2006, 2010, 2014, 2018, 2022],
        'HomeTeam': ['Uruguay', 'Italy', 'Italy', 'Uruguay', 'West Germany', 'Brazil', 
                     'Brazil', 'England', 'Brazil', 'Netherlands', 'Argentina', 'Italy', 
                     'Argentina', 'West Germany', 'Brazil', 'Brazil', 'Germany', 'Italy', 
                     'Netherlands', 'Germany', 'France', 'Argentina'],
        'AwayTeam': ['Argentina', 'Czechoslovakia', 'Hungary', 'Brazil', 'Hungary', 'Sweden', 
                     'Czechoslovakia', 'West Germany', 'Italy', 'West Germany', 'Netherlands', 'West Germany', 
                     'West Germany', 'Argentina', 'Italy', 'France', 'Brazil', 'France', 
                     'Spain', 'Argentina', 'Croatia', 'France'],
        'HomeGoals': [4, 2, 4, 2, 3, 5, 3, 4, 4, 1, 3, 3, 3, 1, 0, 0, 0, 1, 0, 1, 4, 3],
        'AwayGoals': [2, 1, 2, 1, 2, 2, 1, 2, 1, 2, 1, 1, 2, 0, 0, 3, 2, 1, 1, 0, 2, 3],
        'WinCondition': ['Normal', 'Extra Time', 'Normal', 'Normal', 'Normal', 'Normal', 
                         'Normal', 'Extra Time', 'Normal', 'Normal', 'Extra Time', 'Normal', 
                         'Normal', 'Normal', 'Penalties', 'Normal', 'Normal', 'Penalties', 
                         'Extra Time', 'Extra Time', 'Normal', 'Penalties']
    }
    return pd.DataFrame(data)

def generate_synthetic_matches(num_matches=1000, seed=42):
    """
    Generates synthetic match-level data to simulate historical scores and stages.
    """
    np.random.seed(seed)
    random.seed(seed)
    
    years = [1930, 1934, 1938, 1950, 1954, 1958, 1962, 1966, 1970, 1974, 
             1978, 1982, 1986, 1990, 1994, 1998, 2002, 2006, 2010, 2014, 2018, 2022]
    stages = ['Group Stage', 'Round of 16', 'Quarter-finals', 'Semi-finals', 'Third Place', 'Final']
    teams = ['Brazil', 'Germany', 'Italy', 'Argentina', 'France', 'Uruguay', 'England', 
             'Spain', 'Netherlands', 'Portugal', 'Belgium', 'Croatia', 'Mexico', 'USA']
    
    data = []
    for _ in range(num_matches):
        year = random.choice(years)
        stage = random.choice(stages)
        match_teams = random.sample(teams, 2)
        home_team = match_teams[0]
        away_team = match_teams[1]
        
        # Poisson distribution for goals
        home_goals = np.random.poisson(1.5)
        away_goals = np.random.poisson(1.1)
        
        data.append({
            'Year': year,
            'Stage': stage,
            'HomeTeam': home_team,
            'AwayTeam': away_team,
            'HomeGoals': home_goals,
            'AwayGoals': away_goals,
            'TotalGoals': home_goals + away_goals
        })
        
    return pd.DataFrame(data)

if __name__ == "__main__":
    print("Generating World Cup Summary Data...")
    df_summary = generate_world_cup_summary()
    print(df_summary.head())
    print("-" * 50)
    
    print("Generating Historical Finals Data...")
    df_finals = generate_historical_finals()
    print(df_finals.head())
    print("-" * 50)
    
    print("Generating Synthetic Match Data...")
    df_matches = generate_synthetic_matches()
    print(df_matches.head())
    print(f"Total synthetic matches generated: {len(df_matches)}")
    print("-" * 50)
    
    print("Data generation and validation complete. Ready for Module 1.")
