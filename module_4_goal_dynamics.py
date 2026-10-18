import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from data_generation import generate_synthetic_matches

def load_and_transform_data():
    """
    Loads and processes match-level data to analyze goal dynamics.
    """
    df = generate_synthetic_matches()
    
    # Calculate Score Differential (Home Goals - Away Goals)
    df['GoalDifferential'] = df['HomeGoals'] - df['AwayGoals']
    
    # Determine the Match Outcome
    def determine_outcome(row):
        if row['GoalDifferential'] > 0:
            return 'Home Win'
        elif row['GoalDifferential'] < 0:
            return 'Away Win'
        else:
            return 'Draw'
            
    df['Outcome'] = df.apply(determine_outcome, axis=1)
    
    return df

def visualize_goal_dynamics(df):
    """
    Generates visualizations for match-level goal distributions and stages.
    """
    sns.set_theme(style="whitegrid")
    
    # --- Figure 1: Home vs Away Goal Distributions ---
    plt.figure(figsize=(10, 6))
    sns.kdeplot(df['HomeGoals'], fill=True, label='Home Goals', color='blue', alpha=0.5)
    sns.kdeplot(df['AwayGoals'], fill=True, label='Away Goals', color='orange', alpha=0.5)
    plt.title('Distribution of Home vs Away Goals', fontsize=14, fontweight='bold')
    plt.xlabel('Goals Scored', fontweight='bold')
    plt.ylabel('Density', fontweight='bold')
    plt.xlim(0, max(df['HomeGoals'].max(), df['AwayGoals'].max()) + 1)
    plt.legend()
    plt.tight_layout()
    plt.savefig('outputs/fig8_goal_distributions.png')
    plt.close()

    # --- Figure 2: Total Goals by Tournament Stage ---
    plt.figure(figsize=(12, 6))
    
    # Define order of stages for logical plotting
    stage_order = ['Group Stage', 'Round of 16', 'Quarter-finals', 'Semi-finals', 'Third Place', 'Final']
    
    sns.boxplot(data=df, x='Stage', y='TotalGoals', order=stage_order, palette='Set2')
    plt.title('Total Goals Scored by Tournament Stage', fontsize=14, fontweight='bold')
    plt.xlabel('Tournament Stage', fontweight='bold')
    plt.ylabel('Total Goals in Match', fontweight='bold')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('outputs/fig9_goals_by_stage.png')
    plt.close()
    
    print("Module 4 visualizations generated and saved as PNG files in outputs/ folder.")

def generate_insights(df):
    """
    Extracts and prints key insights regarding goal dynamics.
    """
    print("\n--- Key Analytical Insights: Match-Level Goal Dynamics ---")
    
    home_avg = df['HomeGoals'].mean()
    away_avg = df['AwayGoals'].mean()
    
    print(f"Insight 1 (Home vs Away Scoring): The designated 'Home' team scores an average of {home_avg:.2f} goals "
          f"per match, compared to {away_avg:.2f} for the 'Away' team. This slight bias in the synthetic data mirrors "
          f"the nominal home advantage often observed in football scheduling.")
    
    # Calculate standard deviation or variance across stages
    group_goals = df[df['Stage'] == 'Group Stage']['TotalGoals'].mean()
    final_goals = df[df['Stage'] == 'Final']['TotalGoals'].mean()
    
    print(f"Insight 2 (Goals by Stage): Group stage matches average {group_goals:.2f} total goals. "
          f"In contrast, Final matches average {final_goals:.2f} goals. While our synthetic data is somewhat normalized, "
          f"in reality, knockout stages (especially finals) often see tighter, lower-scoring affairs due to the high stakes.")
    
    draw_pct = (len(df[df['Outcome'] == 'Draw']) / len(df)) * 100
    print(f"Insight 3 (Draw Probability): Across all matches, {draw_pct:.1f}% end in a draw at the end of regulation time, "
          f"highlighting the low-scoring, highly competitive nature of the sport.")

if __name__ == "__main__":
    print("Executing Module 4: Match-Level Goal Dynamics...")
    matches_df = load_and_transform_data()
    visualize_goal_dynamics(matches_df)
    generate_insights(matches_df)
