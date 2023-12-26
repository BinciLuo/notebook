# Mac
```brew install go```
# Beego
1. ```go install github.com/beego/bee/v2@latest```
2. Add to ~/.zshrc or ~/.bash_profile:
```shell
export GOROOT=/usr/local/go
export GOPATH=$HOME/go
export PATH=$PATH:$GOPATH/bin
export PATH=$PATH:/usr/local/go/bin
export GOBIN=$GOPATH/bin
export GO111MODULE=on
export GOPROXY=https://goproxy.cn,direct
export PATH=$PATH:$GOROOT/bin:$GOBIN
```
