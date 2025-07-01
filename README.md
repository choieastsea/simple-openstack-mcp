# simple-openstack-mcp

`openstack-cli`를 실행할 수 있는 환경에서, 복잡한 오픈스택 명령어 실행을 llm이 대신해줄 수 있도록 하는 fastmcp 기반의 mcp 서버입니다.

## How To

### openstack 관련 설정

해당 mcp 서버가 실행되는 환경에서 openstack cli가 실행 가능해야하며, `clouds.yaml`에 접근하고자 하는 오픈스택의 인증 정보가 저장되어 있어야 합니다. 예시는 다음과 같습니다.

```yaml
clouds:
  ...: # openstack명
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

### mcp tool 연결
claude desktop을 사용한다면 `claude_desktop_config.json`에 아래와 같이 추가합니다. (이외에 사용하고자 하는 llm client에 다음과 같은 설정을 추가하면 됩니다)

```json
{
    "mcpServers": {
      "openstack": {
        "command": "uv",
        "args": [
          "--directory",
          "${REPOSITORY_ABS_PATH}/simple-openstack-mcp",
          "run",
          "server.py"
        ]
      }
    }
}

```
### fastmcp 서버 실행
해당 repository 디렉토리에서 다음 명령어가 정상적으로 수행되면 됩니다.
```
❯uv init
❯uv install
❯uv run server.py
```
