# The contents of this file are automatically generated
# at time 2018-02-06 12:58:28

from altair.schema.base import SchemaBase
from altair.schema.loader import load_schema


class Root(SchemaBase):
    """Root schema wrapper"""
    _json_schema = load_schema()


class Aggregate(SchemaBase):
    """Aggregate schema wrapper"""
    _json_schema = {'$ref': '#/definitions/Aggregate', 'definitions': Root._json_schema['definitions']}


class AggregateOp(SchemaBase):
    """AggregateOp schema wrapper"""
    _json_schema = {'$ref': '#/definitions/AggregateOp', 'definitions': Root._json_schema['definitions']}


class AggregateTransform(SchemaBase):
    """AggregateTransform schema wrapper"""
    _json_schema = {'$ref': '#/definitions/AggregateTransform', 'definitions': Root._json_schema['definitions']}


class AggregatedFieldDef(SchemaBase):
    """AggregatedFieldDef schema wrapper"""
    _json_schema = {'$ref': '#/definitions/AggregatedFieldDef', 'definitions': Root._json_schema['definitions']}


class Anchor(SchemaBase):
    """Anchor schema wrapper"""
    _json_schema = {'$ref': '#/definitions/Anchor', 'definitions': Root._json_schema['definitions']}


class AnyMark(SchemaBase):
    """AnyMark schema wrapper"""
    _json_schema = {'$ref': '#/definitions/AnyMark', 'definitions': Root._json_schema['definitions']}


class AutoSizeParams(SchemaBase):
    """AutoSizeParams schema wrapper"""
    _json_schema = {'$ref': '#/definitions/AutoSizeParams', 'definitions': Root._json_schema['definitions']}


class AutosizeType(SchemaBase):
    """AutosizeType schema wrapper"""
    _json_schema = {'$ref': '#/definitions/AutosizeType', 'definitions': Root._json_schema['definitions']}


class Axis(SchemaBase):
    """Axis schema wrapper"""
    _json_schema = {'$ref': '#/definitions/Axis', 'definitions': Root._json_schema['definitions']}


class AxisConfig(SchemaBase):
    """AxisConfig schema wrapper"""
    _json_schema = {'$ref': '#/definitions/AxisConfig', 'definitions': Root._json_schema['definitions']}


class AxisOrient(SchemaBase):
    """AxisOrient schema wrapper"""
    _json_schema = {'$ref': '#/definitions/AxisOrient', 'definitions': Root._json_schema['definitions']}


class AxisResolveMap(SchemaBase):
    """AxisResolveMap schema wrapper"""
    _json_schema = {'$ref': '#/definitions/AxisResolveMap', 'definitions': Root._json_schema['definitions']}


class BarConfig(SchemaBase):
    """BarConfig schema wrapper"""
    _json_schema = {'$ref': '#/definitions/BarConfig', 'definitions': Root._json_schema['definitions']}


class BasicType(SchemaBase):
    """BasicType schema wrapper"""
    _json_schema = {'$ref': '#/definitions/BasicType', 'definitions': Root._json_schema['definitions']}


class BinParams(SchemaBase):
    """BinParams schema wrapper"""
    _json_schema = {'$ref': '#/definitions/BinParams', 'definitions': Root._json_schema['definitions']}


class BinTransform(SchemaBase):
    """BinTransform schema wrapper"""
    _json_schema = {'$ref': '#/definitions/BinTransform', 'definitions': Root._json_schema['definitions']}


class BrushConfig(SchemaBase):
    """BrushConfig schema wrapper"""
    _json_schema = {'$ref': '#/definitions/BrushConfig', 'definitions': Root._json_schema['definitions']}


class CalculateTransform(SchemaBase):
    """CalculateTransform schema wrapper"""
    _json_schema = {'$ref': '#/definitions/CalculateTransform', 'definitions': Root._json_schema['definitions']}


class CompositeUnitSpec(SchemaBase):
    """CompositeUnitSpec schema wrapper"""
    _json_schema = {'$ref': '#/definitions/CompositeUnitSpec', 'definitions': Root._json_schema['definitions']}


class ConditionalFieldDef(SchemaBase):
    """ConditionalFieldDef schema wrapper"""
    _json_schema = {'$ref': '#/definitions/Conditional<FieldDef>', 'definitions': Root._json_schema['definitions']}


