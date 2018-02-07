# The contents of this file are automatically generated
# at time 2018-02-06 15:24:21

from altair.schema.base import SchemaBase, Undefined
from altair.schema.loader import load_schema


class Root(SchemaBase):
    """A Root json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = load_schema()
    def __init__(self, *args, **kwds):
        super(Root, self).__init__(*args, **kwds)


class Aggregate(SchemaBase):
    """A Aggregate json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/Aggregate', 'definitions': Root._json_schema['definitions']}
    def __init__(self, *args):
        super(Aggregate, self).__init__(*args)


class AggregateOp(SchemaBase):
    """A AggregateOp json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/AggregateOp', 'definitions': Root._json_schema['definitions']}
    def __init__(self, *args):
        super(AggregateOp, self).__init__(*args)


class AggregateTransform(SchemaBase):
    """A AggregateTransform json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/AggregateTransform', 'definitions': Root._json_schema['definitions']}
    def __init__(self, aggregate, groupby=Undefined):
        super(AggregateTransform, self).__init__(aggregate=aggregate, groupby=groupby)


class AggregatedFieldDef(SchemaBase):
    """A AggregatedFieldDef json schema wrapper"""
    _valid_attr_map = {'as': 'as_'}
    _json_schema = {'$ref': '#/definitions/AggregatedFieldDef', 'definitions': Root._json_schema['definitions']}
    def __init__(self, as_, field, op):
        super(AggregatedFieldDef, self).__init__(as_=as_, field=field, op=op)


class Anchor(SchemaBase):
    """A Anchor json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/Anchor', 'definitions': Root._json_schema['definitions']}
    def __init__(self, *args):
        super(Anchor, self).__init__(*args)


class AnyMark(SchemaBase):
    """A AnyMark json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/AnyMark', 'definitions': Root._json_schema['definitions']}
    def __init__(self, *args, **kwds):
        super(AnyMark, self).__init__(*args, **kwds)


class AutoSizeParams(SchemaBase):
    """A AutoSizeParams json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/AutoSizeParams', 'definitions': Root._json_schema['definitions']}
    def __init__(self, contains=Undefined, resize=Undefined, type=Undefined):
        super(AutoSizeParams, self).__init__(contains=contains, resize=resize, type=type)


class AutosizeType(SchemaBase):
    """A AutosizeType json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/AutosizeType', 'definitions': Root._json_schema['definitions']}
    def __init__(self, *args):
        super(AutosizeType, self).__init__(*args)


class Axis(SchemaBase):
    """A Axis json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/Axis', 'definitions': Root._json_schema['definitions']}
    def __init__(self, domain=Undefined, format=Undefined, grid=Undefined, labelAngle=Undefined, labelBound=Undefined, labelFlush=Undefined, labelOverlap=Undefined, labelPadding=Undefined, labels=Undefined, maxExtent=Undefined, minExtent=Undefined, offset=Undefined, orient=Undefined, position=Undefined, tickCount=Undefined, tickSize=Undefined, ticks=Undefined, title=Undefined, titleMaxLength=Undefined, titlePadding=Undefined, values=Undefined, zindex=Undefined):
        super(Axis, self).__init__(domain=domain, format=format, grid=grid, labelAngle=labelAngle, labelBound=labelBound, labelFlush=labelFlush, labelOverlap=labelOverlap, labelPadding=labelPadding, labels=labels, maxExtent=maxExtent, minExtent=minExtent, offset=offset, orient=orient, position=position, tickCount=tickCount, tickSize=tickSize, ticks=ticks, title=title, titleMaxLength=titleMaxLength, titlePadding=titlePadding, values=values, zindex=zindex)


class AxisConfig(SchemaBase):
    """A AxisConfig json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/AxisConfig', 'definitions': Root._json_schema['definitions']}
    def __init__(self, bandPosition=Undefined, domain=Undefined, domainColor=Undefined, domainWidth=Undefined, grid=Undefined, gridColor=Undefined, gridDash=Undefined, gridOpacity=Undefined, gridWidth=Undefined, labelAngle=Undefined, labelBound=Undefined, labelColor=Undefined, labelFlush=Undefined, labelFont=Undefined, labelFontSize=Undefined, labelLimit=Undefined, labelOverlap=Undefined, labelPadding=Undefined, labels=Undefined, maxExtent=Undefined, minExtent=Undefined, shortTimeLabels=Undefined, tickColor=Undefined, tickRound=Undefined, tickSize=Undefined, tickWidth=Undefined, ticks=Undefined, titleAlign=Undefined, titleAngle=Undefined, titleBaseline=Undefined, titleColor=Undefined, titleFont=Undefined, titleFontSize=Undefined, titleFontWeight=Undefined, titleLimit=Undefined, titleMaxLength=Undefined, titlePadding=Undefined, titleX=Undefined, titleY=Undefined):
        super(AxisConfig, self).__init__(bandPosition=bandPosition, domain=domain, domainColor=domainColor, domainWidth=domainWidth, grid=grid, gridColor=gridColor, gridDash=gridDash, gridOpacity=gridOpacity, gridWidth=gridWidth, labelAngle=labelAngle, labelBound=labelBound, labelColor=labelColor, labelFlush=labelFlush, labelFont=labelFont, labelFontSize=labelFontSize, labelLimit=labelLimit, labelOverlap=labelOverlap, labelPadding=labelPadding, labels=labels, maxExtent=maxExtent, minExtent=minExtent, shortTimeLabels=shortTimeLabels, tickColor=tickColor, tickRound=tickRound, tickSize=tickSize, tickWidth=tickWidth, ticks=ticks, titleAlign=titleAlign, titleAngle=titleAngle, titleBaseline=titleBaseline, titleColor=titleColor, titleFont=titleFont, titleFontSize=titleFontSize, titleFontWeight=titleFontWeight, titleLimit=titleLimit, titleMaxLength=titleMaxLength, titlePadding=titlePadding, titleX=titleX, titleY=titleY)


class AxisOrient(SchemaBase):
    """A AxisOrient json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/AxisOrient', 'definitions': Root._json_schema['definitions']}
    def __init__(self, *args):
        super(AxisOrient, self).__init__(*args)


class AxisResolveMap(SchemaBase):
    """A AxisResolveMap json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/AxisResolveMap', 'definitions': Root._json_schema['definitions']}
    def __init__(self, x=Undefined, y=Undefined):
        super(AxisResolveMap, self).__init__(x=x, y=y)


class BarConfig(SchemaBase):
    """A BarConfig json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/BarConfig', 'definitions': Root._json_schema['definitions']}
    def __init__(self, align=Undefined, angle=Undefined, baseline=Undefined, binSpacing=Undefined, color=Undefined, continuousBandSize=Undefined, cursor=Undefined, discreteBandSize=Undefined, dx=Undefined, dy=Undefined, fill=Undefined, fillOpacity=Undefined, filled=Undefined, font=Undefined, fontSize=Undefined, fontStyle=Undefined, fontWeight=Undefined, href=Undefined, interpolate=Undefined, limit=Undefined, opacity=Undefined, orient=Undefined, radius=Undefined, shape=Undefined, size=Undefined, stroke=Undefined, strokeDash=Undefined, strokeDashOffset=Undefined, strokeOpacity=Undefined, strokeWidth=Undefined, tension=Undefined, text=Undefined, theta=Undefined):
        super(BarConfig, self).__init__(align=align, angle=angle, baseline=baseline, binSpacing=binSpacing, color=color, continuousBandSize=continuousBandSize, cursor=cursor, discreteBandSize=discreteBandSize, dx=dx, dy=dy, fill=fill, fillOpacity=fillOpacity, filled=filled, font=font, fontSize=fontSize, fontStyle=fontStyle, fontWeight=fontWeight, href=href, interpolate=interpolate, limit=limit, opacity=opacity, orient=orient, radius=radius, shape=shape, size=size, stroke=stroke, strokeDash=strokeDash, strokeDashOffset=strokeDashOffset, strokeOpacity=strokeOpacity, strokeWidth=strokeWidth, tension=tension, text=text, theta=theta)


class BasicType(SchemaBase):
    """A BasicType json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/BasicType', 'definitions': Root._json_schema['definitions']}
    def __init__(self, *args):
        super(BasicType, self).__init__(*args)


class BinParams(SchemaBase):
    """A BinParams json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/BinParams', 'definitions': Root._json_schema['definitions']}
    def __init__(self, base=Undefined, divide=Undefined, extent=Undefined, maxbins=Undefined, minstep=Undefined, nice=Undefined, step=Undefined, steps=Undefined):
        super(BinParams, self).__init__(base=base, divide=divide, extent=extent, maxbins=maxbins, minstep=minstep, nice=nice, step=step, steps=steps)


class BinTransform(SchemaBase):
    """A BinTransform json schema wrapper"""
    _valid_attr_map = {'as': 'as_'}
    _json_schema = {'$ref': '#/definitions/BinTransform', 'definitions': Root._json_schema['definitions']}
    def __init__(self, as_, bin, field):
        super(BinTransform, self).__init__(as_=as_, bin=bin, field=field)


class BrushConfig(SchemaBase):
    """A BrushConfig json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/BrushConfig', 'definitions': Root._json_schema['definitions']}
    def __init__(self, fill=Undefined, fillOpacity=Undefined, stroke=Undefined, strokeDash=Undefined, strokeDashOffset=Undefined, strokeOpacity=Undefined, strokeWidth=Undefined):
        super(BrushConfig, self).__init__(fill=fill, fillOpacity=fillOpacity, stroke=stroke, strokeDash=strokeDash, strokeDashOffset=strokeDashOffset, strokeOpacity=strokeOpacity, strokeWidth=strokeWidth)


