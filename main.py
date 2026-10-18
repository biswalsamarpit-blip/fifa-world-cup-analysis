from data_generation import generate_world_cup_summary, generate_historical_finals, generate_synthetic_matches
import module_1_overview
import module_2_team_performance
import module_3_host_advantage
import os

def main():
    print("=========================================")
    print("FIFA World Cup Analysis Project Execution")
    print("=========================================\n")
    
    # Ensure outputs directory exists
    if not os.path.exists('outputs'):
        os.makedirs('outputs')
        
    print("Data Validation...")
    df_summary = generate_world_cup_summary()
    df_finals = generate_historical_finals()
    df_matches = generate_synthetic_matches()
    print("Data loaded successfully.\n")
    
    print("--- Running Module 1 ---")
    df_m1 = module_1_overview.load_and_transform_data()
    module_1_overview.visualize_overview(df_m1)
    module_1_overview.generate_insights(df_m1)
    
    print("\n--- Running Module 2 ---")
    df_m2 = module_2_team_performance.load_and_transform_data()
    module_2_team_performance.visualize_team_performance(df_m2)
    module_2_team_performance.generate_insights(df_m2)
    
    print("\n--- Running Module 3 ---")
    df_m3 = module_3_host_advantage.load_and_transform_data()
    module_3_host_advantage.visualize_host_advantage(df_m3)
    module_3_host_advantage.generate_insights(df_m3)
    
    print("\n--- Running Module 4 ---")
    import module_4_goal_dynamics
    df_m4 = module_4_goal_dynamics.load_and_transform_data()
    module_4_goal_dynamics.visualize_goal_dynamics(df_m4)
    module_4_goal_dynamics.generate_insights(df_m4)
    
    print("\n--- Running Module 5 ---")
    import module_5_dashboard
    module_5_dashboard.create_interactive_dashboard()

if __name__ == "__main__":
    main()
