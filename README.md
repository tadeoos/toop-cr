# Code review task

The aim of this task is to verify your programming and communication skills.
Review this code as you would review your colleague's work.

There's no fixed time limit for this task, but we estimate it shouldn't take longer than 30 minutes.
Write all your comments in english.

The code you'll be checking is a ticket-selling app.

The business requirements are:
* There is a finite pool of tickets.
* Ticket pool is available for a limited amount of time.
* Customers can buy tickets until the pool is depleted.
* A single Customer can buy a limited number of tickets.
* Ticket checkout is time-limited. If Customer does not complete a checkout process in time, the tickets return to the pool. Tickets should remain unavailable for the duration of checkout process.
* App provides a RESTful API.

It's a prototype, so it's OK to skip implementation of time-consuming parts, like storing models in the database.
However, there should be proper interfaces that will allow replacing the prototype code with full implementation (like adding ORM).
The app is not complete. The parts that are finished should be correct and meet code quality standards.

Below you'll find a message from your faux colleague about what they did.

> Hi, here's what I did:
> * Event and ticket models
> * In-memory storage of events and tickets (for our prototype purposes)
> * Model managers with listing and adding functionality
> * API for adding and listing events
> * API for listing orders (adding orders not done yet)

## Installation and running

Run app
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
FLASK_DEBUG=1 FLASK_APP=booking.app flask run
```

Run tests
```bash
py.test tests
```

# For recruiters

How to use this task and assessment rules are in project Wiki
