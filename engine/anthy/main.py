# vim:set noet ts=4:
#
# ibus - The Input Bus
#
# Copyright (c) 2007-2008 Huang Peng <shawn.p.huang@gmail.com>
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the
# Free Software Foundation, Inc., 59 Temple Place, Suite 330,
# Boston, MA  02111-1307  USA

import dbus
import dbus.connection
import dbus.mainloop.glib
import ibus
import factory
import gtk

class IMApp:
	def __init__ (self):
		self._dbusconn = dbus.connection.Connection (ibus.IBUS_ADDR)
		self._dbusconn.add_signal_receiver (self._disconnected_cb, 
							"Disconnected", 
							dbus_interface = dbus.LOCAL_IFACE)
		self._engine = factory.DemoEngineFactory (self._dbusconn)
		self._ibus = self._dbusconn.get_object (ibus.IBUS_NAME, ibus.IBUS_PATH)
		self._ibus.RegisterFactories ([factory.FACTORY_PATH], **ibus.DEFAULT_ASYNC_HANDLERS)

	def run (self):
		gtk.main ()

	def _disconnected_cb (self):
		print "disconnected"
		gtk.main_quit ()
	

def main ():
	IMApp ().run ()

if __name__ == "__main__":
	dbus.mainloop.glib.DBusGMainLoop (set_as_default=True)
	main ()
