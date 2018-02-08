from . import wrapper


class Color(wrapper.MarkPropFieldDefWithCondition):
    pass


class ColorValue(wrapper.MarkPropValueDefWithCondition):
    pass


class Column(wrapper.FacetFieldDef):
    pass


class Detail(wrapper.FieldDef):
    pass


class Href(wrapper.FieldDefWithCondition):
    pass


class Href(wrapper.ValueDefWithCondition):
    pass


class Opacity(wrapper.MarkPropFieldDefWithCondition):
    pass


class OpacityValue(wrapper.MarkPropValueDefWithCondition):
    pass


class Order(wrapper.OrderFieldDef):
    pass


class Row(wrapper.FacetFieldDef):
    pass


class Shape(wrapper.MarkPropFieldDefWithCondition):
    pass


class ShapeValue(wrapper.MarkPropValueDefWithCondition):
    pass


class Size(wrapper.MarkPropFieldDefWithCondition):
    pass


class SizeValue(wrapper.MarkPropValueDefWithCondition):
    pass


class Text(wrapper.TextFieldDefWithCondition):
    pass


class TextValue(wrapper.TextValueDefWithCondition):
    pass


class Tooltip(wrapper.TextFieldDefWithCondition):
    pass


class TooltipValue(wrapper.TextValueDefWithCondition):
    pass


class X(wrapper.PositionFieldDef):
    pass


class XValue(wrapper.ValueDef):
    pass


class X2(wrapper.FieldDef):
    pass


class X2Value(wrapper.ValueDef):
    pass


class Y(wrapper.PositionFieldDef):
    pass


class YValue(wrapper.ValueDef):
    pass


class Y2(wrapper.FieldDef):
    pass


class Y2Value(wrapper.ValueDef):
    pass
