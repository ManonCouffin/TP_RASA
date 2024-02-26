# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

import random

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

animals_db = {
    'dog': 'https://media.istockphoto.com/id/467923438/photo/silly-dog-tilts-head-in-front-of-barn.jpg?s=612x612&w=0&k=20&c=haPwfoPl_ggvNKAga_Qv4r88qWdcpH-qZ5DaBba6-8U=',
    'cat': 'https://images.ctfassets.net/ub3bwfd53mwy/5zi8myLobtihb1cWl3tj8L/45a40e66765f26beddf7eeee29f74723/6_Image.jpg?w=750"
    'butterflies': 'https://images.unsplash.com/photo-1545703399-4313b14625d9?q=80&w=1000&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxleHBsb3JlLWZlZWR8NHx8fGVufDB8fHx8fA%3D%3D'
}

class ActionShowImage(Action):

     def name(self) -> Text:
         return "action_show_image"
        
     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        animal_type = next(tracker.get_latest_entity_values("animal"),None)
        
        if not animal_type: 
             msg = f"I don't have a photo of a {animal_type}... Try another animal like a dog, a cat,..."
             dispatcher.utter_message(text=msg)
             return []
        
        animal_image = animals_db.get(animal_type,None) 
        
        dispatcher.utter_message(text = "Let me see ... I found this ... Does it help ? ", image=animal_image)

class ActionFavoriteAnimal(Action):

     def name(self) -> Text:
         return "action_favorite_animal"
        
     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        animal_type = next(tracker.get_latest_entity_values("animal"),None)
        if not animal_type: 
             msg = f"I'm sure they will help you get better!"
             dispatcher.utter_message(text=msg)
             return []
        
        animal_image = animals_db.get(animal_type,None) 
        
        dispatcher.utter_message(text = "I found this picture !", image=animal_image)