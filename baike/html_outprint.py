# coding:utf-8
# 输出

class HtmlOutputer(object):

    def __init__(self):
        self.datas = []

    def collect_data(self,data):
        if data is None:
           return
        self.datas.append(data)

    def output_html(self):
        fout = open('output.html','w')
        fout.write ("<html>")
        fout.write("<body>")
        fout.write("<table>")

       # ascii 编码 需要转utf-8  encode('utf-8')
        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td>%s</td>"  %data['url'])
            fout.write("<td>%s</td>" % data['title'].encode('utf-8'))
            fout.write("<td>%s</td>" % data['summary'].encode('utf-8'))
            fout.write("</tr>")

        fout.write("</html>")
        fout.write("</body>")
        fout.write("</table>")