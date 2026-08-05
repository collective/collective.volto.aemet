---
myst:
  html_meta:
    "description": "AEMET integration with Plone how-to guides"
    "property=og:description": "AEMET Plone how-to guides"
    "property=og:title": "AEMET integration with Plone how-to guides"
    "keywords": "AEMET, service, Plone, integration, documentation, how-to, guides"
---

# Security access

The {term}`collective.volto.aemet` {term}`add-on` includes the following roles and permissions:

## Roles

- ``AEMET`` role.

  ```{note}
  New feature inclueded in this {term}`add-on`.
  ```

## Permissions

- ``volto.aemet: Manage AEMET Settings``

  ```{note}
  New feature inclueded in this {term}`add-on`.
  ```

  This permission grants access to the following roles:

  - ``AEMET`` role.

    ```{tip}
    If to grant this role to a user, this inherited the permissions that included, and there are details bellow:
    ```

- The ``Plone Site Setup: Overview`` permission grants access to the `Site Setup: Overview ` view to the following roles:

  - The ``Manager`` role.

  - The ``Site Administrator`` role.

  - The ``AEMET`` role.
