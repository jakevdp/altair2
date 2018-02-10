# The contents of this file are automatically generated
# at time 2018-02-09 12:32:46

from altair.schema import wrapper
from altair.utils import parse_shorthand


class Color(wrapper.MarkPropFieldDefWithCondition):
    """Color channel"""
    def __init__(self, field, **kwargs):
        kwds = parse_shorthand(field)
        kwds.update(kwargs)
        super(Color, self).__init__(**kwds)


class ColorValue(wrapper.MarkPropValueDefWithCondition):
    """Color channel"""
    def __init__(self, value, *args, **kwargs):
        super(ColorValue, self).__init__(value=value, *args, **kwargs)


class Column(wrapper.FacetFieldDef):
    """Column channel"""
    def __init__(self, field, **kwargs):
        kwds = parse_shorthand(field)
        kwds.update(kwargs)
        super(Column, self).__init__(**kwds)


class Detail(wrapper.FieldDef):
    """Detail channel"""
    def __init__(self, field, **kwargs):
        kwds = parse_shorthand(field)
        kwds.update(kwargs)
        super(Detail, self).__init__(**kwds)


class Href(wrapper.FieldDefWithCondition):
    """Href channel"""
    def __init__(self, field, **kwargs):
        kwds = parse_shorthand(field)
        kwds.update(kwargs)
        super(Href, self).__init__(**kwds)


class HrefValue(wrapper.ValueDefWithCondition):
    """Href channel"""
    def __init__(self, value, *args, **kwargs):
        super(HrefValue, self).__init__(value=value, *args, **kwargs)


class Opacity(wrapper.MarkPropFieldDefWithCondition):
    """Opacity channel"""
    def __init__(self, field, **kwargs):
        kwds = parse_shorthand(field)
        kwds.update(kwargs)
        super(Opacity, self).__init__(**kwds)


class OpacityValue(wrapper.MarkPropValueDefWithCondition):
    """Opacity channel"""
    def __init__(self, value, *args, **kwargs):
        super(OpacityValue, self).__init__(value=value, *args, **kwargs)


class Order(wrapper.OrderFieldDef):
    """Order channel"""
    def __init__(self, field, **kwargs):
        kwds = parse_shorthand(field)
        kwds.update(kwargs)
        super(Order, self).__init__(**kwds)


class Row(wrapper.FacetFieldDef):
    """Row channel"""
    def __init__(self, field, **kwargs):
        kwds = parse_shorthand(field)
        kwds.update(kwargs)
        super(Row, self).__init__(**kwds)


class Shape(wrapper.MarkPropFieldDefWithCondition):
    """Shape channel"""
    def __init__(self, field, **kwargs):
        kwds = parse_shorthand(field)
        kwds.update(kwargs)
        super(Shape, self).__init__(**kwds)


class ShapeValue(wrapper.MarkPropValueDefWithCondition):
    """Shape channel"""
    def __init__(self, value, *args, **kwargs):
        super(ShapeValue, self).__init__(value=value, *args, **kwargs)


class Size(wrapper.MarkPropFieldDefWithCondition):
    """Size channel"""
    def __init__(self, field, **kwargs):
        kwds = parse_shorthand(field)
        kwds.update(kwargs)
        super(Size, self).__init__(**kwds)


class SizeValue(wrapper.MarkPropValueDefWithCondition):
    """Size channel"""
    def __init__(self, value, *args, **kwargs):
        super(SizeValue, self).__init__(value=value, *args, **kwargs)


class Text(wrapper.TextFieldDefWithCondition):
    """Text channel"""
    def __init__(self, field, **kwargs):
        kwds = parse_shorthand(field)
        kwds.update(kwargs)
        super(Text, self).__init__(**kwds)


class TextValue(wrapper.TextValueDefWithCondition):
    """Text channel"""
    def __init__(self, value, *args, **kwargs):
        super(TextValue, self).__init__(value=value, *args, **kwargs)


class Tooltip(wrapper.TextFieldDefWithCondition):
    """Tooltip channel"""
    def __init__(self, field, **kwargs):
        kwds = parse_shorthand(field)
        kwds.update(kwargs)
        super(Tooltip, self).__init__(**kwds)


class TooltipValue(wrapper.TextValueDefWithCondition):
    """Tooltip channel"""
    def __init__(self, value, *args, **kwargs):
        super(TooltipValue, self).__init__(value=value, *args, **kwargs)


class X(wrapper.PositionFieldDef):
    """X channel"""
    def __init__(self, field, **kwargs):
        kwds = parse_shorthand(field)
        kwds.update(kwargs)
        super(X, self).__init__(**kwds)


class XValue(wrapper.ValueDef):
    """X channel"""
    def __init__(self, value, *args, **kwargs):
        super(XValue, self).__init__(value=value, *args, **kwargs)


class X2(wrapper.FieldDef):
    """X2 channel"""
    def __init__(self, field, **kwargs):
        kwds = parse_shorthand(field)
        kwds.update(kwargs)
        super(X2, self).__init__(**kwds)


class X2Value(wrapper.ValueDef):
    """X2 channel"""
    def __init__(self, value, *args, **kwargs):
        super(X2Value, self).__init__(value=value, *args, **kwargs)


class Y(wrapper.PositionFieldDef):
    """Y channel"""
    def __init__(self, field, **kwargs):
        kwds = parse_shorthand(field)
        kwds.update(kwargs)
        super(Y, self).__init__(**kwds)


class YValue(wrapper.ValueDef):
    """Y channel"""
    def __init__(self, value, *args, **kwargs):
        super(YValue, self).__init__(value=value, *args, **kwargs)


class Y2(wrapper.FieldDef):
    """Y2 channel"""
    def __init__(self, field, **kwargs):
        kwds = parse_shorthand(field)
        kwds.update(kwargs)
        super(Y2, self).__init__(**kwds)


class Y2Value(wrapper.ValueDef):
    """Y2 channel"""
    def __init__(self, value, *args, **kwargs):
        super(Y2Value, self).__init__(value=value, *args, **kwargs)
