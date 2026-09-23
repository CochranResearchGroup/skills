# ChatGPT GitHub Engineering

This additive plugin contains repository-analysis workflows for ChatGPT used
alongside ChatGPT's native GitHub app. The app connection is separate from the
plugin: each user must connect GitHub and authorize the repositories they want
ChatGPT to read.

The native GitHub app is read-only. These skills search, inspect, analyze, and
cite repository content. When a workflow would normally edit files, run tests,
create issues, or open a pull request, it returns a proposed artifact or a
handoff for a write-capable coding environment instead.

## Install one skill

Run `python3 packaging/build.py --output-dir <directory>`, then upload the
desired ZIP through **ChatGPT → Plugins → Skills → Create → Upload from your
computer**.

## Install the plugin

The same command creates `chatgpt-github-engineering-plugin.zip`. A workspace
administrator can also import this repository as a marketplace using:

- Source: `https://github.com/CochranResearchGroup/skills`
- Path: blank
- Branch: the reviewed publication branch or tag

Importing the marketplace does not connect GitHub or grant repository access.
