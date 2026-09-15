from abc import ABC, abstractmethod

# =====================================================================
# ABSTRACTION: Defines an essential contract while hiding details.
# =====================================================================
class SmartDevice(ABC):
    def __init__(self, device_id: str, brand: str):
        self.device_id = device_id
        self.brand = brand

    @abstractmethod
    def operate(self) -> str:
        """Abstract contract method to be hidden and implemented by subclasses."""
        pass


# =====================================================================
# ENCAPSULATION: Protects internal states (_temperature) from bad values.
# =====================================================================
class Thermostat(SmartDevice):
    def __init__(self, device_id: str, brand: str, default_temp: float):
        super().__init__(device_id, brand)
        self._temperature = default_temp  # Encapsulated attribute

    @property
    def temperature(self) -> float:
        return self._temperature

    @temperature.setter
    def temperature(self, val: float):
        # Enforces invariants (safety checks)
        if 15.0 <= val <= 30.0:
            self._temperature = val
        else:
            raise ValueError("Temperature out of safe operating limits (15°C - 30°C)!")

    # OVERRIDING: Customizes the abstract method for specialized behavior
    def operate(self) -> str:
        return f"Thermostat {self.device_id} is regulating climate at {self._temperature}°C."


# =====================================================================
# INHERITANCE: Models a strict valid "IS-A" relationship (Speaker IS-A SmartDevice)
# =====================================================================
class SmartSpeaker(SmartDevice):
    def __init__(self, device_id: str, brand: str, volume: int = 50):
        super().__init__(device_id, brand)
        self.volume = volume

    # OVERRIDING: Customizes behavior specialized for speakers
    def operate(self) -> str:
        return f"SmartSpeaker {self.device_id} is streaming audio at volume {self.volume}%."


# =====================================================================
# COMPOSITION: Models a "HAS-A" relationship. Automation Hub HAS devices.
# =====================================================================
class AutomationHub:
    def __init__(self, hub_name: str):
        self.hub_name = hub_name
        self.connected_devices = []  # Composition container

    def add_device(self, device: SmartDevice):
        self.connected_devices.append(device)

    # POLYMORPHISM: Processes different subclasses through a common shared interface
    def run_system_check(self):
        print(f"--- Running Hub: {self.hub_name} ---")
        for device in self.connected_devices:
            # Code interacts via abstract 'operate()', regardless of actual underlying class
            print(device.operate())


# =====================================================================
# EXECUTION (OBJECTS & IDENTITY)
# =====================================================================
if __name__ == "__main__":
    # OBJECTS: Combining identity, state, and behavior
    living_room_temp = Thermostat("T-101", "Nest", 21.0)
    kitchen_speaker = SmartSpeaker("S-202", "Sonos", 40)

    # Testing Encapsulation
    living_room_temp.temperature = 24.5  # Allowed
    print(f"Updated Temp: {living_room_temp.temperature}°C")

    # Creating the Composed Hub System
    my_home_hub = AutomationHub("Main House Controller")
    my_home_hub.add_device(living_room_temp)
    my_home_hub.add_device(kitchen_speaker)

    # Executing Polymorphism
    my_home_hub.run_system_check()
