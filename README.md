# Cedarling python example

## Intro

At first you need to install the python module from documentation.

Then initialize virtual environment with cedarling python module.

Role by default is read from user_token `role` field.

___

## Cedar-policy cli

### Install

```bash
cargo install cedar-policy-cli
```

### Translate schema to json

```bash
cedar translate-schema --direction cedar-to-json -s .\project_files\cedarling_core.schema  > .\project_files\cedarling_core_schema.json
```

## Build policy store

This script read schema and policies from `project_files` folder, then build policy store file.

```bash
python3 build_policy.py
```

To script work correctly in `cedarling_core_policies.cedar` file before each policy should present comment.

## Run example

```bash
python example.py
```
