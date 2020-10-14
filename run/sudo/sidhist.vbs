
'
' Example usage of ICloneSecurityPrincipal::AddSidHistory
'
' Copyright (c) 1999 Microsoft Corporation



option explicit
const SCRIPT_FILENAME    = "sidhist.vbs"
const SCRIPT_SOURCE_NAME = "sidhist.vbt"
const SCRIPT_DATE        = "Aug 17 2001"
const SCRIPT_TIME        = "12:42:14"
const ARG_COUNT          = 6

' command line parameters
Dim srcDC       ' source domain controller                     
Dim srcDom      ' source domain                                
Dim srcSam      ' source principal SAM name
Dim dstDC       ' destination controller                       
Dim dstDom      ' destination domain                           
Dim dstSam      ' destination principal SAM name

If wscript.arguments.count <> ARG_COUNT Then
   PrintUsage
End If

Dim args()
ReDim args(0)
args(0) = ""

Dim i
For i = 0 to wscript.arguments.count - 1
    ReDim Preserve args(i)
    args(i) = wscript.arguments.item(i)
Next

srcDC   = GetArgValue("srcdc",   args)
srcDom  = GetArgValue("srcdom",  args)
srcSam  = GetArgValue("srcsam",  args)
dstDC   = GetArgValue("dstdc",   args)
dstDom  = GetArgValue("dstdom",  args)
dstSam  = GetArgValue("dstsam",  args)

If CheckForBadArgs(args) Then
    wscript.echo "Unknown command-line arguments specified"
    PrintUsage
End If


' Create the COM object implementing ICloneSecurity Principal

Dim clonepr
Set clonepr = CreateObject("DSUtils.ClonePrincipal")

On Error Resume Next

' Connect to the source and destination domain controllers

clonepr.Connect srcDC, srcDom, dstDC, dstDom
If Err.Number then
    DumpErr
    wscript.quit(0)
Else
    wscript.echo "Connected"
End If

' Add the SID of the source principal to the sid history of the destination
' principal.

clonepr.AddSidHistory srcSam, dstSam, 0
If Err.Number then
    DumpErr
    wscript.quit(0)
Else
    wscript.echo "Success"
End If

wscript.quit(0)



Function GetArgValue(argName, args())
    Dim a
    Dim v
    Dim iLenArgName
    Dim x
    Dim iArgCount
    Dim fullArgName

    fullArgName = "/" & argName & ":"
    iArgCount = Ubound(args)

    ' Get the length of the argname we are looking for
    iLenArgName = Len(fullArgName)
    GetArgValue = "" ' default to nothing
    
    For x = 0 To iArgCount 
        If Len(args(x)) >= iLenArgName Then

            a = Mid(args(x), 1, iLenArgName)
            If UCase(a) = UCase(fullArgName) Then

                ' erase it so we can look for unknown args later
                v = args(x)
                args(x) = ""

                If Len(v) > iLenArgName Then
                    GetArgValue = Mid(v, iLenArgName + 1)
                    Exit Function
                Else 
                    GetArgValue = ""
                    Exit Function
                End If
            End If
        End If
    Next 
End Function



Function CheckForBadArgs(args())
    For i = 0 to UBound(args) 
        If Len(args(i)) > 0 Then
            CheckForBadArgs = 1
            Exit Function
        End If
    Next

    CheckForBadArgs = 0
End Function
                


Sub PrintUsage
   Echo "Usage: cscript " & SCRIPT_FILENAME & " /srcdc:<dcname> /srcdom:<domain>"
   Echo "/srcsam:<name> /dstdc:<dcname> /dstdom:<domain> /dstsam:<name>"
   Echo ""
   Echo "Parameters:"
   Echo " /srcdc   - source domain controller NetBIOS computer name (without leading \\)"
   Echo ""
   Echo " /srcdom  - source domain NetBIOS name"
   Echo ""
   Echo " /srcsam  - source principal SAM name"
   Echo ""
   Echo " /dstdc   - destination domain controller NetBIOS computer name (without "
   Echo "            leading \\)"
   Echo "            This script must be run on the machine indicated here."
   Echo ""
   Echo " /dstdom  - destination domain DNS name"
   Echo ""
   Echo " /dstsam  - destination principal SAM name"
   Echo ""
   Echo SCRIPT_DATE & " " & SCRIPT_TIME
   wscript.quit(0)
End Sub



Sub DumpErr
    wscript.echo "Error 0x" & CStr(Hex(Err.Number)) & " occurred."
    wscript.echo "Error Description: " & Err.Description
    wscript.echo "Error HelpContext: " & Err.HelpContext
    wscript.echo "Error HelpFile   : " & Err.HelpFile
    wscript.echo "Error Source     : " & Err.Source
    Err.Clear
End Sub


sub Echo(byref message)
   wscript.echo message
end sub
