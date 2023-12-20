# Imports
from importlib.resources import path
import json as js
import os
import datetime
from typing import Dict

tempFile: str = "userData/userData.json"


# Functions

'''
This file provides all the functions for managing events 
'''

'''
Appends a new event to the provided event jsonFile

eventName: string -> Provide the name of the event that you would like to create

desc: string: The description of the event

date: The due date for the event

jsonFile: string -> The path to the events file


'''
def createEvent(eventName: str, desc: str, date: any, jsonFile: any) -> list:
    # Load JSON file
    osPath = jsonFile # Path to the file 

    with open(osPath, "r+", encoding='utf-8') as file:
        jsonData: str = js.load(file)
        
        if "events" not in jsonData:
            jsonData["events"] = {} # Gen the events table in JSON

    
        if eventName not in jsonData["events"]:
            dataEntry = jsonData["events"]["template"]

            dataEntry["desc"]["content"] = desc # Sets the desc content
            dataEntry["date"] = date # Sets the date entry

            jsonData["events"][eventName] = dataEntry
        else:
            print("Cannot do this operation!")
            return {"success": False, "note": "The note with this name exists, please try again"} # Return the data
    
        # Dump the JSON file 
        file.seek(0)
        js.dump(jsonData, file, indent=4)
        file.truncate()
        return {"success": True, "note": ""}

'''
Patches the note with passed in updateContent based on the updateType

eventName: string -> Provide the name of the event that you would like to update

updateType: str -> What you would like to update. I.e desc or date

updateContent: any -> The content that you would like to update the event with. I.e the event description and the event date

jsonFile: string -> The path to the events file

return: list -> This will return the status list to show if it was successful or a failure.
'''
def updateEvent(eventName: str, updateContent: any, updateType: str, jsonFile: any) -> list:
    # Load JSON file
    osPath: str = jsonFile # Path to the file

    with open(osPath, "r+", encoding='utf-8') as file:
        jsonData: any = js.load(file)

        if "events" in jsonData: 
            if eventName in jsonData["events"]:
                if updateType == "desc":
                    jsonData["events"][eventName][updateType]["content"] = updateContent # Patch the content of the desc
                else:
                    jsonData["events"][eventName][updateType] = updateContent # Patch the date

                # Dump JSON file
                file.seek(0)
                js.dump(jsonData, file, indent=4)
                file.truncate()
                print("Success")
                return {"success": True, "note": ""}
            else:
                print("Failed")
                return {"success": False, "note": "The event with this title was not found"}
        else:
            print("Failed")
            return {"success": True, "note": "This is an invalid event file"}
                
'''
This function will delete a note from the note file provided

eventName: string -> Provide the name of the event that you would like to delete

jsonFile: string -> The path to the events file

Return: List -> This will return the status list to show if it was successful or a failure.

'''
def deleteEvent(eventName: str, jsonFile: any) -> list:
    # Load JSON file
    osPath: str  = jsonFile # Path to the file 

    with open(osPath, "r+", encoding='utf-8') as file:
        jsonData = js.load(file)

        if "events" in jsonData: 
            if eventName in jsonData["events"]:
                del jsonData["events"][eventName] # Delete the note

                # Dump JSON file
                file.seek(0)
                js.dump(jsonData, file, indent=4)
                file.truncate()
                return {"success": True, "note": ""}
            else:
                print("Failed")
                return {"success": False, "note": "The event with this title was not found"}
        else:
            print("Failed")
            return {"success": True, "note": "This is an invalid events  file"}


'''
This will get every single event inside of a specific file and return it as a dictionary

jsonFile: string -> The path to the events file

Return: Dict -> Dictionary containing the different events from the JSON file. Alternatively, this will return the status list to show if it was successful or a failure.
'''
def getEvents(jsonFile: str) -> Dict:
    osPath: str = jsonFile

    with open(osPath, "r") as file:
        jsonData: any = js.load(file)

        eventsTable: dict = jsonData["events"]

        return eventsTable.items()


#------- Testing -------#

