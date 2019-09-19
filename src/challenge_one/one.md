# QA Challenge
> QA Challenge One - Keep The Devs Out

This file is to build an understanding of how to configure a VPC (In Theory) to avoid Developers working on patches while QA is attempting to test.


## Overview
```
Assuming the following things are true:
1. VPC has already been created with the following instances:
	a. Bastion
	b. Instance with Apache, HTTPD, and currently running latest web code from application
	c. Instance(s) with necessary APIs, micro-services, etc, running latest code/implementation from dev
	d. Instance with necessary dependencies for testing
2. Jenkins instance with the ability to promote/rollback code deployments via scm
```

## Design
```
Devs will promote code to scm under the branch labeled "dev"
Once a deployment is ready and code review is completed, then the devs will promote the ticket to the QA gatekeeper
QA Gatekeeper will review all stories and/or documentation to promote the "dev" branch to "qa" branch
QA Gatekeeper will remotely login to Jenkins/AWS CodePipeline/etc and trigger the build
Jenkins will promote the latest UI, DB and micro-services.
QA Gatekeeper will note on story to the respective dev that the deployment is completed and ask for a promotion smoke test
Dev will validate the code deployment occurs in the web application exclusively, and sigh off on the promotion to qa.

QA team will open PuTTY and ssh into the VPC bastion
From the bastion host, which will be acting as a proxy/tunnel/jumpbox to the other instances, then the QA team will then jump to the testing machine
The testing machine will have dependencies already installed, see "install_before_test.sh"
The QA team will begin developing and testing their scripts.
If a change to the microservice, ui or db occurs duiring the QA teams testing, then a detailed ticket will need to be approved before deployment
Any hotfixes that are promoted to QA-env are done at the QA Gatekeepers discretion, only after the first round of bugs are made and testing completes.
```

## Daily Shutdowns/Startups of VPC/Instances
```
Every night the instances will shutdown to preserve cost and resources
Every morning the instances will startup
Every morning as part of a startup script in /etc/init.d/ will check /etc/passwd for any users not specified in an exception script on the bastion
The startup script will then proceed to delete any users from the bastion host except the pre-specified qa testers/sysAdmin
```

## Conclusion
```
The purpose of the startup script is not to isolate any of the team or "block" their entry to the vpc implicitly. Rather, the purpose of the script and the above documentation is set forth to establish a baseline and a process. In my time, I have rarely heard of developers going behind the teams back and modifying code that has already been promoted to a new environment. That does not mean it is not true, however, I am of the firm belief that the time they are spending (if applicable) to modify a promotions code, could be better used in advaning the deliverables for that iteration. 

The established document illustrating a guideline and setup for an environment should be used to establish a process, since without a process, there is no way to scale development work. Of the core tenants of the agile environment, this aims to satisfy the following: "Creating processes that promote sustainable efforts" and "Maintaining a constant pace for completed work"
```