class CalculateTransform(SchemaBase):
    """A CalculateTransform json schema wrapper"""
    _valid_attr_map = {'as': 'as_'}
    _json_schema = {'$ref': '#/definitions/CalculateTransform', 'definitions': Root._json_schema['definitions']}
    def __init__(self, as_, calculate):
        super(CalculateTransform, self).__init__(as_=as_, calculate=calculate)


class CompositeUnitSpec(SchemaBase):
    """A CompositeUnitSpec json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/CompositeUnitSpec', 'definitions': Root._json_schema['definitions']}
    def __init__(self, encoding, mark, data=Undefined, description=Undefined, height=Undefined, name=Undefined, projection=Undefined, selection=Undefined, title=Undefined, transform=Undefined, width=Undefined):
        super(CompositeUnitSpec, self).__init__(encoding=encoding, mark=mark, data=data, description=description, height=height, name=name, projection=projection, selection=selection, title=title, transform=transform, width=width)


class ConditionalFieldDef(SchemaBase):
    """A ConditionalFieldDef json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/Conditional<FieldDef>', 'definitions': Root._json_schema['definitions']}
    def __init__(self, *args, **kwds):
        super(ConditionalFieldDef, self).__init__(*args, **kwds)


class ConditionalMarkPropFieldDef(SchemaBase):
    """A ConditionalMarkPropFieldDef json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/Conditional<MarkPropFieldDef>', 'definitions': Root._json_schema['definitions']}
    def __init__(self, *args, **kwds):
        super(ConditionalMarkPropFieldDef, self).__init__(*args, **kwds)


class ConditionalTextFieldDef(SchemaBase):
    """A ConditionalTextFieldDef json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/Conditional<TextFieldDef>', 'definitions': Root._json_schema['definitions']}
    def __init__(self, *args, **kwds):
        super(ConditionalTextFieldDef, self).__init__(*args, **kwds)


class ConditionalValueDef(SchemaBase):
    """A ConditionalValueDef json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/Conditional<ValueDef>', 'definitions': Root._json_schema['definitions']}
    def __init__(self, *args, **kwds):
        super(ConditionalValueDef, self).__init__(*args, **kwds)


class ConditionalPredicateFieldDef(SchemaBase):
    """A ConditionalPredicateFieldDef json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/ConditionalPredicate<FieldDef>', 'definitions': Root._json_schema['definitions']}
    def __init__(self, test, type, aggregate=Undefined, bin=Undefined, field=Undefined, timeUnit=Undefined):
        super(ConditionalPredicateFieldDef, self).__init__(test=test, type=type, aggregate=aggregate, bin=bin, field=field, timeUnit=timeUnit)


class ConditionalPredicateMarkPropFieldDef(SchemaBase):
    """A ConditionalPredicateMarkPropFieldDef json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/ConditionalPredicate<MarkPropFieldDef>', 'definitions': Root._json_schema['definitions']}
    def __init__(self, test, type, aggregate=Undefined, bin=Undefined, field=Undefined, legend=Undefined, scale=Undefined, sort=Undefined, timeUnit=Undefined):
        super(ConditionalPredicateMarkPropFieldDef, self).__init__(test=test, type=type, aggregate=aggregate, bin=bin, field=field, legend=legend, scale=scale, sort=sort, timeUnit=timeUnit)


class ConditionalPredicateTextFieldDef(SchemaBase):
    """A ConditionalPredicateTextFieldDef json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/ConditionalPredicate<TextFieldDef>', 'definitions': Root._json_schema['definitions']}
    def __init__(self, test, type, aggregate=Undefined, bin=Undefined, field=Undefined, format=Undefined, timeUnit=Undefined):
        super(ConditionalPredicateTextFieldDef, self).__init__(test=test, type=type, aggregate=aggregate, bin=bin, field=field, format=format, timeUnit=timeUnit)


class ConditionalPredicateValueDef(SchemaBase):
    """A ConditionalPredicateValueDef json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/ConditionalPredicate<ValueDef>', 'definitions': Root._json_schema['definitions']}
    def __init__(self, test, value):
        super(ConditionalPredicateValueDef, self).__init__(test=test, value=value)


class ConditionalSelectionFieldDef(SchemaBase):
    """A ConditionalSelectionFieldDef json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/ConditionalSelection<FieldDef>', 'definitions': Root._json_schema['definitions']}
    def __init__(self, selection, type, aggregate=Undefined, bin=Undefined, field=Undefined, timeUnit=Undefined):
        super(ConditionalSelectionFieldDef, self).__init__(selection=selection, type=type, aggregate=aggregate, bin=bin, field=field, timeUnit=timeUnit)


class ConditionalSelectionMarkPropFieldDef(SchemaBase):
    """A ConditionalSelectionMarkPropFieldDef json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/ConditionalSelection<MarkPropFieldDef>', 'definitions': Root._json_schema['definitions']}
    def __init__(self, selection, type, aggregate=Undefined, bin=Undefined, field=Undefined, legend=Undefined, scale=Undefined, sort=Undefined, timeUnit=Undefined):
        super(ConditionalSelectionMarkPropFieldDef, self).__init__(selection=selection, type=type, aggregate=aggregate, bin=bin, field=field, legend=legend, scale=scale, sort=sort, timeUnit=timeUnit)


class ConditionalSelectionTextFieldDef(SchemaBase):
    """A ConditionalSelectionTextFieldDef json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/ConditionalSelection<TextFieldDef>', 'definitions': Root._json_schema['definitions']}
    def __init__(self, selection, type, aggregate=Undefined, bin=Undefined, field=Undefined, format=Undefined, timeUnit=Undefined):
        super(ConditionalSelectionTextFieldDef, self).__init__(selection=selection, type=type, aggregate=aggregate, bin=bin, field=field, format=format, timeUnit=timeUnit)


class ConditionalSelectionValueDef(SchemaBase):
    """A ConditionalSelectionValueDef json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/ConditionalSelection<ValueDef>', 'definitions': Root._json_schema['definitions']}
    def __init__(self, selection, value):
        super(ConditionalSelectionValueDef, self).__init__(selection=selection, value=value)


class Config(SchemaBase):
    """A Config json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/Config', 'definitions': Root._json_schema['definitions']}
    def __init__(self, area=Undefined, autosize=Undefined, axis=Undefined, axisBand=Undefined, axisBottom=Undefined, axisLeft=Undefined, axisRight=Undefined, axisTop=Undefined, axisX=Undefined, axisY=Undefined, background=Undefined, bar=Undefined, circle=Undefined, countTitle=Undefined, fieldTitle=Undefined, geoshape=Undefined, invalidValues=Undefined, legend=Undefined, line=Undefined, mark=Undefined, numberFormat=Undefined, padding=Undefined, point=Undefined, projection=Undefined, range=Undefined, rect=Undefined, rule=Undefined, scale=Undefined, selection=Undefined, square=Undefined, stack=Undefined, style=Undefined, text=Undefined, tick=Undefined, timeFormat=Undefined, title=Undefined, view=Undefined):
        super(Config, self).__init__(area=area, autosize=autosize, axis=axis, axisBand=axisBand, axisBottom=axisBottom, axisLeft=axisLeft, axisRight=axisRight, axisTop=axisTop, axisX=axisX, axisY=axisY, background=background, bar=bar, circle=circle, countTitle=countTitle, fieldTitle=fieldTitle, geoshape=geoshape, invalidValues=invalidValues, legend=legend, line=line, mark=mark, numberFormat=numberFormat, padding=padding, point=point, projection=projection, range=range, rect=rect, rule=rule, scale=scale, selection=selection, square=square, stack=stack, style=style, text=text, tick=tick, timeFormat=timeFormat, title=title, view=view)


class CsvDataFormat(SchemaBase):
    """A CsvDataFormat json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/CsvDataFormat', 'definitions': Root._json_schema['definitions']}
    def __init__(self, parse=Undefined, type=Undefined):
        super(CsvDataFormat, self).__init__(parse=parse, type=type)


class Data(SchemaBase):
    """A Data json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/Data', 'definitions': Root._json_schema['definitions']}
    def __init__(self, *args, **kwds):
        super(Data, self).__init__(*args, **kwds)


class DataFormat(SchemaBase):
    """A DataFormat json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/DataFormat', 'definitions': Root._json_schema['definitions']}
    def __init__(self, *args, **kwds):
        super(DataFormat, self).__init__(*args, **kwds)


class DateTime(SchemaBase):
    """A DateTime json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/DateTime', 'definitions': Root._json_schema['definitions']}
    def __init__(self, date=Undefined, day=Undefined, hours=Undefined, milliseconds=Undefined, minutes=Undefined, month=Undefined, quarter=Undefined, seconds=Undefined, utc=Undefined, year=Undefined):
        super(DateTime, self).__init__(date=date, day=day, hours=hours, milliseconds=milliseconds, minutes=minutes, month=month, quarter=quarter, seconds=seconds, utc=utc, year=year)


