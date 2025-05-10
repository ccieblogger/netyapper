class MockNetBoxMCPClient:
    """
    Simulated NetBox MCP client for development/testing.
    """
    def get_device_info(self, device: str) -> dict:
        # Return fake device info
        return {
            "device": device,
            "interfaces": [
                {"name": "GigabitEthernet1", "ip": "192.168.1.1"},
                {"name": "GigabitEthernet2", "ip": "192.168.2.1"}
            ]
        }

    def get_interface_ip(self, device: str, interface: str) -> dict:
        # Return fake interface IP
        if interface == "GigabitEthernet1":
            return {"device": device, "interface": interface, "ip": "192.168.1.1"}
        elif interface == "GigabitEthernet2":
            return {"device": device, "interface": interface, "ip": "192.168.2.1"}
        else:
            return {"device": device, "interface": interface, "ip": None, "error": "Interface not found"}
