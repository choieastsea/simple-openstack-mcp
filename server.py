import os
from fastmcp import FastMCP
from commander import OpenStackCommander

mcp = FastMCP(name="simple-openstack-mcp", dependencies=[])


@mcp.tool()
def exec_openstack(cmd: str) -> str:
    """
    Execute an OpenStack CLI command.
    """
    if not cmd.strip().startswith("openstack"):
        raise ValueError("Command must start with 'openstack'")
    return OpenStackCommander.execute(cmd)


if __name__ == "__main__":
    clouds_yaml_path = os.path.join(os.getcwd(), "clouds.yaml")
    if os.path.exists(clouds_yaml_path):
        os.environ["OS_CLIENT_CONFIG_FILE"] = clouds_yaml_path
    print("Using clouds.yaml from:", os.environ["OS_CLIENT_CONFIG_FILE"])
    mcp.run()