class Day(SchemaBase):
    """A Day json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/Day', 'definitions': Root._json_schema['definitions']}
    def __init__(self, *args):
        super(Day, self).__init__(*args)


class Encoding(SchemaBase):
    """A Encoding json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/Encoding', 'definitions': Root._json_schema['definitions']}
    def __init__(self, color=Undefined, detail=Undefined, href=Undefined, opacity=Undefined, order=Undefined, shape=Undefined, size=Undefined, text=Undefined, tooltip=Undefined, x=Undefined, x2=Undefined, y=Undefined, y2=Undefined):
        super(Encoding, self).__init__(color=color, detail=detail, href=href, opacity=opacity, order=order, shape=shape, size=size, text=text, tooltip=tooltip, x=x, x2=x2, y=y, y2=y2)


class EncodingWithFacet(SchemaBase):
    """A EncodingWithFacet json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/EncodingWithFacet', 'definitions': Root._json_schema['definitions']}
    def __init__(self, color=Undefined, column=Undefined, detail=Undefined, href=Undefined, opacity=Undefined, order=Undefined, row=Undefined, shape=Undefined, size=Undefined, text=Undefined, tooltip=Undefined, x=Undefined, x2=Undefined, y=Undefined, y2=Undefined):
        super(EncodingWithFacet, self).__init__(color=color, column=column, detail=detail, href=href, opacity=opacity, order=order, row=row, shape=shape, size=size, text=text, tooltip=tooltip, x=x, x2=x2, y=y, y2=y2)


class FacetFieldDef(SchemaBase):
    """A FacetFieldDef json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/FacetFieldDef', 'definitions': Root._json_schema['definitions']}
    def __init__(self, type, aggregate=Undefined, bin=Undefined, field=Undefined, header=Undefined, sort=Undefined, timeUnit=Undefined):
        super(FacetFieldDef, self).__init__(type=type, aggregate=aggregate, bin=bin, field=field, header=header, sort=sort, timeUnit=timeUnit)


class FacetMapping(SchemaBase):
    """A FacetMapping json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/FacetMapping', 'definitions': Root._json_schema['definitions']}
    def __init__(self, column=Undefined, row=Undefined):
        super(FacetMapping, self).__init__(column=column, row=row)


class FieldDef(SchemaBase):
    """A FieldDef json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/FieldDef', 'definitions': Root._json_schema['definitions']}
    def __init__(self, type, aggregate=Undefined, bin=Undefined, field=Undefined, timeUnit=Undefined):
        super(FieldDef, self).__init__(type=type, aggregate=aggregate, bin=bin, field=field, timeUnit=timeUnit)


class FieldDefWithCondition(SchemaBase):
    """A FieldDefWithCondition json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/FieldDefWithCondition', 'definitions': Root._json_schema['definitions']}
    def __init__(self, type, aggregate=Undefined, bin=Undefined, condition=Undefined, field=Undefined, timeUnit=Undefined):
        super(FieldDefWithCondition, self).__init__(type=type, aggregate=aggregate, bin=bin, condition=condition, field=field, timeUnit=timeUnit)


class MarkPropFieldDefWithCondition(SchemaBase):
    """A MarkPropFieldDefWithCondition json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/MarkPropFieldDefWithCondition', 'definitions': Root._json_schema['definitions']}
    def __init__(self, type, aggregate=Undefined, bin=Undefined, condition=Undefined, field=Undefined, legend=Undefined, scale=Undefined, sort=Undefined, timeUnit=Undefined):
        super(MarkPropFieldDefWithCondition, self).__init__(type=type, aggregate=aggregate, bin=bin, condition=condition, field=field, legend=legend, scale=scale, sort=sort, timeUnit=timeUnit)


class TextFieldDefWithCondition(SchemaBase):
    """A TextFieldDefWithCondition json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/TextFieldDefWithCondition', 'definitions': Root._json_schema['definitions']}
    def __init__(self, type, aggregate=Undefined, bin=Undefined, condition=Undefined, field=Undefined, format=Undefined, timeUnit=Undefined):
        super(TextFieldDefWithCondition, self).__init__(type=type, aggregate=aggregate, bin=bin, condition=condition, field=field, format=format, timeUnit=timeUnit)


class FieldEqualPredicate(SchemaBase):
    """A FieldEqualPredicate json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/FieldEqualPredicate', 'definitions': Root._json_schema['definitions']}
    def __init__(self, equal, field, timeUnit=Undefined):
        super(FieldEqualPredicate, self).__init__(equal=equal, field=field, timeUnit=timeUnit)


class FieldOneOfPredicate(SchemaBase):
    """A FieldOneOfPredicate json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/FieldOneOfPredicate', 'definitions': Root._json_schema['definitions']}
    def __init__(self, field, oneOf, timeUnit=Undefined):
        super(FieldOneOfPredicate, self).__init__(field=field, oneOf=oneOf, timeUnit=timeUnit)


class FieldRangePredicate(SchemaBase):
    """A FieldRangePredicate json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/FieldRangePredicate', 'definitions': Root._json_schema['definitions']}
    def __init__(self, field, range, timeUnit=Undefined):
        super(FieldRangePredicate, self).__init__(field=field, range=range, timeUnit=timeUnit)


class FilterTransform(SchemaBase):
    """A FilterTransform json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/FilterTransform', 'definitions': Root._json_schema['definitions']}
    def __init__(self, filter):
        super(FilterTransform, self).__init__(filter=filter)


class FontStyle(SchemaBase):
    """A FontStyle json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/FontStyle', 'definitions': Root._json_schema['definitions']}
    def __init__(self, *args):
        super(FontStyle, self).__init__(*args)


class FontWeight(SchemaBase):
    """A FontWeight json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/FontWeight', 'definitions': Root._json_schema['definitions']}
    def __init__(self, *args):
        super(FontWeight, self).__init__(*args)


class FontWeightNumber(SchemaBase):
    """A FontWeightNumber json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/FontWeightNumber', 'definitions': Root._json_schema['definitions']}
    def __init__(self, *args):
        super(FontWeightNumber, self).__init__(*args)


class FacetSpec(SchemaBase):
    """A FacetSpec json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/FacetSpec', 'definitions': Root._json_schema['definitions']}
    def __init__(self, facet, spec, data=Undefined, description=Undefined, name=Undefined, resolve=Undefined, title=Undefined, transform=Undefined):
        super(FacetSpec, self).__init__(facet=facet, spec=spec, data=data, description=description, name=name, resolve=resolve, title=title, transform=transform)


class HConcatSpec(SchemaBase):
    """A HConcatSpec json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/HConcatSpec', 'definitions': Root._json_schema['definitions']}
    def __init__(self, hconcat, data=Undefined, description=Undefined, name=Undefined, resolve=Undefined, title=Undefined, transform=Undefined):
        super(HConcatSpec, self).__init__(hconcat=hconcat, data=data, description=description, name=name, resolve=resolve, title=title, transform=transform)


class LayerSpec(SchemaBase):
    """A LayerSpec json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/LayerSpec', 'definitions': Root._json_schema['definitions']}
    def __init__(self, layer, data=Undefined, description=Undefined, height=Undefined, name=Undefined, resolve=Undefined, title=Undefined, transform=Undefined, width=Undefined):
        super(LayerSpec, self).__init__(layer=layer, data=data, description=description, height=height, name=name, resolve=resolve, title=title, transform=transform, width=width)


class RepeatSpec(SchemaBase):
    """A RepeatSpec json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/RepeatSpec', 'definitions': Root._json_schema['definitions']}
    def __init__(self, repeat, spec, data=Undefined, description=Undefined, name=Undefined, resolve=Undefined, title=Undefined, transform=Undefined):
        super(RepeatSpec, self).__init__(repeat=repeat, spec=spec, data=data, description=description, name=name, resolve=resolve, title=title, transform=transform)


class Spec(SchemaBase):
    """A Spec json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/Spec', 'definitions': Root._json_schema['definitions']}
    def __init__(self, *args, **kwds):
        super(Spec, self).__init__(*args, **kwds)


class CompositeUnitSpecAlias(SchemaBase):
    """A CompositeUnitSpecAlias json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/CompositeUnitSpecAlias', 'definitions': Root._json_schema['definitions']}
    def __init__(self, encoding, mark, data=Undefined, description=Undefined, height=Undefined, name=Undefined, projection=Undefined, selection=Undefined, title=Undefined, transform=Undefined, width=Undefined):
        super(CompositeUnitSpecAlias, self).__init__(encoding=encoding, mark=mark, data=data, description=description, height=height, name=name, projection=projection, selection=selection, title=title, transform=transform, width=width)


class FacetedCompositeUnitSpecAlias(SchemaBase):
    """A FacetedCompositeUnitSpecAlias json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/FacetedCompositeUnitSpecAlias', 'definitions': Root._json_schema['definitions']}
    def __init__(self, encoding, mark, data=Undefined, description=Undefined, height=Undefined, name=Undefined, projection=Undefined, selection=Undefined, title=Undefined, transform=Undefined, width=Undefined):
        super(FacetedCompositeUnitSpecAlias, self).__init__(encoding=encoding, mark=mark, data=data, description=description, height=height, name=name, projection=projection, selection=selection, title=title, transform=transform, width=width)


class VConcatSpec(SchemaBase):
    """A VConcatSpec json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/VConcatSpec', 'definitions': Root._json_schema['definitions']}
    def __init__(self, vconcat, data=Undefined, description=Undefined, name=Undefined, resolve=Undefined, title=Undefined, transform=Undefined):
        super(VConcatSpec, self).__init__(vconcat=vconcat, data=data, description=description, name=name, resolve=resolve, title=title, transform=transform)


