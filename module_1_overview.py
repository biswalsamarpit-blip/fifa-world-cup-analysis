import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from data_generation import generate_world_cup_summary

def load_and_transform_data():
    """
    Loads the World Cup summary data and performs necessary transformations.
    """
    # 1. Data Loading
    df = generate_world_cup_summary()
    
    # 2. Cleaning & Transformation
    # Calculate average goals per match for each tournament
    df['GoalsPerMatch'] = df['GoalsScored'] / df['MatchesPlayed']
    
    # Sort by year to ensure chronological order
    df = df.sort_values(by='Year').reset_index(drop=True)
    
    return df

def visualize_overview(df):
    """
    Generates static and statistical visualizations for the World Cup overview.
    Saves the plots as image files.
    """
    sns.set_theme(style="whitegrid")
    
    # --- Figure 1: Evolution of Total Goals and Matches Played ---
    fig, ax1 = plt.subplots(figsize=(12, 6))
    
    color = 'tab:blue'
    ax1.set_xlabel('Year', fontweight='bold')
    ax1.set_ylabel('Total Goals Scored', color=color, fontweight='bold')
    ax1.plot(df['Year'], df['GoalsScored'], color=color, marker='o', label='Goals Scored')
    ax1.tick_params(axis='y', labelcolor=color)
    ax1.set_xticks(df['Year'])
    ax1.set_xticklabels(df['Year'], rotation=45)
    
    ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
    color = 'tab:red'
    ax2.set_ylabel('Matches Played', color=color, fontweight='bold')
    ax2.plot(df['Year'], df['MatchesPlayed'], color=color, marker='s', linestyle='--', label='Matches Played')
    ax2.tick_params(axis='y', labelcolor=color)
    
    plt.title('Evolution of Total Goals and Matches Played (1930 - 2022)', fontsize=14, fontweight='bold')
    fig.tight_layout()
    plt.savefig('outputs/fig1_goals_and_matches.png')
    plt.close()

    # --- Figure 2: Goal-Scoring Trends (Goals per Match) ---
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=df, x='Year', y='GoalsPerMatch', marker='o', color='purple')
    plt.title('Goals per Match Across World Cup Editions', fontsize=14, fontweight='bold')
    plt.xlabel('Year', fontweight='bold')
    plt.ylabel('Average Goals per Match', fontweight='bold')
    plt.xticks(df['Year'], rotation=45)
    
    historical_avg = df['GoalsPerMatch'].mean()
    plt.axhline(historical_avg, color='orange', linestyle='--', label=f"Historical Average: {historical_avg:.2f}")
    plt.legend()
    plt.tight_layout()
    plt.savefig('outputs/fig2_goals_per_match.png')
    plt.close()
    
    # --- Figure 3: World Cup Attendance Growth ---
    plt.figure(figsize=(12, 6))
    sns.barplot(data=df, x='Year', y='Attendance', color='teal')
    plt.title('Total Attendance per World Cup Edition', fontsize=14, fontweight='bold')
    plt.xlabel('Year', fontweight='bold')
    plt.ylabel('Total Attendance', fontweight='bold')
    plt.xticks(rotation=45)
    
    # Format y-axis to show millions for better readability
    plt.gca().yaxis.set_major_formatter(plt.matplotlib.ticker.FuncFormatter(lambda x, p: format(int(x), ',')))
    plt.tight_layout()
    plt.savefig('outputs/fig3_attendance.png')
    plt.close()
    
    print("Visualizations successfully generated and saved as PNG files.")

def generate_insights(df):
    """
    Extracts and prints key analytical insights from the data.
    """
    print("\n--- Key Analytical Insights ---")
    
    # 1. Total Goals and Matches
    max_goals_year = df.loc[df['GoalsScored'].idxmax()]
    print(f"Insight 1 (Total Goals vs. Matches): As the number of teams and matches increased "
          f"(especially the 32-team format in 1998), total goals scored have consistently risen. "
          f"The {max_goals_year['Year']} World Cup saw the highest total goals with {max_goals_year['GoalsScored']}.")
    
    # 2. Goal-Scoring Trend
    highest_gpm = df.loc[df['GoalsPerMatch'].idxmax()]
    lowest_gpm = df.loc[df['GoalsPerMatch'].idxmin()]
    print(f"Insight 2 (Goal-Scoring Trends): Despite total goals increasing, the average 'Goals per Match' "
          f"peaked early in {highest_gpm['Year']} ({highest_gpm['GoalsPerMatch']:.2f} GPM). Modern football has "
          f"seen a stabilization, often dipping below the historical average to hit a low in "
          f"{lowest_gpm['Year']} ({lowest_gpm['GoalsPerMatch']:.2f} GPM), reflecting more defensive tactical setups.")
    
    # 3. Attendance
    max_attendance = df.loc[df['Attendance'].idxmax()]
    print(f"Insight 3 (Attendance Growth): The tournament's global appeal has surged. The "
          f"{max_attendance['Year']} World Cup holds the record for total attendance with over "
          f"{max_attendance['Attendance']:,} spectators, heavily influenced by stadium capacities in the host nation ({max_attendance['HostCountry']}).")
    
if __name__ == "__main__":
    print("Executing Module 1: World Cup Overview...")
    world_cup_df = load_and_transform_data()
    visualize_overview(world_cup_df)
    generate_insights(world_cup_df)
