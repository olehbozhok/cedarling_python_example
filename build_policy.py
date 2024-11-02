import json
import base64
from datetime import datetime


SCHEMA_PATH = "project_files/cedarling_core_schema.json"
POLICY_PATH = "project_files/cedarling_core_policies.cedar"


def build_schema():
    with open(SCHEMA_PATH) as f:
        # load using json to validate json on correctness
        schema = json.load(f)
    # convert dict to json string utf-8 and encode to base64
    return base64.b64encode(json.dumps(schema).encode('utf-8')).decode('utf-8')


def build_policies():
    policies = {}
    with open(POLICY_PATH, 'r', encoding='utf-8') as f:
        # assume that each policy start with "//"
        # and first line is a comment

        for raw_policy in f.read().split('//'):
            policy_lines = raw_policy.split('\n')
            # first line is comment
            comment = policy_lines[0]

            # other lines are the policy

            policy = '\n'.join(
                filter(lambda s: s.strip() != "", policy_lines[1:]))

            if policy == "":
                continue

            policies[str(policy.__hash__())] = {
                "description": comment,
                "policy_content": base64.b64encode(policy.encode('utf-8')).decode('utf-8'),
                "creation_date": datetime.now().isoformat()
            }
    return policies


def build_policy_store():
    policy_store = {
        "cedar_version": "v2.4.7",
        "cedar_policies": build_policies(),
        "cedar_schema": build_schema(),
        "trusted_issuers": [
            #     {
            #     "name": "Jans",
            #     "description": "Jans IDP",
            #     "openid_configuration_endpoint": "https://test-casa.gluu.info/.well-known/openid-configuration",
            #     "token_metadata": []
            # }
        ]
    }
    return policy_store


if __name__ == "__main__":
    with open("policy_store.json", 'w') as f:
        json.dump(build_policy_store(), f)
