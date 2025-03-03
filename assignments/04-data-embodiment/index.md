---
layout: default
title: "4: Data Embodiment"
parent: Assignments
has_children: true
---

# Data Embodiment

[![Shiftr MQTT Broker window](data_embodiment.jpg)](https://ide-education.cloud.shiftr.io)

In this weeks assignment we are going to use online data to inform our design by embodying it into a physical artefact. We will use [MQTT](https://mqtt.org) (a lightweight protocol for the Internet of Things) to provide you with multiple data sources that you can use in this assignment.

The five datasources we provide are:

1. The wind speed, as reported by a virtual windspeed sensor (you can decide to locate it anywhere on planet earth), it shows values between 0 km/hour and 120 km/hhour.
2. The length of a virtual queue at a coffee machine (which coffee machine is up to you), values are between 0 and 20 people.
3. The temperature measure somewhere (you can locate this sensor anywhere on planet earth too), values are between -20 and 40 degrees Celcius.
4. A [Perlin Noise](https://en.wikipedia.org/wiki/Perlin_noise) function that returns smooth values between -1 and 1. This is actually the basis of the above virtual sensors. It's values are scaled to an appropriate range to make it meaningfull for that sensor.
5. The current coordinates of the ISS and its calculated distance to IDE in Delft. These values are based on an [real-online datasource provided by NASA](https://wheretheiss.at). The distance between the IDE-building and the ISS is calculated and shown, roughly between 8000 and 14000 km and the projected location on the earth surface is shown in [latitude and longitude](https://en.wikipedia.org/wiki/Geographic_coordinate_system).


You can follow the flow of data when going to [https://ide-education.cloud.shiftr.io](https://ide-education.cloud.shiftr.io/)

---

## Before we begin

For this week’s assignment, we prepared a lot of different code snippets to help you along. They are meant for you to use and **modify** for your specific design and device. Simple copy+pasting without a rough understanding of *what* you are copying **will not work!**

Although we will use a lot of code, you are not required to understand every little line, but rather analyse your needs and search for the specific code sample.

{: .warning } 
As a prerequisite for this tutorial to work, make sure you followed and successfully completed [Tutorial 4 of the Connected Interaction Kit website](https://id-studiolab.github.io/Connected-Interaction-Kit/tutorials/03-connect-to-the-internet/) and connected your ItsyBitsy to the internet. 



[Get started](step-1){: .btn .btn-blue }

If you’re unable to connect to the internet, don’t worry! We’ve provided a fallback method that allows you to use previously stored data from the same sources. This ensures you can still complete the tutorial and practice working with the data.

However, it’s essential to revisit this tutorial later when you have internet access. Connecting to the MQTT server is a key part of understanding how to integrate real-time data into your prototypes.

[Fallback data](no_internet){: .btn .btn-blue }