class AthleteState:
    RUN = "_"
    JUMP = "|"


def check_race(athlete, track):
    total_actions = max(len(athlete), len(track))
    min_actions = min(len(athlete), len(track))

    track_segments = list(track)
    athlete_track = ""

    for index in range(total_actions):
        if index >= min_actions:
            athlete_track += "?"
        else:
            segment = track_segments[index]
            state = athlete[index]
            if state == AthleteState.RUN:
                if segment == state:
                    athlete_track += state
                else:
                    athlete_track += "/"
            elif state == AthleteState.JUMP:
                if segment == state:
                    athlete_track += state
                else:
                    athlete_track += "x"

    print(athlete_track)

    return track == athlete_track


race = "_|_|_"

print(
    check_race(
        [
            AthleteState.RUN,
            AthleteState.JUMP,
            AthleteState.RUN,
            AthleteState.JUMP,
            AthleteState.RUN,
        ],
        race,
    )
)
print(
    check_race(
        [
            AthleteState.RUN,
            AthleteState.RUN,
            AthleteState.RUN,
            AthleteState.JUMP,
            AthleteState.RUN,
        ],
        race,
    )
)
print(
    check_race(
        [
            AthleteState.RUN,
            AthleteState.RUN,
            AthleteState.JUMP,
            AthleteState.JUMP,
            AthleteState.RUN,
        ],
        race,
    )
)
print(
    check_race(
        [
            AthleteState.RUN,
            AthleteState.RUN,
            AthleteState.JUMP,
            AthleteState.JUMP,
            AthleteState.RUN,
        ],
        "_|_|_|_",
    )
)
print(
    check_race(
        [AthleteState.RUN, AthleteState.JUMP, AthleteState.RUN, AthleteState.JUMP],
        race,
    )
)
print(
    check_race(
        [
            AthleteState.RUN,
            AthleteState.JUMP,
            AthleteState.RUN,
            AthleteState.JUMP,
            AthleteState.RUN,
            AthleteState.JUMP,
            AthleteState.RUN,
        ],
        race,
    )
)
print(
    check_race(
        [
            AthleteState.JUMP,
            AthleteState.JUMP,
            AthleteState.JUMP,
            AthleteState.JUMP,
            AthleteState.JUMP,
        ],
        "|||||",
    )
)
print(
    check_race(
        [
            AthleteState.JUMP,
            AthleteState.JUMP,
            AthleteState.JUMP,
            AthleteState.JUMP,
            AthleteState.JUMP,
        ],
        "||?||",
    )
)
