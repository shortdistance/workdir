#-------------------------------------------------------------------------------
# Name:        Ä£¿é1
# Purpose:
#
# Author:      raychang
#
# Created:     29/09/2014
# Copyright:   (c) raychang 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import webbrowser

if __name__ == '__main__':
    url = 'http://www.python.org/'  # Open URL in a new tab, if a browser window is already open.
    webbrowser.open(url)

    con = webbrowser.get()
    print con
    con.open_new('http://www.baidu.com')
    #webbrowser.open_new_tab(url + 'doc/')   # Open URL in new window, raising the window if possible.
    #webbrowser.open_new(url)