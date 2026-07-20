# collective.volto.aemet

[![Latest Version](https://img.shields.io/pypi/v/collective.volto.aemet.svg)](https://pypi.org/project/collective.volto.aemet/) [![Supported - Python Versions](https://img.shields.io/pypi/pyversions/collective.volto.aemet.svg?style=plastic)](https://pypi.org/project/collective.volto.aemet/) [![Number of PyPI downloads](https://img.shields.io/pypi/dm/collective.volto.aemet.svg)](https://pypi.org/project/collective.volto.aemet/) [![License](https://img.shields.io/pypi/l/collective.volto.aemet.svg)](https://pypi.org/project/collective.volto.aemet/)

[![AEMET](https://raw.githubusercontent.com/collective/collective.volto.aemet/refs/heads/main/docs/source/_static/logo.svg)](https://www.aemet.es/)

An integration for the [AEMET](https://www.aemet.es/) service with Plone.

## Features

- Control panel in Plone registry to manage ``AEMET settings``.
- RestApi endpoint that exposes these settings for Volto.
- RestApi endpoint that exposes the current weather forecast for location defined on the **AEMET Settings** control panel.

## Screenshot

**Add-on Configuration Access**

<img width="290" alt="Add-on Configuration" src="https://raw.githubusercontent.com/collective/collective.volto.aemet/refs/heads/main/docs/source/images/addon-configuration-aemet-icon.png">

---

**AEMET Settings control panel**

<img width="720" alt="AEMET Settings" src="https://raw.githubusercontent.com/collective/collective.volto.aemet/refs/heads/main/docs/source/images/aemet-settings.png">

---

## Volto integration

To use this product in Volto, your Volto project needs to include a new add-on: https://github.com/collective/volto-aemet

## Translations

This product has been translated into

- English
- Spanish

## Compatibility

- Tested with Python 3.12 and Plone 6.1.5.

## Install it

Install `collective.volto.aemet` with `pip`:

```shell
pip install collective.volto.aemet
```

And to create the `Plone` site:

```shell
make create-site
```

---

## @aemet-settings route

Anonymous users can't access registry resources by default with ``plone.restapi`` (there is a special permission).

To avoid enabling registry access to everyone, this package exposes a dedicated RestApi route with ``AEMET`` settings: *@aemet-settings*:

Get the information from the ``AEMET`` settings via `curl` command:

```shell
curl -X GET http://localhost:8080/Plone/@controlpanels/aemet-settings \
  -H "Accept: application/json" \
  --user admin:admin
```

This route returns a JSON object containing the ``AEMET`` weather forecast settings and data via `curl` command:

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

Update the `location_id` field value of the ``AEMET`` settings:

```shell
curl -i -X PATCH http://localhost:8080/Plone/@controlpanels/aemet-settings \
  -H "Accept: application/json" \
  -H "Content-Type: application/json" \
  --data '{"location_id": "28058"}' \
  --user admin:admin
```

This route returns a HTTP response:

```shell
HTTP/1.1 204 No Content
Connection: close
Date: Fri, 17 Jul 2026 12:52:40 GMT
Server: waitress
Via: waitress
X-Powered-By: Zope (www.zope.dev), Python (www.python.org)
```

---

## @aemet-weather-forecast route

This route is used to fetch the current weather forecast for location defined on the **AEMET Settings control panel**:

```shell
curl -X GET http://localhost:8080/Plone/++api++/@aemet-weather-forecast
```

This route returns a JSON object containing the ``AEMET`` weather forecast data:

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

This can be used in for a _Volto integration_ for example the `WeatherForecast` component available into the [volto-aemet](https://github.com/collective/volto-aemet) add-on.

---

## Contribute

- [Issue tracker](https://github.com/collective/collective.volto.aemet/issues)
- [Source code](https://github.com/collective/collective.volto.aemet/)
- [Documentation](https://collectivevoltoaemet.readthedocs.io/)

### Prerequisites ✅

-   An [operating system](https://6.docs.plone.org/install/create-project-cookieplone.html#prerequisites-for-installation) that runs all the requirements mentioned.
-   [uv](https://6.docs.plone.org/install/create-project-cookieplone.html#uv)
-   [Make](https://6.docs.plone.org/install/create-project-cookieplone.html#make)
-   [Git](https://6.docs.plone.org/install/create-project-cookieplone.html#git)
-   [Docker](https://docs.docker.com/get-started/get-docker/) (optional)

### Installation 🔧

1.  Clone this repository, then change your working directory.

    ```shell
    git clone git@github.com:collective/collective.volto.aemet.git
    cd collective.volto.aemet
    ```

2.  Install this code base.

    ```shell
    make install
    ```


### Add features using `plonecli` or `bobtemplates.plone`

This package provides markers as strings (`<!-- extra stuff goes here -->`) that are compatible with [`plonecli`](https://github.com/plone/plonecli) and [`bobtemplates.plone`](https://github.com/plone/bobtemplates.plone).
These markers act as hooks to add all kinds of subtemplates, including behaviors, control panels, upgrade steps, or other subtemplates from `plonecli`.

To run `plonecli` with configuration to target this package, run the following command.

```shell
make add <template_name>
```

For example, you can add a content type to your package with the following command.

```shell
make add content_type
```

You can add a behavior with the following command.

```shell
make add behavior
```

#### See also:

You can check the list of available subtemplates in the [`bobtemplates.plone` `README.md` file](https://github.com/plone/bobtemplates.plone/?tab=readme-ov-file#provided-subtemplates).
See also the documentation of [Mockup and Patternslib](https://6.docs.plone.org/classic-ui/mockup.html) for how to build the UI toolkit for Classic UI.

## Credits

Developed with the support of:

- [Agencia Estatal de Meteorología - AEMET. Gobierno de España](https://www.aemet.es/).

  <img width="500" alt="AEMET Logo" src="https://raw.githubusercontent.com/collective/collective.volto.aemet/refs/heads/main/docs/source/images/aemet-logo-blue.svg">

- [Instituto Municipal de Deportes - IMD, Seville City Council, Spain](https://imd.sevilla.org/).

  <img width="200" alt="IMD Logo" src="https://raw.githubusercontent.com/collective/collective.volto.aemet/refs/heads/main/docs/source/images/imd-ayto-logo.svg">

### Acknowledgements 🙏

Generated using [Cookieplone (0.9.10)](https://github.com/plone/cookieplone) and [cookieplone-templates (eb40854)](https://github.com/plone/cookieplone-templates/commit/eb4085428af6261227bcb086ece110bbe5475d89) on 2025-11-06 19:48:38.313942. A special thanks to all contributors and supporters!

## Authors

This product was developed by [Leonardo J. Caballero G.](https://github.com/macagua).

<img width="100" alt="Leonardo J. Caballero G." src="https://avatars.githubusercontent.com/u/185395?v=4&size=100">

### Contributors

You can see a list of contributors in the [CONTRIBUTORS.md](https://raw.githubusercontent.com/collective/collective.volto.aemet/refs/heads/main/CONTRIBUTORS.md) file.

## License

The project is licensed under GPLv2.
