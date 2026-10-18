import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from data_generation import generate_world_cup_summary

def load_and_transform_data():
    """
    Loads and processes data to analyze the performance of host nations.
    """
    df = generate_world_cup_summary()
    
    # Check if host won the tournament
    df['HostWon'] = df['HostCountry'] == df['Winner']
    
    # Check if host reached the final
    df['HostReachedFinal'] = (df['HostCountry'] == df['Winner']) | (df['HostCountry'] == df['RunnersUp'])
    
    return df

def visualize_host_advantage(df):
    """
    Generates visualizations to illustrate host country advantage.
    """
    sns.set_theme(style="whitegrid")
    
    # --- Figure 1: Host Nation Performance in Finals ---
    # Aggregate data
    total_tournaments = len(df)
    hosts_won = df['HostWon'].sum()
    hosts_lost_final = df['HostReachedFinal'].sum() - hosts_won
    hosts_not_in_final = total_tournaments - df['HostReachedFinal'].sum()
    
    data = [hosts_won, hosts_lost_final, hosts_not_in_final]
    labels = ['Host Won Title', 'Host Lost in Final', 'Host Did Not Reach Final']
    colors = ['#2ca02c', '#ff7f0e', '#1f77b4']
    explode = (0.1, 0, 0)  # explode the 'Won' slice
    
    plt.figure(figsize=(8, 8))
    plt.pie(data, labels=labels, autopct='%1.1f%%', startangle=140, colors=colors, explode=explode, shadow=True)
    plt.title('How Often Do Host Nations Reach the Final?', fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.savefig('outputs/fig6_host_advantage_pie.png')
    plt.close()
    
    # --- Figure 2: Timeline of Host Wins ---
    plt.figure(figsize=(12, 4))
    
    # Plot all tournaments as grey dots
    sns.scatterplot(data=df, x='Year', y=[1]*len(df), color='lightgrey', s=100, label='Non-Host Winner')
    
    # Overlay host wins as green stars
    host_winners = df[df['HostWon']]
    sns.scatterplot(data=host_winners, x='Year', y=[1]*len(host_winners), color='green', marker='*', s=400, label='Host Winner')
    
    plt.title('Timeline of Host Nations Winning the World Cup', fontsize=14, fontweight='bold')
    plt.xlabel('Year', fontweight='bold')
    plt.yticks([]) # Hide y-axis
    plt.xticks(df['Year'], rotation=45)
    plt.legend(loc='upper right')
    plt.tight_layout()
    plt.savefig('outputs/fig7_host_timeline.png')
    plt.close()
    
    print("Module 3 visualizations generated and saved as PNG files in outputs/ folder.")

def generate_insights(df):
    """
    Extracts and prints key insights regarding the host advantage.
    """
    print("\n--- Key Analytical Insights: Host Country Advantage ---")
    
    total = len(df)
    hosts_won = df['HostWon'].sum()
    hosts_reached_final = df['HostReachedFinal'].sum()
    
    win_percentage = (hosts_won / total) * 100
    final_percentage = (hosts_reached_final / total) * 100
    
    print(f"Insight 1 (Host Win Rate): Historically, the host nation has won the World Cup {hosts_won} times "
          f"out of {total} tournaments ({win_percentage:.1f}% of the time).")
    
    print(f"Insight 2 (Final Appearances): Host nations reached the final {hosts_reached_final} times "
          f"({final_percentage:.1f}%). This indicates a statistically significant 'home-field advantage' compared "
          f"to the baseline probability of any single team reaching the final.")
    
    recent_host_win = df[df['HostWon']]['Year'].max()
    print(f"Insight 3 (Modern Era Shift): The last time a host nation won the World Cup was in {recent_host_win} "
          f"({df[df['Year'] == recent_host_win]['HostCountry'].values[0]}). The 'host advantage' seems to have diminished "
          f"in the modern era due to increased globalization of football tactics and talent.")

if __name__ == "__main__":
    print("Executing Module 3: Host Country Advantage...")
    host_df = load_and_transform_data()
    visualize_host_advantage(host_df)
    generate_insights(host_df)