class GeoType(SchemaBase):
    """A GeoType json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/GeoType', 'definitions': Root._json_schema['definitions']}
    def __init__(self, *args):
        super(GeoType, self).__init__(*args)


class Header(SchemaBase):
    """A Header json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/Header', 'definitions': Root._json_schema['definitions']}
    def __init__(self, format=Undefined, labelAngle=Undefined, title=Undefined):
        super(Header, self).__init__(format=format, labelAngle=labelAngle, title=title)


class HorizontalAlign(SchemaBase):
    """A HorizontalAlign json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/HorizontalAlign', 'definitions': Root._json_schema['definitions']}
    def __init__(self, *args):
        super(HorizontalAlign, self).__init__(*args)


class InlineData(SchemaBase):
    """A InlineData json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/InlineData', 'definitions': Root._json_schema['definitions']}
    def __init__(self, values, format=Undefined):
        super(InlineData, self).__init__(values=values, format=format)


class Interpolate(SchemaBase):
    """A Interpolate json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/Interpolate', 'definitions': Root._json_schema['definitions']}
    def __init__(self, *args):
        super(Interpolate, self).__init__(*args)


class InterpolateParams(SchemaBase):
    """A InterpolateParams json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/InterpolateParams', 'definitions': Root._json_schema['definitions']}
    def __init__(self, type, gamma=Undefined):
        super(InterpolateParams, self).__init__(type=type, gamma=gamma)


class IntervalSelection(SchemaBase):
    """A IntervalSelection json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/IntervalSelection', 'definitions': Root._json_schema['definitions']}
    def __init__(self, type, bind=Undefined, empty=Undefined, encodings=Undefined, fields=Undefined, mark=Undefined, on=Undefined, resolve=Undefined, translate=Undefined, zoom=Undefined):
        super(IntervalSelection, self).__init__(type=type, bind=bind, empty=empty, encodings=encodings, fields=fields, mark=mark, on=on, resolve=resolve, translate=translate, zoom=zoom)


class IntervalSelectionConfig(SchemaBase):
    """A IntervalSelectionConfig json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/IntervalSelectionConfig', 'definitions': Root._json_schema['definitions']}
    def __init__(self, bind=Undefined, empty=Undefined, encodings=Undefined, fields=Undefined, mark=Undefined, on=Undefined, resolve=Undefined, translate=Undefined, zoom=Undefined):
        super(IntervalSelectionConfig, self).__init__(bind=bind, empty=empty, encodings=encodings, fields=fields, mark=mark, on=on, resolve=resolve, translate=translate, zoom=zoom)


class JsonDataFormat(SchemaBase):
    """A JsonDataFormat json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/JsonDataFormat', 'definitions': Root._json_schema['definitions']}
    def __init__(self, parse=Undefined, property=Undefined, type=Undefined):
        super(JsonDataFormat, self).__init__(parse=parse, property=property, type=type)


class Legend(SchemaBase):
    """A Legend json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/Legend', 'definitions': Root._json_schema['definitions']}
    def __init__(self, entryPadding=Undefined, format=Undefined, offset=Undefined, orient=Undefined, padding=Undefined, tickCount=Undefined, title=Undefined, type=Undefined, values=Undefined, zindex=Undefined):
        super(Legend, self).__init__(entryPadding=entryPadding, format=format, offset=offset, orient=orient, padding=padding, tickCount=tickCount, title=title, type=type, values=values, zindex=zindex)


class LegendConfig(SchemaBase):
    """A LegendConfig json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/LegendConfig', 'definitions': Root._json_schema['definitions']}
    def __init__(self, cornerRadius=Undefined, entryPadding=Undefined, fillColor=Undefined, gradientHeight=Undefined, gradientLabelBaseline=Undefined, gradientLabelLimit=Undefined, gradientLabelOffset=Undefined, gradientStrokeColor=Undefined, gradientStrokeWidth=Undefined, gradientWidth=Undefined, labelAlign=Undefined, labelBaseline=Undefined, labelColor=Undefined, labelFont=Undefined, labelFontSize=Undefined, labelLimit=Undefined, labelOffset=Undefined, offset=Undefined, orient=Undefined, padding=Undefined, shortTimeLabels=Undefined, strokeColor=Undefined, strokeDash=Undefined, strokeWidth=Undefined, symbolColor=Undefined, symbolSize=Undefined, symbolStrokeWidth=Undefined, symbolType=Undefined, titleAlign=Undefined, titleBaseline=Undefined, titleColor=Undefined, titleFont=Undefined, titleFontSize=Undefined, titleFontWeight=Undefined, titleLimit=Undefined, titlePadding=Undefined):
        super(LegendConfig, self).__init__(cornerRadius=cornerRadius, entryPadding=entryPadding, fillColor=fillColor, gradientHeight=gradientHeight, gradientLabelBaseline=gradientLabelBaseline, gradientLabelLimit=gradientLabelLimit, gradientLabelOffset=gradientLabelOffset, gradientStrokeColor=gradientStrokeColor, gradientStrokeWidth=gradientStrokeWidth, gradientWidth=gradientWidth, labelAlign=labelAlign, labelBaseline=labelBaseline, labelColor=labelColor, labelFont=labelFont, labelFontSize=labelFontSize, labelLimit=labelLimit, labelOffset=labelOffset, offset=offset, orient=orient, padding=padding, shortTimeLabels=shortTimeLabels, strokeColor=strokeColor, strokeDash=strokeDash, strokeWidth=strokeWidth, symbolColor=symbolColor, symbolSize=symbolSize, symbolStrokeWidth=symbolStrokeWidth, symbolType=symbolType, titleAlign=titleAlign, titleBaseline=titleBaseline, titleColor=titleColor, titleFont=titleFont, titleFontSize=titleFontSize, titleFontWeight=titleFontWeight, titleLimit=titleLimit, titlePadding=titlePadding)


class LegendOrient(SchemaBase):
    """A LegendOrient json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/LegendOrient', 'definitions': Root._json_schema['definitions']}
    def __init__(self, *args):
        super(LegendOrient, self).__init__(*args)


class LegendResolveMap(SchemaBase):
    """A LegendResolveMap json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/LegendResolveMap', 'definitions': Root._json_schema['definitions']}
    def __init__(self, color=Undefined, opacity=Undefined, shape=Undefined, size=Undefined):
        super(LegendResolveMap, self).__init__(color=color, opacity=opacity, shape=shape, size=size)


class LocalMultiTimeUnit(SchemaBase):
    """A LocalMultiTimeUnit json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/LocalMultiTimeUnit', 'definitions': Root._json_schema['definitions']}
    def __init__(self, *args):
        super(LocalMultiTimeUnit, self).__init__(*args)


class LocalSingleTimeUnit(SchemaBase):
    """A LocalSingleTimeUnit json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/LocalSingleTimeUnit', 'definitions': Root._json_schema['definitions']}
    def __init__(self, *args):
        super(LocalSingleTimeUnit, self).__init__(*args)


class LogicalAndPredicate(SchemaBase):
    """A LogicalAndPredicate json schema wrapper"""
    _valid_attr_map = {'and': 'and_'}
    _json_schema = {'$ref': '#/definitions/LogicalAnd<Predicate>', 'definitions': Root._json_schema['definitions']}
    def __init__(self, and_):
        super(LogicalAndPredicate, self).__init__(and_=and_)


class SelectionAnd(SchemaBase):
    """A SelectionAnd json schema wrapper"""
    _valid_attr_map = {'and': 'and_'}
    _json_schema = {'$ref': '#/definitions/SelectionAnd', 'definitions': Root._json_schema['definitions']}
    def __init__(self, and_):
        super(SelectionAnd, self).__init__(and_=and_)


class LogicalNotPredicate(SchemaBase):
    """A LogicalNotPredicate json schema wrapper"""
    _valid_attr_map = {'not': 'not_'}
    _json_schema = {'$ref': '#/definitions/LogicalNot<Predicate>', 'definitions': Root._json_schema['definitions']}
    def __init__(self, not_):
        super(LogicalNotPredicate, self).__init__(not_=not_)


class SelectionNot(SchemaBase):
    """A SelectionNot json schema wrapper"""
    _valid_attr_map = {'not': 'not_'}
    _json_schema = {'$ref': '#/definitions/SelectionNot', 'definitions': Root._json_schema['definitions']}
    def __init__(self, not_):
        super(SelectionNot, self).__init__(not_=not_)


class LogicalOperandPredicate(SchemaBase):
    """A LogicalOperandPredicate json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/LogicalOperand<Predicate>', 'definitions': Root._json_schema['definitions']}
    def __init__(self, *args, **kwds):
        super(LogicalOperandPredicate, self).__init__(*args, **kwds)


class SelectionOperand(SchemaBase):
    """A SelectionOperand json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/SelectionOperand', 'definitions': Root._json_schema['definitions']}
    def __init__(self, *args, **kwds):
        super(SelectionOperand, self).__init__(*args, **kwds)


class LogicalOrPredicate(SchemaBase):
    """A LogicalOrPredicate json schema wrapper"""
    _valid_attr_map = {'or': 'or_'}
    _json_schema = {'$ref': '#/definitions/LogicalOr<Predicate>', 'definitions': Root._json_schema['definitions']}
    def __init__(self, or_):
        super(LogicalOrPredicate, self).__init__(or_=or_)


class SelectionOr(SchemaBase):
    """A SelectionOr json schema wrapper"""
    _valid_attr_map = {'or': 'or_'}
    _json_schema = {'$ref': '#/definitions/SelectionOr', 'definitions': Root._json_schema['definitions']}
    def __init__(self, or_):
        super(SelectionOr, self).__init__(or_=or_)


class LookupData(SchemaBase):
    """A LookupData json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/LookupData', 'definitions': Root._json_schema['definitions']}
    def __init__(self, data, key, fields=Undefined):
        super(LookupData, self).__init__(data=data, key=key, fields=fields)


