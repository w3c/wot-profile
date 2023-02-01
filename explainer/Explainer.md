# Draft: Web of Things (WoT) Profile - Explainer

The WoT profile 
<a href="https://w3c.github.io/wot-profile/">WoT Profile</a>, 
defines a Profiling Mechanism and a HTTP Baseline Profile,
which enables out-of-the-box interoperability among things and devices.
Out-of-the-box interoperability implies that devices can be integrated together
into various application scenarios without deep level adaptations.

Typically only minor configuration operations are necessary
(such as entering a network key, or IP address) to use the device in a certain scenario.
These actions can be done by anyone without specific training.

The WoT Profile have been defined with the objective of out-of-the-box interoperability and easy implementability - it defines prescriptive rules and requirements for properties and actions, which are expected to satisfy the majority of deployment scenarios.

In addition to the baseline profile, the WoT Profile specification defines the HTTP SSE Profile 
and the HTTP Webhook Profile. These enable asynchronous notifications.
The HTTP SSE Profile is using the SSE protocol, the HTTP Webhook Profile 
uses a WebHook mechanism. A device can conform to only one of these profiles or implement a combination of these. 

To claim compliance with a profile, a Thing must conform with all the normative statements in that profile specification.

####	Out-of-the-box interoperability

Out-of-the-box interoperability implies that devices can be integrated together into various application scenarios without deep level adaptations. Typically only minor configuration operations are necessary (such as entering a network key, or IP address) to use the device in a certain scenario. These actions can be done by anyone without specific training.

The WoT HTTP Profile is defined with the primary goal of providing interoperability guarantees among all devices implementing the profile. A secondary goal of profiles is to limit implementation complexity for developers to foster adoption of the WoT standard.

 The WoT HTTP Profile defines required metadata fields and constraints on the supported interactions and protocol endpoints. Additionally it introduces constraints on data schemas which are required for devices in real-world deployments.
The format does not forbid the use of additional elements of the WoT Thing Description for vendor specific extensions; however, use of such extensions will impact interoperability.
Devices which implement the HTTP Profile, are out-of-the-box interoperable with other HTTP Profile compliant devices.
Furthermore, the HTTP Profile simplifies device validation and compliance testing, since a corresponding conformance test suite can be defined.


### Profile Requirements

A Profile defines a finite set of features and capabilities to implement by the consumer. It
limits the number of options, for example the set of possible protocols, to a finite set, so that a consumer can consume any TD in a given profile with a finite and static code base.


#### Interoperability
This is the most important objective of the profile. A TD Consumer satisfying the requirements of a profile should be able to process any TD also satisfying the profile and should be able to correctly interact with all affordances of the Thing such a TD describes.

#### Limit and reduce complexity
Implementation complexity is reduced by eliminating the need of RDF processing,
simplifying thing description to have fewer variations and thus limiting the effort for JSON implementation, clarifying ambigutiesto define interpretation of a TD and behavior of the thing and consumer.

#### Developer guidance
The profile defines what needs to be implemented by a device.including behavioral goals and recommendations about best practice for the implementation of Consumers and Things.

#### Validatible TDs
Whether or not a TD satisfies the requirements of a given profile must be verifiable with automated tools. TD validation tools are available, these can be used and extended for specific profiles.

##	Information Model constraints
The information model of the profile is a subset of the information model of the Thing Description. Additional constraints and normative requirements are defined, such as mandatory metadata fields, data types and formats, limitations and other clarifications.
Additionally the profile describes a set of recommended practices, that are derived from implementation experiences in various domains. These avoid misinterpretations and interoperability problems in the field.
There have been cases in the past where misinterpretations of time values, different metric systems or other ambiguous data has led to catastrophic events. A famous example is the Mars Climate Orbiter [14], which has been lost because of different metric systems (SI vs. imperial) used by different teams.

##	HTTP Baseline Profile
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

