
# simple-openstack-mcp
This is a `fastmcp`-based MCP server that allows an LLM to execute complex OpenStack commands for you in an environment where `openstack-cli` is runnable.

## How To

### OpenStack Configuration

The `openstack-cli` must be executable in the environment where this MCP server runs. Additionally, the authentication credentials for the target OpenStack cloud must be stored in `clouds.yaml`. Here is an example:

```yaml
clouds:
  ...: # openstack_cloud_name
    auth:
      auth_url: ...
      username: ...
      password: ...
      project_id: ...
      project_name: ...
      user_domain_name: ...
    region_name: ...
    interface: "public"
    identity_api_version: 3
```

### Connecting the MCP Tool

If you are using `Claude Desktop` or `VScode Copilot`, add the following to your claude_desktop_config.json. You can add similar settings to other LLM clients you wish to use.

```json
{
    "mcpServers": {
      "openstack": {
        "command": "uv",
        "args": [
          "--directory",
          "${REPOSITORY_ABS_PATH}/simple-openstack-mcp",
          "-m",
          "server"
        ]
      }
    }
}
```

If you don't have the repository cloned locally, you can also run it with uvx:

```json
{
    "mcpServers": {
      "openstack": {
        "command": "uvx",
        "args": [
          "--from",
          "git+https://github.com/choieastsea/simple-openstack-mcp",
          "simple-openstack-mcp"
        ]
      }
    }
}
```
## Running the fastmcp Server locally

The following commands should run successfully from the repository directory:

```bash
❯ uv sync
❯ uv run -m server
```