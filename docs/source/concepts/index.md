---
myst:
  html_meta:
    "description": "AEMET Plone concepts"
    "property=og:description": "AEMET integration with Plone concepts"
    "property=og:title": "AEMET integration with Plone concepts"
    "keywords": "AEMET, service, Plone, integration, documentation, concepts"
---

# Functional concepts

Functional concepts of integration with {term}`AEMET` service in {term}`Plone` and {term}`Volto`.

## Overview

The {term}`AEMET` integration facilitates the reuse of the web services such as:

- REST APIs
- XML/JSON data files

Which published by {term}`AEMET`, enabling {term}`Plone` to act as an intermediary
between the platform and the user interface developed in {term}`Volto`.

---

# Objectives of integration

The integration aims to achieve the following objectives:

* Display official weather information directly on the website.
* Centralise access to {term}`AEMET` services via the {term}`Plone` backend.
* Reduce direct calls from the browser to external services.
* Facilitate the reuse of weather data across different {term}`Volto` blocks and components.
* Enable configuration of the service via the {term}`Plone` Control Panel.

---

# Integration architecture

```text
                +---------------------------+
                |          Volto            |
                |       React Frontend      |
                +------------+--------------+
                             |
                        REST API
                             |
                +------------v--------------+
                |          Plone            |
                |    Integration service    |
                +------------+--------------+
                             |
                      HTTP / HTTPS
                             |
                +------------v--------------+
                |        API AEMET          |
                +---------------------------+
```

---

# Functional components

## Backend (Plone)

The backend is responsible for:

* Managing authentication with the {term}`AEMET` API.
* Making enquiries to meteorological services.
* Processing responses in JSON or XML format.
* Temporarily storing the information (cache).
* Exposing its own REST services to {term}`Volto`.
* Logging errors and events related to the integration.

---

## Frontend (Volto)

{term}`Volto` utilises the `REST` services provided by {term}`Plone` to:

* Display the weather forecast.
* Display weather icons.
* Show maximum and minimum temperatures.
* Display weather warnings.
* Integrate the information into reusable blocks.

---

# Service configuration

The integration must lets the following to be configures from within {term}`Plone`:

* Base address of the service.
* Default county or municipality.
* Logging level.

These settings can be stores via a configuration panel (`Registry`) from the Control Panel.

---

# Weather forecast

One of the main features is the ability to obtain a forecast for a specific town or town.

The information may include:

* Sky conditions.
* High temperature.
* Low temperature.
* Chance of precipitation.

This information can be displaying on a card or block within {term}`Volto`.

---

# Weather warnings

Users can view the official warnings issued by {term}`AEMET`.

Examples:

* Heavy rain.
* Snowfall.
* Strong winds.
* Coastal phenomena.
* High temperatures.
* Low temperatures.

These warnings can be highlighting using visual elements with different priority levels.

---

# Volto blocks

The integration may offer specific reusable blocks, for example:

## Weather block

Display:

* Weather icon.
* Current temperature.
* High and low.
* Sky condition.

---

## Forecast block

Displays the multi-day forecast.

This may include:

* Day.
* Icon.
* Temperatures.
* Chance of rain.

---

# Error handling

The integration must account for situations such as:

* {term}`AEMET` service unavailable.
* Timeout.
* Municipality doesn't exist.
* Communication error.

The system must log these events and provide clear responses to the frontend.

---

# Security

The following practices are recommends:

* Keep the configuration on the backend only.
* Always use `HTTPS`.
* Validate the parameters received from {term}`Volto`.
* Limit the number of permitted queries.
* Log invalid access attempts.

---

# Use cases

## Institutional website

Display the weather forecast for the city where the institution is locates.

---

# Benefits of integration

* Official information from {term}`AEMET`.
* Decoupled architecture between backend and frontend.
* Reusable components in {term}`Volto`.
* Centralised configuration via {term}`Plone`.
* Scalability for future weather-related features.

---

# Best practices

* Centralise all calls to {term}`AEMET` in the {term}`Plone` backend.
* Expose only proprietary REST services to {term}`Volto`.
* Implement a configurable cache.
* Design reusable blocks for presenting information.
* Keep the access key secure and separate from the frontend.
* Log errors and monitor the status of the integration to facilitate maintenance.
