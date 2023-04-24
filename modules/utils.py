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

        for workspace, commands in workspaceConfig.items():
            composedConfig[workspace] = []

            for command in commands:
                commandLis = []
                
                if command[1] is None:
                    commandLis.append(f"exec {command[0]}")
                    
                
                else:
                    commandLis.append(f"exec {command[0]}; workspace {command[1]}")

                if command[2] is not None:
                    commandLis.append(f"exec sleep {command[2]}")

                composedConfig[workspace].append(commandLis)
        
        return composedConfig
            


    def invokei3Commands(self, workspace):
        composedConfig = self.composei3Command()
        if workspace not in composedConfig:
            return
            
        for command in composedConfig[workspace]:
            self.i3.command(command)