# container : code-server

    
[image](https://docs.linuxserver.io/images/docker-code-server/)


## docker compose
    
```yaml
---
services:
  code-server:
    image: lscr.io/linuxserver/code-server:latest
    container_name: code-server
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Etc/UTC
      - PASSWORD= #optional
      - HASHED_PASSWORD= #optional
      - SUDO_PASSWORD=password #optional
      - SUDO_PASSWORD_HASH= #optional
      - PROXY_DOMAIN= #optional
      - DEFAULT_WORKSPACE= #optional
    volumes:
      - ./config:/config
    ports:
      - 8443:8443
    restart: unless-stopped
```