class ConditionalMarkPropFieldDef(SchemaBase):
    """ConditionalMarkPropFieldDef schema wrapper"""
    _json_schema = {'$ref': '#/definitions/Conditional<MarkPropFieldDef>', 'definitions': Root._json_schema['definitions']}


class ConditionalTextFieldDef(SchemaBase):
    """ConditionalTextFieldDef schema wrapper"""
    _json_schema = {'$ref': '#/definitions/Conditional<TextFieldDef>', 'definitions': Root._json_schema['definitions']}


class ConditionalValueDef(SchemaBase):
    """ConditionalValueDef schema wrapper"""
    _json_schema = {'$ref': '#/definitions/Conditional<ValueDef>', 'definitions': Root._json_schema['definitions']}


class ConditionalPredicateFieldDef(SchemaBase):
    """ConditionalPredicateFieldDef schema wrapper"""
    _json_schema = {'$ref': '#/definitions/ConditionalPredicate<FieldDef>', 'definitions': Root._json_schema['definitions']}


class ConditionalPredicateMarkPropFieldDef(SchemaBase):
    """ConditionalPredicateMarkPropFieldDef schema wrapper"""
    _json_schema = {'$ref': '#/definitions/ConditionalPredicate<MarkPropFieldDef>', 'definitions': Root._json_schema['definitions']}


class ConditionalPredicateTextFieldDef(SchemaBase):
    """ConditionalPredicateTextFieldDef schema wrapper"""
    _json_schema = {'$ref': '#/definitions/ConditionalPredicate<TextFieldDef>', 'definitions': Root._json_schema['definitions']}


class ConditionalPredicateValueDef(SchemaBase):
    """ConditionalPredicateValueDef schema wrapper"""
    _json_schema = {'$ref': '#/definitions/ConditionalPredicate<ValueDef>', 'definitions': Root._json_schema['definitions']}


class ConditionalSelectionFieldDef(SchemaBase):
    """ConditionalSelectionFieldDef schema wrapper"""
    _json_schema = {'$ref': '#/definitions/ConditionalSelection<FieldDef>', 'definitions': Root._json_schema['definitions']}


class ConditionalSelectionMarkPropFieldDef(SchemaBase):
    """ConditionalSelectionMarkPropFieldDef schema wrapper"""
    _json_schema = {'$ref': '#/definitions/ConditionalSelection<MarkPropFieldDef>', 'definitions': Root._json_schema['definitions']}


class ConditionalSelectionTextFieldDef(SchemaBase):
    """ConditionalSelectionTextFieldDef schema wrapper"""
    _json_schema = {'$ref': '#/definitions/ConditionalSelection<TextFieldDef>', 'definitions': Root._json_schema['definitions']}


class ConditionalSelectionValueDef(SchemaBase):
    """ConditionalSelectionValueDef schema wrapper"""
    _json_schema = {'$ref': '#/definitions/ConditionalSelection<ValueDef>', 'definitions': Root._json_schema['definitions']}


class Config(SchemaBase):
    """Config schema wrapper"""
    _json_schema = {'$ref': '#/definitions/Config', 'definitions': Root._json_schema['definitions']}


class CsvDataFormat(SchemaBase):
    """CsvDataFormat schema wrapper"""
    _json_schema = {'$ref': '#/definitions/CsvDataFormat', 'definitions': Root._json_schema['definitions']}


class Data(SchemaBase):
    """Data schema wrapper"""
    _json_schema = {'$ref': '#/definitions/Data', 'definitions': Root._json_schema['definitions']}


class DataFormat(SchemaBase):
    """DataFormat schema wrapper"""
    _json_schema = {'$ref': '#/definitions/DataFormat', 'definitions': Root._json_schema['definitions']}


class DateTime(SchemaBase):
    """DateTime schema wrapper"""
    _json_schema = {'$ref': '#/definitions/DateTime', 'definitions': Root._json_schema['definitions']}


class Day(SchemaBase):
    """Day schema wrapper"""
    _json_schema = {'$ref': '#/definitions/Day', 'definitions': Root._json_schema['definitions']}


class Encoding(SchemaBase):
    """Encoding schema wrapper"""
    _json_schema = {'$ref': '#/definitions/Encoding', 'definitions': Root._json_schema['definitions']}


class EncodingWithFacet(SchemaBase):
    """EncodingWithFacet schema wrapper"""
    _json_schema = {'$ref': '#/definitions/EncodingWithFacet', 'definitions': Root._json_schema['definitions']}


