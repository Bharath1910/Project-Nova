#!/home/bharath/.pyenv/versions/projectNova/bin/python

from pydymenu import rofi
import os

def showExistingProjects():
    projects = os.listdir("/home/bharath/Documents/Codes/projects")
    gui_select = rofi(projects, prompt="Pick a project: ", multi=True)

    if gui_select:
        if gui_select[0].startswith("new"):
            createNewProject(gui_select[0].split(" ")[1])
            return

        os.system("code /home/bharath/Documents/Codes/projects/" + gui_select[0])


def createNewProject(projectName, techStack=""):
    os.system("mkdir /home/bharath/Documents/Codes/projects/" + projectName)
    if techStack == "py":
        os.system(f"pyenv virtualenv {projectName}")
        os.system(f"pyenv activate {projectName}")

    elif techStack == "mern":
        os.system(f"mkdir /home/bharath/Documents/Codes/projects/{projectName}/client")
        os.system(f"mkdir /home/bharath/Documents/Codes/projects/{projectName}/server")

    os.system("code /home/bharath/Documents/Codes/projects/" + projectName)


if __name__ == "__main__":
    showExistingProjects()