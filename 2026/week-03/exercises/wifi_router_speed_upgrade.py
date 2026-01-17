# Create a Router class that contains a WiFiModule object.
# The WiFiModule should have an attribute speed (default 100 Mbps)
# and a method show_speed() that prints the current speed. Add a method
# upgrade_speed() that upgrades the speed to 300 Mbps if it’s not already.
# Create a router with default speed, show the speed, upgrade it,
# and show the speed again.

class Router:
    """A single attempt to represent a router."""

    def __init__(self, wifi):
        """Initialize the router's attributes."""
        self.wifi = wifi
        self.speed = WiFiModule()


class WiFiModule:
    """A single attempt to model a WiFi module for a router."""

    def __init__(self, speed=100):
        """Initialize the attributes of WiFi module"""
        self.speed = speed

    def show_speed(self):
        """Print a statement describing the wifi speed."""
        print(f"The Internet speed of the WiFi is {self.speed}Mbps.\n")

    def upgrade_speed(self):
        """Upgrade the internet speed if possible."""
        if self.speed == 100:
            self.speed = 300
            print("The speed of the Internet is now upgraded.")
        else:
            print("The WiFi speed is already upgraded.")


router = Router('Cosmote')
router.speed.show_speed()

router.speed.upgrade_speed()
router.speed.show_speed()
