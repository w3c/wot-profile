# Web of Things (WoT) Profile - Explainer

## Why do we need a Profile? 

The W3C WoT Architecture [wot-architecture11] and the WoT Thing Description [wot-thing-description11] have been developed as a versatile format, that allows describing the interactions between multiple devices and protocols.

This flexibility permits an easy integration of new device types and protocols, however it risks interoperability, since there are no guarantees that two devices which are formally spec-compliant, will be able to communicate.

To increase adoption of the WoT specifications, interoperability between on premise devices, edge devices and the cloud is essential. Even if every manufacturer is implementing the current Thing Description specification in full flexibility, there is no interoperability guarantee; many choices are still left to the implementations and there are very few normative requirements that a device has to fulfill.

## The WoT Profile Specification

The WoT Profile 
<a href="https://w3c.github.io/wot-profile/">WoT Profile</a>, 
defines a Profiling Mechanism and a HTTP Basic Profile,
which enables out-of-the-box interoperability among things and devices.
Out-of-the-box interoperability implies that devices can be integrated together
into various application scenarios without deep level adaptations.

Typically only minor configuration operations are necessary
(such as entering a network key, or IP address) to use the device in a certain scenario.
These actions can be done by anyone without specific training.

The WoT Basic Profile has been defined with the objective of out-of-the-box interoperability and easy implementability - it defines prescriptive rules and requirements for properties and actions, which are expected to satisfy the majority of deployment scenarios.

In addition to the HTTP Basic Profile, the WoT Profile specification defines the HTTP SSE Profile 
and the HTTP Webhook Profile. These enable asynchronous notifications for events.
The HTTP SSE Profile is using the SSE protocol, the HTTP Webhook Profile 
uses a WebHook mechanism. A device can conform to only one of these profiles or implement a combination of these. 

To claim compliance with a profile, a Thing must conform with all the normative statements in that profile specification.

### Out-of-the-box interoperability

Out-of-the-box interoperability implies that devices can be integrated together into various application scenarios without deep level adaptations. Typically only minor configuration operations are necessary (such as entering a network key, or IP address) to use the device in a certain scenario. These actions can be done by anyone without specific training.

The WoT HTTP Profile is defined with the primary goal of providing interoperability guarantees among all devices implementing the profile. A secondary goal of profiles is to limit implementation complexity for developers to foster adoption of the WoT standard.

 The WoT HTTP Profile defines required metadata fields and constraints on the supported interactions and protocol endpoints. Additionally it introduces constraints on data schemas which are required for devices in real-world deployments.
The format does not forbid the use of additional elements of the WoT Thing Description for vendor specific extensions; however, use of such extensions will impact interoperability.
Devices which implement the HTTP Profile, are out-of-the-box interoperable with other HTTP Profile compliant devices.
Furthermore, the HTTP Profile simplifies device validation and compliance testing, since a corresponding conformance test suite can be defined.

### HTTP Baseline Profile
The HTTP profile defines a protocol binding which describes how a Consumer communicates with a Web Thing using JSON payloads over the HTTP protocol. It contains binding rules for properties and actions.

A Consumer of  a Web Thing conforming to the HTTP Baseline Profile must implement this protocol binding.

#### Properties

|   Operation  | Description                        |
| ------------- | --------------------- |
| readproperty |  read the value of a single property |
| writeproperty | write the value of a single property |
| readallproperties  | read all properties of the web thing |
|  writemultipleproperties | write multiple properties |

#### Actions

 The Baseline Profile defines synchronous and asynchronous action models. 
 It defines four operations that can be applied to an action endpoint.

|   Operations    | Description                     |
| --------------- | --------------------- |
| invokeaction    | send an action request |
| queryaction     | query the status of an ongoing asynchronous action request |
| cancelaction    | cancel an ongoing asynchronous action request |
| queryallactions | query the status of all ongoing action requests |

On synchronous actions, the action output result is contained in the response.
For asynchronous actions the operation returns an ActionStatus object in the response.
This ActionStatus object contains a status member and a URL that can be used to query the action status using the queryaction operation.

On synchronous actions, the action output result is contained in the response. For asynchronous actions the operation returns an Action Status object in the response. This Action Status object contains a status member and a URL that can be used to query the status of the action using the queryaction operation.

### Common Error Responses
If any of the operations on properties, actions and events defined above are unsuccessful, the Web Thing must send an HTTP response with an HTTP error code which describes the reason for the failure. The profile restricts the permitted error codes to enable uniform and common error handling across devices from multiple manufacturers.

### Events

Events are used for asynchronous notifications. To keep the implementation effort for the HTTP Baseline profile low, two separate event mechanisms are specified in two different profiles, the HTTP SSE Profile and the HTTP WebHook Profile.

These event profiles may be used stand-alone, or in conjunction with the HTTP Baseline Profile 
in order to provide operations to read and write properties and invoke, query and cancel actions.

Event subscriptions can be either performed for individual event sources or can be registered at top-level for the entire thing.

The following operations for events are defined:

|   Operation  | Description                        |
| ------------- | --------------------- |
|subscribeevent  | 	subscription to a single event source |
|unsubscribeevent |	unsubscribe to a single event source |
|subscribeallevents	 | top level subscription to all event sources |
|unsubscribeallevents |	top level unsubscribe to all event |sources |

## Accessibility

The WoT Thing Description and the WoT Profile only contain hints for user interfaces, but do not contain any layout or other directives.
It contains recommendation about elements that must be present in an environment that requres an accessible user interface.

## Internationalisation

Profile compliant devices will be implemented on real world runtime environments. Common implementation runtimes are Java, JavaScript/node.js and Python. 
These have only support for a limited set of languages. To facilitate interoperability between devices that are implemented on these runtimes, the profile will recommend a common subset of the languages that are supported by these environments.  

## Security Considerations

The WoT Profile Specification adopts the Security Considerations of the WoT Architecture and WoT Thing Description specifications.  

The HTTP Profile defines a subset of the security schemes that may be implemented on compliant devices.

While WoT supports the description of a wide variety of security schemes, profiles define a small subset that are known to be appropriately secure for the use cases each profile targets.

## Privacy Considerations

The WoT Profile Specification adopts the Privacy Considerations of the WoT Architecture and WoT Thing Description specifications.  
