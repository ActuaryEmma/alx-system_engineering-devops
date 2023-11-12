Using one of the web stack debugging project issue or an outage you have personally face, write a postmortem. Most of you will never have faced an outage, so just get creative and invent your own :)

Requirements:

    Issue Summary (that is often what executives will read) must contain:
        duration of the outage with start and end times (including timezone)
        what was the impact (what service was down/slow? What were user experiencing? How many % of the users were affected?)
        what was the root cause

    Timeline (format bullet point, format: time - keep it short, 1 or 2 sentences) must contain:
        when was the issue detected
        how was the issue detected (monitoring alert, an engineer noticed something, a customer complained…)
        actions taken (what parts of the system were investigated, what were the assumption on the root cause of the issue)
        misleading investigation/debugging paths that were taken
        which team/individuals was the incident escalated to
        how the incident was resolved

    Root cause and resolution must contain:
        explain in detail what was causing the issue
        explain in detail how the issue was fixed

    Corrective and preventative measures must contain:
        what are the things that can be improved/fixed (broadly speaking)
        a list of tasks to address the issue (be very specific, like a TODO, example: patch Nginx server, add monitoring on server memory…)

 *******************************************************************
`
Issue Summary:
On the evening of October 20, 2023, from 8:00 PM to 10:00 PM EAT, our system experienced a critical outage, impacting 70% of our user base. Users were unable to log in to our website, coinciding with the release of end-of-term results.
Root Cause:
The root cause was insufficient capacity to handle a sudden spike in user traffic. Our infrastructure, composed of only two web servers, struggled to manage the surge in login requests. The unexpected strain intensified as both parents and students sought access to recently published results.
Timeline:
Detection Time: 8:00 PM EAT
Detection Method: Customer complaints and escalation from customer service
Actions Taken:
Software engineers identified it as a server issue based on a 500 (Internal Server Error) code.
Logs were examined, revealing excessive traffic as the culprit.
Misleading Paths:
Initially explored code-related issues before realizing the problem was infrastructure-related.
Escalation:
Incident escalated to the software engineering team.
Resolution:
Added more web servers and implemented a load balancer to evenly distribute incoming traffic.
Resolution:
Resolution Details: To address the problem, additional web servers were incorporated, and a load balancer was implemented to efficiently distribute incoming traffic, preventing future overloads.

Corrective and Preventative Measures:
Improvements/Fixes:
Increase server capacity to accommodate traffic spikes.
Enhance monitoring tools to detect potential issues proactively.
Tasks:
Add more web servers(Nginx) to the infrastructure.
Implement a load balancer for effective traffic distribution.
Integrate monitoring tools to detect and alert on server load issues.
Establish automated scaling mechanisms to dynamically adjust resources based on demand.
Conduct a comprehensive review of infrastructure to identify and address potential bottlenecks.
Develop a communication plan for users during similar incidents to manage expectations.
`
