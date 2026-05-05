import pandas as pd
from faker import Faker
import random

fake = Faker()


def generate_players(n=100):
    players = []

    for i in range(n):
        players.append({
            "player_id": i + 1,
            "name": fake.name(),
            "email": fake.email(),
            "country": fake.country(),
            "signup_date": fake.date_between(start_date="-2y", end_date="today")
        })

    return pd.DataFrame(players)


def generate_deposits(players_df, n=500):
    deposits = []

    for i in range(n):
        player = players_df.sample(1).iloc[0]

        deposits.append({
            "deposit_id": i + 1,
            "player_id": player["player_id"],
            "amount": round(random.uniform(10, 500), 2),
            "timestamp": fake.date_time_between(start_date="-30d", end_date="now")
        })

    return pd.DataFrame(deposits)


def generate_bets(players_df, n=1000):
    bets = []

    for i in range(n):
        player = players_df.sample(1).iloc[0]
        bet_amount = round(random.uniform(1, 100), 2)
        win_amount = round(bet_amount * random.choice([0, 0.5, 1, 2]), 2)

        bets.append({
            "bet_id": i + 1,
            "player_id": player["player_id"],
            "game": random.choice(["slots", "blackjack", "roulette"]),
            "bet_amount": bet_amount,
            "win_amount": win_amount,
            "timestamp": fake.date_time_between(start_date="-30d", end_date="now")
        })

    return pd.DataFrame(bets)


if __name__ == "__main__":
    players_df = generate_players(100)
    deposits_df = generate_deposits(players_df, 500)
    bets_df = generate_bets(players_df, 1000)

    players_df.to_csv("data/sample/players.csv", index=False)
    deposits_df.to_csv("data/sample/deposits.csv", index=False)
    bets_df.to_csv("data/sample/bets.csv", index=False)

    print("Mock data generated successfully!")