class FacetFieldDef(SchemaBase):
    """FacetFieldDef schema wrapper"""
    _json_schema = {'$ref': '#/definitions/FacetFieldDef', 'definitions': Root._json_schema['definitions']}


class FacetMapping(SchemaBase):
    """FacetMapping schema wrapper"""
    _json_schema = {'$ref': '#/definitions/FacetMapping', 'definitions': Root._json_schema['definitions']}


class FieldDef(SchemaBase):
    """FieldDef schema wrapper"""
    _json_schema = {'$ref': '#/definitions/FieldDef', 'definitions': Root._json_schema['definitions']}


class FieldDefWithCondition(SchemaBase):
    """FieldDefWithCondition schema wrapper"""
    _json_schema = {'$ref': '#/definitions/FieldDefWithCondition', 'definitions': Root._json_schema['definitions']}


class MarkPropFieldDefWithCondition(SchemaBase):
    """MarkPropFieldDefWithCondition schema wrapper"""
    _json_schema = {'$ref': '#/definitions/MarkPropFieldDefWithCondition', 'definitions': Root._json_schema['definitions']}


class TextFieldDefWithCondition(SchemaBase):
    """TextFieldDefWithCondition schema wrapper"""
    _json_schema = {'$ref': '#/definitions/TextFieldDefWithCondition', 'definitions': Root._json_schema['definitions']}


class FieldEqualPredicate(SchemaBase):
    """FieldEqualPredicate schema wrapper"""
    _json_schema = {'$ref': '#/definitions/FieldEqualPredicate', 'definitions': Root._json_schema['definitions']}


class FieldOneOfPredicate(SchemaBase):
    """FieldOneOfPredicate schema wrapper"""
    _json_schema = {'$ref': '#/definitions/FieldOneOfPredicate', 'definitions': Root._json_schema['definitions']}


class FieldRangePredicate(SchemaBase):
    """FieldRangePredicate schema wrapper"""
    _json_schema = {'$ref': '#/definitions/FieldRangePredicate', 'definitions': Root._json_schema['definitions']}


class FilterTransform(SchemaBase):
    """FilterTransform schema wrapper"""
    _json_schema = {'$ref': '#/definitions/FilterTransform', 'definitions': Root._json_schema['definitions']}


class FontStyle(SchemaBase):
    """FontStyle schema wrapper"""
    _json_schema = {'$ref': '#/definitions/FontStyle', 'definitions': Root._json_schema['definitions']}


class FontWeight(SchemaBase):
    """FontWeight schema wrapper"""
    _json_schema = {'$ref': '#/definitions/FontWeight', 'definitions': Root._json_schema['definitions']}


class FontWeightNumber(SchemaBase):
    """FontWeightNumber schema wrapper"""
    _json_schema = {'$ref': '#/definitions/FontWeightNumber', 'definitions': Root._json_schema['definitions']}


class FacetSpec(SchemaBase):
    """FacetSpec schema wrapper"""
    _json_schema = {'$ref': '#/definitions/FacetSpec', 'definitions': Root._json_schema['definitions']}


class HConcatSpec(SchemaBase):
    """HConcatSpec schema wrapper"""
    _json_schema = {'$ref': '#/definitions/HConcatSpec', 'definitions': Root._json_schema['definitions']}


class LayerSpec(SchemaBase):
    """LayerSpec schema wrapper"""
    _json_schema = {'$ref': '#/definitions/LayerSpec', 'definitions': Root._json_schema['definitions']}


class RepeatSpec(SchemaBase):
    """RepeatSpec schema wrapper"""
    _json_schema = {'$ref': '#/definitions/RepeatSpec', 'definitions': Root._json_schema['definitions']}


class Spec(SchemaBase):
    """Spec schema wrapper"""
    _json_schema = {'$ref': '#/definitions/Spec', 'definitions': Root._json_schema['definitions']}


class CompositeUnitSpecAlias(SchemaBase):
    """CompositeUnitSpecAlias schema wrapper"""
    _json_schema = {'$ref': '#/definitions/CompositeUnitSpecAlias', 'definitions': Root._json_schema['definitions']}


class FacetedCompositeUnitSpecAlias(SchemaBase):
    """FacetedCompositeUnitSpecAlias schema wrapper"""
    _json_schema = {'$ref': '#/definitions/FacetedCompositeUnitSpecAlias', 'definitions': Root._json_schema['definitions']}


