import unittest
from unittest.mock import patch
from ticketing_system_Keiffer import Ticket, TicketSystem
import datetime

class TestTicketSystem(unittest.TestCase):

    def test_ticket_initialization(self):
        ticket = Ticket(1)
        self.assertEqual(ticket.ticket_num, 1)
        self.assertIsInstance(ticket.time_stamp, datetime.datetime)

    def test_generate_ticket(self):
        system = TicketSystem()
        system.generate_ticket()
        self.assertEqual(len(system.queue), 1)
        self.assertEqual(system.queue[0].ticket_num, 1)

    def test_process_ticket(self):
        system = TicketSystem()
        system.generate_ticket()
        self.assertEqual(len(system.queue), 1)
        self.assertEqual(system.queue[0].ticket_num, 1)
        system.process_ticket()
        self.assertAlmostEqual(len(system.queue), 0)

    @patch('time.sleep', return_value=None)  # Mocking time.sleep to speed up tests
    def test_process_tickets(self, _):
        system = TicketSystem()
        for i in range(3):
            system.generate_ticket()
        system.process_ticket()
        self.assertEqual(len(system.queue), 2)

    @patch('time.sleep', return_value=None)  # Mocking time.sleep to speed up tests
    def test_run(self, _):
        system = TicketSystem()
        system.run(num_ticket=3, delay_range=(0, 0))
        self.assertEqual(len(system.queue), 0)

if __name__ == "__main__":
    unittest.main()

