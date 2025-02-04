from collections import deque
import datetime
import time
import random

class Ticket:
  """A simple ticket class"""

  def __init__(self, ticket_num):
    self.ticket_num = ticket_num
    # self.time_stamp = time_stamp
    # self.time_stamp = datetime.datetime.now()
    self.time_stamp = datetime.datetime.now().strftime('%d.%m.%Y %H:%M:%S,%f')
  
  def __str__(self):
    return f"Ticket #{self.ticket_num}, Timestamp: {self.time_stamp}"

class TicketQueue:
  """Manages ticket queue and numbering"""
  def __init__(self):
    self.queue_num = 1

  def increase_queue(self):
    self.queue_num += 1
  
class TicketSystem:
  """Simulates a ticketing system"""
  def __init__(self):
    self.queue = deque()
    self.ticket_queue = TicketQueue()

  def generate_ticket(self):
    """Generate a ticket and add to queue"""
    ticket_num = self.ticket_queue.queue_num
    self.ticket_queue.increase_queue()

    new_ticket = Ticket(ticket_num)
    self.queue.append(new_ticket)
    print(f"Generated: {new_ticket}")

  def process_tickets(self):
    while self.queue:
      ticket = self.queue.popleft()
      print(f"Processing: {ticket}")
      time.sleep(random.uniform(1,3))

  def run(self, num_tickets, gen_delay_range):
    """Runs ticketing system"""
    print("Starting ticket generation phase. . .")
    for _ in range(num_tickets):
      self.generate_ticket()
      time.sleep(random.uniform(*gen_delay_range))

    print("\nStarting ticket processing phase . . .")
    self.process_tickets()
    print("\nAll tickets have been processed") 

if __name__=="__main__":
  system = TicketSystem()
  num_tickets = 5
  gen_delay_range = (0.5, 2)

  system.run(num_tickets, gen_delay_range)
  # ticket_q = TicketQueue()
  # q = deque()

  # for i in range(3):
  #   generate_ticket(q, ticket_q)

  # for item in q:
  #   print(item)

  # print(q[0], q[0].ticket_num)
  # print(len(q))
  # print(q[0].ticket_num, q[1].ticket_num, q[2].ticket_num)