class VConcatSpec(SchemaBase):
    """VConcatSpec schema wrapper"""
    _json_schema = {'$ref': '#/definitions/VConcatSpec', 'definitions': Root._json_schema['definitions']}


class GeoType(SchemaBase):
    """GeoType schema wrapper"""
    _json_schema = {'$ref': '#/definitions/GeoType', 'definitions': Root._json_schema['definitions']}


class Header(SchemaBase):
    """Header schema wrapper"""
    _json_schema = {'$ref': '#/definitions/Header', 'definitions': Root._json_schema['definitions']}


class HorizontalAlign(SchemaBase):
    """HorizontalAlign schema wrapper"""
    _json_schema = {'$ref': '#/definitions/HorizontalAlign', 'definitions': Root._json_schema['definitions']}


class InlineData(SchemaBase):
    """InlineData schema wrapper"""
    _json_schema = {'$ref': '#/definitions/InlineData', 'definitions': Root._json_schema['definitions']}


class Interpolate(SchemaBase):
    """Interpolate schema wrapper"""
    _json_schema = {'$ref': '#/definitions/Interpolate', 'definitions': Root._json_schema['definitions']}


class InterpolateParams(SchemaBase):
    """InterpolateParams schema wrapper"""
    _json_schema = {'$ref': '#/definitions/InterpolateParams', 'definitions': Root._json_schema['definitions']}


class IntervalSelection(SchemaBase):
    """IntervalSelection schema wrapper"""
    _json_schema = {'$ref': '#/definitions/IntervalSelection', 'definitions': Root._json_schema['definitions']}


class IntervalSelectionConfig(SchemaBase):
    """IntervalSelectionConfig schema wrapper"""
    _json_schema = {'$ref': '#/definitions/IntervalSelectionConfig', 'definitions': Root._json_schema['definitions']}


class JsonDataFormat(SchemaBase):
    """JsonDataFormat schema wrapper"""
    _json_schema = {'$ref': '#/definitions/JsonDataFormat', 'definitions': Root._json_schema['definitions']}


class Legend(SchemaBase):
    """Legend schema wrapper"""
    _json_schema = {'$ref': '#/definitions/Legend', 'definitions': Root._json_schema['definitions']}


class LegendConfig(SchemaBase):
    """LegendConfig schema wrapper"""
    _json_schema = {'$ref': '#/definitions/LegendConfig', 'definitions': Root._json_schema['definitions']}


class LegendOrient(SchemaBase):
    """LegendOrient schema wrapper"""
    _json_schema = {'$ref': '#/definitions/LegendOrient', 'definitions': Root._json_schema['definitions']}


class LegendResolveMap(SchemaBase):
    """LegendResolveMap schema wrapper"""
    _json_schema = {'$ref': '#/definitions/LegendResolveMap', 'definitions': Root._json_schema['definitions']}


class LocalMultiTimeUnit(SchemaBase):
    """LocalMultiTimeUnit schema wrapper"""
    _json_schema = {'$ref': '#/definitions/LocalMultiTimeUnit', 'definitions': Root._json_schema['definitions']}


class LocalSingleTimeUnit(SchemaBase):
    """LocalSingleTimeUnit schema wrapper"""
    _json_schema = {'$ref': '#/definitions/LocalSingleTimeUnit', 'definitions': Root._json_schema['definitions']}


class LogicalAndPredicate(SchemaBase):
    """LogicalAndPredicate schema wrapper"""
    _json_schema = {'$ref': '#/definitions/LogicalAnd<Predicate>', 'definitions': Root._json_schema['definitions']}


class SelectionAnd(SchemaBase):
    """SelectionAnd schema wrapper"""
    _json_schema = {'$ref': '#/definitions/SelectionAnd', 'definitions': Root._json_schema['definitions']}


class LogicalNotPredicate(SchemaBase):
    """LogicalNotPredicate schema wrapper"""
    _json_schema = {'$ref': '#/definitions/LogicalNot<Predicate>', 'definitions': Root._json_schema['definitions']}


class SelectionNot(SchemaBase):
    """SelectionNot schema wrapper"""
    _json_schema = {'$ref': '#/definitions/SelectionNot', 'definitions': Root._json_schema['definitions']}


