import glib #for the GeoPoint class
import wx #for user interface

#opens a file with a list of GeoPoints and reads them into pointslist[]
def LoadPoints(event):
    pointslist = []
    import sqlite3
    conn = sqlite3.connect(dbname.GetValue())
    curs = conn.cursor()
    sqlCmd = 'SELECT * FROM tblGeopoints'
    curs.execute(sqlCmd)

    #reads in the (file based )data
    rows = curs.fetchall()

    #put the fetchall into a list of GeoPoints
    points = []
    for row in rows:
        point = glib.GeoPoint(row[0],row[1],row[2])
        points.append(point)
        
    #make a GeoPoint for user location
    userLocation = glib.GeoPoint(float(lat.GetValue()),float(lon.GetValue()), 'Your Location')
        
    #find the point from the points list that is closest to userLocation
    closest = points[0]
    for x in points:
        if x.Distance(userLocation) < closest.Distance(userLocation):
            closest = x

        #display the message that tells the user which point they are closest to
    message.SetValue('You are closest to ' + closest.GetDescription() + ' which is located at '
                        + str(closest.GetPoint()) + '.')
        
##########################################################################################################
#create the GUI       
app = wx.App()
win = wx.Frame(None, title = "GeoPoints App",
               size = (410,350))

#add text boxes and labels:
dbname = wx.TextCtrl(win, pos = (5,30), size = (210,25))
dbnameLbl = wx.StaticText(win, pos = (5,5), size = (210,25),
                            label = "Enter Database Name")

lat = wx.TextCtrl(win, pos = (225,30), size = (80, 25))
latLbl = wx.StaticText (win, pos = (225,5), size = (210,25),
                            label = "Latitude")

lon = wx.TextCtrl(win, pos = (310,30), size = (80,25))
lonLbl = wx.StaticText(win, pos = (315,5), size = (215,25),
                           label = "Longitude")

message = wx.TextCtrl (win, pos = (5,95),size = (390,260),
                       style = wx.TE_MULTILINE | wx.HSCROLL)

#add submit button 
submitBtn = wx.Button(win, label = 'SUBMIT', pos = (160,60),
                   size = (80, 25))
#event handler
submitBtn.Bind(wx.EVT_BUTTON, LoadPoints)

win.Show()
app.MainLoop()
            
