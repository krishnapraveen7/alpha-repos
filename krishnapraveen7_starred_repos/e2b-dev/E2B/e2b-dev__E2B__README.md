<p align="center">
  <img width="100" src="/readme-assets/logo-circle.png" alt="e2b logo">
</p>

<h1 align="center">
  Cloud Runtime for AI Agents
</h1>

<h3 align="center">
  Secure sandboxed cloud environments made for AI agents and AI apps
</h3>

<h4 align="center">
  <a href="https://e2b.dev/docs">Docs</a> |
  <a href="https://e2b.dev">Website</a> |
  <a href="https://discord.gg/U7KEcGErtQ">Discord</a> |
  <a href="https://twitter.com/e2b_dev">Twitter</a>
</h4>

<h4 align="center">
  <a href="https://pypi.org/project/e2b/">
    <img alt="Last 1 month downloads for the Python SDK" loading="lazy" width="200" height="20" decoding="async" data-nimg="1"
    style="color:transparent;width:auto;height:100%" src="https://img.shields.io/pypi/dm/e2b?label=PyPI%20Downloads">
  </a>
  <a href="https://www.npmjs.com/package/e2b">
    <img alt="Last 1 month downloads for the Python SDK" loading="lazy" width="200" height="20" decoding="async" data-nimg="1"
    style="color:transparent;width:auto;height:100%" src="https://img.shields.io/npm/dm/e2b?label=NPM%20Downloads">
  </a>
</h4>

<img width="100%" src="/readme-assets/preview.png" alt="Cover image">

## What is E2B?

E2B Sandbox is a secure sandboxed cloud environment made for AI agents and AI
apps. Sandboxes allow AI agents and apps to have long running cloud secure
environments. In these environments, large language models can use the same
tools as humans do. For example:

- Cloud browsers
- GitHub repositories and CLIs
- Coding tools like linters, autocomplete, "go-to defintion"
- Running LLM generated code
- Audio & video editing

**The E2B sandbox can be connected to any LLM and any AI agent or app.**

---

### Code interpreter SDK
We have built a [dedicated SDK](https://github.com/e2b-dev/code-interpreter) for building custom code interpreters in your AI apps. It's build on top of E2B and our core E2B SDK.

### Getting started & documentation

> Please visit [documentation](https://e2b.dev/docs) to get started.

To create and control a sandbox, you use our SDK:

**Python**

1. Install SDK

```bash
pip install e2b
```

2. Start sandbox

```py
from e2b import Sandbox

# Create sandbox
sandbox = Sandbox()

# Let an LLM use the sandbox here
# Visit https://e2b.dev/docs/sandbox/overview to learn more about sandboxes.

# Close sandbox once done
sandbox.close()
```

**JavaScript & TypeScript**

1. Install SDK

```bash
npm install e2b
```

2. Start sandbox

```js
import { Sandbox } from "e2b";

// Create sandbox
const sandbox = await Sandbox.create();

// Let an LLM use the sandbox here
// Visit https://e2b.dev/docs/sandbox/overview to learn more about sandboxes.

// Close sandbox once done
await sandbox.close();
```

## Repository Structure

This repository is a monorepo containing:

1. [Python SDK](/packages/python-sdk)
1. [JS SDK](/packages/js-sdk)
1. [CLI](/packages/cli)
1. [Documentation](/apps/web/)
