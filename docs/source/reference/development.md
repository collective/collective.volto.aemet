---
myst:
  html_meta:
    "description": "AEMET integration with Volto development guides"
    "property=og:description": "AEMET Volto development guides"
    "property=og:title": "AEMET integration with Volto development guides"
    "keywords": "Volto, AEMET integration with Volto, development, guides"
---

# Development

The development of this add-on is done in isolation using a new approach using pnpm workspaces and latest `mrs-developer` and other Volto core improvements.
For this reason, it only works with pnpm and Volto 18 (currently in alpha).

## Prerequisites ✅

-   An [operating system](https://6.docs.plone.org/install/create-project-cookieplone.html#prerequisites-for-installation) that runs all the requirements mentioned.
-   [uv](https://6.docs.plone.org/install/create-project-cookieplone.html#uv)
-   [Make](https://6.docs.plone.org/install/create-project-cookieplone.html#make)
-   [Git](https://6.docs.plone.org/install/create-project-cookieplone.html#git)
-   [Docker](https://docs.docker.com/get-started/get-docker/) (optional)

## Installation 🔧

1.  Clone this repository, then change your working directory.

    ```shell
    git clone git@github.com:collective/collective.volto.aemet.git
    cd collective.volto.aemet
    ```

2.  Install this code base.

    ```shell
    make install
    ```


## Make convenience commands

Run `make help` to list the available commands.

```text
check                          Check and fix code base according to Plone standards
clean                          Clean installation and instance (data left intact)
console                        Start a console into a Plone instance
create-site                    Create a new site from scratch
format                         Check and fix code base according to Plone standards
help                           This help message
install                        Install Plone and dependencies
lint                           Check and fix code base according to Plone standards
release                        Create a release
remove-data                    Remove all content
start                          Start a Plone instance on localhost:8080
sync                           Sync project dependencies
test                           run tests
test-coverage                  run tests with coverage
```

## Development environment set up

Install package requirements.

```shell
make install
```

## Start developing

Start the backend.

```shell
make sync
```

In a separate terminal session, start the frontend.

```shell
make start
```

## Lint code

Run Python tools in analyze mode.

```shell
make lint
```

## Format code

Run Python tools in fix mode.

```shell
make format
```

## i18n

Extract the i18n messages to locales.

```shell
make i18n
```

## Unit tests

Run unit tests.

```shell
make test
```

Run unit tests with coverage report.

```shell
test-coverage
```

## Contents

Create a new site from scratch

```shell
make create-site
```

Remove all content

```shell
make remove-data
```

## Releases

Create a release of this add-on

```shell
make release
```

---

## Add features using `plonecli` or `bobtemplates.plone`

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

### See also:

You can check the list of available subtemplates in the [`bobtemplates.plone` `README.md` file](https://github.com/plone/bobtemplates.plone/?tab=readme-ov-file#provided-subtemplates).
See also the documentation of [Mockup and Patternslib](https://6.docs.plone.org/classic-ui/mockup.html) for how to build the UI toolkit for Classic UI.
