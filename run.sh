cedar translate-schema --direction cedar-to-json -s ./project_files/cedarling_core.schema  > ./project_files/cedarling_core_schema.json

python ./build_policy.py

cargo run


echo "done"