class LogicalOperandPredicate(SchemaBase):
    """LogicalOperandPredicate schema wrapper"""
    _json_schema = {'$ref': '#/definitions/LogicalOperand<Predicate>', 'definitions': Root._json_schema['definitions']}


class SelectionOperand(SchemaBase):
    """SelectionOperand schema wrapper"""
    _json_schema = {'$ref': '#/definitions/SelectionOperand', 'definitions': Root._json_schema['definitions']}


class LogicalOrPredicate(SchemaBase):
    """LogicalOrPredicate schema wrapper"""
    _json_schema = {'$ref': '#/definitions/LogicalOr<Predicate>', 'definitions': Root._json_schema['definitions']}


class SelectionOr(SchemaBase):
    """SelectionOr schema wrapper"""
    _json_schema = {'$ref': '#/definitions/SelectionOr', 'definitions': Root._json_schema['definitions']}


class LookupData(SchemaBase):
    """LookupData schema wrapper"""
    _json_schema = {'$ref': '#/definitions/LookupData', 'definitions': Root._json_schema['definitions']}


class LookupTransform(SchemaBase):
    """LookupTransform schema wrapper"""
    _json_schema = {'$ref': '#/definitions/LookupTransform', 'definitions': Root._json_schema['definitions']}


class Mark(SchemaBase):
    """Mark schema wrapper"""
    _json_schema = {'$ref': '#/definitions/Mark', 'definitions': Root._json_schema['definitions']}


class MarkConfig(SchemaBase):
    """MarkConfig schema wrapper"""
    _json_schema = {'$ref': '#/definitions/MarkConfig', 'definitions': Root._json_schema['definitions']}


class MarkDef(SchemaBase):
    """MarkDef schema wrapper"""
    _json_schema = {'$ref': '#/definitions/MarkDef', 'definitions': Root._json_schema['definitions']}


class Month(SchemaBase):
    """Month schema wrapper"""
    _json_schema = {'$ref': '#/definitions/Month', 'definitions': Root._json_schema['definitions']}


class MultiSelection(SchemaBase):
    """MultiSelection schema wrapper"""
    _json_schema = {'$ref': '#/definitions/MultiSelection', 'definitions': Root._json_schema['definitions']}


class MultiSelectionConfig(SchemaBase):
    """MultiSelectionConfig schema wrapper"""
    _json_schema = {'$ref': '#/definitions/MultiSelectionConfig', 'definitions': Root._json_schema['definitions']}


class MultiTimeUnit(SchemaBase):
    """MultiTimeUnit schema wrapper"""
    _json_schema = {'$ref': '#/definitions/MultiTimeUnit', 'definitions': Root._json_schema['definitions']}


class NamedData(SchemaBase):
    """NamedData schema wrapper"""
    _json_schema = {'$ref': '#/definitions/NamedData', 'definitions': Root._json_schema['definitions']}


class NiceTime(SchemaBase):
    """NiceTime schema wrapper"""
    _json_schema = {'$ref': '#/definitions/NiceTime', 'definitions': Root._json_schema['definitions']}


class OrderFieldDef(SchemaBase):
    """OrderFieldDef schema wrapper"""
    _json_schema = {'$ref': '#/definitions/OrderFieldDef', 'definitions': Root._json_schema['definitions']}


class Orient(SchemaBase):
    """Orient schema wrapper"""
    _json_schema = {'$ref': '#/definitions/Orient', 'definitions': Root._json_schema['definitions']}


class Padding(SchemaBase):
    """Padding schema wrapper"""
    _json_schema = {'$ref': '#/definitions/Padding', 'definitions': Root._json_schema['definitions']}


class PositionFieldDef(SchemaBase):
    """PositionFieldDef schema wrapper"""
    _json_schema = {'$ref': '#/definitions/PositionFieldDef', 'definitions': Root._json_schema['definitions']}


class Predicate(SchemaBase):
    """Predicate schema wrapper"""
    _json_schema = {'$ref': '#/definitions/Predicate', 'definitions': Root._json_schema['definitions']}


class Projection(SchemaBase):
    """Projection schema wrapper"""
    _json_schema = {'$ref': '#/definitions/Projection', 'definitions': Root._json_schema['definitions']}


class ProjectionConfig(SchemaBase):
    """ProjectionConfig schema wrapper"""
    _json_schema = {'$ref': '#/definitions/ProjectionConfig', 'definitions': Root._json_schema['definitions']}


