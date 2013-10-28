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
        value = super(FloatValidator, self).to_python(value)
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
                if ext not in self.extensions:
                    raise twc.ValidationError('"%s" is not a valid extension :  only "%s" are allowed' % (ext, ', '.join([e for e in self.extensions])), self)


bs_file_field_js = twc.JSLink(
    modname=__name__,
    filename='static/bs.js',
    resources=[tw2j.jquery_js],
    location='headbottom')


class BsFileField(twf.InputField):
    template = "tw2.bs.templates.doublefilefield"
    type = 'text'
    placeholder = 'Enter url here'
    resources = [bs_file_field_js]

    @classmethod
    def post_define(cls):
        pass

    def prepare(self):
        super(BsFileField, self).prepare()
        self.safe_modify('resources')
        start_field = 'file'
        if isinstance(self.value, basestring):
            start_field = 'text'
        self.add_call(twc.js_function('bs_init_file_field')(self.compound_id, start_field))

    def _validate(self, value, state=None):
        v = super(BsFileField, self)._validate(value, state)
        return v


class BsTripleFileField(twf.TextField):
    template = "tw2.bs.templates.triplefilefield"
    type = 'text'
    placeholder = 'Enter url here'
    resources = [bs_file_field_js]
    options = []

    @classmethod
    def post_define(cls):
        pass

    def prepare(self):
        super(BsTripleFileField, self).prepare()
        self.safe_modify('resources')
        start_field = 'file'
        if isinstance(self.value, basestring):
            start_field = 'text'
        else:
            try:
                json.loads(self.value)
                start_field = 'select'
            except:
                pass
        self.add_call(twc.js_function('bs_init_triple_file_field')(self.compound_id, start_field))
        opts = []
        for opt in self.options:
            d = {}
            if len(opt) == 2:
                d['value'] = opt[0]
                d['display'] = opt[1]
            else:
                d['value'] = opt
                d['display'] = opt
            opts.append(d)
        self.safe_modify('attrs')
        self.attrs['opts'] = opts

    def _validate(self, value, state=None):
        return super(BsTripleFileField, self)._validate(value, state)


# class Multi(tw2.dynforms.GrowingGridLayout):
#     pass

class StripBlanksAndBSRadioButtons(twc.Validator):
    def any_content(self, val):
        if isinstance(val, (list, tuple)):
            for v in val:
                if self.any_content(v):
                    return True
            return False
        elif isinstance(val, dict):
            for k in val:
                if k == 'id':
                    continue
                if 'bs_group' in k:
                    continue
                if self.any_content(val[k]):
                    return True
            return False
        elif isinstance(val, FieldStorage):
            try:
                return bool(val.filename)
            except:
                return False
        else:
            return bool(val)

    def to_python(self, value, state=None):
        return [v for v in value if self.any_content(v)]


class BsMultipleValidator(object):
    def regroup(self, values):
        result = {}
        for value in values:
            for k, v in value.iteritems():
                if k not in result:
                    result[k] = []
                result[k].append(v)
        return result

    def validate(self, inst, value, state=None):
        if not isinstance(value, (list, tuple)):
            raise twc.ValidationError("Corrupted, %s must be a list." % value)
        removefirst = False
        if len(value) > 1:
            removefirst = True
            value = value[1:]
        for i, v in enumerate(value):
            k = i
            if removefirst:
                k += 1
            inst.children[k].value = v
        if removefirst:
            inst.children[0].value = ''
        any_errors = False
        data = []
        for i, v in enumerate(value):
            try:
                k = i
                if removefirst:
                    k += 1
                data.append(inst.children[k]._validate(v, data))
            except twc.validation.catch:
                data.append(twc.validation.Invalid)
                any_errors = True
        if removefirst:
            data.insert(0, '')
        if any_errors:
            raise twc.validation.ValidationError('childerror', inst.validator, inst)
        return data


class BsMultiple(twd.GrowingGridLayout):

    template = "tw2.bs.templates.multiple"

    def prepare(self):
        super(BsMultiple, self).prepare()

    def _validate(self, value, state=None):
        value = [v for v in value if not ('del.x' in v and 'del.y' in v)]
        value = StripBlanksAndBSRadioButtons().to_python(value)
        vv = StripBlanksAndBSRadioButtons().to_python(value)
        if not vv:
            vv = [None]
        value = BsMultipleValidator().validate(self, [None] + vv, state)
        value = BsMultipleValidator().regroup(value[1:])
        debug('Got value(s) "%s"' % value)
        return value
