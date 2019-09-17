# WoT Profiles

## Use Cases
* As an end user, I want to know whether a device will work with my system before I purchase it to avoid wasting money.
    - Installers of IoT devices want to be able to determine if a given device will be compatible with the rest of their installed systems and whether they will have access to its data and affordances.

* As a developer, I want TDs to be as simple as possible so that I can efficiently develop them.
   - Here "simple" should relate to the end goal, "efficiently develop"; that is, TDs should be straightforward for the average developer to complete and validate.

* As a developer, I want to be able to validate that a Thing will be compatible with a Consumer without having to test against every possible consumer.

## Requirements
The group has reached consensus on the following requirements.

### Interoperability 
Proposers: Oracle, Intel, Siemens, Fujitsu

## Proposed Requirements
The following possible requirements are still under discussion and definition.
Please put your proposed requirements into a separate section and mark it with your company name to make sure
we discuss with the appropriate contributors.  

### Limit complexity 
Proposer: Oracle

#### Discussion
* Siemens: Need to define what *complexity* means!

### Human readability
Proposer: Oracle

Human-readable information such as title and description should be mandatory to
encourage inclusion of this information for documentation purposes.

#### Discussion
* Siemens: w.r.t. title/description?

### Developer guidance 
Proposers: Fujitsu, Siemens

A profile should help define what needs to be implemented.

#### Multiple profiles
Proposer: Intel, Siemens

The mechanism used to indicate that a TD satisfies a profile should be
general enough to indicate the TD satisfies the requirements for multiple profiles.

### Composable profiles
Proposer: Intel

It should be possible to combine multiple profiles both for production and
consumption:
* It should be possible to indicate that a consumer can ingest TDs that
satisfy one or more profiles, even if each TDs individually only satisfies
one profile.  For example, a Smart Building may need to use both "home"
devices and "industrial" devices.  A gateway consuming TDs should be 
able to ingest TDs designed for both the home and industrial contexts.
* Thing that satisfies all the requirements for multiple TDs
(for example, a device using protocols common to two different usage contexts)
should be able to indicate that.

### Validatible
Proposer: Intel

Whether or not a TD satisfies the requirements of a given profile should
be verifiable with automated tools.

### Identification of profiles
Proposers: Intel, Siemens, Fujitsu

There should be a mechanism to identify which profiles a TD satisfies.
This mechanism should be intrinsic to a TD, i.e. be in-band.

### Profile should define a finite set of features and capabilities to implement by the consumer.
Proposers: Intel, Oracle, Fujitsu

#### Discussion
* Siemens: isn't this the rationale of a profile?

### Limit resource consumption
Proposers: Intel, Oracle, Siemens, Fujitsu

### Follow Security and Privacy Best Practices
Proposers: Intel

Profiles should not specify security and protocol combinations that do not satisfy security best practices
as described in the WoT Security Best Practices document.

### Use nosec only in Developer contexts
There should be a mechanism to allow "nosec" but only in a Developer context.

#### Discussion
* Intel: debatable - nosec may still be useful in a closed network even for production.
