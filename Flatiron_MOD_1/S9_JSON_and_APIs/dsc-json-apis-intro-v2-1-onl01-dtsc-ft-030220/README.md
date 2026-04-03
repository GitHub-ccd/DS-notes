
# JSON and APIs - Introduction

## Introduction

In this section, you’ll learn about an additional data type: JSON (which stands for JavaScript Object Notation), as well as APIs (Application Programming Interfaces).  

JSON is the new standard data format for the web. An older data format that is still used on the web is XML, or Extensible Markup Language, which you’ll have a chance to learn more about in the Appendix. APIs are one of the many ways you’ll access data as a data scientist.

## Working with JSON files

A substantial part of the job of a professional data scientist is to find and access data. You've spent a bunch of time looking at how to pull information from relational databases, but there is lots of information you might need to work with that is either not in a relational database, or that is not exposed to you via a relational database. 

For example, you might work with a third party website that has a lot of geographical data (perhaps points of interest near state highways). Within their company, they may well store the data within a relational database, but you might have to access it using an API (an Application Programming Interface - a way your computer can talk to their computer to go get some information!). Over the next couple of sections, we'll be looking at accessing data through APIs and enough HTML and CSS to get started with web scraping (downloading information automatically from websites). In this section, you'll look at a key data storage format, JSON, that you may well come across when retrieving data from other web applications or from inside your company.

### JSON

You'll start off this section with a brief introduction to JSON so you know what this file format looks like. You'll then get some hands-on practice loading and parsing data from JSON files into Python.

### JSON Schemas

Once you've learned how to import data that has been stored in the JSON format, you'll look at JSON schemas - a way to describe the expected structure of a given JSON file.

### Exploring JSON Schemas

Finally, you'll get a lot more practice working with JSON schemas, exploring unknown schemas, accessing and manipulating data inside a JSON file and then converting JSON to alternate data formats such as `pandas DataFrames`. This lab will be a great chance for you to practice your Python programming skills and get comfortable with importing and transforming JSON data - something you may well have to do on a regular basis as a professional data scientist.

## APIs

One of the many ways you'll find yourself accessing data as a professional data scientist is via APIs (Application Programming Interfaces). Typically, you'll send a request and get some data back, often in JSON or XML format. In this section, you'll get some hands-on experience retrieving and working with data provided by a range of different APIs.

### Introduction to APIs

In this section, we'll provide a conceptual introduction to various kinds of APIs and some of the reasons that businesses create them. 

### The Client Server Model 

We then look at the basic model of "clients" and "servers" to provide a framework for thinking about how your "client" retrieves information from an API "server". 

### The Request/Response Cycle 

Next, we'll look at the fundamental mechanism by which web-based APIs are typically accessed - sending an HTTP request and then processing the response provided by the server. We'll also get a little experience working with HTTP requests using the Python `.get()` method within the `requests` package. We also get some hands-on experience retrieving information from NASA using [Open Notify](http://open-notify.org/).

### APIs and OAuth

Usually, access to a given API is limited to avoid abuse. One of the most common mechanisms for identifying your API requests to make sure they fit within acceptable usage guidelines is OAuth - Open Authorization - a standard for authorizing clients across web requests. In this section, we'll provide an overview of what OAuth is and how it works by looking at how it is implemented by Dropbox. 

### Working with the Yelp API

Next, we'll get some practice working with a real API, retrieving information from the Yelp API. 

### Creating interactive maps with Folium 

We wrap up the section by creating interactive maps with Folium. In the Appendix, we include a Lab where you can build a Geographic Information System using Folium and data obtained from the Yelp API to display it on an interactive map.

## Summary

Whether it’s from an API or a NoSQL store, it's quite possible that some of the data you find yourself working with will be stored using JSON. In this section, you'll build the confidence to be able to import and transform such data.

Also, many companies provide access to their data via an API, so being able to connect to and work with data provided via an API is a critical skill as a professional data scientist!
