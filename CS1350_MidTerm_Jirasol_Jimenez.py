from abc import ABC, abstractmethod

class Room(ABC):
    def __init__(self, room_number, nights):
        self.room_number = room_number
        self.nights = nights
    @abstractmethod
    def cost(self):
        pass

    def receipt(self):
        return f"Room {self.room_number}: {self.nights} nights, Total Cost: ${self.cost():.2f}"
    @staticmethod
    def validate_nights(nights):
        if not isinstance(nights, int) or nights <= 0:
            raise ValueError("Nights must be a positive integer.")
    
    def StandardRoom(Room):
        def __init__(self, room_number, nights, rate=100.00):
            super().__init__(room_number, nights)
            self.rate = rate
        self.validate_nights(nights)
    def cost(self):
        return self.rate * self.nights

    def DeluxeRoom(Room):
        def __init__(self, room_number, nights, rate=100.00, breakfast=15.00):
            super().__init__(room_number, nights)
            self.rate = rate
            self.breakfast = breakfast
        self.validate_nights(nights)
    
    def cost(self):
        return (self.rate * self.nights) + (self.breakfast)

    def SuiteRoom(Room):
        def __init__(self, room_number, nights, rate=250.00, breakfast=15.00, spa_access=50.00):
            super().__init__(room_number, nights)
            self.rate = rate
            self.breakfast = breakfast
            self.spa_access = spa_access
            self.validate_nights(nights)
        def discount(self):
            if self.nights > 3:
                return 0.10
            return 0.0
        def cost(self):
            return (self.nights * self.rate) * (1 - self.discount())
class Room(ABC):
    def __init__(self, room_number, nights):
        self.validate_nights(nights)
        self.room_number = room_number
        self.nights = nights

    @abstractmethod
    def cost(self):
        pass

    def receipt(self):
        return (
            f"Room {self.room_number}: {self.nights} nights, "
            f"Total Cost: ${self.cost():.2f}"
        )

    @staticmethod
    def validate_nights(nights):
        if not isinstance(nights, int) or nights <= 0:
            raise ValueError("Nights must be a positive integer.")


class StandardRoom(Room):
    def __init__(self, room_number, nights, rate=100.00):
        super().__init__(room_number, nights)
        self.rate = rate

    def cost(self):
        return self.rate * self.nights


class DeluxeRoom(Room):
    def __init__(self, room_number, nights, rate=100.00, breakfast=15.00):
        super().__init__(room_number, nights)
        self.rate = rate
        self.breakfast = breakfast

    def cost(self):
        return (self.rate + self.breakfast) * self.nights


class SuiteRoom(Room):
    def __init__(
        self, room_number, nights, rate=250.00, breakfast=15.00, spa_access=50.00
    ):
        super().__init__(room_number, nights)
        self.rate = rate
        self.breakfast = breakfast
        self.spa_access = spa_access

    def discount(self):
        return 0.10 if self.nights > 3 else 0.0

    def cost(self):
        subtotal = (self.rate + self.breakfast) * self.nights + self.spa_access
        return subtotal * (1 - self.discount())


def invoice(rooms):
    for room in rooms:
        print(room.receipt())
    return sum(room.cost() for room in rooms)


room = [
    StandardRoom(101, 2),
    DeluxeRoom(205, 2, rate=120.00),
    SuiteRoom(901, 3),
]

total = invoice(room)
print(f"Invoice total: ${total:.2f}")

try:
    Room.validate_nights(0)
except ValueError as e:
    print(f"Caught: {e}")

total = invoice(room)

try:
    Room.validate_nights(0)
except ValueError as e:
    print(f"Caught: {e}")

class Session:
    def __init__(self, title, attendees=None):
        self.title = title
        self.attendees = attendees if attendees is not None else []
        pass

    def register(self,name):
        if name not in self.attendees:
            self.attendees.append(name)
            print(f"{name} has been registered for {self.title}.")
        pass
    def unregister(self,name):
        if name in self.attendees:
            self.attendees.remove(name)
            print(f"{name} has been unregistered from {self.title}.")
        else:
            print(f"{name} is absent for {self.title}.")
        pass
    def attendee_count(self):
        return len(self.attendees)
    pass

    def attended_all(sessions):
        if not sessions:
            return []
        common_attendees = set(sessions[0].attendees)
        for session in sessions[1:]:
            common_attendees.intersection_update(session.attendees)
        return list(common_attendees)
    def attended_exactly_one(sessions):
        attendee_counts = {}
        for session in sessions:
            for attendee in session.attendees:
                attendee_counts[attendee] = attendee_counts.get(attendee, 0) + 1
        return [attendee for attendee, count in attendee_counts.items() if count == 1]
    pass
    def no_shows(registered, sessions):
        attended = set()
        for session in sessions:
            attended.update(session.attendees)
        return list(registered - attended)
    pass
    def summary(sessions):
        summary_dict = {}
        for session in sessions:
            summary_dict[session.title] = session.attendee_count()
        return summary_dict

keynote = Session("Keynote")
for p in ["Ana", "Ben", "Cruz", "Dee"]:
    keynote.register(p)

workshop = Session("Workshop")
for p in ["Ana", "Cruz", "Eli"]:
    workshop.register(p)
panel = Session("Panel")
for p in ["Ana", "Dee", "Eli", "Fay"]:
    panel.register(p)

workshop.unregister("Eli")
workshop.unregister("Zed")
print(workshop.attendee_count())

sessions = [keynote, workshop, panel]
print("Attended All:", Session.attended_all(sessions))
print("Attended Exactly One:", Session.attended_exactly_one(sessions))

print("No Shows:", Session.no_shows({"Ana", "Ben", "Fay", "Gus"}, sessions))

print("Summary:", Session.summary(sessions))
