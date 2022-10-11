!macro customInstall
  DetailPrint "Register client-demo URI Handler"
  DeleteRegKey HKCR "client-demo"
  WriteRegStr HKCR "client-demo" "" "URL:client-demo"
  WriteRegStr HKCR "client-demo" "URL Protocol" ""
  WriteRegStr HKCR "client-demo\shell" "" ""
  WriteRegStr HKCR "client-demo\shell\Open" "" ""
  WriteRegStr HKCR "client-demo\shell\Open\command" "" "$INSTDIR\${APP_EXECUTABLE_FILENAME} %1"
!macroend