An action request is triggered by a HTTP POST request to an action endpoint.

    POST /things/lamp/actions/fade HTTP/1.1
    Host: mythingserver.com
    Content-Type: application/json
    Accept: application/json

    {
    "level": 100,
    "duration": 5
    }


It responds with one of three response formats:

-	Synchronous Action Response
-	Asynchronous Action Response
-	Error Response


On synchronous actions, the action output result is contained in the response. For asynchronous actions the operation returns an Action Status object in the response. This Action Status object contains a status member and a URL that can be used to query the status of the action using the queryaction operation.

    HTTP/1.1 201 CREATED
    Content-Type: application/json
    Location: /things/lamp/actions/fade/123e4567-e89b-12d3-a456-426655
    {
    "status": "pending",
    "href": "/things/lamp/actions/fade/123e4567-e89b-12d3-a456-426655"
    }


###	Common Error Responses
If any of the operations on properties, actions and events defined above are unsuccessful, the Web Thing must send an HTTP response with an HTTP error code which describes the reason for the failure. The profile restricts the permitted error codes.

- 400 Bad Request
- 401 Unauthorized
- 403 Forbidden
- 404 Not Found
- 500 Internal Server Error

If an HTTP error response contains a body, the content of that body must conform with the Problem Details format.

    HTTP/1.1 400 Bad Request
    Content-Type: application/json
    {
    "status": "failed",
    "error": {
        "type": "https://mythingserver.com/docs/errors/invalid-level",
        "title": "Invalid value for level provided",
        "invalid-params": [
        {
            "name": "level",
            "reason": "Must be a valid number between 0 and 100",
        }
        ]
    }
    }

###	Events

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


##	Security
The HTTP Profile defines a subset of the security schemes that may be implemented on compliant devices.
A security scheme must be defined at the global level, so all interactions use the same security scheme.
 A thing may however adopt multiple alternative security schemes, so that (for instance) both password and OAuth2 access may be permitted.  As discussed in the following, while WoT supports the description of a wide variety of security schemes, profiles define a small subset that are known to be appropriately secure for the use cases each profile targets.

###	Transport Security
For the HTTP Profile, a compliant Thing must implement at least TLS 1.2 and ideally TLS 1.3 for secure transport and mutual authentication.
Mutual authentication places some requirements on identification that can most easily be satisfied using publicly-visible URLs and the use of certificate authorities to distribute and validate public keys, however in some circumstances pre-shared keys and certificates may be used (e.g. on private factory networks).
Relying on network security only (e.g. WEP) and using insecure HTTP for transport is highly discouraged, except for testing.

Unfortunately, browsers tend to only support TLS on publicly-visible URLs supported by the Web PKI (CA) system. In case a browser needs to be used e.g. to access a dashboard, it needs a public URL in order to use this system. However, to avoid unnecessary exposure of individual Things it is highly recommended that a publicly visible URL be provided only for a limited number of such services.
Limiting the number of access points made accessible to the public network reduces the attack surface.  Such access points should also be supported by systems that can be easily kept up to date with security patches, such as gateways and hubs.

###	Authorization
A variety of authentication methods are supported by the WoT, but the most suitable ones are simple password identification (for simple situations, such as a home hub; either plain or digest passwords are suitable, but only in combination with TLS) and the use of bearer tokens and OAuth2 for situations in which a large number of devices and users are expected, or where higher security is required.
OAuth2 allows separating the management of user authorizations and authentication from actual access to Things, so that (for example) a user's authorizations can be revoked without having to access and modify each Thing. Using OAuth2, access can also be constrained to certain classes of interactions using scopes.

##	Compliance and Validation
Checking that a WoT Thing Description document is compliant with a profile can mostly be accomplished using existing tools such as JSON Schema and SHACL.  In general, however, checking that a Thing’s actual behavior is consistent with its Thing Description is more difficult, but tools are under development that can partially automate this. Since the W3C does not have a formal certification procedure, alternative mechanisms will have to be used to share information about conformant and non-conformant devices. 



