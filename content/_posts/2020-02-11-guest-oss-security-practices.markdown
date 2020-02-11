Title: Open-Source Security Best Practices You Can't Ignore in 2020
Headline: guest article by Gilad David Maayan
author: Gilad David Maayan
date: 2020-02-11 13:00
comments: true
og_image: images/cyber-security.jpg
twitter_image: images/cyber-security.jpg

![cyber-security image](/images/cyber-security.jpg "cyber-security image")

Open source components are incredibly useful in shortening development time.
Open source projects are created, maintained, and used by developers of all
levels and companies of all sizes. However, you can’t always determine who
created the code and who edited the project. For all you know, there’s a
piece of spyware hiding somewhere in the codebase. Read on to learn how to
apply open source security in 2020.


What Is Open-Source Software?
-----------------------------

Open-source software uses freely available code so that anyone can view
and modify it. It is created collaboratively by communities of developers
at no charge. Some of the most popular open-source programs are Linux,
Kubernetes, Jenkins, and WordPress.

Open-source software can have many
[different licensing terms](https://levelup.gitconnected.com/understanding-open-source-license-types-5a577c4a09d5).
There are more than 1400 different open-source licenses, the most common of which are
MIT, GPL, and Apache. Most licenses have two things in common:

- Licenses do not require a license fee for the software
- Licenses allow anyone to contribute or modify to the program

Open-source software isn’t always free of charge-companies often charge for support,
implementation, and additional features added on to open-source components. However,
open-source software can be cheaper to implement. This cost savings is why modern
enterprise software relies heavily on open source components. Likewise, many popular
commercial applications use thousands of open source components as part of their code.


Open-Source Risks You Must Know About
-------------------------------------

There are several risks you might face when using and including open-source components.

Public Nature of Vulnerabilities
================================

Open-source code is publicly available for inspection. This allows community members
to contribute to identifying and fixing vulnerabilities. Ideally, contributors can
develop patches quickly, before the vulnerability is made public.

Once discovered, open-source vulnerabilities are published on the National Vulnerability Database
([NVD](https://nvd.nist.gov/)). This database is publicly available and searchable,
meaning that both open-source users and hackers can see vulnerability information.
Hackers use this public availability to their advantage, attempting to exploit
vulnerabilities as soon as a flaw is announced. This can enable hackers to attack
systems before users get a chance to apply patches.

A well-known example of this exploitation is the Equifax breach, in which 143 million
records were compromised. This breach occurred because attackers were able to exploit
a known vulnerability in the open-source Apache Struts framework. Although this
vulnerability was made public several years before, Equifax never patched their systems
to protect against it.

License and Use Infringement
============================

Open-source projects lack standard commercial controls, trusting contributors to act ethically.
Unfortunately, this means that proprietary code may get included in projects without a
project maintainer’s awareness.

An example of this occurring was seen in a case brought by SCO Group.
They accused IBM of including part of their proprietary code, into Project Monterey.
This code was unknowingly incorporated through open-source components that IBM included in the project.

Operational Risks
=================

Operational inefficiencies can be a major source of risk when using open-source
components. In particular, inefficiencies caused by inadequate tracking or
monitoring of components. If you are unaware of what components you have or where
components are stored, you cannot ensure your systems are up to date.

The possibility of losing support for a component is another risk you might face.
Open-source projects are based on voluntary engagement. If a community loses
interest in a project, it can see decreased support or be dropped entirely.
For such projects, you become directly responsible for ensuring that vulnerabilities
are identified and patched.

To address these risks, you need to ensure that you maintain an inventory of components.
Doing so can provide visibility of your risks and can help ensure that you are using
components uniformly. Often, this means using software composition analysis tools to
automate this process and reduce manual labor.


Best Practices For Using Open-Source Securely in 2020
-----------------------------------------------------

As the number of open-source projects increases, the likelihood that your systems will
include open-source components increases. To ensure that these components provide
maximum benefit with minimum risk, there are several
[open source security](https://www.whitesourcesoftware.com/open-source-security/)
best practices you should adopt.

Balance Functionality and Risk
==============================

You may be able to gain the functionality you need with just part of an
open-source project. When considering the inclusion of an open-source project,
evaluate its components before you include anything. You may find that you only
need one library or service instead of an entire project. By limiting what you include,
you can reduce the risk of including additional vulnerabilities and simplify integration.

Consider Historical Security
============================

To be considered secure, code must be reviewed and tested for vulnerabilities.
However, testing takes time and testing tools can be expensive so it may be
overlooked in open-source projects. You can get a better idea of the overall
security of a project by evaluating how security is addressed in a project’s
documentation. If a project doesn’t specify how vulnerabilities are identified
or what measures are taken to prevent flaws, you should be wary.

Before including components, consider the security history of a project,
including the average number and type of bugs per release. If a project has a
history with lots of vulnerabilities, consider looking for an alternative.
You should also take into account how long it takes a community to fix vulnerabilities
once reported. Slow fixes can signal weak community support or significant issues
with the source code.

Consider Community Size and Engagement
======================================

Open-source software is typically supported by volunteers, including amateur developers.
This means projects can suffer from a lack of consistency. Ideally, projects have a
medium to large community base. This signals that quality is likely to be higher
and that projects are unlikely to be abandoned.

You should also consider the size and frequency of releases a community is putting out.
If releases are haphazard or infrequent, you will have a harder time maintaining any
components you include. For the most reliable projects, release schedules are set
and you can anticipate the amount of effort to devote to maintenance.

Conclusion
----------

Hopefully, this article helped you learn the importance of open source security.
In a time when networks become increasingly distributed, securing your applications
becomes a crucial element of the development process. Many developers have already
realized that and are in the process of shifting security to the left. That means
you’re putting security as a top priority throughout all development stages to
ensure your code is as secure as possible.

---

Author Bio


![Gilad David Maayan](/images/giladimage.jpg "Gilad David Maayan")

Gilad David Maayan is a technology writer who has worked with over 150 technology
companies including SAP, Samsung NEXT, NetApp and Imperva, producing technical and
thought leadership content that elucidates technical solutions for developers and IT leadership.


LinkedIn:
[https://www.linkedin.com/in/giladdavidmaayan/]([https://www.linkedin.com/in/giladdavidmaayan/)
