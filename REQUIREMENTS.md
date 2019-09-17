# WoT Profiles

## Use Cases
* As an end user, I want to know whether a device will work with my system before I purchase it to avoid wasting money.
    - Installers of IoT devices want to be able to determine if a given device will be compatible with the rest of their installed systems and whether they will have access to its data and affordances.

* As a developer, I want TDs to be as simple as possible so that I can efficiently develop them.
   - Here "simple" should relate to the end goal, "efficiently develop"; that is, TDs should be straightforward for the average developer to complete and validate.

* As a developer, I want to be able to validate that a Thing will be compatible with a Consumer without having to test against every possible consumer.

## Requirements

Please put your requirements into the sections of the document and mark it with your company name to make sure
we discuss with the appropriate contributors.  Requirements for which we have not reached consensus should be
under "Possible".

### Resolved

#### Interoperability (Oracle, Intel, Siemens, Fujitsu)

### Possible

#### Limit Complexity (Oracle)

Siemens: Need to define what *complexity* means!

#### Human readability (Oracle)

Siemens: w.r.t. title/description?

#### Developer guidance (Fujitsu, Siemens)
This may be a topic for wider consideration in the WoT group.
A profile can help to explain what to implement.

#### Composable profiles (Intel)
How does a composition model work?

#### Multiple profiles (Intel, Siemens)

#### Identification of profiles (Intel, Siemens, Fujitsu)
Need to add a mechanism to identify which profiles are described in a TD.

#### Profile should define a finite set of features and capabilities to implement by the consumer. (Intel, Oracle, Fujitsu)

Siemens: isn't it the rational of a profile?

#### Limit resource consumption (Intel, Oracle, Siemens, Fujitsu)

#### Follow Security and Privacy Best Practices
Profiles should not specify security and protocol combinations that do not satisfy security best practices
as described in the WoT Security Best Practices document.
There should be a mechanism to allow "nosec" but only in a Developer context (debatable - may still be useful
in a closed network).
