import concurrent.futures
from subprocess import Popen, CREATE_NEW_CONSOLE, run

# PRIMES = [
#     {"id": 4731},
#     {"id": 4732},
#     {"id": 4733},
#     {"id": 4734},
#     {"id": 4735},
#     {"id": 4736},
#     {"id": 5015},
#     {"id": 5016},
#     {"id": 5017},
#     {"id": 5244},
#     {"id": 5245},
#     {"id": 5246},
#     {"id": 5373},
#     {"id": 5583},
#     {"id": 5595},
#     {"id": 5597},
#     {"id": 5600},
#     {"id": 5601},
#     {"id": 5602},
#     {"id": 5603},
#     {"id": 5606},
#     {"id": 5607},
#     {"id": 5608},
#     {"id": 5681},
#     {"id": 5683},
#     {"id": 5740},
#     {"id": 6742},
#     {"id": 6743},
#     {"id": 6865},
# ]
PRIMES = [
    {"id": 4731},
    {"id": 4732},
    {"id": 4733},
    {"id": 4734},
    {"id": 4735},
    {"id": 4736},
    {"id": 5015},
    {"id": 5016},
    {"id": 5017},
    {"id": 5244},
    {"id": 5245},
]


def runRobotAsync(queue):
    run(
        [
            "D:/Rocketbot_win_20240528/rocketbot.exe",
            "-start=prueba",
            "-db=D:/Rocketbot/Tests/robot.db",
            "-queue=" + str(queue["id"]),
        ],
        creationflags=CREATE_NEW_CONSOLE,
    )
    return


def main():
    with concurrent.futures.ProcessPoolExecutor(max_workers=5) as executor:
        result = list(executor.map(runRobotAsync, PRIMES))

    print(result)


if __name__ == "__main__":
    main()
