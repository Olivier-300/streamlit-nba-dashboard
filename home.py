import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt

# Function to load and clean the data
def load_data():
    # Load the regular season and playoff data from Excel files
    regular_season_path = 'players_stats_regular.xlsx'
    playoff_path = 'players_stats_playoff.xlsx'

    # Read the Excel files
    regular_data = pd.read_excel(regular_season_path)
    playoff_data = pd.read_excel(playoff_path)

    # Add a column to identify the type of season
    regular_data["Season Type"] = "Regular Season"
    playoff_data["Season Type"] = "Playoffs"

    # Combine both datasets
    combined_data = pd.concat([regular_data, playoff_data], ignore_index=True)

    # Remove TEAM_ID and PLAYER_ID columns
    combined_data = combined_data.drop(columns=["TEAM_ID", "PLAYER_ID"], errors='ignore')

    # Clean up Season Type formatting (replace 'Regular%20Season' with 'Regular Season')
    combined_data["Season Type"] = combined_data["Season Type"].replace("Regular%20Season", "Regular Season")

    return combined_data

# Function to draw the basketball court using Matplotlib
def draw_court(ax=None, color='black', lw=2):
    if ax is None:
        ax = plt.gca()

    # Create the basketball hoop
    hoop = plt.Circle((0, 0), radius=7.5, linewidth=lw, color=color, fill=False)

    # Create the backboard
    backboard = plt.Rectangle((-30, -7.5), 60, 1, linewidth=lw, color=color)

    # Create the paint
    outer_box = plt.Rectangle((-80, -47.5), 160, 190, linewidth=lw, color=color, fill=False)
    inner_box = plt.Rectangle((-60, -47.5), 120, 190, linewidth=lw, color=color, fill=False)

    # Create the free throw top arc
    top_free_throw = plt.Circle((0, 142.5), radius=60, linewidth=lw, color=color, fill=False)
    bottom_free_throw = plt.Circle((0, 142.5), radius=60, linewidth=lw, color=color, fill=False, linestyle='dashed')

    # Restricted zone
    restricted = plt.Circle((0, 0), radius=40, linewidth=lw, color=color, fill=False)

    # Three-point arc
    three_point_arc = plt.Circle((0, 0), radius=237.5, linewidth=lw, color=color, fill=False)

    # Add the court elements to the axes
    ax.add_patch(hoop)
    ax.add_patch(backboard)
    ax.add_patch(outer_box)
    ax.add_patch(inner_box)
    ax.add_patch(top_free_throw)
    ax.add_patch(bottom_free_throw)
    ax.add_patch(restricted)
    ax.add_patch(three_point_arc)

    # Set the limits and aspect ratio
    ax.set_xlim(-250, 250)
    ax.set_ylim(0, 470)
    ax.set_aspect(1)

    return ax

# Function to plot shot chart
def plot_shot_chart(player_name, shot_data):
    """
    Plot the shot chart for a specific player.
    """
    # Filter the shot data for the selected player
    player_data = shot_data[shot_data['PLAYER_NAME'] == player_name]

    # Create a figure and axis
    fig, ax = plt.subplots(figsize=(12, 11))

    # Draw the court
    draw_court(ax)

    # Plot shot locations as a scatter plot
    made_shots = player_data[player_data['SHOT_MADE_FLAG'] == 1]
    missed_shots = player_data[player_data['SHOT_MADE_FLAG'] == 0]

    # Plot made shots (in green) and missed shots (in red)
    ax.scatter(made_shots['LOC_X'], made_shots['LOC_Y'], color='green', label='Made Shots', s=100, alpha=0.6)
    ax.scatter(missed_shots['LOC_X'], missed_shots['LOC_Y'], color='red', label='Missed Shots', s=100, alpha=0.6)

    # Add title and legend
    ax.set_title(f'{player_name} Shot Chart', fontsize=18)
    ax.legend(loc='upper right')

    # Show the plot
    st.pyplot(fig)

