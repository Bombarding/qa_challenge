## Challenge

```
 QA Challenge Project:

 Part 1:

Environment Setup Goal-

The machines the test team needs will have predefined configurations we'll call DevA, DevB, and DevC.  An on-demand ability to obtain DevA—DevC boxes, but they should not be accessible by Developers because the Developers can't be trusted to not make one-off hacks to Testing machines to make bugs go away.

 

Equipment and Software-

 

§  The hypervisors are EXSi with vSphere present as needed. You can imagine any quantity 1..N bare-metal servers as you'd want, all collocated, so there are LAN speed and reliability interconnections between them.

§  You can add any support boxes: network hardware, software servers, etc. that you might need.

§  The boxes DevA and DevB are Linux hosts (Centos if you want to be specific). DevC is Windows 10. SupD is also CentOS. Because this is not a resource balancing trial, I'm intentionally not specifying guest or host capacities.

§  The lab will be accessed remotely from HQ and other known origins.

§  The guest machines should have separate logins per engineer and the guest machines should be addressable by name. None of the lab should be accessible to the public at large.

§  The guest machines must be addressable with IPv4, you may use IPv6 anywhere it helps you accomplish your goals (including not at all)

Deliverable

You should deliver documentation explaining the layout of the lab and the means by which your "customers" can request resources. The audience for this document is someone exactly as skilled and knowledgeable as you. Put another way, assume you are walking into a new lab and provide the type of system documentation you'd like to be handed on your first day.

 

I have a preference for Markdown if you can use that to express what you need. If not, HTML is preferred to Google Docs, and just about anything is preferred to Microsoft Word. Diagrams, multi-media, and suchlike are acceptable if you feel they are needed; I'm not expecting them.

Part 2:

Testing framework portion —

You may use whatever tools or framework you like to accomplish this task. The first part requires that you create "smoke tests" to confirm a sample site conforms to some degree of expected behavior. 

You may use either of the QA practice sites:

§  https://automationintesting.online/

§  http://automationpractice.com/

§  http://newtours.demoaut.com/

You may also choose any other publicly accessible site that you think better suited to this exercise, but you'll need to explain why you opted for your choice over the provided ones. The sample sites were chosen only because they appear often in the QA web literature, not any deeper reason. The amount of the site you cover with tests is not a factor of this evaluation, indeed, we'll consider the variety of techniques employed and their pedagogical value to be the salient criteria.

You will likely be able to accomplish this task on your personal machine. If you request, we can furnish you with your own Cloud instance with SSH access for the duration of the project.

 

Teaching -

It is expected that the tests you create will serve as examples for the second part of the project. You need to provide materials for one of the interviewers to make additional tests using your model. You can expect your audience to be a development engineer who is well versed in the craft but lacking any QA specific skills. You can assume that your "student" is as quick with new technologies and concepts as you are.

Prepare sufficient written material to allow your student/reviewer to generate additional tests similar to some that you have already created. While we'll discuss your project with you afterwards, the written materials will be the only avenue for you to instruct your student. You can certainly point to external reference materials for framework setup.

The choice of instructional format is up to you. Simplicity and clarity are preferred over flash and art. As an example, Markdown would be preferable to animated slides. Conversely if you feel animated slides and video are essential to your communication, you may submit them.

Guidance -

§  Simple is better than complex

§  There is no expectation that your solution scale beyond this challenge project

§  There is a great deal of latitude afforded you in this project. We do expect this to be more than a half-day's effort, but your reviewer's time is prized. You'll want to demonstrate your capabilities but not flood us.

Deliverable —

1) A github repo would be ideal but If you develop this on your own system, please submit your work products in a tarball. We can accept submissions via Dropbox or Google Drive or provide you with Drive space for delivery.

If you develop on our resources, we still want a tarball, but you can leave it on the VM itself.

2) Documentation on what the test does, how to run it, and how another qa or dev can continue writing the scripts.
```