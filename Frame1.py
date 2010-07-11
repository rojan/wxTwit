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
import wx.grid
import twitter

def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1BUTTON1, wxID_FRAME1BUTTON2, wxID_FRAME1GRID1, 
 wxID_FRAME1PANEL1, wxID_FRAME1TEXTCTRL1, 
] = [wx.NewId() for _init_ctrls in range(6)]

class Frame1(wx.Frame):
    api = 0
    usrname = 0
    pswd = 0
    def _init_coll_gridSizer1_Items(self, parent):
        # generated method, don't edit

        parent.AddWindow(self.button1, 0, border=10,
              flag=wx.RIGHT | wx.ALIGN_RIGHT)

    def _init_coll_gridSizer2_Items(self, parent):
        # generated method, don't edit

        parent.AddWindow(self.button2, 0, border=10, flag=wx.LEFT)

    def _init_coll_boxSizer2_Items(self, parent):
        # generated method, don't edit

        parent.AddWindow(self.textCtrl1, 0, border=10, flag=wx.ALL | wx.EXPAND)
        parent.AddSizer(self.gridSizer1, 0, border=0, flag=wx.GROW)
        parent.AddSizer(self.gridSizer2, 0, border=0, flag=0)
        parent.AddWindow(self.grid1, 0, border=10, flag=wx.EXPAND | wx.ALL)

    def _init_sizers(self):
        # generated method, don't edit
        self.boxSizer2 = wx.BoxSizer(orient=wx.VERTICAL)

        self.gridSizer1 = wx.GridSizer(cols=0, hgap=0, rows=1, vgap=0)

        self.gridSizer2 = wx.GridSizer(cols=0, hgap=0, rows=1, vgap=0)

        self._init_coll_boxSizer2_Items(self.boxSizer2)
        self._init_coll_gridSizer1_Items(self.gridSizer1)
        self._init_coll_gridSizer2_Items(self.gridSizer2)

        self.panel1.SetSizer(self.boxSizer2)

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(439, 87), size=wx.Size(539, 561),
              style=wx.DEFAULT_FRAME_STYLE, title=u'wxTwit')
        self.SetClientSize(wx.Size(539, 561))
        self.Bind(wx.EVT_CLOSE, self.OnFrame1Close)

        self.panel1 = wx.Panel(id=wxID_FRAME1PANEL1, name='panel1', parent=self,
              pos=wx.Point(0, 0), size=wx.Size(539, 561),
              style=wx.TAB_TRAVERSAL)

        self.textCtrl1 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL1, name='textCtrl1',
              parent=self.panel1, pos=wx.Point(10, 10), size=wx.Size(519, 48),
              style=0, value=u'')
        self.textCtrl1.SetFont(wx.Font(11, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'Sans'))
        self.textCtrl1.SetMaxLength(140)

        self.button1 = wx.Button(id=wxID_FRAME1BUTTON1, label=u'Post',
              name='button1', parent=self.panel1, pos=wx.Point(444, 68),
              size=wx.Size(85, 32), style=0)
        self.button1.Bind(wx.EVT_BUTTON, self.OnButton1Button,
              id=wxID_FRAME1BUTTON1)

        self.grid1 = wx.grid.Grid(id=wxID_FRAME1GRID1, name='grid1',
              parent=self.panel1, pos=wx.Point(10, 142), size=wx.Size(519, 402),
              style=0)
        self.grid1.SetRowLabelSize(0)
        self.grid1.SetDefaultRowSize(55)
        self.grid1.SetCellHighlightPenWidth(0)
        self.grid1.EnableEditing(False)
        self.grid1.SetColLabelSize(0)
        self.grid1.SetDefaultCellFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'Sans'))
        self.grid1.SetDefaultCellBackgroundColour(wx.Colour(77, 77, 77))
        self.grid1.SetDefaultCellTextColour(wx.Colour(229, 229, 229))
        self.grid1.SetGridLineColour(wx.Colour(127, 127, 127))
        self.grid1.EnableGridLines(False)
        self.grid1.Bind(wx.EVT_MOUSEWHEEL, self.OnGrid1Mousewheel)

        self.button2 = wx.Button(id=wxID_FRAME1BUTTON2, label=u'Reload',
              name='button2', parent=self.panel1, pos=wx.Point(10, 100),
              size=wx.Size(85, 32), style=0)
        self.button2.Bind(wx.EVT_BUTTON, self.OnButton2Button,
              id=wxID_FRAME1BUTTON2)

        self._init_sizers()

    def twit(self, uname, pwd): 
        global usrname
        global pswd
        global api
        usrname = uname
        pswd = pwd        
        api = twitter.Api(username = usrname, password = pswd)
        try:             
            self.grid1.CreateGrid(25, 3)            
            self.grid1.DisableDragColSize()
            # setting the width of the columns
            self.grid1.SetColSize(0, 105)
            self.grid1.SetCellTextColour(0, 0, wx.Colour(67, 109, 225))
            self.grid1.SetColSize(1, 350)
            self.grid1.SetColSize(2, 30)
            #getid = twitter.Status()
            status = api.GetFriendsTimeline(usrname,25)
            i=0
                       
            for s in status:
                # wraps text inside a cell          
                self.grid1.SetCellRenderer(i,0,wx.grid.GridCellAutoWrapStringRenderer())
                self.grid1.SetCellTextColour(i, 0, wx.Colour(94, 144, 239))
                self.grid1.SetCellValue(i, 0, s.user.screen_name.encode("utf-8"))
                # wraps text inside a cell
                self.grid1.SetCellRenderer(i,1,wx.grid.GridCellAutoWrapStringRenderer())
                self.grid1.SetCellValue(i, 1, s.text.encode("utf-8"))
                            
                i += 1                
        except:
            self.Close()        
             
    def __init__(self, parent):
        self._init_ctrls(parent)
       
    # posts twitter updates
    def OnButton1Button(self, event):
        post = self.textCtrl1.GetValue()
        if post == "": #checks blank post
            wx.MessageBox("You are trying to post an empty message. There must be at least one character and not more than 140 characters.")
        else :
            api.PostUpdate(post) 
            self.textCtrl1.SetValue("") 
            
# exit program
    def OnFrame1Close(self, event):
        exit()


    def OnButton2Button(self, event):
        event.Skip()
        # Reloding/Refresing method goes here

    def OnGrid1Mousewheel(self, event):
##        self.grid1.
        event.Skip()
