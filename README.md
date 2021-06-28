# WoT Profile
      
The **[WoT Profile](http://w3c.github.io/wot-profile/)** specification serves two purposes:

- It defines a generic **Profiling Mechanism** which
provides a mechanism to describe a profile in an unambiguous way.
This mechanism can be used to define additional profiles.

- In addition it defines a **Core Profile** of the Thing Description 
for use with selected protocols. The <a>Core Profile</a> formalizes
the results of several plug-fests that were conducted by the WoT
Interest Group and of tests that were conducted as part of the
development. It is expected that additional profiles for thing
templates and other protocols will be defined in the near future.

Devices that constrain their use of the Thing Description to the **WoT Core Profile** can **interoperate other out-of-the-box**.

A rendered version of the profile specification is available at: [WoT Profile](http://w3c.github.io/wot-profile/)

Motivation:

The [W3C Web of Things Architecture](https://www.w3.org/TR/wot-architecture/) and 
[Web of Things Thing Description](https://www.w3.org/TR/wot-thing-description/) 
define a powerful mechanism and a format to describe myriads of very
different devices, which may be connected over various protocols. The
format is very flexible and open and puts very few normative
requirements on devices that implement it.

		
However, this flexibility de-facto prevents interoperability, since,
without additional <strong>rules</strong>, it allows implementers to
make many choices that do not provide <strong>guarantees</strong> of
common behavior between implementations.

These rules have to be prescriptive, to ensure that compliant
implementations satisfy the semantic guarantees, that are implied by
them. We call this set of rules a **Profile**.

WoT Profile work is conducted as part of the WoT architecture TF, 
please see https://www.w3.org/WoT/IG/wiki/WG_WoT_Architecture_WebConf
for more information and call logistics.
