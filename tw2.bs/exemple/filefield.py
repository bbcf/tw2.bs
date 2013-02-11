import tw2.core
import tw2.forms
import tw2.devtools
import tw2.bs


class Index(tw2.core.Page):
    title = 'tw2.bs FileField'
    template = 'genshi:./index.html'

    def fetch_data(self, req):
        print "Fetch data : %s" % req
        self.req = str(req)


class BsForm(tw2.forms.FormPage):
    resources = [tw2.core.CSSLink(filename='bs.css')]
    title = 'Movie'

    class child(tw2.forms.TableForm):
        bsfielfield = tw2.bs.BsFileField()

tw2.devtools.dev_server(port=8000)
