---
myst:
  html_meta:
    "description": "Terms and definitions used throughout the AEMET integration with Plone documentation."
    "property=og:description": "Terms and definitions used throughout the AEMET integration with Plone documentation."
    "property=og:title": "Glossary"
    "keywords": "AEMET, service, Plone, integration, documentation, glossary, term, definition"
---

This glossary provides terms and definitions relevant to {term}`AEMET` integration with {term}`Plone`.

(glossary-label)=

# Glossary

```{glossary}
:sorted: true

AEMET
    `AEMET` (Agencia Estatal de Meteorología) is the _Spanish State Meteorological Agency_.
    It is the public body responsible for the development, implementation, and provision of meteorological
    and climatological services in Spain. It publishes official weather forecasts, warnings, and climate data
    through its website and open data services, including XML feeds per municipality.

    ```{tip}
    More infomation checkout the official [website](https://www.aemet.es/es/portada).
    ```

Plone
    [Plone](https://plone.org/) is an open-source content management system that is used to create, edit, and
    manage digital content, like websites, intranets and custom solutions. It comes with over 20 years of growth,
    optimisations, and refinements. The result is a system trusted by governments, universities, businesses, and
    other organisations all over the world.

Volto
    [Volto](https://github.com/plone/volto) is the default React-based frontend for {term}`Plone` 6.
    It communicates with the {term}`Plone` backend via exclusively through the {term}`plone.restapi` REST API.
    The {term}`volto-aemet` consumes the {term}`@aemet-weather-forecast` endpoint to display weather data in {term}`Volto` blocks.

add-on
    An add-on in {term}`Plone` extends its core functionality.
    It is distributed as a Python package and installed via the {term}`Plone` Site Setup.
    {term}`collective.volto.aemet` is a {term}`Plone` add-on.

    Its companion {term}`volto-aemet` is a {term}`Volto` (JavaScript) add-on.

    In {term}`Volto`, an add-on is a JavaScript package.

    In {term}`Plone` core, an add-on is a Python package.

    -   [Plone core add-ons](https://github.com/collective/awesome-plone#readme)
    -   [Volto add-ons](https://github.com/collective/awesome-volto#readme)
    -   [Add-ons tagged with the trove classifier `Framework :: Plone` on PyPI](https://pypi.org/search/?c=Framework+%3A%3A+Plone)

plone.restapi
    [plone.restapi](https://6.docs.plone.org/plone.restapi/docs/source/) is the RESTful hypermedia API for {term}`Plone`.
    It enables {term}`Volto` and other clients to interact with {term}`Plone` content and configuration over HTTP using JSON.
    This {term}`add-on` registers its services and control panel adapters through ``plone.restapi``.
    It is used by {term}`collective.volto.aemet` to expose the `@aemet-settings` and `@aemet-weather-forecast` endpoints to the Volto frontend.

Control Panel
    Checkout the {term}`AEMET Settings` term.

AEMET Settings
    The {term}`AEMET Settings` configuration panel available in {term}`Plone`'s Site Setup under `Add-on Configuration`.
    It allows administrators to configure the {term}`Location ID` field stored in {term}`plone.registry`.

plone.registry
    A {term}`Plone` component that stores configuration values as named records.
    {term}`collective.volto.aemet` uses it to persist the {term}`IAemetSettings` interface fields ({term}`location_id`).

Registry
    The {term}`Plone` Registry is a key-value store for site configuration, managed by the {term}`plone.registry` package.
    Settings are declared through Zope schema interfaces and stored as typed records.
    In this {term}`add-on` the records are declared in {term}`IAemetSettings` and stored under the ``aemet`` prefix (e.g. ``aemet.location_id``).
    They can be read using ``plone.api.portal.get_registry_record("aemet.location_id")``.

GenericSetup
    A {term}`Plone` framework for managing configuration through filesystem-based import and export profiles.
    {term}`collective.volto.aemet` uses a `GenericSetup` profile to register its registry records and control panel on installation.

collective.volto.aemet
    `collective.volto.aemet` is the {term}`Plone` {term}`add-on` that integrates {term}`AEMET` weather data into a {term}`Plone` site.
    It provides a control panel to configure the target municipality, a REST API endpoint to expose weather forecast data, and a
    browser layer ({term}`IAemetLayer`) to scope its components.
    It is designed to work together with the {term}`volto-aemet` {term}`Volto` {term}`add-on`.

    ```{tip}
    More infomation checkout the official [documentation](https://collectivevoltoaemet.readthedocs.io/en/latest/).
    ```

volto-aemet
    `volto-aemet` is the {term}`Volto` {term}`add-on` that integrates {term}`AEMET` weather data into a {term}`Plone` site via
    the {term}`collective.volto.aemet` {term}`add-on`.
    It provides a control panel to configure the target municipality, Two {term}`Volto` content blocks.

    ```{tip}
    More infomation checkout the official [documentation](https://volto-aemet.readthedocs.io/en/latest/).
    ```

IAemetLayer
    ``IAemetLayer`` is a browser layer marker interface provided by this {term}`add-on`.
    It is applied to the request when the {term}`add-on` is installed, scoping all views, services, and adapters to sites where the {term}`add-on` is active.

IAemetSettings
    ``IAemetSettings`` is the Zope schema interface that declares the configuration fields for the {term}`AEMET` {term}`add-on`.
    Currently it defines a single field: {term}`location_id`.
    It is used as the schema for both the {term}`AEMET Settings` control panel and the {term}`Plone` {term}`Registry` records.

Location ID
location_id
    The Location ID is a numeric code that uniquely identifies a Spanish municipality in the {term}`AEMET` service in `XML` data.
    It is used to construct the URL of the XML feed, for example:
    ``https://www.aemet.es/xml/municipios/localidad_28058.xml`` for Madrid (``28058``),
    or ``localidad_41091.xml`` for Sevilla (``41091``).
    It is configured via the {term}`AEMET Settings` control panel and stored in the {term}`Plone` registry under the key ``aemet.location_id``.

@@aemet-settings
    A REST API endpoint exposed by {term}`collective.volto.aemet` that provides the {term}`AEMET Settings` to the {term}`Volto` frontend.
    Anonymous users cannot access the {term}`Plone` registry directly, so this dedicated endpoint is used instead.

    ```{note}
    Take a look to the {ref}`aemet-settings-route` section.
    ```

@aemet-weather-forecast
    A REST API endpoint exposed by this {term}`add-on` that provides the publicly accessible (``zope2.View`` permission) and returns a
    JSON object with the current day's weather forecast for the configured municipality, fetched from the {term}`AEMET` XML service.

    **Example:** Take a look to the {ref}`aemet-weather-forecast-route` section.

WeatherForecastGet
    ``WeatherForecastGet`` is the {term}`Plone` REST API service class (``plone.restapi.services.Service``) that handles ``GET`` requests to the {term}`@aemet-weather-forecast` endpoint.
    It retrieves the {term}`Location ID` from the registry, fetches the AEMET XML feed, parses it, and returns a JSON structure with the forecast for the current day, including temperatures, sky state, and time period.

Sky state
estado_cielo
    The sky state is a meteorological descriptor included in the AEMET XML feed for each time period of the day.
    It consists of a numeric code (e.g. ``11`` for *Despejado*) and a human-readable description (e.g. *Cubierto*, *Tormenta*).
    The {term}`WeatherForecastGet` service selects the sky state for the active time period and falls back to broader periods (``00-12``, ``12-24``, ``00-24``) if the specific one is not available.

Time period
    A time period is a 6-hour interval used in the AEMET XML feed to segment the day's forecast.
    The four standard periods are ``00-06``, ``06-12``, ``12-18``, and ``18-24``.
    The {term}`WeatherForecastGet` service selects the period matching the current server hour.

```
