---
myst:
  html_meta:
    "description": "AEMET integration with Plone Tutorials"
    "property=og:description": "AEMET integration with Plone Tutorials"
    "property=og:title": "AEMET integration with Plone Tutorials"
    "keywords": "AEMET, service, Plone, integration, documentation, tutorials"
---

# Custom REST services

{term}`Plone` can expose specific endpoints for {term}`Volto`. These services encapsulate
the logic for communicating with {term}`AEMET` and provide a standardised format
for the front end.

---

(aemet-settings-route)=
## AEMET settings route

Anonymous users can't access registry resources by default with {term}`plone.restapi` (there is a special permission).

To avoid enabling registry access to everyone, this package exposes a dedicated RestApi `route` with
{term}`AEMET Settings` (`@aemet-settings`):

Get the information from the {term}`AEMET Settings` via `curl` command:

```shell
curl -X GET http://localhost:8080/Plone/@controlpanels/aemet-settings \
  -H "Accept: application/json" \
  --user admin:admin
```

This `route` returns a `JSON` object containing the {term}`AEMET Settings` and weather forecast data via `curl` command:

```json
{
  "@id": "http://localhost:8080/Plone/@controlpanels/aemet-settings",
  "data": {
    "location_id": "41091"
  },
  "group": "Add-on Configuration",
  "schema": {
    "fieldsets": [
      {
        "behavior": "plone",
        "fields": [
          "location_id"
        ],
        "id": "default",
        "title": "Default"
      }
    ],
    "properties": {
      "location_id": {
        "description": "The Location ID of the AEMET service, for example '41091' to Sevilla location ID.",
        "factory": "Text line (String)",
        "title": "Location ID",
        "type": "string"
      }
    },
    "required": [
      "location_id"
    ],
    "type": "object"
  },
  "title": "AEMET Settings"
}
```

Below is a `PATCH` operation to set up the {term}`location_id` field value of the
{term}`AEMET Settings`:

```shell
curl -i -X PATCH http://localhost:8080/Plone/@controlpanels/aemet-settings \
  -H "Accept: application/json" \
  -H "Content-Type: application/json" \
  --data '{"location_id": "28058"}' \
  --user admin:admin
```

This `route` returns a HTTP response:

```shell
HTTP/1.1 204 No Content
Connection: close
Date: Fri, 17 Jul 2026 12:52:40 GMT
Server: waitress
Via: waitress
X-Powered-By: Zope (www.zope.dev), Python (www.python.org)
```

That means you updates the value in the {term}`AEMET Settings` control panel field correctly.

```{note}
You can validate the update operation, going to ``Site setup > Add-on Settings > AEMET Settings``.
```

---

(aemet-weather-forecast-route)=
## AEMET weather forecast route

This `route` is uses to fetch the current weather forecast for location defined on the {term}`AEMET Settings` {term}`Control panel`:

```shell
curl -X GET http://localhost:8080/Plone/++api++/@aemet-weather-forecast
```

This `route` returns a `JSON` object containing the {term}`AEMET` weather forecast data:

```json
{
  "forecast": [
    {
      "currentHour": 14,
      "date": "2026-07-17",
      "name": "Madrid",
      "province": "Madrid",
      "skyState": "Despejado",
      "skyStateValue": "11",
      "tempMax": "34",
      "tempMin": "20",
      "timePeriod": "12-18"
    }
  ]
}
```

This `route` can be implements in a {term}`Volto` _integration_, for example, the `WeatherForecast` component available into the {term}`volto-aemet` {term}`add-on`.
