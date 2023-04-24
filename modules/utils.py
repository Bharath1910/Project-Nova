import json
import i3ipc

class Utils:
    def __init__(self):
        self.i3 = i3ipc.Connection()

    def parseConfiguration(self, configFile="~/.config/nova/config.json"):
        with open(configFile, "r") as file:
            config = json.load(file)
            self.projectDirectories = config["projectDirectories"]
            
    def parseJSON(self):
        with open("workspaces.json", "r") as file:
            workspaceConfig = json.load(file)
            return workspaceConfig
            
    def composei3Command(self):
        workspaceConfig = self.parseJSON()
        composedConfig = {}

        for workspaceName, commands in workspaceConfig.items():
            composedCommands = []
            for commandWorkspaceDelay in commands:
                i3Command = f"exec {commandWorkspaceDelay[0]}; workspace {commandWorkspaceDelay[1]}"
                composedCommands.append(i3Command)

                delay = commandWorkspaceDelay[2]
                composedCommands.append(f"exec sleep {delay}")

            composedConfig[workspaceName] = composedCommands
        
        return composedConfig

    def invokei3Commands(self, workspace):
        composedConfig = self.composei3Command()
        if workspace not in composedConfig:
            return
            
        for command in composedConfig[workspace]:
            self.i3.command(command)