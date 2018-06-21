::open the start softwares
::echat_desktop proj
E:
cd /workspace/echat_desktop
tasklist | find /i "node.exe" && taskkill /f /t /im node.exe
tasklist | find /i "node.exe" || start "node" node proxy.js 
  