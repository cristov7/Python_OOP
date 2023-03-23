# # Interface Segregation (ISP):


class PowerCable:
    def plug_in_power(self):
        pass


class RCAConnectable:
    def connect_by_device_via_rca_cable(self):
        pass


class HDMIConnectable:
    def connect_by_device_via_hdmi_cable(self):
        pass


class EthernetConnectable:
    def connect_by_device_via_ethernet_cable(self):
        pass


class Television(HDMIConnectable, RCAConnectable, PowerCable):
    def connect_to_dvd(self):
        self.connect_by_device_via_rca_cable()

    def connect_to_game_console(self):
        self.connect_by_device_via_hdmi_cable()


class DVDPlayer(HDMIConnectable, PowerCable):
    def connect_to_tv(self):
        self.connect_by_device_via_hdmi_cable()


class GameConsole(HDMIConnectable, EthernetConnectable, PowerCable):
    def connect_to_tv(self):
        self.connect_by_device_via_hdmi_cable()

    def connect_to_router(self):
        self.connect_by_device_via_ethernet_cable()


class Router(EthernetConnectable, PowerCable):
    def connect_to_tv(self):
        self.connect_by_device_via_ethernet_cable()

    def connect_to_game_console(self):
        self.connect_by_device_via_ethernet_cable()
