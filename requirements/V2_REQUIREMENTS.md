# WoT Profiles 2.0 Use Cases & Requirements

## Introduction

The [Web of Things](https://www.w3.org/WoT/) (WoT) seeks to counter the fragmentation of the [Internet of Things](https://en.wikipedia.org/wiki/Internet_of_things) (IoT) by using and extending existing, standardized web technologies.

The [W3C WoT Thing Description 1.1 specification](https://w3c.github.io/wot-profile/#bib-wot-thing-description11) defines an information model and JSON-based representation format for describing the capabilities of connected devices and the interfaces with which to communicate with them. Thing Descriptions are designed to be protocol-agnostic and flexible enough to describe a wide range of existing ("brownfield") IoT devices.

In order to provide this level of flexibility the Thing Description specification includes a number of extension points including protocol bindings, payload bindings, security mechanisms, link relations and semantic contexts. As long as all of the capabilities of a device can be described using a Thing Description and a [Consumer](https://w3c.github.io/wot-profile/#dfn-consumer) implements all of the extensions used, the Consumer should be able to interoperate with that device. However, the result of this extensible architecture is that any given Consumer can only interoperate with a subset of possible [Web Things](https://w3c.github.io/wot-profile/#dfn-thing).


"WoT Profiles" are a mechanism by which out-of-the-box interoperability between WoT [Consumers](https://w3c.github.io/wot-profile/#dfn-consumer) and [Things](https://w3c.github.io/wot-profile/#dfn-thing) can be guaranteed, by constraining a Thing to a finite list of options for each extension point, and requiring that it conforms to certain defaults. As long as a Consumer implements all of the extensions and defaults prescribed by a Profile, it should be guaranteed to be able to use all of the capabilities of a Thing which conform to that Profile, without Thing-specific customisation.

Profiles will be designed specifically for new ("greenfield") implementations where developers have the freedom to conform to a prescriptive protocol binding and set of common constraints, in order to benefit from this additional level of interoperability.

## Use Cases

As a developer of a WoT Consumer, I want to guarantee out-of-the-box interoperability with a wide range of WoT Things.

As a developer of a WoT Thing, I want to guarantee out-of-the-box interoperability with a wide range of WoT Consumers.

### Smart Home

As the developer of DIY smart home hub software, I want to safely expose an HTTP-based API for monitoring and controlling a home which conforms to a common standard, so that cloud services from multiple vendors can add value to a user's smart home without having to implement a vendor-specific API.

As the developer of a smart home mobile app, I want to offer my users out-of-the-box interoperability with a wide range of smart home devices so that I can maximise the audience for my app.

As the developer of a smart home device, I want my device to be controllable by any smart home hub software and/or any smart home mobile app that conforms to a common standard....

### Smart Buildings

As the developer of a smart building hub, I want to safely expose an HTTP-based API for monitoring and controlling a commercial building which conforms to a common standard, so that cloud services from multiple vendors can consume data from that hub without having to implement a vendor-specific API.

As the developer of a smart building cloud service, I want to be able to provide data analytics for smart buildings using smart building hubs from different vendors which conform to a common standard, rather than having to implement multiple vendor-specific APIs.

### Smart Cities

### Manufacturing

### Energy

### Transportation

### Agriculture

## Requirements

### WoT Profiles Specification

The WoT Profiles specification:
1. MUST define a mechanism by which the author of a WoT Thing Description can denote that the Thing it describes conforms to a particular profile
2. MUST define a registry of profiles to which WoT Things and WoT Consumers may conform
3. SHOULD aim to keep the number of registered profiles as small as possible by rejecting profiles that significantly overlap in technologies or use cases, in order to minimise fragmentation on the Web of Things
### Individual Profiles

Individual profile documents:
1. MUST specify an identifier (URI) which identifies the profile 
2. SHOULD constrain a finite set of protocol bindings that a conformant Thing may use and that a conformant Consumer can be expected to support
	1. MAY constrain conformant Things to always follow certain defaults defined in a protocol binding document
3. SHOULD constrain a finite set of payload bindings that a conformant Thing may use and that a conformant Consumer can be expected to support
	1. MAY constrain conformant Things to always follow certain default payload formats defined in a payload binding document
	2. MAY constrain conformant Things to follow certain conventions such as date formats and error formats
4. SHOULD constrain a finite set of security mechanisms that a conformant Thing may use and that a conformant Consumer can be expected to support
5. SHOULD constrain a finite set of discovery mechanisms that a conformant Thing may use and that a conformant Consumer can be expected to support
6. MAY constrain a finite set of link relation types that a conformant Thing is recommended to use, and how they should be interpreted by a WoT Consumer
7. MAY constrain a finite set of semantic contexts that a conformant Thing is recommended to use and that a conformant Consumer can be expected to support
8. SHOULD NOT directly extend the WoT Thing Description information model, which should be defined using TD context extensions
9. SHOULD NOT define protocol behaviour, which should be defined in a protocol binding document
10. SHOULD NOT define data payload formats, which should be specified in a payload binding document
11. SHOULD NOT define discovery mechanisms, which should be defined in the WoT Discovery specification
12. SHOULD NOT define security mechanisms, which should be defined in a protocol binding document
13. SHOULD NOT describe an existing single-vendor IoT platform, which should be defined in a platform binding document
14. MUST NOT include any assertions which would require a Thing Description of a conformant Web Thing to be non-conformant with the Thing Description 2.0 specification