# Function to display the profile page
def page_profile():
    st.title("Olivier Leroi-Morant - Profile")

    st.write("""
    ### Engineering Student at EFREI Paris
    Currently pursuing an engineering degree in digital technologies at **EFREI Paris** (2021 - 2026), with an international exchange experience at **Concordia University** in Montreal (August 2023 - December 2023).
    I am actively looking for a **2-year work-study opportunity** as a **Data Scientist** starting in **September 2024** with a rhythm of 3 days in a company and 2 days at school.
    
    #### Education:
    - **EFREI Paris** (2021 - 2026): Currently studying digital engineering.
    - **Concordia University** (Montreal) - Exchange program (August 2023 - December 2023).
    - **Lycée Jean Baptiste Corot** (2018 - 2021): High School Diploma (Baccalauréat Général) with a specialization in Mathematics, Physics, Chemistry, and LLCE English, along with the Maths Expertes option.
    
    #### Projects:
    - **PRONOBO (2024)**: Developed a football match prediction site (Liga, Ligue 1) using data scraping and machine learning (Random Forest).  
      Technologies used: Python, Scikit Learn, BeautifulSoup.
    - **NBA STATS (2024)**: Created an algorithm for predicting NBA statistics with a focus on scraping data and implementing machine learning (Linear Regression).  
      Technologies used: Python, Scikit Learn, Selenium.
    - **PC FOREST (2024)**: Developed a deep learning model for patent classification with a 92% F1 score. The model identified important keywords during the classification process.  
      Technologies used: Python, TensorFlow, Fast Text.
    
    #### Professional Experience:
    - **Darty – Multimedia Salesperson (2022 - 2023, 2 months)**: Managed multimedia sales and handled customer payments.
    - **Complétude – Private Tutor (Current)**: Provided tutoring in Mathematics and English to students ranging from elementary to high school levels.
    
    #### Technical Skills:
    - **Programming Languages:** Java, Python, JavaScript, R, HTML/CSS, C, Vue JS.
    - **Libraries & Frameworks:** Scikit Learn, Pandas, Matplotlib, Seaborn, PySpark, TensorFlow.
    - **Databases:** MySQL, Hadoop.
    - **Other Tools:** Linux, MATLAB, Excel, Git, Bash.
    
    #### Soft Skills:
    - Team Spirit, Curiosity, Creativity, Dynamism, Autonomy.
    
    #### Languages:
    - **French**: Native.
    - **English**: TOEIC 950.
    - **Spanish**: Intermediate.
    
    #### Interests and Hobbies:
    - **Basketball**: Captain of the middle school basketball team.
    - **Theater**: Leader of a theater group.
    
    #### Contact:
    - **Phone:** 06 13 48 72 46
    - **Email:** olivier.leroimorant@gmail.com
    - [GitHub](https://github.com/Olivier-300)
    - [LinkedIn](https://www.linkedin.com/in/olivier-leroi-morant-data-science/)
    """)

    # Add links to GitHub and LinkedIn
    st.write("[My GitHub](https://github.com/Olivier-300)")
    st.write("[My LinkedIn](https://www.linkedin.com/in/olivier-leroi-morant-data-science/)")

