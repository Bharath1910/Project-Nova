from modules import utils

utils = utils.Utils()

def test_composei3Command():
    composedConfig = utils.composei3Command()

    expectedResult = {
        "Regular": [
            [
                "exec firefox-developer-edition --new-tab https://www.youtube.com", 
                "exec sleep 5"
            ], 
            ["exec spotify", "exec sleep 4"],
            ["exec discord", "exec sleep 2"],
            ["exec telegram-desktop"]
        ],

        "DLD Lab": [
            ["exec firefox-developer-edition --new-tab https://edaplayground.com"],
            ["exec logseq; workspace 1"]
        ],

        "Java Lab": [
            ["exec teams; workspace 1", "exec sleep 1"],
            ["exec code; workspace 2"],
        ]
    }
    
    for composedCommands, expectedCommands in zip(composedConfig.values(), expectedResult.values()):
        for composedCommand, expectedCommand in zip(composedCommands, expectedCommands):
            for composedSubCommand, expectedSubCommand in zip(composedCommand, expectedCommand):
                assert composedSubCommand == expectedSubCommand