class ProjectionType(SchemaBase):
    """ProjectionType schema wrapper"""
    _json_schema = {'$ref': '#/definitions/ProjectionType', 'definitions': Root._json_schema['definitions']}


class RangeConfig(SchemaBase):
    """RangeConfig schema wrapper"""
    _json_schema = {'$ref': '#/definitions/RangeConfig', 'definitions': Root._json_schema['definitions']}


class RangeConfigValue(SchemaBase):
    """RangeConfigValue schema wrapper"""
    _json_schema = {'$ref': '#/definitions/RangeConfigValue', 'definitions': Root._json_schema['definitions']}


class Repeat(SchemaBase):
    """Repeat schema wrapper"""
    _json_schema = {'$ref': '#/definitions/Repeat', 'definitions': Root._json_schema['definitions']}


class RepeatRef(SchemaBase):
    """RepeatRef schema wrapper"""
    _json_schema = {'$ref': '#/definitions/RepeatRef', 'definitions': Root._json_schema['definitions']}


class Resolve(SchemaBase):
    """Resolve schema wrapper"""
    _json_schema = {'$ref': '#/definitions/Resolve', 'definitions': Root._json_schema['definitions']}


class ResolveMode(SchemaBase):
    """ResolveMode schema wrapper"""
    _json_schema = {'$ref': '#/definitions/ResolveMode', 'definitions': Root._json_schema['definitions']}


class Scale(SchemaBase):
    """Scale schema wrapper"""
    _json_schema = {'$ref': '#/definitions/Scale', 'definitions': Root._json_schema['definitions']}


class ScaleConfig(SchemaBase):
    """ScaleConfig schema wrapper"""
    _json_schema = {'$ref': '#/definitions/ScaleConfig', 'definitions': Root._json_schema['definitions']}


class ScaleResolveMap(SchemaBase):
    """ScaleResolveMap schema wrapper"""
    _json_schema = {'$ref': '#/definitions/ScaleResolveMap', 'definitions': Root._json_schema['definitions']}


class ScaleType(SchemaBase):
    """ScaleType schema wrapper"""
    _json_schema = {'$ref': '#/definitions/ScaleType', 'definitions': Root._json_schema['definitions']}


class SchemeParams(SchemaBase):
    """SchemeParams schema wrapper"""
    _json_schema = {'$ref': '#/definitions/SchemeParams', 'definitions': Root._json_schema['definitions']}


class SelectionConfig(SchemaBase):
    """SelectionConfig schema wrapper"""
    _json_schema = {'$ref': '#/definitions/SelectionConfig', 'definitions': Root._json_schema['definitions']}


class SelectionDef(SchemaBase):
    """SelectionDef schema wrapper"""
    _json_schema = {'$ref': '#/definitions/SelectionDef', 'definitions': Root._json_schema['definitions']}


class SelectionDomain(SchemaBase):
    """SelectionDomain schema wrapper"""
    _json_schema = {'$ref': '#/definitions/SelectionDomain', 'definitions': Root._json_schema['definitions']}


class SelectionPredicate(SchemaBase):
    """SelectionPredicate schema wrapper"""
    _json_schema = {'$ref': '#/definitions/SelectionPredicate', 'definitions': Root._json_schema['definitions']}


class SelectionResolution(SchemaBase):
    """SelectionResolution schema wrapper"""
    _json_schema = {'$ref': '#/definitions/SelectionResolution', 'definitions': Root._json_schema['definitions']}


class SingleDefChannel(SchemaBase):
    """SingleDefChannel schema wrapper"""
    _json_schema = {'$ref': '#/definitions/SingleDefChannel', 'definitions': Root._json_schema['definitions']}


class SingleSelection(SchemaBase):
    """SingleSelection schema wrapper"""
    _json_schema = {'$ref': '#/definitions/SingleSelection', 'definitions': Root._json_schema['definitions']}


class SingleSelectionConfig(SchemaBase):
    """SingleSelectionConfig schema wrapper"""
    _json_schema = {'$ref': '#/definitions/SingleSelectionConfig', 'definitions': Root._json_schema['definitions']}


class SingleTimeUnit(SchemaBase):
    """SingleTimeUnit schema wrapper"""
    _json_schema = {'$ref': '#/definitions/SingleTimeUnit', 'definitions': Root._json_schema['definitions']}


class SortField(SchemaBase):
    """SortField schema wrapper"""
    _json_schema = {'$ref': '#/definitions/SortField', 'definitions': Root._json_schema['definitions']}


