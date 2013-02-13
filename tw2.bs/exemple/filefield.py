import tw2.core
import tw2.forms
import tw2.devtools
import tw2.bs
import tw2.jquery


class Index(tw2.core.Page):
    title = 'tw2.bs FileField'

    def fetch_data(self, req):
        print "Fetch data : %s" % req
        self.req = str(req)


bs_file_field_js = tw2.core.JSLink(
    modname=__name__,
    filename='static/bs.js',
    resources=[tw2.jquery.jquery_js],
    location='headbottom')


class BsForm(tw2.forms.FormPage):
    resources = [bs_file_field_js]
    title = 'BioScript Widgets'

    class child(tw2.forms.TableForm):
        one = tw2.bs.BsFileField(validator=tw2.bs.BsFileFieldValidator(required=True))
        two = tw2.bs.BsFileField(validator=tw2.bs.BsFileFieldValidator(required=True, extensions=['bed']))
        three = tw2.forms.TextField()

tw2.devtools.dev_server(port=8000)
