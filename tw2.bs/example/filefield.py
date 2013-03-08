import tw2.core
import tw2.forms
import tw2.devtools
import tw2.bs
import tw2.jquery
import tw2.dynforms


 # child = twd.HidingTableLayout()

 #    input_type = twd.HidingRadioButtonList(label='Input type',
 #                                           options=('Table', 'Signal'),
 #                                           mapping={'Table':  ['table'],
 #                                                    'Signal': ['signals', 'feature_type', 'assembly']},
 #                                           help_text='Select input type (Formatted table, or signal tracks)')
 #    table = twf.FileField(label='Table: ',
 #                          help_text='Select scores table',
 #                          validator=twf.FileValidator(required=True))
 #    feature_type = twd.HidingSingleSelectField(label='Feature type: ',
 #                                               options=ftypes, prompt_text=None,
 #                                               mapping={ftypes[-1][0]: ['features'],
 #                                                        1: ['upstream', 'downstream']},
 #                                               help_text='Choose a feature set or upload your own',
 #                                               validator=twc.Validator(required=True))
 #    class signals(twb.BsMultiple):
 #        files = twb.BsFileField(label='Signal: ',
 #                                help_text='Select signal file (.g. bedgraph)',
 #                                validator=twf.FileValidator(required=True))


class Index(tw2.forms.FormPage):
    title = 'test'

    class child(tw2.forms.TableForm):
        class child(tw2.dynforms.HidingTableLayout):
            input_type = tw2.dynforms.HidingRadioButtonList(label='',
                options=('File upload', 'Url'),
                mapping={'File upload': ['fupload'], 'Url': ['url']})
            fupload = tw2.bs.BsFileField(validator=tw2.bs.BsFileFieldValidator(required=True))
            url = tw2.forms.TextField()

        submit = tw2.forms.SubmitButton(id="submit", value="submit")


class Index2(tw2.forms.FormPage):
    title = 'test'

    class child(tw2.forms.TableForm):
        class child(tw2.dynforms.HidingTableLayout):
            input_type = tw2.dynforms.HidingRadioButtonList(label='',
                options=('File upload', 'Url'),
                mapping={'File upload': ['inputs'], 'Url': ['url']})
            class inputs(tw2.bs.BsMultiple):
                files = tw2.bs.BsFileField(validator=tw2.bs.BsFileFieldValidator(required=True))
            url = tw2.forms.TextField()

        submit = tw2.forms.SubmitButton(id="submit", value="submit")


class Double(tw2.forms.FormPage):
    title = 'BioScript Widgets'

    class child(tw2.forms.TableForm):
        one = tw2.bs.BsFileField(validator=tw2.bs.BsFileFieldValidator(required=True))


class Triple(tw2.forms.FormPage):
    title = 'BioScript Widgets'

    class child(tw2.forms.TableForm):
        one = tw2.bs.BsTripleFileField(validator=tw2.bs.BsFileFieldValidator(required=True), options=[('one', '{"p": "http://one", "d": "one"}'), ('two', '{"p": "http://two", "d": "two"}'), ('not valid', '{"p": "cdcsd", "d": "two"}')])


class Mult(tw2.forms.FormPage):
    title = 'BioScript multiple widget'

    class child(tw2.forms.TableForm):
        class inputs(tw2.bs.BsMultiple):
            files = tw2.bs.BsFileField(validator=tw2.bs.BsFileFieldValidator(required=True))


class Test(tw2.forms.FormPage):
    title = 'BioScript multiple widget'

    class child(tw2.forms.TableForm):
        class child(tw2.dynforms.GrowingGridLayout):
            toto = tw2.forms.TextField(validator=tw2.core.Validator(required=True))


class Mult3(tw2.forms.FormPage):
    title = 'BioScript multiple widget'

    class child(tw2.forms.TableForm):
        class multi(tw2.bs.BsMultiple):
            test = tw2.bs.BsTripleFileField(options=['one', 'two'])

tw2.devtools.dev_server(port=8000)