class LookupTransform(SchemaBase):
    """A LookupTransform json schema wrapper"""
    _valid_attr_map = {'as': 'as_', 'from': 'from_'}
    _json_schema = {'$ref': '#/definitions/LookupTransform', 'definitions': Root._json_schema['definitions']}
    def __init__(self, from_, lookup, as_=Undefined, default=Undefined):
        super(LookupTransform, self).__init__(from_=from_, lookup=lookup, as_=as_, default=default)


class Mark(SchemaBase):
    """A Mark json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/Mark', 'definitions': Root._json_schema['definitions']}
    def __init__(self, *args):
        super(Mark, self).__init__(*args)


class MarkConfig(SchemaBase):
    """A MarkConfig json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/MarkConfig', 'definitions': Root._json_schema['definitions']}
    def __init__(self, align=Undefined, angle=Undefined, baseline=Undefined, color=Undefined, cursor=Undefined, dx=Undefined, dy=Undefined, fill=Undefined, fillOpacity=Undefined, filled=Undefined, font=Undefined, fontSize=Undefined, fontStyle=Undefined, fontWeight=Undefined, href=Undefined, interpolate=Undefined, limit=Undefined, opacity=Undefined, orient=Undefined, radius=Undefined, shape=Undefined, size=Undefined, stroke=Undefined, strokeDash=Undefined, strokeDashOffset=Undefined, strokeOpacity=Undefined, strokeWidth=Undefined, tension=Undefined, text=Undefined, theta=Undefined):
        super(MarkConfig, self).__init__(align=align, angle=angle, baseline=baseline, color=color, cursor=cursor, dx=dx, dy=dy, fill=fill, fillOpacity=fillOpacity, filled=filled, font=font, fontSize=fontSize, fontStyle=fontStyle, fontWeight=fontWeight, href=href, interpolate=interpolate, limit=limit, opacity=opacity, orient=orient, radius=radius, shape=shape, size=size, stroke=stroke, strokeDash=strokeDash, strokeDashOffset=strokeDashOffset, strokeOpacity=strokeOpacity, strokeWidth=strokeWidth, tension=tension, text=text, theta=theta)


class MarkDef(SchemaBase):
    """A MarkDef json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/MarkDef', 'definitions': Root._json_schema['definitions']}
    def __init__(self, type, align=Undefined, angle=Undefined, baseline=Undefined, clip=Undefined, color=Undefined, cursor=Undefined, dx=Undefined, dy=Undefined, fill=Undefined, fillOpacity=Undefined, filled=Undefined, font=Undefined, fontSize=Undefined, fontStyle=Undefined, fontWeight=Undefined, href=Undefined, interpolate=Undefined, limit=Undefined, opacity=Undefined, orient=Undefined, radius=Undefined, shape=Undefined, size=Undefined, stroke=Undefined, strokeDash=Undefined, strokeDashOffset=Undefined, strokeOpacity=Undefined, strokeWidth=Undefined, style=Undefined, tension=Undefined, text=Undefined, theta=Undefined):
        super(MarkDef, self).__init__(type=type, align=align, angle=angle, baseline=baseline, clip=clip, color=color, cursor=cursor, dx=dx, dy=dy, fill=fill, fillOpacity=fillOpacity, filled=filled, font=font, fontSize=fontSize, fontStyle=fontStyle, fontWeight=fontWeight, href=href, interpolate=interpolate, limit=limit, opacity=opacity, orient=orient, radius=radius, shape=shape, size=size, stroke=stroke, strokeDash=strokeDash, strokeDashOffset=strokeDashOffset, strokeOpacity=strokeOpacity, strokeWidth=strokeWidth, style=style, tension=tension, text=text, theta=theta)


class Month(SchemaBase):
    """A Month json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/Month', 'definitions': Root._json_schema['definitions']}
    def __init__(self, *args):
        super(Month, self).__init__(*args)


class MultiSelection(SchemaBase):
    """A MultiSelection json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/MultiSelection', 'definitions': Root._json_schema['definitions']}
    def __init__(self, type, empty=Undefined, encodings=Undefined, fields=Undefined, nearest=Undefined, on=Undefined, resolve=Undefined, toggle=Undefined):
        super(MultiSelection, self).__init__(type=type, empty=empty, encodings=encodings, fields=fields, nearest=nearest, on=on, resolve=resolve, toggle=toggle)


class MultiSelectionConfig(SchemaBase):
    """A MultiSelectionConfig json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/MultiSelectionConfig', 'definitions': Root._json_schema['definitions']}
    def __init__(self, empty=Undefined, encodings=Undefined, fields=Undefined, nearest=Undefined, on=Undefined, resolve=Undefined, toggle=Undefined):
        super(MultiSelectionConfig, self).__init__(empty=empty, encodings=encodings, fields=fields, nearest=nearest, on=on, resolve=resolve, toggle=toggle)


class MultiTimeUnit(SchemaBase):
    """A MultiTimeUnit json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/MultiTimeUnit', 'definitions': Root._json_schema['definitions']}
    def __init__(self, *args, **kwds):
        super(MultiTimeUnit, self).__init__(*args, **kwds)


class NamedData(SchemaBase):
    """A NamedData json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/NamedData', 'definitions': Root._json_schema['definitions']}
    def __init__(self, name, format=Undefined):
        super(NamedData, self).__init__(name=name, format=format)


class NiceTime(SchemaBase):
    """A NiceTime json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/NiceTime', 'definitions': Root._json_schema['definitions']}
    def __init__(self, *args):
        super(NiceTime, self).__init__(*args)


class OrderFieldDef(SchemaBase):
    """A OrderFieldDef json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/OrderFieldDef', 'definitions': Root._json_schema['definitions']}
    def __init__(self, type, aggregate=Undefined, bin=Undefined, field=Undefined, sort=Undefined, timeUnit=Undefined):
        super(OrderFieldDef, self).__init__(type=type, aggregate=aggregate, bin=bin, field=field, sort=sort, timeUnit=timeUnit)


class Orient(SchemaBase):
    """A Orient json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/Orient', 'definitions': Root._json_schema['definitions']}
    def __init__(self, *args):
        super(Orient, self).__init__(*args)


class Padding(SchemaBase):
    """A Padding json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/Padding', 'definitions': Root._json_schema['definitions']}
    def __init__(self, *args, **kwds):
        super(Padding, self).__init__(*args, **kwds)


class PositionFieldDef(SchemaBase):
    """A PositionFieldDef json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/PositionFieldDef', 'definitions': Root._json_schema['definitions']}
    def __init__(self, type, aggregate=Undefined, axis=Undefined, bin=Undefined, field=Undefined, scale=Undefined, sort=Undefined, stack=Undefined, timeUnit=Undefined):
        super(PositionFieldDef, self).__init__(type=type, aggregate=aggregate, axis=axis, bin=bin, field=field, scale=scale, sort=sort, stack=stack, timeUnit=timeUnit)


class Predicate(SchemaBase):
    """A Predicate json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/Predicate', 'definitions': Root._json_schema['definitions']}
    def __init__(self, *args, **kwds):
        super(Predicate, self).__init__(*args, **kwds)


class Projection(SchemaBase):
    """A Projection json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/Projection', 'definitions': Root._json_schema['definitions']}
    def __init__(self, center=Undefined, clipAngle=Undefined, clipExtent=Undefined, coefficient=Undefined, distance=Undefined, fraction=Undefined, lobes=Undefined, parallel=Undefined, precision=Undefined, radius=Undefined, ratio=Undefined, rotate=Undefined, spacing=Undefined, tilt=Undefined, type=Undefined):
        super(Projection, self).__init__(center=center, clipAngle=clipAngle, clipExtent=clipExtent, coefficient=coefficient, distance=distance, fraction=fraction, lobes=lobes, parallel=parallel, precision=precision, radius=radius, ratio=ratio, rotate=rotate, spacing=spacing, tilt=tilt, type=type)


class ProjectionConfig(SchemaBase):
    """A ProjectionConfig json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/ProjectionConfig', 'definitions': Root._json_schema['definitions']}
    def __init__(self, center=Undefined, clipAngle=Undefined, clipExtent=Undefined, coefficient=Undefined, distance=Undefined, fraction=Undefined, lobes=Undefined, parallel=Undefined, precision=Undefined, radius=Undefined, ratio=Undefined, rotate=Undefined, spacing=Undefined, tilt=Undefined, type=Undefined):
        super(ProjectionConfig, self).__init__(center=center, clipAngle=clipAngle, clipExtent=clipExtent, coefficient=coefficient, distance=distance, fraction=fraction, lobes=lobes, parallel=parallel, precision=precision, radius=radius, ratio=ratio, rotate=rotate, spacing=spacing, tilt=tilt, type=type)


