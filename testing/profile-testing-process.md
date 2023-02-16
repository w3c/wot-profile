# Profile testing for CR / PR transition

Target is to determine implementability of the specification by a consumer and a thing.
This implies to verify all RFC2119 assertions defined by the specification.
If an assertion relates to a consumer we need two consumer implementations that implement it.
If an assertion relates to a thing we need two thing implementations that implement it.
If an assertion relates to a consumer and a thing we need two consumer and thing implementations that implement it.

On any mismatch of assertions or contradicting assertions between consumers and things, 
issues for these assertions have to be created.

Implementation results are provided in the format described in manual.csv
(categories.csv describes which assertion applies to things and/or consumers)

## Thing validation

### validation of TDs against Profile assertions

#### Baseline assumption: TDs are already validated against the TD specification.
(can be validated by appropriate tooling in the TD directory)
For details see instructions in the tesfest "readme".

### Verify thing assertions  

## Consumer validation

### Verify consumer assertions (manually)

most consumer assertions are behavioral: 

* An application needs to read a TD and interact with a thing and demonstrate the behavior. 

* Two separate interoperable pairs of consumers and things are required.