class SortOrder(SchemaBase):
    """SortOrder schema wrapper"""
    _json_schema = {'$ref': '#/definitions/SortOrder', 'definitions': Root._json_schema['definitions']}


class StackOffset(SchemaBase):
    """StackOffset schema wrapper"""
    _json_schema = {'$ref': '#/definitions/StackOffset', 'definitions': Root._json_schema['definitions']}


class StyleConfigIndex(SchemaBase):
    """StyleConfigIndex schema wrapper"""
    _json_schema = {'$ref': '#/definitions/StyleConfigIndex', 'definitions': Root._json_schema['definitions']}


class TextConfig(SchemaBase):
    """TextConfig schema wrapper"""
    _json_schema = {'$ref': '#/definitions/TextConfig', 'definitions': Root._json_schema['definitions']}


class TickConfig(SchemaBase):
    """TickConfig schema wrapper"""
    _json_schema = {'$ref': '#/definitions/TickConfig', 'definitions': Root._json_schema['definitions']}


class TimeUnit(SchemaBase):
    """TimeUnit schema wrapper"""
    _json_schema = {'$ref': '#/definitions/TimeUnit', 'definitions': Root._json_schema['definitions']}


class TimeUnitTransform(SchemaBase):
    """TimeUnitTransform schema wrapper"""
    _json_schema = {'$ref': '#/definitions/TimeUnitTransform', 'definitions': Root._json_schema['definitions']}


class TitleOrient(SchemaBase):
    """TitleOrient schema wrapper"""
    _json_schema = {'$ref': '#/definitions/TitleOrient', 'definitions': Root._json_schema['definitions']}


class TitleParams(SchemaBase):
    """TitleParams schema wrapper"""
    _json_schema = {'$ref': '#/definitions/TitleParams', 'definitions': Root._json_schema['definitions']}


class TopLevelFacetedUnitSpec(SchemaBase):
    """TopLevelFacetedUnitSpec schema wrapper"""
    _json_schema = {'$ref': '#/definitions/TopLevel<FacetedUnitSpec>', 'definitions': Root._json_schema['definitions']}


class TopLevelFacetSpec(SchemaBase):
    """TopLevelFacetSpec schema wrapper"""
    _json_schema = {'$ref': '#/definitions/TopLevel<FacetSpec>', 'definitions': Root._json_schema['definitions']}


class TopLevelHConcatSpec(SchemaBase):
    """TopLevelHConcatSpec schema wrapper"""
    _json_schema = {'$ref': '#/definitions/TopLevel<HConcatSpec>', 'definitions': Root._json_schema['definitions']}


class TopLevelLayerSpec(SchemaBase):
    """TopLevelLayerSpec schema wrapper"""
    _json_schema = {'$ref': '#/definitions/TopLevel<LayerSpec>', 'definitions': Root._json_schema['definitions']}


class TopLevelRepeatSpec(SchemaBase):
    """TopLevelRepeatSpec schema wrapper"""
    _json_schema = {'$ref': '#/definitions/TopLevel<RepeatSpec>', 'definitions': Root._json_schema['definitions']}


class TopLevelVConcatSpec(SchemaBase):
    """TopLevelVConcatSpec schema wrapper"""
    _json_schema = {'$ref': '#/definitions/TopLevel<VConcatSpec>', 'definitions': Root._json_schema['definitions']}


class TopLevelExtendedSpec(SchemaBase):
    """TopLevelExtendedSpec schema wrapper"""
    _json_schema = {'$ref': '#/definitions/TopLevelExtendedSpec', 'definitions': Root._json_schema['definitions']}


class TopoDataFormat(SchemaBase):
    """TopoDataFormat schema wrapper"""
    _json_schema = {'$ref': '#/definitions/TopoDataFormat', 'definitions': Root._json_schema['definitions']}


class Transform(SchemaBase):
    """Transform schema wrapper"""
    _json_schema = {'$ref': '#/definitions/Transform', 'definitions': Root._json_schema['definitions']}


class Type(SchemaBase):
    """Type schema wrapper"""
    _json_schema = {'$ref': '#/definitions/Type', 'definitions': Root._json_schema['definitions']}


class UrlData(SchemaBase):
    """UrlData schema wrapper"""
    _json_schema = {'$ref': '#/definitions/UrlData', 'definitions': Root._json_schema['definitions']}


