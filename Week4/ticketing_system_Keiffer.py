from collections import deque
import datetime
import time
import random

class Ticket:
  def __init__(self, ticket_num):
    self.ticket_num = ticket_num
    self.time_stamp = datetime.datetime.now()

  def __str__(self):
    return f"Ticket #{self.ticket_num}, Timestamp: {self.time_stamp}"

class TicketQueue:
  def __init__(self):
    self.queue_num = 1

  def increase_queue(self):
    self.queue_num += 1

class TicketSystem:
  def __init__(self):
    self.queue = deque()
    self.ticket_queue = TicketQueue()

  def generate_ticket(self):
    new_ticket = Ticket(self.ticket_queue.queue_num)
    self.queue.append(new_ticket)
    self.ticket_queue.increase_queue()
    print(f"Generated: {new_ticket}")

  def process_ticket(self):
    ticket = self.queue.popleft()
    print(f"Processed: {ticket}")

  def run(self, num_ticket, delay_range):
    print("Starting the queue and generating phase . . .")

    # GENERATE ALL TICKETS
    for _ in range(num_ticket):
      self.generate_ticket()
      time.sleep(random.uniform(*delay_range))
    
    print("Starting the ticket processing phase . . .")
    # PROCEESS ALL TICKETS
    for _ in range(num_ticket):
      self.process_ticket()
      time.sleep(random.uniform(*delay_range))
    

if __name__=="__main__":
  ticket_system = TicketSystem()

  number_of_tickets = 20
  time_day = (0.25, 1.5)

  ticket_system.run(number_of_tickets, time_day)


# Video Submission:
# 1. Test Cases
# 2. Time & Space Complexity
# 3. Refinement