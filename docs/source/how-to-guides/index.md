---
myst:
  html_meta:
    "description": "AEMET integration with Plone how-to guides"
    "property=og:description": "AEMET Plone how-to guides"
    "property=og:title": "AEMET integration with Plone how-to guides"
    "keywords": "Plone, AEMET integration with Plone, how-to, guides"
---

# General information

This part of the documentation contains how-to guides, including installation and usage.

## Features

- Control panel in Plone registry to manage ``AEMET settings``.

- RestApi endpoint that exposes these ``AEMET settings`` for _Volto integration_.

- RestApi endpoint that exposes the current _weather forecast_ for the _Location ID_ defined on the ``AEMET settings`` control panel.

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

## Enable it

Go to the `Site setup`, next to the `Add-ons` control panel, find the `collective.volto.aemet` add-on and click on the `Install` button. 

## Setting it

This integration uses the `AEMET` service called '[Predicción por municipios](https://www.aemet.es/es/eltiempo/prediccion/municipios)'
on its website. For example, for the every municipality:

- '[Sevilla (Sevilla)](https://www.aemet.es/es/eltiempo/prediccion/municipios/sevilla-id41091)', it provides very detailed information
   on the weather forecast for this municipality. It also exports information in `XML` format:

   - https://www.aemet.es/xml/municipios/localidad_41091.xml

     **NOTE:** The `XML` file name has a prefix called `localidad_` and a suffix with an **ID**. For example, the ID for the municipality
     of _Seville_ is `41091`. This **ID** will be used later in the `AEMET Settings` control panel.

To use this add-on, go to the `Site setup`, next to the ``Add-on Configuration`` icon, as shown below:

<img width="290" alt="Add-on Configuration" src="../images/addon-configuration-aemet-icon.png">

---

This `AEMET Settings`, you can access the control panel, as shown below:

<img width="720" alt="AEMET Settings" src="../images/aemet-settings.png">

In this control panel, you can configure the following fields:

- ``Location ID``, The Location ID of the `AEMET` service, for example '41091' to Sevilla location ID.

## Use it

To use the `AEMET` integration you need add the [volto-aemet](https://github.com/collective/volto-aemet) add-on, in your Volto project and
use the amazain features incluided.
