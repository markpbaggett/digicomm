# digicomm

## About

A simple Python library that wraps the Digital Commons v2 Real Time API.

## Installation

```bash
pip install digicomm
```

## Usage

```python
from digicomm import DigitalCommons

x = DigitalCommons(site_url=:'trace.tennessee.edu', key='my-digital-commons-key').query(('q', 'video'),('title', '2013'),('limit', '2'))
```
