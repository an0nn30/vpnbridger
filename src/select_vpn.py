# window.py
#
# Copyright 2020 anonneo
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from gi.repository import Gtk


@Gtk.Template(resource_path='/org/example/App/select_vpn.ui')
class VpnWindow(Gtk.ApplicationWindow):
    __gtype_name__ = 'VpnWindow'

    connectButton = Gtk.Template.Child()
    selectServerBox = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.connectButton.connect("clicked", self.on_connect_button_clicked)

        # Initialize Combo Box with Values
        for server in self.get_server_listings():
            self.selectServerBox.append_text(server["host"])


    def on_connect_button_clicked(self, widget):
        print("Clicked!")

    def get_server_listings(self):
        servers = []
        with open('/home/anonneo/.ssh/config', 'r') as fp:
            line = fp.readline()
            cnt = 1
            while line:
                if line.split(" ")[0] == "Host":
                    server = {
                        "host":""
                    }
                    server["host"] = line.split(" ")[1]
                    servers.append(server)
                line = fp.readline()
        print (servers)
        return servers




    
