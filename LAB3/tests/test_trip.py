# Łatwiejsze

import unittest
from src.trip import Trip


class TestTripInitialization(unittest.TestCase):
    def test_trip_creation(self):
        trip = Trip("Paris", 7)
        self.assertIsInstance(trip, Trip)

    def test_trip_attributes(self):
        trip = Trip("Paris", 7)
        self.assertEqual(trip.destination, "Paris")
        self.assertEqual(trip.duration, 7)

    def test_calculate_cost(self):
        trip1 = Trip("Paris", 7)
        self.assertEqual(trip1.calculate_cost(), 700)

        trip2 = Trip("Rome", 5)
        self.assertEqual(trip2.calculate_cost(), 500)

    def test_add_participant(self):
        trip = Trip("Paris", 7)
        trip.add_participant("John")
        self.assertIn("John", trip.participants)

    def test_calculate_cost_zero(self):
        trip = Trip("Berlin", 0)
        self.assertEqual(trip.calculate_cost(), 0)

    def test_add_participants_multiple(self):
        trip = Trip("Paris", 7)
        participants = ["John", "Alice", "Bob"]
        for participant in participants:
            trip.add_participant(participant)
        for participant in participants:
            self.assertIn(participant, trip.participants)

    def test_add_empty_participant(self):
        trip = Trip("Paris", 7)
        with self.assertRaises(ValueError) as context:
            trip.add_participant("")
        self.assertEqual(str(context.exception), "Participant name cannot be empty")

    def test_add_participant_same_multiple(self):
        trip = Trip("Paris", 7)
        trip.add_participant("John")
        trip.add_participant("John")
        trip.add_participant("John")
        self.assertEqual(trip.participants.count("John"), 3)


if __name__ == "__main__":
    unittest.main()