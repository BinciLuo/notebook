# Install
## brew
```
/bin/zsh -c "$(curl -fsSL https://gitee.com/cunkai/HomebrewCN/raw/master/Homebrew.sh)"
```
# Service
## launchctl
### Operations
- ```launchctl stop ${SERVICE_NAME}``` 
- ```launchctl start ${SERVICE_NAME}```
- ```launchctl load /Library/LaunchAgents/${SERVICE_NAME}.plist```(for all user)
### Create a service
1. ```cd /Library/LaunchAgents/```
2. ```sudo vim ${SERVICE_NAME}.plist``` and insert:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>${SERVICE_NAME}</string>
    <key>ProgramArguments</key>
    <array>
        <string>${EXEC_FILE_ABSOLUTE_PATH}</string>
        <string>${PARAM_1}</string>
        <string>${PARAM_2}</string>
    </array>
    <key>RunAtLoad</key>
    <true/>
</dict>
</plist>
```
3. ```launchctl load /Library/LaunchAgents/${SERVICE_NAME}.plist```