class UtcMultiTimeUnit(SchemaBase):
    """UtcMultiTimeUnit schema wrapper"""
    _json_schema = {'$ref': '#/definitions/UtcMultiTimeUnit', 'definitions': Root._json_schema['definitions']}


class UtcSingleTimeUnit(SchemaBase):
    """UtcSingleTimeUnit schema wrapper"""
    _json_schema = {'$ref': '#/definitions/UtcSingleTimeUnit', 'definitions': Root._json_schema['definitions']}


class ValueDef(SchemaBase):
    """ValueDef schema wrapper"""
    _json_schema = {'$ref': '#/definitions/ValueDef', 'definitions': Root._json_schema['definitions']}


class ValueDefWithCondition(SchemaBase):
    """ValueDefWithCondition schema wrapper"""
    _json_schema = {'$ref': '#/definitions/ValueDefWithCondition', 'definitions': Root._json_schema['definitions']}


class MarkPropValueDefWithCondition(SchemaBase):
    """MarkPropValueDefWithCondition schema wrapper"""
    _json_schema = {'$ref': '#/definitions/MarkPropValueDefWithCondition', 'definitions': Root._json_schema['definitions']}


class TextValueDefWithCondition(SchemaBase):
    """TextValueDefWithCondition schema wrapper"""
    _json_schema = {'$ref': '#/definitions/TextValueDefWithCondition', 'definitions': Root._json_schema['definitions']}


class VerticalAlign(SchemaBase):
    """VerticalAlign schema wrapper"""
    _json_schema = {'$ref': '#/definitions/VerticalAlign', 'definitions': Root._json_schema['definitions']}


class VgAxisConfig(SchemaBase):
    """VgAxisConfig schema wrapper"""
    _json_schema = {'$ref': '#/definitions/VgAxisConfig', 'definitions': Root._json_schema['definitions']}


class VgBinding(SchemaBase):
    """VgBinding schema wrapper"""
    _json_schema = {'$ref': '#/definitions/VgBinding', 'definitions': Root._json_schema['definitions']}


class VgCheckboxBinding(SchemaBase):
    """VgCheckboxBinding schema wrapper"""
    _json_schema = {'$ref': '#/definitions/VgCheckboxBinding', 'definitions': Root._json_schema['definitions']}


class VgEventStream(SchemaBase):
    """VgEventStream schema wrapper"""
    _json_schema = {'$ref': '#/definitions/VgEventStream', 'definitions': Root._json_schema['definitions']}


class VgGenericBinding(SchemaBase):
    """VgGenericBinding schema wrapper"""
    _json_schema = {'$ref': '#/definitions/VgGenericBinding', 'definitions': Root._json_schema['definitions']}


class VgMarkConfig(SchemaBase):
    """VgMarkConfig schema wrapper"""
    _json_schema = {'$ref': '#/definitions/VgMarkConfig', 'definitions': Root._json_schema['definitions']}


class VgProjectionType(SchemaBase):
    """VgProjectionType schema wrapper"""
    _json_schema = {'$ref': '#/definitions/VgProjectionType', 'definitions': Root._json_schema['definitions']}


class VgRadioBinding(SchemaBase):
    """VgRadioBinding schema wrapper"""
    _json_schema = {'$ref': '#/definitions/VgRadioBinding', 'definitions': Root._json_schema['definitions']}


class VgRangeBinding(SchemaBase):
    """VgRangeBinding schema wrapper"""
    _json_schema = {'$ref': '#/definitions/VgRangeBinding', 'definitions': Root._json_schema['definitions']}


class VgScheme(SchemaBase):
    """VgScheme schema wrapper"""
    _json_schema = {'$ref': '#/definitions/VgScheme', 'definitions': Root._json_schema['definitions']}


class VgSelectBinding(SchemaBase):
    """VgSelectBinding schema wrapper"""
    _json_schema = {'$ref': '#/definitions/VgSelectBinding', 'definitions': Root._json_schema['definitions']}


class VgTitleConfig(SchemaBase):
    """VgTitleConfig schema wrapper"""
    _json_schema = {'$ref': '#/definitions/VgTitleConfig', 'definitions': Root._json_schema['definitions']}


class ViewConfig(SchemaBase):
    """ViewConfig schema wrapper"""
    _json_schema = {'$ref': '#/definitions/ViewConfig', 'definitions': Root._json_schema['definitions']}

