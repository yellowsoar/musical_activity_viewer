<!-- MarkdownTOC -->

- [About](#about)
- [Run server](#run-server)
- [DNS](#dns)
  - [Any HTTP Server](#any-http-server)
  - [SSH tunnel](#ssh-tunnel)
- [Contribute](#contribute)
- [Document](#document)

<!-- /MarkdownTOC -->

## About

This is a musical activity viewer webste.

## Run server

- Install `docker engine`  
  <https://docs.docker.com/engine/install/>
- Install `make`  
  <https://www.gnu.org/software/make/>
- Install `git`  
  <https://git-scm.com/book/en/v2/Getting-Started-Installing-Git>
- Clone MSA repository to the server  
  `git clone https://github.com/yellowsoar/musical_activity_viewer.git`
- Change Directory to MSA folder  
  `cd musical_activity_viewer`  
  Generate `.env` file  
  `make gen-env`
- Use the following commands to run MSA  
  `make rm build up log` or `make build go`
- Open the following URL  
  <http://127.0.0.1:8888>
- Note:  
  By default all web server listen on 0.0.0.0  
  To keep it safe feel free to modify it.
- Done!

## DNS

There are at leas two solutions to make it work on the host server.

### Any HTTP Server

- Install any http server you like on the host server.
- Forward the request to localhost:8080
- Done!

### SSH tunnel

- Cloudflare tunnel  
  <https://www.cloudflare.com/products/tunnel/>
- Ngrok  
  <https://ngrok.com/docs/getting-started/>
- Check awesome selfhosted  
  <https://github.com/awesome-selfhosted/awesome-selfhosted#proxy>

## Contribute

Comming soon...

## Document

Working in progress...

