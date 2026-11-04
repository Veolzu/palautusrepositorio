from rich.console import Console
from rich.table import Table

from player import PlayerReader, PlayerStats

def make_table(season):
    table = Table(
        title=f"{season} scoring leaders",
        header_style="bold white",
        border_style="bright_blue",
    )
    table.add_column("Player", style="cyan", no_wrap=True)
    table.add_column("Team", style="magenta")
    table.add_column("Goals", justify="right", style="green")
    table.add_column("Assists", justify="right", style="green")
    table.add_column("Points", justify="right", style="bold green")

    return table

def update_table(table, players):
    for player in players:
        table.add_row(
            player.name,
            player.team,
            str(player.goals),
            str(player.assists),
            str(player.goals + player.assists),
        )
    return table

def main():
    season = input("season (eg. 2018-19): ")

    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)

    while True:
        mode = input("Search by (n)ationality, (t)eam or empty to quit: ")
        if mode == "":
            break
        if mode.lower() == "n":
            nationality = input("nationality (e.g FIN): ")
            players = stats.top_scorers_by_nationality(nationality)
        elif mode.lower() == "t":
            team = input("team (e.g BOS): ")
            players = stats.top_players_by_team(team)
        else:
            print("Unknown mode, choose 'n' or 't'.")
            continue

        table = make_table(season)
        table = update_table(table, players)

        Console().print(table)


if __name__ == "__main__":
    main()
