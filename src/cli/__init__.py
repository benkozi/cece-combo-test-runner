"""The `ufs-chem-assay` entrypoint: assembles a run of the application under
test — source checkout, target-driver build, input data, the pytest
session — from one YAML run config, rendering shell scripts and executing
them on this node. pytest stays the test entry point; no test logic lives
here."""
