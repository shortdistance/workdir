from rdflib.namespace import XSD
from rdflib import Literal

print Literal('01', datatype=XSD.Integer)
print Literal('2016-09-12', datatype=XSD.Datetime)
"""
Sting
Boolean
Base64Binary
HexBinary
Float
Decimal Integer NonPositiveInteger Long NonNegativeInteger NegativeInteger Int Short Byte  UnsignedLong PositiveInteger UnsignedInt UnsignedShort UnsignedByte
Double
AnyURI
QName
NOTATION

Duration
Datetime
Time
Date
GYearMonth
GYear
GMonthDay
GDay
GMonth
"""