class ProjectionType(SchemaBase):
    """A ProjectionType json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/ProjectionType', 'definitions': Root._json_schema['definitions']}
    def __init__(self, *args):
        super(ProjectionType, self).__init__(*args)


class RangeConfig(SchemaBase):
    """A RangeConfig json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/RangeConfig', 'definitions': Root._json_schema['definitions']}
    def __init__(self, category=Undefined, diverging=Undefined, heatmap=Undefined, ordinal=Undefined, ramp=Undefined, symbol=Undefined, **kwds):
        super(RangeConfig, self).__init__(category=category, diverging=diverging, heatmap=heatmap, ordinal=ordinal, ramp=ramp, symbol=symbol, **kwds)


class RangeConfigValue(SchemaBase):
    """A RangeConfigValue json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/RangeConfigValue', 'definitions': Root._json_schema['definitions']}
    def __init__(self, *args, **kwds):
        super(RangeConfigValue, self).__init__(*args, **kwds)


class Repeat(SchemaBase):
    """A Repeat json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/Repeat', 'definitions': Root._json_schema['definitions']}
    def __init__(self, column=Undefined, row=Undefined):
        super(Repeat, self).__init__(column=column, row=row)


class RepeatRef(SchemaBase):
    """A RepeatRef json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/RepeatRef', 'definitions': Root._json_schema['definitions']}
    def __init__(self, repeat):
        super(RepeatRef, self).__init__(repeat=repeat)


class Resolve(SchemaBase):
    """A Resolve json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/Resolve', 'definitions': Root._json_schema['definitions']}
    def __init__(self, axis=Undefined, legend=Undefined, scale=Undefined):
        super(Resolve, self).__init__(axis=axis, legend=legend, scale=scale)


class ResolveMode(SchemaBase):
    """A ResolveMode json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/ResolveMode', 'definitions': Root._json_schema['definitions']}
    def __init__(self, *args):
        super(ResolveMode, self).__init__(*args)


class Scale(SchemaBase):
    """A Scale json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/Scale', 'definitions': Root._json_schema['definitions']}
    def __init__(self, base=Undefined, clamp=Undefined, domain=Undefined, exponent=Undefined, interpolate=Undefined, nice=Undefined, padding=Undefined, paddingInner=Undefined, paddingOuter=Undefined, range=Undefined, rangeStep=Undefined, round=Undefined, scheme=Undefined, type=Undefined, zero=Undefined):
        super(Scale, self).__init__(base=base, clamp=clamp, domain=domain, exponent=exponent, interpolate=interpolate, nice=nice, padding=padding, paddingInner=paddingInner, paddingOuter=paddingOuter, range=range, rangeStep=rangeStep, round=round, scheme=scheme, type=type, zero=zero)


class ScaleConfig(SchemaBase):
    """A ScaleConfig json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/ScaleConfig', 'definitions': Root._json_schema['definitions']}
    def __init__(self, bandPaddingInner=Undefined, bandPaddingOuter=Undefined, clamp=Undefined, continuousPadding=Undefined, maxBandSize=Undefined, maxFontSize=Undefined, maxOpacity=Undefined, maxSize=Undefined, maxStrokeWidth=Undefined, minBandSize=Undefined, minFontSize=Undefined, minOpacity=Undefined, minSize=Undefined, minStrokeWidth=Undefined, pointPadding=Undefined, rangeStep=Undefined, round=Undefined, textXRangeStep=Undefined, useUnaggregatedDomain=Undefined):
        super(ScaleConfig, self).__init__(bandPaddingInner=bandPaddingInner, bandPaddingOuter=bandPaddingOuter, clamp=clamp, continuousPadding=continuousPadding, maxBandSize=maxBandSize, maxFontSize=maxFontSize, maxOpacity=maxOpacity, maxSize=maxSize, maxStrokeWidth=maxStrokeWidth, minBandSize=minBandSize, minFontSize=minFontSize, minOpacity=minOpacity, minSize=minSize, minStrokeWidth=minStrokeWidth, pointPadding=pointPadding, rangeStep=rangeStep, round=round, textXRangeStep=textXRangeStep, useUnaggregatedDomain=useUnaggregatedDomain)


class ScaleResolveMap(SchemaBase):
    """A ScaleResolveMap json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/ScaleResolveMap', 'definitions': Root._json_schema['definitions']}
    def __init__(self, color=Undefined, opacity=Undefined, shape=Undefined, size=Undefined, x=Undefined, y=Undefined):
        super(ScaleResolveMap, self).__init__(color=color, opacity=opacity, shape=shape, size=size, x=x, y=y)


class ScaleType(SchemaBase):
    """A ScaleType json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/ScaleType', 'definitions': Root._json_schema['definitions']}
    def __init__(self, *args):
        super(ScaleType, self).__init__(*args)


class SchemeParams(SchemaBase):
    """A SchemeParams json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/SchemeParams', 'definitions': Root._json_schema['definitions']}
    def __init__(self, name, extent=Undefined):
        super(SchemeParams, self).__init__(name=name, extent=extent)


class SelectionConfig(SchemaBase):
    """A SelectionConfig json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/SelectionConfig', 'definitions': Root._json_schema['definitions']}
    def __init__(self, interval=Undefined, multi=Undefined, single=Undefined):
        super(SelectionConfig, self).__init__(interval=interval, multi=multi, single=single)


class SelectionDef(SchemaBase):
    """A SelectionDef json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/SelectionDef', 'definitions': Root._json_schema['definitions']}
    def __init__(self, *args, **kwds):
        super(SelectionDef, self).__init__(*args, **kwds)


class SelectionDomain(SchemaBase):
    """A SelectionDomain json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/SelectionDomain', 'definitions': Root._json_schema['definitions']}
    def __init__(self, *args, **kwds):
        super(SelectionDomain, self).__init__(*args, **kwds)


class SelectionPredicate(SchemaBase):
    """A SelectionPredicate json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/SelectionPredicate', 'definitions': Root._json_schema['definitions']}
    def __init__(self, selection):
        super(SelectionPredicate, self).__init__(selection=selection)


class SelectionResolution(SchemaBase):
    """A SelectionResolution json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/SelectionResolution', 'definitions': Root._json_schema['definitions']}
    def __init__(self, *args):
        super(SelectionResolution, self).__init__(*args)


class SingleDefChannel(SchemaBase):
    """A SingleDefChannel json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/SingleDefChannel', 'definitions': Root._json_schema['definitions']}
    def __init__(self, *args):
        super(SingleDefChannel, self).__init__(*args)


class SingleSelection(SchemaBase):
    """A SingleSelection json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/SingleSelection', 'definitions': Root._json_schema['definitions']}
    def __init__(self, type, bind=Undefined, empty=Undefined, encodings=Undefined, fields=Undefined, nearest=Undefined, on=Undefined, resolve=Undefined):
        super(SingleSelection, self).__init__(type=type, bind=bind, empty=empty, encodings=encodings, fields=fields, nearest=nearest, on=on, resolve=resolve)


class SingleSelectionConfig(SchemaBase):
    """A SingleSelectionConfig json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/SingleSelectionConfig', 'definitions': Root._json_schema['definitions']}
    def __init__(self, bind=Undefined, empty=Undefined, encodings=Undefined, fields=Undefined, nearest=Undefined, on=Undefined, resolve=Undefined):
        super(SingleSelectionConfig, self).__init__(bind=bind, empty=empty, encodings=encodings, fields=fields, nearest=nearest, on=on, resolve=resolve)


class SingleTimeUnit(SchemaBase):
    """A SingleTimeUnit json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/SingleTimeUnit', 'definitions': Root._json_schema['definitions']}
    def __init__(self, *args, **kwds):
        super(SingleTimeUnit, self).__init__(*args, **kwds)


class SortField(SchemaBase):
    """A SortField json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/SortField', 'definitions': Root._json_schema['definitions']}
    def __init__(self, op, field=Undefined, order=Undefined):
        super(SortField, self).__init__(op=op, field=field, order=order)


class SortOrder(SchemaBase):
    """A SortOrder json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/SortOrder', 'definitions': Root._json_schema['definitions']}
    def __init__(self, *args):
        super(SortOrder, self).__init__(*args)


class StackOffset(SchemaBase):
    """A StackOffset json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/StackOffset', 'definitions': Root._json_schema['definitions']}
    def __init__(self, *args):
        super(StackOffset, self).__init__(*args)


class StyleConfigIndex(SchemaBase):
    """A StyleConfigIndex json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/StyleConfigIndex', 'definitions': Root._json_schema['definitions']}
    def __init__(self, **kwds):
        super(StyleConfigIndex, self).__init__(**kwds)


class TextConfig(SchemaBase):
    """A TextConfig json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/TextConfig', 'definitions': Root._json_schema['definitions']}
    def __init__(self, align=Undefined, angle=Undefined, baseline=Undefined, color=Undefined, cursor=Undefined, dx=Undefined, dy=Undefined, fill=Undefined, fillOpacity=Undefined, filled=Undefined, font=Undefined, fontSize=Undefined, fontStyle=Undefined, fontWeight=Undefined, href=Undefined, interpolate=Undefined, limit=Undefined, opacity=Undefined, orient=Undefined, radius=Undefined, shape=Undefined, shortTimeLabels=Undefined, size=Undefined, stroke=Undefined, strokeDash=Undefined, strokeDashOffset=Undefined, strokeOpacity=Undefined, strokeWidth=Undefined, tension=Undefined, text=Undefined, theta=Undefined):
        super(TextConfig, self).__init__(align=align, angle=angle, baseline=baseline, color=color, cursor=cursor, dx=dx, dy=dy, fill=fill, fillOpacity=fillOpacity, filled=filled, font=font, fontSize=fontSize, fontStyle=fontStyle, fontWeight=fontWeight, href=href, interpolate=interpolate, limit=limit, opacity=opacity, orient=orient, radius=radius, shape=shape, shortTimeLabels=shortTimeLabels, size=size, stroke=stroke, strokeDash=strokeDash, strokeDashOffset=strokeDashOffset, strokeOpacity=strokeOpacity, strokeWidth=strokeWidth, tension=tension, text=text, theta=theta)


