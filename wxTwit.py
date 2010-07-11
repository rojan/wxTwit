#------------------------------------------------------------------------------------------------
#    wxTwit is a Twitter client made by using Boa constructor 0.6.1, wxPython, python_twitter
#    Author : Rojan Sinha [www.rojan.com.np]
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# email : rojansinha[at]gmail[dot]com
#------------------------------------------------------------------------------------------------
#!/usr/bin/env python
#Boa:App:BoaApp

import wx
import Login

modules ={u'Frame1': [0, '', u'Frame1.py'],
 u'Login': [1, 'Main frame of Application', u'Login.py']}

class BoaApp(wx.App):
    def OnInit(self):
        self.main = Login.create(None)
        self.main.Show()
        self.SetTopWindow(self.main)
        return True

def main():
    application = BoaApp(0)
    application.MainLoop()

if __name__ == '__main__':
    main()
