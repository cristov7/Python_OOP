from project.formula_teams.red_bull_team import RedBullTeam
from project.formula_teams.mercedes_team import MercedesTeam


class F1SeasonApp:
    def __init__(self):
        self.red_bull_team: RedBullTeam or None = None  # red_bull_team == red_bull_team_object or None
        self.mercedes_team: MercedesTeam or None = None  # mercedes_team == mercedes_team_object or None

    def register_team_for_season(self, team_name: str, budget: int) -> [str, Exception]:
        if team_name == "Red Bull":
            self.red_bull_team = RedBullTeam(budget)
            return f"{team_name} has joined the new F1 season."
        elif team_name == "Mercedes":
            self.mercedes_team = MercedesTeam(budget)
            return f"{team_name} has joined the new F1 season."
        else:
            raise ValueError("Invalid team name!")

    def new_race_results(self, race_name: str, red_bull_pos: int, mercedes_pos: int) -> [Exception, str]:
        if not self.red_bull_team or not self.mercedes_team:
            raise Exception("Not all teams have registered for the season.")
        else:
            red_bull_revenue_message = self.red_bull_team.calculate_revenue_after_race(red_bull_pos)
            mercedes_revenue_message = self.mercedes_team.calculate_revenue_after_race(mercedes_pos)
            ahead_team = "Red Bull" if red_bull_pos < mercedes_pos else "Mercedes"
            return f"Red Bull: {red_bull_revenue_message}. " \
                   f"Mercedes: {mercedes_revenue_message}. " \
                   f"{ahead_team} is ahead at the {race_name} race."