class TickConfig(SchemaBase):
    """A TickConfig json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/TickConfig', 'definitions': Root._json_schema['definitions']}
    def __init__(self, align=Undefined, angle=Undefined, bandSize=Undefined, baseline=Undefined, color=Undefined, cursor=Undefined, dx=Undefined, dy=Undefined, fill=Undefined, fillOpacity=Undefined, filled=Undefined, font=Undefined, fontSize=Undefined, fontStyle=Undefined, fontWeight=Undefined, href=Undefined, interpolate=Undefined, limit=Undefined, opacity=Undefined, orient=Undefined, radius=Undefined, shape=Undefined, size=Undefined, stroke=Undefined, strokeDash=Undefined, strokeDashOffset=Undefined, strokeOpacity=Undefined, strokeWidth=Undefined, tension=Undefined, text=Undefined, theta=Undefined, thickness=Undefined):
        super(TickConfig, self).__init__(align=align, angle=angle, bandSize=bandSize, baseline=baseline, color=color, cursor=cursor, dx=dx, dy=dy, fill=fill, fillOpacity=fillOpacity, filled=filled, font=font, fontSize=fontSize, fontStyle=fontStyle, fontWeight=fontWeight, href=href, interpolate=interpolate, limit=limit, opacity=opacity, orient=orient, radius=radius, shape=shape, size=size, stroke=stroke, strokeDash=strokeDash, strokeDashOffset=strokeDashOffset, strokeOpacity=strokeOpacity, strokeWidth=strokeWidth, tension=tension, text=text, theta=theta, thickness=thickness)


class TimeUnit(SchemaBase):
    """A TimeUnit json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/TimeUnit', 'definitions': Root._json_schema['definitions']}
    def __init__(self, *args, **kwds):
        super(TimeUnit, self).__init__(*args, **kwds)


class TimeUnitTransform(SchemaBase):
    """A TimeUnitTransform json schema wrapper"""
    _valid_attr_map = {'as': 'as_'}
    _json_schema = {'$ref': '#/definitions/TimeUnitTransform', 'definitions': Root._json_schema['definitions']}
    def __init__(self, as_, field, timeUnit):
        super(TimeUnitTransform, self).__init__(as_=as_, field=field, timeUnit=timeUnit)


class TitleOrient(SchemaBase):
    """A TitleOrient json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/TitleOrient', 'definitions': Root._json_schema['definitions']}
    def __init__(self, *args):
        super(TitleOrient, self).__init__(*args)


class TitleParams(SchemaBase):
    """A TitleParams json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/TitleParams', 'definitions': Root._json_schema['definitions']}
    def __init__(self, text, anchor=Undefined, offset=Undefined, orient=Undefined, style=Undefined):
        super(TitleParams, self).__init__(text=text, anchor=anchor, offset=offset, orient=orient, style=style)


class TopLevelFacetedUnitSpec(SchemaBase):
    """A TopLevelFacetedUnitSpec json schema wrapper"""
    _valid_attr_map = {'$schema': 'schema'}
    _json_schema = {'$ref': '#/definitions/TopLevel<FacetedUnitSpec>', 'definitions': Root._json_schema['definitions']}
    def __init__(self, encoding, mark, autosize=Undefined, background=Undefined, config=Undefined, data=Undefined, description=Undefined, height=Undefined, name=Undefined, padding=Undefined, projection=Undefined, schema=Undefined, selection=Undefined, title=Undefined, transform=Undefined, width=Undefined):
        super(TopLevelFacetedUnitSpec, self).__init__(encoding=encoding, mark=mark, autosize=autosize, background=background, config=config, data=data, description=description, height=height, name=name, padding=padding, projection=projection, schema=schema, selection=selection, title=title, transform=transform, width=width)


class TopLevelFacetSpec(SchemaBase):
    """A TopLevelFacetSpec json schema wrapper"""
    _valid_attr_map = {'$schema': 'schema'}
    _json_schema = {'$ref': '#/definitions/TopLevel<FacetSpec>', 'definitions': Root._json_schema['definitions']}
    def __init__(self, facet, spec, autosize=Undefined, background=Undefined, config=Undefined, data=Undefined, description=Undefined, name=Undefined, padding=Undefined, resolve=Undefined, schema=Undefined, title=Undefined, transform=Undefined):
        super(TopLevelFacetSpec, self).__init__(facet=facet, spec=spec, autosize=autosize, background=background, config=config, data=data, description=description, name=name, padding=padding, resolve=resolve, schema=schema, title=title, transform=transform)


class TopLevelHConcatSpec(SchemaBase):
    """A TopLevelHConcatSpec json schema wrapper"""
    _valid_attr_map = {'$schema': 'schema'}
    _json_schema = {'$ref': '#/definitions/TopLevel<HConcatSpec>', 'definitions': Root._json_schema['definitions']}
    def __init__(self, hconcat, autosize=Undefined, background=Undefined, config=Undefined, data=Undefined, description=Undefined, name=Undefined, padding=Undefined, resolve=Undefined, schema=Undefined, title=Undefined, transform=Undefined):
        super(TopLevelHConcatSpec, self).__init__(hconcat=hconcat, autosize=autosize, background=background, config=config, data=data, description=description, name=name, padding=padding, resolve=resolve, schema=schema, title=title, transform=transform)


class TopLevelLayerSpec(SchemaBase):
    """A TopLevelLayerSpec json schema wrapper"""
    _valid_attr_map = {'$schema': 'schema'}
    _json_schema = {'$ref': '#/definitions/TopLevel<LayerSpec>', 'definitions': Root._json_schema['definitions']}
    def __init__(self, layer, autosize=Undefined, background=Undefined, config=Undefined, data=Undefined, description=Undefined, height=Undefined, name=Undefined, padding=Undefined, resolve=Undefined, schema=Undefined, title=Undefined, transform=Undefined, width=Undefined):
        super(TopLevelLayerSpec, self).__init__(layer=layer, autosize=autosize, background=background, config=config, data=data, description=description, height=height, name=name, padding=padding, resolve=resolve, schema=schema, title=title, transform=transform, width=width)


class TopLevelRepeatSpec(SchemaBase):
    """A TopLevelRepeatSpec json schema wrapper"""
    _valid_attr_map = {'$schema': 'schema'}
    _json_schema = {'$ref': '#/definitions/TopLevel<RepeatSpec>', 'definitions': Root._json_schema['definitions']}
    def __init__(self, repeat, spec, autosize=Undefined, background=Undefined, config=Undefined, data=Undefined, description=Undefined, name=Undefined, padding=Undefined, resolve=Undefined, schema=Undefined, title=Undefined, transform=Undefined):
        super(TopLevelRepeatSpec, self).__init__(repeat=repeat, spec=spec, autosize=autosize, background=background, config=config, data=data, description=description, name=name, padding=padding, resolve=resolve, schema=schema, title=title, transform=transform)


class TopLevelVConcatSpec(SchemaBase):
    """A TopLevelVConcatSpec json schema wrapper"""
    _valid_attr_map = {'$schema': 'schema'}
    _json_schema = {'$ref': '#/definitions/TopLevel<VConcatSpec>', 'definitions': Root._json_schema['definitions']}
    def __init__(self, vconcat, autosize=Undefined, background=Undefined, config=Undefined, data=Undefined, description=Undefined, name=Undefined, padding=Undefined, resolve=Undefined, schema=Undefined, title=Undefined, transform=Undefined):
        super(TopLevelVConcatSpec, self).__init__(vconcat=vconcat, autosize=autosize, background=background, config=config, data=data, description=description, name=name, padding=padding, resolve=resolve, schema=schema, title=title, transform=transform)


class TopLevelExtendedSpec(SchemaBase):
    """A TopLevelExtendedSpec json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/TopLevelExtendedSpec', 'definitions': Root._json_schema['definitions']}
    def __init__(self, *args, **kwds):
        super(TopLevelExtendedSpec, self).__init__(*args, **kwds)


class TopoDataFormat(SchemaBase):
    """A TopoDataFormat json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/TopoDataFormat', 'definitions': Root._json_schema['definitions']}
    def __init__(self, feature=Undefined, mesh=Undefined, parse=Undefined, type=Undefined):
        super(TopoDataFormat, self).__init__(feature=feature, mesh=mesh, parse=parse, type=type)


class Transform(SchemaBase):
    """A Transform json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/Transform', 'definitions': Root._json_schema['definitions']}
    def __init__(self, *args, **kwds):
        super(Transform, self).__init__(*args, **kwds)


class Type(SchemaBase):
    """A Type json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/Type', 'definitions': Root._json_schema['definitions']}
    def __init__(self, *args, **kwds):
        super(Type, self).__init__(*args, **kwds)


