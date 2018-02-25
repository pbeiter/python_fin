### from https://gist.githubusercontent.com/jackparmer/eed4fa204650f03fe8a4/raw/de4af8d70c77ff3ffc418ea2365a2622df61286e/reports.py
import os
import webbrowser

def html_gen(loc, name1, name2, name3, name4, name5):
    
    html_string = '''

    <html>

        <head>
        <title>Portfolio analysis</title>
        </head>
        <body>
            <h1>Portfolio performance</h1>

            <!-- *** Section 1 *** --->
            <h2>Section 1: Individual stocks</h2>
            
            <h2>Assets performance</h2>
            <img src="C:/Users/pbeiter/Desktop/Python finance/fig/'''+name1+'''.png"/ alt="description">
            <img src="C:/Users/pbeiter/Desktop/Python finance/fig/'''+name2+'''.png"/ alt="description">
            <h2>Assets correlation matrix</h2>
            <img src="C:/Users/pbeiter/Desktop/Python finance/fig/'''+name3+'''.png"/ alt="description">
            <h2>Assets distribution</h2>
            <img src="C:/Users/pbeiter/Desktop/Python finance/fig/'''+name4+'''.png"/ alt="description">
            <h2>Assets boxplot</h2>
            <img src="C:/Users/pbeiter/Desktop/Python finance/fig/'''+name5+'''.png"/ alt="description">
                     
            <!-- *** Section 2 *** --->
            <h2>Section 2: Title 2</h2>
            
        </body>
    </html>'''

    f = open(loc,'w')
    f.write(html_string)
    f.close()

    url = 'file://' + os.path.realpath(loc)
    #url = 'file:{}'.format(pathname2url(os.path.abspath('1.html')))

    new_tab=2
    webbrowser.open(url,new=new_tab)


    #<img src="C:/Users/pbeiter/Desktop/Python finance/fig/.png"/ alt="description">