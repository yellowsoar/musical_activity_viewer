<!-- MarkdownTOC -->

- [About](#about)
- [Run on server](#run-on-server)
- [Contribute](#contribute)
- [Document](#document)

<!-- /MarkdownTOC -->

## About

This is a musical activity viewer webste.

## Run on server

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
  To keep it safe please modify it, if you know what you are doing.
- Done!

## Contribute

Comming soon...

## Document

Working in progress...

