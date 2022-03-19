from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
import signal

import webbrowser
webbrowser.open('C:/github/Call_Python/button_test/button_test.html')

dbname = '../database.db'
    
def diary_world(request):
    in_data=request.params
    row=in_data["row"]
    cols=in_data["cols"]
    before_r=in_data["before_r"]
    after_r=in_data["after_r"]
    before_g=in_data["before_g"]
    after_g=in_data["after_g"]
    before_b=in_data["before_b"]
    after_b=in_data["after_b"]

    f = open(r"color_code.txt", "r")

    getdata=""
    
    
    
    getdata=getdata+"<style>.example2{ border: none;}</style>"

    getdata=getdata+"<input type=\"radio\" id=\"xxxx\" name=\"fruit\" value=\"copy\" checked=\"checked\" onchange=\"func1()\">"
    getdata=getdata+"<label for=\"xxxx\">コピー</label>"

    getdata=getdata+"<input type=\"radio\" id=\"xxxx\" name=\"fruit\" value=\"paste\" onchange=\"func1()\">"
    getdata=getdata+"<label for=\"xxxx\">貼り付け</label>"

    getdata=getdata+"<input  type=\"button\" value=\"コピーした色\" id=999999 ></input><br>"

    getdata=getdata+"<script language=\"javascript\" type=\"text/javascript\">"
    getdata=getdata+"function func1() {"
    getdata=getdata+"var fruits = document.getElementsByName(\"fruit\");for(var i = 0; i < fruits.length; i++){if(fruits[i].checked) {color=fruits[i].value; }}}"
    getdata=getdata+"func1();"
    getdata=getdata+"</script>"

    count_max=int(cols)*int(row)

    for count in range(count_max):
        rgb=f.readline()
        #print(rgb[:3])
        #print(rgb[3:5])
        #print(rgb[5:])
        r=rgb[:3]
        g=rgb[3:5]
        b=rgb[5:]

        tblr=r.maketrans(before_r, after_r)  
        r = r.translate(tblr)

        tblg=g.maketrans(before_g, after_g)  
        g = g.translate(tblg)

        tblb=b.maketrans(before_b, after_b)  
        b = b.translate(tblb)

        concat_rgb = r+g+b
        #print(rgb)
        getdata=getdata+"<input onclick=\"buttonClick(this.id)\"  type=\"button\" value=\" \" id="    
        getdata=getdata+str(count)    
        getdata=getdata+" style=\"background-color:"+concat_rgb+";\" class=\"example2\" ></input>"    
        if((count%int(cols))==(int(cols)-1)):
            getdata=getdata+"<br>"    


        getdata=getdata+ "<script>"


        getdata=getdata+ "function buttonClick(count){"
        getdata=getdata+ "if (color==\"copy\"){"
        getdata=getdata+ "color_copy=document.getElementById(count).style.backgroundColor;"
        getdata=getdata+ "document.getElementById(999999).style.backgroundColor = color_copy;"
        getdata=getdata+ "}else if (color==\"paste\") {"      

        getdata=getdata+ "document.getElementById(count).style.backgroundColor = color_copy;"

        getdata=getdata+ "}else{";      
        getdata=getdata+ "document.getElementById(count).style.backgroundColor = color;"
        getdata=getdata+ "}"

        getdata=getdata+ "}"        
        getdata=getdata+ "</script>"












                        
    return Response(str(getdata))

def from_rgb_to_colorcode(rgb):
    return "#%02x%02x%02x" % rgb

    #実行処理  python サーバーを立てています
if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    with Configurator() as config:
        config.add_route('diary', '/')
        config.add_view(diary_world, route_name='diary',renderer="jsonp")
        app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 6543, app)
    server.serve_forever()
