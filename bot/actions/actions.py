from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionGreet(Action):
    def name(self) -> Text:
        return "action_greet"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(response="utter_greet")
        return []

class ActionHappy(Action):
    def name(self) -> Text:
        return "action_happy"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(response="utter_happy")
        return []

class ActionCheerUp(Action):
    def name(self) -> Text:
        return "action_cheer_up"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(response="utter_cheer_up")
        return []

class ActionDidThatHelp(Action):
    def name(self) -> Text:
        return "action_did_that_help"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(response="utter_did_that_help")
        return []

class ActionGoodbye(Action):
    def name(self) -> Text:
        return "action_goodbye"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(response="utter_goodbye")
        return []

class ActionSportsNews(Action):
    def name(self) -> Text:
        return "action_sports_news"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(response="utter_sports_news")
        return []

class ActionSportsSchedule(Action):
    def name(self) -> Text:
        return "action_sports_schedule"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(response="utter_sports_schedule")
        return []

class ActionSportsScores(Action):
    def name(self) -> Text:
        return "action_sports_scores"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(response="utter_sports_scores")
        return []

class ActionSportsStandings(Action):
    def name(self) -> Text:
        return "action_sports_standings"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(response="utter_sports_standings")
        return []

class ActionSportsAnalysis(Action):
    def name(self) -> Text:
        return "action_sports_analysis"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(response="utter_sports_analysis")
        return []

class ActionSportsTrivia(Action):
    def name(self) -> Text:
        return "action_sports_trivia"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(response="utter_sports_trivia")
        return []

class ActionSportsInjuryUpdates(Action):
    def name(self) -> Text:
        return "action_sports_injury_updates"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(response="utter_sports_injury_updates")
        return []

class ActionSportsTransferNews(Action):
    def name(self) -> Text:
        return "action_sports_transfer_news"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(response="utter_sports_transfer_news")
        return []

class ActionSportsEventInformation(Action):
    def name(self) -> Text:
        return "action_sports_event_information"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(response="utter_sports_event_information")
        return []

