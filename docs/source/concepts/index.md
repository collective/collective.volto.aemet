---
myst:
  html_meta:
    "description": "AEMET integration with Plone concepts"
    "property=og:description": "AEMET Plone concepts"
    "property=og:title": "AEMET integration with Plone concepts"
    "keywords": "Plone, AEMET integration with Plone, concepts"
---

# Functional concepts

Functional concepts of integration with AEMET in Plone and Volto

## Introduction

The integration of **AEMET (State Meteorological Agency)** with **Plone CMS** and **Volto**
enables official meteorological information to be incorporated into a website, providing
users with up-to-date data on weather conditions, forecasts, weather warnings and other
relevant climate information.

This integration facilitates the reuse of the web services (REST APIs and XML/JSON files)
published by AEMET, enabling Plone to act as an intermediary between the platform and the
user interface developed in Volto.

---

# Objectives of integration

The integration aims to achieve the following objectives:

* Display official weather information directly on the website.
* Centralise access to AEMET services via the Plone backend.
* Reduce direct calls from the browser to external services.
* Facilitate the reuse of weather data across different Volto blocks and components.
* Enable configuration of the service via the Plone Control Panel.

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

* Managing authentication with the AEMET API.
* Making enquiries to meteorological services.
* Processing responses in JSON or XML format.
* Temporarily storing the information (cache).
* Exposing its own REST services to Volto.
* Logging errors and events related to the integration.

---

## Frontend (Volto)

Volto utilises the REST services provided by Plone to:

* Display the weather forecast.
* Display weather icons.
* Show maximum and minimum temperatures.
* Display weather warnings.
* Integrate the information into reusable blocks.

---

# Service configuration

The integration must allow the following to be configured from within Plone:

* Base URL of the service.
* Default county or municipality.
* Logging level.

These settings can be stored via a configuration panel (`Registry`) accessible from the Control Panel.

---

# Weather forecast

One of the main features is the ability to obtain a forecast for a specific town or town.

The information may include:

* Sky conditions.
* High temperature.
* Low temperature.
* Chance of precipitation.

This information can be displayed on a card or block within Volto.

---

# Weather warnings

Users can view the official warnings issued by AEMET.

Examples:

* Heavy rain.
* Snowfall.
* Strong winds.
* Coastal phenomena.
* High temperatures.
* Low temperatures.

These warnings can be highlighted using visual elements with different priority levels.

---

# Volto blocks

The integration may offer specific reusable blocks, for example:

## Weather Block

Display:

* Weather icon.
* Current temperature.
* High and low.
* Sky condition.

---

## Forecast Block

Displays the multi-day forecast.

This may include:

* Day.
* Icon.
* Temperatures.
* Chance of rain.

---

# Error handling

The integration must account for situations such as:

* AEMET service unavailable.
* Timeout.
* Municipality does not exist.
* Communication error.

The system must log these events and provide clear responses to the frontend.

---

# Security

The following practices are recommended:

* Keep the configuration on the backend only.
* Always use HTTPS.
* Validate the parameters received from Volto.
* Limit the number of permitted queries.
* Log invalid access attempts.

---

# Use cases

## Institutional website

Display the weather forecast for the city where the institution is located.

---

# Benefits of integration

* Official information from AEMET.
* Decoupled architecture between backend and frontend.
* Reusable components in Volto.
* Centralised configuration via Plone.
* Scalability for future weather-related features.

---

# Best practices

* Centralise all calls to AEMET in the Plone backend.
* Expose only proprietary REST services to Volto.
* Implement a configurable cache.
* Design reusable blocks for presenting information.
* Keep the access key secure and separate from the frontend.
* Log errors and monitor the status of the integration to facilitate maintenance.
