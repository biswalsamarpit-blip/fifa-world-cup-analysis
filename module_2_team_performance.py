import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from data_generation import generate_world_cup_summary, generate_historical_finals

def load_and_transform_data():
    """
    Loads and processes data to calculate titles won and final appearances by team.
    """
    summary_df = generate_world_cup_summary()
    
    # 1. Calculate Titles Won
    titles_won = summary_df['Winner'].value_counts().reset_index()
    titles_won.columns = ['Team', 'TitlesWon']
    
    # 2. Calculate Final Appearances
    # A team appears in the final if they are the Winner or the RunnersUp
    finalists = pd.concat([summary_df['Winner'], summary_df['RunnersUp']])
    final_appearances = finalists.value_counts().reset_index()
    final_appearances.columns = ['Team', 'FinalAppearances']
    
    # 3. Merge Data
    performance_df = pd.merge(final_appearances, titles_won, on='Team', how='left')
    performance_df['TitlesWon'] = performance_df['TitlesWon'].fillna(0).astype(int)
    
    # Calculate runner-up finishes
    performance_df['RunnerUpFinishes'] = performance_df['FinalAppearances'] - performance_df['TitlesWon']
    
    # Sort primarily by Titles Won, then by Final Appearances
    performance_df = performance_df.sort_values(by=['TitlesWon', 'FinalAppearances'], ascending=[False, False]).reset_index(drop=True)
    
    return performance_df

def visualize_team_performance(df):
    """
    Generates visualizations for team performance, including titles and final appearances.
    """
    sns.set_theme(style="whitegrid")
    
    # Filter to teams that have reached at least one final for cleaner charts
    top_teams = df[df['FinalAppearances'] > 0]
    
    # --- Figure 1: Titles Won by Nation ---
    plt.figure(figsize=(10, 6))
    sns.barplot(data=top_teams[top_teams['TitlesWon'] > 0], x='Team', y='TitlesWon', hue='Team', legend=False, palette='viridis')
    plt.title('FIFA World Cup Titles Won by Nation', fontsize=14, fontweight='bold')
    plt.xlabel('Nation', fontweight='bold')
    plt.ylabel('Titles Won', fontweight='bold')
    plt.xticks(rotation=45)
    plt.yticks(range(0, top_teams['TitlesWon'].max() + 2))
    plt.tight_layout()
    plt.savefig('outputs/fig4_titles_won.png')
    plt.close()

    # --- Figure 2: Final Appearances vs Titles Won ---
    plt.figure(figsize=(12, 6))
    
    # Melt the dataframe for Seaborn grouped barplot
    melted_df = pd.melt(top_teams, id_vars=['Team'], value_vars=['TitlesWon', 'RunnerUpFinishes'], 
                        var_name='Result', value_name='Count')
    
    # Rename values for better legend
    melted_df['Result'] = melted_df['Result'].replace({'TitlesWon': 'Champion', 'RunnerUpFinishes': 'Runner-Up'})
    
    sns.barplot(data=melted_df, x='Team', y='Count', hue='Result', palette=['gold', 'silver'])
    plt.title('World Cup Final Performances: Champions vs Runner-Ups', fontsize=14, fontweight='bold')
    plt.xlabel('Nation', fontweight='bold')
    plt.ylabel('Number of Finals', fontweight='bold')
    plt.xticks(rotation=45)
    plt.legend(title='Final Result')
    plt.tight_layout()
    plt.savefig('outputs/fig5_finals_performances.png')
    plt.close()
    
    print("Module 2 visualizations generated and saved as PNG files.")

def generate_insights(df):
    """
    Extracts and prints key insights regarding team dominance.
    """
    print("\n--- Key Analytical Insights: Team Performance ---")
    
    # Top winner
    top_winner = df.iloc[0]
    print(f"Insight 1 (Most Successful Nation): {top_winner['Team']} is the most successful nation in World Cup history, "
          f"winning {top_winner['TitlesWon']} titles out of {top_winner['FinalAppearances']} final appearances.")
    
    # Most finals without a win
    no_titles = df[df['TitlesWon'] == 0]
    if not no_titles.empty:
        heartbreak_team = no_titles.iloc[0]
        print(f"Insight 2 (Most Final Appearances Without a Title): {heartbreak_team['Team']} has reached the final "
              f"{heartbreak_team['FinalAppearances']} times but has yet to win the tournament, earning them the most runner-up finishes without a trophy.")
    
    # Conversion rate
    df['ConversionRate'] = (df['TitlesWon'] / df['FinalAppearances']) * 100
    perfect_conversion = df[(df['ConversionRate'] == 100) & (df['FinalAppearances'] > 1)]
    if not perfect_conversion.empty:
        teams_perfect = ", ".join(perfect_conversion['Team'].tolist())
        print(f"Insight 3 (Perfect Finals Conversion): The following teams have won every final they have appeared in (with >1 appearance): {teams_perfect}.")
    else:
        one_appearance_perfect = df[(df['ConversionRate'] == 100) & (df['FinalAppearances'] == 1)]
        if not one_appearance_perfect.empty:
             teams_perfect = ", ".join(one_appearance_perfect['Team'].tolist())
             print(f"Insight 3 (Perfect Finals Conversion): The following teams boast a 100% win rate in finals, having won the only final they appeared in: {teams_perfect}.")


if __name__ == "__main__":
    print("Executing Module 2: Team Performance & Championship Analysis...")
    performance_df = load_and_transform_data()
    visualize_team_performance(performance_df)
    generate_insights(performance_df)