class UrlData(SchemaBase):
    """A UrlData json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/UrlData', 'definitions': Root._json_schema['definitions']}
    def __init__(self, url, format=Undefined):
        super(UrlData, self).__init__(url=url, format=format)


class UtcMultiTimeUnit(SchemaBase):
    """A UtcMultiTimeUnit json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/UtcMultiTimeUnit', 'definitions': Root._json_schema['definitions']}
    def __init__(self, *args):
        super(UtcMultiTimeUnit, self).__init__(*args)


class UtcSingleTimeUnit(SchemaBase):
    """A UtcSingleTimeUnit json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/UtcSingleTimeUnit', 'definitions': Root._json_schema['definitions']}
    def __init__(self, *args):
        super(UtcSingleTimeUnit, self).__init__(*args)


class ValueDef(SchemaBase):
    """A ValueDef json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/ValueDef', 'definitions': Root._json_schema['definitions']}
    def __init__(self, value):
        super(ValueDef, self).__init__(value=value)


class ValueDefWithCondition(SchemaBase):
    """A ValueDefWithCondition json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/ValueDefWithCondition', 'definitions': Root._json_schema['definitions']}
    def __init__(self, condition=Undefined, value=Undefined):
        super(ValueDefWithCondition, self).__init__(condition=condition, value=value)


class MarkPropValueDefWithCondition(SchemaBase):
    """A MarkPropValueDefWithCondition json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/MarkPropValueDefWithCondition', 'definitions': Root._json_schema['definitions']}
    def __init__(self, condition=Undefined, value=Undefined):
        super(MarkPropValueDefWithCondition, self).__init__(condition=condition, value=value)


class TextValueDefWithCondition(SchemaBase):
    """A TextValueDefWithCondition json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/TextValueDefWithCondition', 'definitions': Root._json_schema['definitions']}
    def __init__(self, condition=Undefined, value=Undefined):
        super(TextValueDefWithCondition, self).__init__(condition=condition, value=value)


class VerticalAlign(SchemaBase):
    """A VerticalAlign json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/VerticalAlign', 'definitions': Root._json_schema['definitions']}
    def __init__(self, *args):
        super(VerticalAlign, self).__init__(*args)


class VgAxisConfig(SchemaBase):
    """A VgAxisConfig json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/VgAxisConfig', 'definitions': Root._json_schema['definitions']}
    def __init__(self, bandPosition=Undefined, domain=Undefined, domainColor=Undefined, domainWidth=Undefined, grid=Undefined, gridColor=Undefined, gridDash=Undefined, gridOpacity=Undefined, gridWidth=Undefined, labelAngle=Undefined, labelBound=Undefined, labelColor=Undefined, labelFlush=Undefined, labelFont=Undefined, labelFontSize=Undefined, labelLimit=Undefined, labelOverlap=Undefined, labelPadding=Undefined, labels=Undefined, maxExtent=Undefined, minExtent=Undefined, tickColor=Undefined, tickRound=Undefined, tickSize=Undefined, tickWidth=Undefined, ticks=Undefined, titleAlign=Undefined, titleAngle=Undefined, titleBaseline=Undefined, titleColor=Undefined, titleFont=Undefined, titleFontSize=Undefined, titleFontWeight=Undefined, titleLimit=Undefined, titleMaxLength=Undefined, titlePadding=Undefined, titleX=Undefined, titleY=Undefined):
        super(VgAxisConfig, self).__init__(bandPosition=bandPosition, domain=domain, domainColor=domainColor, domainWidth=domainWidth, grid=grid, gridColor=gridColor, gridDash=gridDash, gridOpacity=gridOpacity, gridWidth=gridWidth, labelAngle=labelAngle, labelBound=labelBound, labelColor=labelColor, labelFlush=labelFlush, labelFont=labelFont, labelFontSize=labelFontSize, labelLimit=labelLimit, labelOverlap=labelOverlap, labelPadding=labelPadding, labels=labels, maxExtent=maxExtent, minExtent=minExtent, tickColor=tickColor, tickRound=tickRound, tickSize=tickSize, tickWidth=tickWidth, ticks=ticks, titleAlign=titleAlign, titleAngle=titleAngle, titleBaseline=titleBaseline, titleColor=titleColor, titleFont=titleFont, titleFontSize=titleFontSize, titleFontWeight=titleFontWeight, titleLimit=titleLimit, titleMaxLength=titleMaxLength, titlePadding=titlePadding, titleX=titleX, titleY=titleY)


class VgBinding(SchemaBase):
    """A VgBinding json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/VgBinding', 'definitions': Root._json_schema['definitions']}
    def __init__(self, *args, **kwds):
        super(VgBinding, self).__init__(*args, **kwds)


class VgCheckboxBinding(SchemaBase):
    """A VgCheckboxBinding json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/VgCheckboxBinding', 'definitions': Root._json_schema['definitions']}
    def __init__(self, input, element=Undefined):
        super(VgCheckboxBinding, self).__init__(input=input, element=element)


class VgEventStream(SchemaBase):
    """A VgEventStream json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/VgEventStream', 'definitions': Root._json_schema['definitions']}
    def __init__(self, **kwds):
        super(VgEventStream, self).__init__(**kwds)


class VgGenericBinding(SchemaBase):
    """A VgGenericBinding json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/VgGenericBinding', 'definitions': Root._json_schema['definitions']}
    def __init__(self, input, element=Undefined):
        super(VgGenericBinding, self).__init__(input=input, element=element)


class VgMarkConfig(SchemaBase):
    """A VgMarkConfig json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/VgMarkConfig', 'definitions': Root._json_schema['definitions']}
    def __init__(self, align=Undefined, angle=Undefined, baseline=Undefined, cursor=Undefined, dx=Undefined, dy=Undefined, fill=Undefined, fillOpacity=Undefined, font=Undefined, fontSize=Undefined, fontStyle=Undefined, fontWeight=Undefined, href=Undefined, interpolate=Undefined, limit=Undefined, opacity=Undefined, orient=Undefined, radius=Undefined, shape=Undefined, size=Undefined, stroke=Undefined, strokeDash=Undefined, strokeDashOffset=Undefined, strokeOpacity=Undefined, strokeWidth=Undefined, tension=Undefined, text=Undefined, theta=Undefined):
        super(VgMarkConfig, self).__init__(align=align, angle=angle, baseline=baseline, cursor=cursor, dx=dx, dy=dy, fill=fill, fillOpacity=fillOpacity, font=font, fontSize=fontSize, fontStyle=fontStyle, fontWeight=fontWeight, href=href, interpolate=interpolate, limit=limit, opacity=opacity, orient=orient, radius=radius, shape=shape, size=size, stroke=stroke, strokeDash=strokeDash, strokeDashOffset=strokeDashOffset, strokeOpacity=strokeOpacity, strokeWidth=strokeWidth, tension=tension, text=text, theta=theta)


class VgProjectionType(SchemaBase):
    """A VgProjectionType json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/VgProjectionType', 'definitions': Root._json_schema['definitions']}
    def __init__(self, *args):
        super(VgProjectionType, self).__init__(*args)


class VgRadioBinding(SchemaBase):
    """A VgRadioBinding json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/VgRadioBinding', 'definitions': Root._json_schema['definitions']}
    def __init__(self, input, options, element=Undefined):
        super(VgRadioBinding, self).__init__(input=input, options=options, element=element)


class VgRangeBinding(SchemaBase):
    """A VgRangeBinding json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/VgRangeBinding', 'definitions': Root._json_schema['definitions']}
    def __init__(self, input, element=Undefined, max=Undefined, min=Undefined, step=Undefined):
        super(VgRangeBinding, self).__init__(input=input, element=element, max=max, min=min, step=step)


class VgScheme(SchemaBase):
    """A VgScheme json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/VgScheme', 'definitions': Root._json_schema['definitions']}
    def __init__(self, scheme, count=Undefined, extent=Undefined):
        super(VgScheme, self).__init__(scheme=scheme, count=count, extent=extent)


class VgSelectBinding(SchemaBase):
    """A VgSelectBinding json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/VgSelectBinding', 'definitions': Root._json_schema['definitions']}
    def __init__(self, input, options, element=Undefined):
        super(VgSelectBinding, self).__init__(input=input, options=options, element=element)


class VgTitleConfig(SchemaBase):
    """A VgTitleConfig json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/VgTitleConfig', 'definitions': Root._json_schema['definitions']}
    def __init__(self, anchor=Undefined, angle=Undefined, baseline=Undefined, color=Undefined, font=Undefined, fontSize=Undefined, fontWeight=Undefined, limit=Undefined, offset=Undefined, orient=Undefined):
        super(VgTitleConfig, self).__init__(anchor=anchor, angle=angle, baseline=baseline, color=color, font=font, fontSize=fontSize, fontWeight=fontWeight, limit=limit, offset=offset, orient=orient)


class ViewConfig(SchemaBase):
    """A ViewConfig json schema wrapper"""
    _valid_attr_map = {}
    _json_schema = {'$ref': '#/definitions/ViewConfig', 'definitions': Root._json_schema['definitions']}
    def __init__(self, clip=Undefined, fill=Undefined, fillOpacity=Undefined, height=Undefined, stroke=Undefined, strokeDash=Undefined, strokeDashOffset=Undefined, strokeOpacity=Undefined, strokeWidth=Undefined, width=Undefined):
        super(ViewConfig, self).__init__(clip=clip, fill=fill, fillOpacity=fillOpacity, height=height, stroke=stroke, strokeDash=strokeDash, strokeDashOffset=strokeDashOffset, strokeOpacity=strokeOpacity, strokeWidth=strokeWidth, width=width)

