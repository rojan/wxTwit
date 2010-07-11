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
#Boa:Frame:Frame1

import wx

def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1BUTTON1, wxID_FRAME1BUTTON2, wxID_FRAME1PANEL1, 
 wxID_FRAME1STATICTEXT1, wxID_FRAME1STATICTEXT2, wxID_FRAME1STATICTEXT3, 
 wxID_FRAME1TEXTCTRL1, wxID_FRAME1TEXTCTRL2, 
] = [wx.NewId() for _init_ctrls in range(9)]

class Frame1(wx.Frame):
    def _init_coll_gridSizer4_Items(self, parent):
        # generated method, don't edit

        parent.AddWindow(self.staticText3, 0, border=0, flag=0)

    def _init_coll_gridSizer1_Items(self, parent):
        # generated method, don't edit

        parent.AddWindow(self.staticText1, 0, border=20,
              flag=wx.RIGHT | wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL)
        parent.AddWindow(self.textCtrl1, 0, border=0,
              flag=wx.GROW | wx.ALIGN_CENTER_VERTICAL)

    def _init_coll_gridSizer2_Items(self, parent):
        # generated method, don't edit

        parent.AddWindow(self.staticText2, 0, border=20,
              flag=wx.RIGHT | wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL)
        parent.AddWindow(self.textCtrl2, 0, border=0,
              flag=wx.GROW | wx.ALIGN_CENTER_VERTICAL)

    def _init_coll_boxSizer1_Items(self, parent):
        # generated method, don't edit

        parent.AddSizer(self.gridSizer4, 0, border=0, flag=wx.ALIGN_CENTER)
        parent.AddSizer(self.gridSizer1, 0, border=10,
              flag=wx.GROW | wx.ALIGN_CENTER | wx.ALL)
        parent.AddSizer(self.gridSizer2, 0, border=10,
              flag=wx.GROW | wx.ALIGN_CENTER_HORIZONTAL | wx.ALL)
        parent.AddSizer(self.gridSizer3, 0, border=10,
              flag=wx.ALIGN_TOP | wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_CENTER | wx.ALL)

    def _init_coll_gridSizer3_Items(self, parent):
        # generated method, don't edit

        parent.AddWindow(self.button1, 0, border=0, flag=wx.ALIGN_LEFT)
        parent.AddWindow(self.button2, 0, border=0, flag=wx.ALIGN_RIGHT)

    def _init_sizers(self):
        # generated method, don't edit
        self.boxSizer1 = wx.BoxSizer(orient=wx.VERTICAL)

        self.gridSizer1 = wx.GridSizer(cols=0, hgap=0, rows=1, vgap=0)

        self.gridSizer2 = wx.GridSizer(cols=0, hgap=0, rows=1, vgap=0)

        self.gridSizer3 = wx.GridSizer(cols=0, hgap=0, rows=1, vgap=0)

        self.gridSizer4 = wx.GridSizer(cols=0, hgap=0, rows=1, vgap=0)

        self._init_coll_boxSizer1_Items(self.boxSizer1)
        self._init_coll_gridSizer1_Items(self.gridSizer1)
        self._init_coll_gridSizer2_Items(self.gridSizer2)
        self._init_coll_gridSizer3_Items(self.gridSizer3)
        self._init_coll_gridSizer4_Items(self.gridSizer4)

        self.panel1.SetSizer(self.boxSizer1)

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(515, 288), size=wx.Size(257, 151),
              style=wx.DEFAULT_FRAME_STYLE, title=u'wxTwit | Login')
        self.SetClientSize(wx.Size(257, 151))

        self.panel1 = wx.Panel(id=wxID_FRAME1PANEL1, name='panel1', parent=self,
              pos=wx.Point(0, 0), size=wx.Size(257, 151),
              style=wx.TAB_TRAVERSAL)
        self.panel1.SetForegroundColour(wx.Colour(0, 0, 0))

        self.staticText1 = wx.StaticText(id=wxID_FRAME1STATICTEXT1,
              label=u'User Name', name='staticText1', parent=self.panel1,
              pos=wx.Point(35, 31), size=wx.Size(73, 17), style=0)

        self.textCtrl1 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL1, name='textCtrl1',
              parent=self.panel1, pos=wx.Point(128, 27), size=wx.Size(118, 25),
              style=0, value='')

        self.staticText2 = wx.StaticText(id=wxID_FRAME1STATICTEXT2,
              label=u'Password', name='staticText2', parent=self.panel1,
              pos=wx.Point(49, 76), size=wx.Size(59, 17), style=0)

        self.textCtrl2 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL2, name='textCtrl2',
              parent=self.panel1, pos=wx.Point(128, 72), size=wx.Size(118, 25),
              style=wx.TE_PASSWORD, value='')

        self.button1 = wx.Button(id=wxID_FRAME1BUTTON1, label=u'Login',
              name='button1', parent=self.panel1, pos=wx.Point(30, 117),
              size=wx.Size(98, 32), style=0)
        self.button1.Bind(wx.EVT_BUTTON, self.OnButton1Button,
              id=wxID_FRAME1BUTTON1)

        self.button2 = wx.Button(id=wxID_FRAME1BUTTON2, label=u'Quit',
              name='button2', parent=self.panel1, pos=wx.Point(133, 117),
              size=wx.Size(93, 32), style=0)
        self.button2.Bind(wx.EVT_BUTTON, self.OnButton2Button,
              id=wxID_FRAME1BUTTON2)

        self.staticText3 = wx.StaticText(id=wxID_FRAME1STATICTEXT3,
              label=u'Could not connect', name='staticText3',
              parent=self.panel1, pos=wx.Point(70, 0), size=wx.Size(116, 17),
              style=0)
        self.staticText3.SetForegroundColour(wx.Colour(255, 0, 0))
        self.staticText3.Show(False)

        self._init_sizers()

    def __init__(self, parent):
        self._init_ctrls(parent)           

    def OnButton1Button(self, event):
        uname = self.textCtrl1.GetValue()
        pwd = self.textCtrl2.GetValue()
        try:
            #creates main Frame                            
            import Frame1
            self.MainFrame = Frame1.create(self)            
            self.MainFrame.twit(uname, pwd)
            self.MainFrame.Show(True)
            self.Show(False)
            
        except:
            #shows hidden error msg in Login Frame
            self.staticText3.Show(True)

    def OnButton2Button(self, event):
        self.Close()
