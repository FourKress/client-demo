!macro customInstall
  DetailPrint "Register ustax-tools URI Handler"
  DeleteRegKey HKCR "ustax-tools"
  WriteRegStr HKCR "ustax-tools" "" "URL:ustax-tools"
  WriteRegStr HKCR "ustax-tools" "URL Protocol" ""
  WriteRegStr HKCR "ustax-tools\shell" "" ""
  WriteRegStr HKCR "ustax-tools\shell\Open" "" ""
  WriteRegStr HKCR "ustax-tools\shell\Open\command" "" "$INSTDIR\${APP_EXECUTABLE_FILENAME} %1"
!macroend
