import tw2.core as twc
import tw2.forms as twf
import tw2.dynforms as twd
import tw2.jquery as twj
from cgi import FieldStorage
import os, json

class FloatValidator(twc.RangeValidator):
    """
    Confirm the value is a float. This is derived from :class:`RangeValidator`
    so `min` and `max` can be specified.
    """
    msgs = {'notfloat': 'Must be a float'}

    def to_python(self, value, state=None):
        value = twc.RangeValidator.to_python(self,value,state)
        try:
            if value is None or str(value) == '':
                return None
            else:
                return float(value)
        except ValueError:
            raise twc.ValidationError('notfloat', self)

    def validate_python(self, value, state=None):
        if self.required and value is None:
            raise twc.ValidationError('required', self)
        if value is not None:
            if self.min is not None and float(value) < float(self.min):
                raise twc.ValidationError('toosmall', self)
            if self.max is not None and float(value) > float(self.max):
                raise twc.ValidationError('toobig', self)

    def from_python(self, value):
        if value is None:
            return None
        else:
            return str(value)


class BsFileFieldValidator(twc.Validator):
    """
    Validate the file field if there is one or validate the url.
    """
    msgs = {'required': 'You must enter a value.'}
    extensions = None

    def to_python(self, value, state=None):
        if  value is None or value == '' or \
                (isinstance(value, (list, tuple, dict)) and not value):
            if self.required:
                raise twc.ValidationError('required', self)
        else:
            value = str(value).strip('"'+"'")
        if self.strip and isinstance(value, basestring):
            value = value.strip()
        self._validate_python(value, state)
        return value

    def _validate_python(self, value, state=None):
        if isinstance(value, basestring):
            if not value.startswith('FieldStorage('):
                try:
                    value = json.loads(value)['p']
                except:
                    pass
                if value and not value.startswith(("http://","https://","ftp://")):
                    raise twc.ValidationError('"%s" is not a valid URL.' %value, self)
        elif isinstance(value, FieldStorage):
            if self.required and not getattr(value, 'filename', None):
                raise twc.ValidationError('required', self)
            if self.extensions is not None:
                ext = os.path.splitext(value.filename)[-1][1:]
                errmsg = (ext, ', '.join([e for e in self.extensions]))
                if ext not in self.extensions:
                    raise twc.ValidationError('"%s" is not a valid extension: only "%s" are allowed' %errmsg, self)


class BsFileField(twf.InputField):
    template = "tw2.bs.templates.doublefilefield"
    type = 'text'
    placeholder = 'Enter url here'
    resources = [twc.JSLink(
            modname=__name__,
            filename='static/bs.js',
            resources=[twj.jquery_js],
            location='headbottom')]
    bsfield = 'bs_init_file_field'

    @classmethod
    def post_define(cls):
        pass

    def _start_field(self):
        if isinstance(self.value, basestring):
            return 'text'
        return 'file'

    def _read_opts(self):
        pass

    def prepare(self):
        twf.InputField.prepare(self)
        self.safe_modify('resources')
        self.add_call(twc.js_function(self.bsfield)(self.compound_id, self._start_field()))
        self._read_opts()

class BsTripleFileField(BsFileField):
    template = "tw2.bs.templates.triplefilefield"
    bsfield = 'bs_init_triple_file_field'
    options = []

    def _start_field(self):
        start_field = BsFileField._start_field(self)
        if start_field == 'file':
            try:
                json.loads(self.value)
                return 'select'
            except:
                pass
        return start_field

    def _read_opts(self):
        self.safe_modify('attrs')
        self.attrs['opts'] = [{'value':   opt[0] if isinstance(opt,(list,tuple)) else opt,
                               'display': opt[1] if isinstance(opt,(list,tuple)) else opt}
                              for opt in self.options]


class BsMultiple(twd.GrowingGridLayout):

    template = "tw2.bs.templates.multiple"

    def clear_content(self,val):
        if isinstance(val, (list, tuple)):
            return [self.clear_content(v) for v in val if self.clear_content(v)]
        elif isinstance(val, dict):
            res = dict((k,v) for k,v in val.iteritems()
                       if k != 'id' and 'bs_group' not in k and self.clear_content(v))
            if res: 
                res.update(dict((k,v) for k,v in val.iteritems() if k == 'id' or 'bs_group' in k))
                return res
        elif isinstance(val, FieldStorage) and val.filename:
            return val
        elif val:
            return val


    def _validate(self, value, state=None):
        value = self.clear_content([v for v in value 
                                    if not ('del.x' in v and 'del.y' in v)])
        self.children[0].value = ''
        for k,v in enumerate(value):
            self.children[k+1].value = v 
            self.children[k+1]._validate(v,state)
        result = {}
        for val in value:
            for k, v in val.iteritems():
                if k not in result:
                    result[k] = []
                result[k].append(v)
        return result
