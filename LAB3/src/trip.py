#Łatwiejsze

from typing import List

class Trip:
    def __init__(self, destination: str, duration: int):
        self.destination = destination
        self.duration = max(0, duration)
        self.participants: List[str] = []

    def calculate_cost(self) -> int:
        return self.duration * 100

    def add_participant(self, participant: str):
        if not participant:
            raise ValueError("Participant name cannot be empty")
        self.participants.append(participant)