# Function to display the data analysis page with advanced plots
def page_analysis():
    st.title("Basketball Player Stats - Dynamic Analysis")

    # Load the combined data
    data = load_data()

    # Sidebar filter for season type (Regular Season vs Playoffs)
    season_type = st.sidebar.selectbox("Select Season Type", ["Regular Season", "Playoffs"])

    # Filter data based on season type
    filtered_data = data[data["Season Type"] == season_type]

    # Sidebar filter for season year
    seasons = filtered_data["Years"].unique()
    selected_season = st.sidebar.selectbox("Select Season", seasons)

    # Filter data by season year
    filtered_data = filtered_data[filtered_data["Years"] == selected_season]

    # Multiselect for teams
    teams = filtered_data["TEAM"].unique()
    selected_teams = st.sidebar.multiselect("Select Teams", teams)

    # Filter by teams if any are selected
    if selected_teams:
        filtered_data = filtered_data[filtered_data["TEAM"].isin(selected_teams)]

    # Multiselect for players (without search functionality here)
    selected_players = st.sidebar.multiselect("Select Players", filtered_data["PLAYER"].unique())

    if selected_players:
        filtered_data = filtered_data[filtered_data["PLAYER"].isin(selected_players)]

        # Display filtered data as a dataframe
        st.dataframe(filtered_data)

        # General statistics
        st.write("### General Statistics")
        st.write(filtered_data.describe())

        # If players are selected, display the graphs
        ### 1. Points per Player (Bar Plot)
        st.write("### Points per Player")
        fig_points = px.bar(filtered_data, x="PLAYER", y="PTS", color="PLAYER", title="Points per Player")
        st.plotly_chart(fig_points)

        ### 2. Points per Minute (Scatter Plot)
        st.write("### Points per Minute Played")
        fig_ppm = px.scatter(filtered_data, x="MIN", y="PTS", size="PTS", color="PLAYER",
                             hover_name="PLAYER", title="Points vs Minutes Played",
                             labels={"PTS": "Points", "MIN": "Minutes"})
        st.plotly_chart(fig_ppm)

        ### 3. Efficiency vs Points & FGA (Bubble Chart)
        st.write("### Efficiency vs Points and Field Goals Attempted (FGA)")
        fig_eff = px.scatter(filtered_data, x="PTS", y="EFF", size="FGA", color="PLAYER", hover_name="PLAYER",
                             title="Efficiency vs Points and FGA",
                             labels={"PTS": "Points", "EFF": "Efficiency", "FGA": "Field Goals Attempted"})
        st.plotly_chart(fig_eff)

        ### 4. 3-Point Stats (Bar Plot)
        st.write("### 3-Point Stats (Made, Attempted, %)")
        fig_3pts = go.Figure(data=[
            go.Bar(name='3-Pointers Made (FG3M)', x=filtered_data['PLAYER'], y=filtered_data['FG3M']),
            go.Bar(name='3-Pointers Attempted (FG3A)', x=filtered_data['PLAYER'], y=filtered_data['FG3A']),
            go.Scatter(name='3-Point Percentage (FG3_PCT)', x=filtered_data['PLAYER'], y=filtered_data['FG3_PCT'], mode='lines+markers')
        ])
        fig_3pts.update_layout(barmode='group', title="3-Point Stats per Player", xaxis_title="Player", yaxis_title="Value")
        st.plotly_chart(fig_3pts)

        ### 5. Rebounds, Blocks, and Steals (Grouped Bar Plot)
        st.write("### Rebounds, Blocks, and Steals per Player")
        fig_rbs = go.Figure(data=[
            go.Bar(name='Rebounds (REB)', x=filtered_data['PLAYER'], y=filtered_data['REB']),
            go.Bar(name='Blocks (BLK)', x=filtered_data['PLAYER'], y=filtered_data['BLK']),
            go.Bar(name='Steals (STL)', x=filtered_data['PLAYER'], y=filtered_data['STL'])
        ])
        fig_rbs.update_layout(barmode='group', title="Rebounds, Blocks, and Steals per Player", xaxis_title="Player", yaxis_title="Value")
        st.plotly_chart(fig_rbs)

    else:
        st.write("Please select players from the dropdown to view the statistics.")

# Function to allow searching for players in Court Map section only
def search_player(available_players):
    """
    Function for searching players by typing in their names in Court Map Data section.
    """
    search_query = st.text_input("Search for a Player", "")
    if search_query:
        filtered_players = [player for player in available_players if search_query.lower() in player.lower()]
    else:
        filtered_players = available_players
    return filtered_players

# Function to display shot charts on the basketball court in the Court Map section
def page_court_map():
    st.title("Basketball Court Map - Shot Chart (2023-2024)")

    # Load shot data (you should replace this with actual shot data loading logic)
    shot_data = pd.read_csv('nba_shot_data_2023_2024.csv')  # Make sure you have this data available

    # Text input search for players (available only in Court Map Data)
    available_players = shot_data["PLAYER_NAME"].unique()
    filtered_players = search_player(available_players)

    # Select player from dropdown with search functionality
    player_name = st.selectbox('Select a Player', filtered_players)

    # Plot the shot chart for the selected player
    plot_shot_chart(player_name, shot_data)

# Create a sidebar for navigation
page = st.sidebar.selectbox("Choose a Page", ["Profile", "Data Analysis", "Court Map Data"])

# Display the selected page
if page == "Profile":
    page_profile()
elif page == "Data Analysis":
    page_analysis()
else:
    page_court_map()

