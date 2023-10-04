import sys
import math


def round2(num):
    return math.floor(num * 100 + 0.5) / 100


class Challenge:
    def __init__(self):
        self.solved = False
        self.languages = set()
        self.score = 0
        self.bonus = 0
        self.penalty = 0

    def submit(self, score, language, is_accepted):
        self.score = max(self.score, score)

        if is_accepted:
            # First accepted submission gets double the points
            if not self.solved:
                self.solved = True
                self.bonus += (score + 1)
            # First accepted unique language gets 1 bonus point
            # This applies for the first accepted submission too
            elif language not in self.languages:
                self.bonus += 1
            self.languages.add(language)
        else:
            self.penalty += 1

    def tabulate(self):
        return self.score + self.bonus - self.penalty


class Team:
    def __init__(self, name):
        self.name = name
        self.total_score = 0
        self.challenges = {}
        self.first_submit = 1_000_000
        self.first_accepted = 1_000_000

    def add_record(self, idx, challenge, score, language, is_accepted):
        if challenge not in self.challenges:
            self.challenges[challenge] = Challenge()
        self.challenges[challenge].submit(score, language, is_accepted)

        if self.first_submit == 1_000_000:
            self.first_submit = idx

        if is_accepted and self.first_accepted == 1_000_000:
            self.first_accepted = idx

    def calculate_total(self):
        self.total_score = round2(sum(c.tabulate() for c in self.challenges.values()))
        return self.total_score


def main():
    teams = {}

    for idx, line in enumerate(sys.stdin):
        team_name, score, challenge, language, status = line.strip().split(",")
        score = float(score)
        is_accepted = status == "Accepted"

        if team_name not in teams:
            teams[team_name] = Team(team_name)

        teams[team_name].add_record(idx, challenge, score, language, is_accepted)

    for team_name, team in teams.items():
        team.calculate_total()

    teams = sorted(
        teams.values(),
        key=lambda x: (-x.total_score, x.first_accepted, x.first_submit),
    )

    for rank, team in enumerate(teams):
        print(f"{rank + 1},{team.name},{team.total_score:.2f}")


if __name__ == "__main__":
    main()
