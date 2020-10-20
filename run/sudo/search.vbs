
'********************************************************************
'*
'* File:        SEARCH.VBS
'* Created:     August 1998
'* Version:     1.0
'*
'* Main Function: Performs an LDAP search based on given criteria.
'* Usage: SEARCH.VBS adspath [/C:criteria] [/S:scope] [/P:properties]
'*        [/O:outputfile] [/U:username] [/W:password] [/Q]
'*
'* Copyright (C) 1998 Microsoft Corporation
'*
'********************************************************************

OPTION EXPLICIT
ON ERROR RESUME NEXT

'Define constants
CONST CONST_ERROR                   = 0
CONST CONST_WSCRIPT                 = 1
CONST CONST_CSCRIPT                 = 2
CONST CONST_SHOW_USAGE              = 3
CONST CONST_PROCEED                 = 4

'Declare variables
Dim strOutputFile, intOpMode, blnQuiet, i
Dim strADsPath, strCriteria, strProperties,  strScope, strUserName, strPassword
ReDim strArgumentArray(0)

'Initialize variables
strArgumentArray(0) = ""
blnQuiet = False
strADsPath = ""
strCriteria = "ObjectCategory=*"
strProperties = "ADsPath;"
strScope = "OneLevel"
strUserName = ""
strPassword = ""
strOutputFile = ""

'Get the command line arguments
For i = 0 to Wscript.arguments.count - 1
    ReDim Preserve strArgumentArray(i)
    strArgumentArray(i) = Wscript.arguments.Item(i)
Next

'Check whether the script is run using CScript
Select Case intChkProgram()
    Case CONST_CSCRIPT
        'Do Nothing
    Case CONST_WSCRIPT
        WScript.Echo "Please run this script using CScript." & vbCRLF & _
            "This can be achieved by" & vbCRLF & _
            "1. Using ""CScript SEARCH.vbs arguments"" for Windows 95/98 or" & vbCRLF & _
            "2. Changing the default Windows Scripting Host setting to CScript" & vbCRLF & _
            "    using ""CScript //H:CScript //S"" and running the script using" & vbCRLF & _
            "    ""SEARCH.vbs arguments"" for Windows NT."
        WScript.Quit
    Case Else
        WScript.Quit
End Select


'Parse the command line
intOpMode = intParseCmdLine(strArgumentArray, strADsPath, strCriteria, strProperties, _
            strScope, blnQuiet, strUserName, strPassword, strOutputFile)
If Err.Number then
    Print "Error 0x" & CStr(Hex(Err.Number)) & " occurred in parsing the command line."
    If Err.Description <> "" Then
        Print "Error description: " & Err.Description & "."
    End If
    WScript.Quit
End If

Select Case intOpMode
    Case CONST_SHOW_USAGE
        Call ShowUsage()
    Case CONST_PROCEED
        Call Search(strADsPath, strCriteria, strProperties, _
             strScope, strUserName, strPassword, strOutputFile)
    Case CONST_ERROR
        'Do nothing.
    Case Else                    'Default -- should never happen
        Print "Error occurred in passing parameters."
End Select

'********************************************************************
'*
'* Function intChkProgram()
'* Purpose: Determines which program is used to run this script.
'* Input:   None
'* Output:  intChkProgram is set to one of CONST_ERROR, CONST_WSCRIPT,
'*          and CONST_CSCRIPT.
'*
'********************************************************************

Private Function intChkProgram()

    ON ERROR RESUME NEXT

    Dim strFullName, strCommand, i, j

    'strFullName should be something like C:\WINDOWS\COMMAND\CSCRIPT.EXE
    strFullName = WScript.FullName
    If Err.Number then
        Print "Error 0x" & CStr(Hex(Err.Number)) & " occurred."
        If Err.Description <> "" Then
            If Err.Description <> "" Then
                Print "Error description: " & Err.Description & "."
            End If
        End If
        intChkProgram =  CONST_ERROR
        Exit Function
    End If

    i = InStr(1, strFullName, ".exe", 1)
    If i = 0 Then
        intChkProgram =  CONST_ERROR
        Exit Function
    Else
        j = InStrRev(strFullName, "\", i, 1)
        If j = 0 Then
            intChkProgram =  CONST_ERROR
            Exit Function
        Else
            strCommand = Mid(strFullName, j+1, i-j-1)
            Select Case LCase(strCommand)
                Case "cscript"
                    intChkProgram = CONST_CSCRIPT
                Case "wscript"
                    intChkProgram = CONST_WSCRIPT
                Case Else       'should never happen
                    Print "An unexpected program is used to run this script."
                    Print "Only CScript.Exe or WScript.Exe can be used to run this script."
                    intChkProgram = CONST_ERROR
            End Select
        End If
    End If

End Function

'********************************************************************
'*
'* Function intParseCmdLine()
'* Purpose: Parses the command line.
'* Input:   strArgumentArray    an array containing input from the command line
'* Output:  strADsPath          ADsPath of the root of the search
'*          strCriteria         the search criteria
'*          strProperties       properties to be retrieved
'*          strScope            the search scope
'*          strUserName         name of the current user
'*          strPassword         password of the current user
'*          strOutputFile       an output file name
'*          blnQuiet            specifies whether to suppress messages
'*          intParseCmdLine     is set to one of CONST_ERROR, CONST_SHOW_USAGE, CONST_PROCEED.
'*
'********************************************************************

Private Function intParseCmdLine(strArgumentArray, strADsPath, strCriteria, _
        strProperties, strScope, blnQuiet, strUserName, strPassword, strOutputFile)

    ON ERROR RESUME NEXT

    Dim strFlag, i

    strFlag = strArgumentArray(0)

    If strFlag = "" then                'No arguments have been received
        Print "Arguments are required."
        intParseCmdLine = CONST_ERROR
        Exit Function
    End If

    If (strFlag="help") OR (strFlag="/h") OR (strFlag="\h") OR (strFlag="-h") _
        OR (strFlag = "\?") OR (strFlag = "/?") OR (strFlag = "?") OR (strFlag="h") Then
        intParseCmdLine = CONST_SHOW_USAGE
        Exit Function
    End If

    strADsPath = FormatProvider(strFlag)    'The first parameter must be the ADsPath.

    For i = 1 to UBound(strArgumentArray)
        strFlag = LCase(Left(strArgumentArray(i), InStr(1, strArgumentArray(i), ":")-1))
        If Err.Number Then            'An error occurs if there is no : in the string
            Err.Clear
            If LCase(strArgumentArray(i)) = "/q" Then
                blnQuiet = True
            Else
                Print strArgumentArray(i) & " is not recognized as a valid input."
                intParseCmdLine = CONST_ERROR
                Exit Function
            End If
        Else
            Select Case strFlag
                Case "/c"
                    strCriteria = Right(strArgumentArray(i), Len(strArgumentArray(i))-3)
                Case "/p"
                    strProperties = Right(strArgumentArray(i), Len(strArgumentArray(i))-3) & ";"
                Case "/s"
                    strScope = Right(strArgumentArray(i), Len(strArgumentArray(i))-3)
                Case "/u"
                    strUserName = Right(strArgumentArray(i), Len(strArgumentArray(i))-3)
                Case "/w"
                    strPassword = Right(strArgumentArray(i), Len(strArgumentArray(i))-3)
                Case "/o"
                    strOutputFile = Right(strArgumentArray(i), Len(strArgumentArray(i))-3)
                Case else
                    Print "Invalid flag " & """" & strFlag & """" & "."
                    Print "Please check the input and try again."
                    intParseCmdLine = CONST_ERROR
                    Exit Function
                End Select
        End If
    Next

    intParseCmdLine = CONST_PROCEED

End Function

'********************************************************************
'*
'* Sub ShowUsage()
'* Purpose: Shows the correct usage to the user.
'* Input:   None
'* Output:  Help messages are displayed on screen.
'*
'********************************************************************

Private Sub ShowUsage()

    Wscript.Echo ""
    Wscript.Echo "Performs an LDAP search based on a given criteria." & vbCRLF
    Wscript.Echo "SEARCH.VBS adspath [/C:criteria] [/S:scope] [/P:properties]"
    Wscript.Echo "[/O:outputfile] [/U:username] [/W:password] [/Q]"
    Wscript.echo "   /C, /S, /P, /O, /U, /W"
    Wscript.Echo "                 Parameter specifiers."
    Wscript.echo "   adspath       ADsPath of a user object container."
    Wscript.echo "   criteria      Criteria of the search."
    Wscript.echo "   scope         Sope of the search."
    Wscript.echo "   properties    Properties to be retrieved."
    Wscript.Echo "   outputfile    The output file name."
    Wscript.echo "   username      Username of the current user."
    Wscript.echo "   password      Password of the current user."
    Wscript.echo "   /Q            Suppresses all output messages." & vbCRLF
    Wscript.Echo "DEFAULT VALUES:"
    Wscript.Echo "   If /C is not specified the default is ObjectCategory=*."
    Wscript.Echo "   If /S is not specified the default is OneLevel."
    Wscript.Echo "   If /P is not specified the default is ADsPath." & vbCRLF
    Wscript.Echo "EXAMPLE:"
    Wscript.Echo "SEARCH.VBS ""LDAP://DC=FooFoo,DC=Foo,DC=Com"""
    Wscript.Echo "   /C:""&(ObjectCategory=user)(cn=b*)"" /P:Name /S:SubTree"
    Wscript.Echo "   lists names of all users in domain FooFoo with"
    Wscript.Echo "   cn starting with ""b""." & vbCRLF
    Wscript.Echo "NOTE:"
    Wscript.Echo "   This script requires an LDAP provider."

End Sub

'********************************************************************
'*
'* Sub Search()
'* Purpose: Performs an LDAP search based on a given criteria.
'* Input:   strADsPath      ADsPath of the root of the search
'*          strCriteria     the search criteria
'*          strProperties   properties to be retrieved
'*          strScope        the search scope
'*          strUserName     name of the current user
'*          strPassword     password of the current user
'*          strOutputFile   an output file name
'* Output:  Results of the search are either printed on screen or saved in strOutputFile.
'*
'********************************************************************

Private Sub Search(strADsPath, strCriteria, strProperties, _
    strScope, strUserName, strPassword, strOutputFile)

    ON ERROR RESUME NEXT

    Dim strProvider, strSearchPath, objConnect, objCommand
    Dim  objFileSystem, objOutputFile, objRecordSet, intResult

    'Make sure that the provide is LDAP
    strProvider = Left(strADsPath, InStr(1, strADsPath, ":"))
    If strProvider <> "LDAP:" then
        Print "The provider is not LDAP:."
        Wscript.Quit
    End If

    If strOutputFile = "" Then
        objOutputFile = ""
    Else
        'Create a filesystem object
        set objFileSystem = CreateObject("Scripting.FileSystemObject")
        If Err.Number then
            Print "Error 0x" & CStr(Hex(Err.Number)) & " opening a filesystem object."
            If Err.Description <> "" Then
                Print "Error description: " & Err.Description & "."
            End If
            Exit Sub
        End If
        'Open the file for output
        set objOutputFile = objFileSystem.OpenTextFile(strOutputFile, 8, True)
        If Err.Number then
            Print "Error 0x" & CStr(Hex(Err.Number)) & " opening file " & strOutputFile
            If Err.Description <> "" Then
                Print "Error description: " & Err.Description & "."
            End If
            Exit Sub
        End If
    End If

    strSearchPath =  "<" & strADsPath & ">;"
    strCriteria = "(" & strCriteria & ");"

    Set objConnect = CreateObject("ADODB.Connection")
    If Err.Number then
        Print "Error 0x" & CStr(Hex(Err.Number)) & " ocurred in opening a connection."
        If Err.Description <> "" Then
            Print "Error description: " & Err.Description & "."
        End If
        Exit Sub
    End If

    Set objCommand = CreateObject("ADODB.Command")
    If Err.Number then
        Print "Error 0x" & CStr(Hex(Err.Number)) & " ocurred in creating the command object."
        If Err.Description <> "" Then
            Print "Error description: " & Err.Description & "."
        End If
        Exit Sub
    End If

    objConnect.Provider = "ADsDSOObject"
    If strUserName = "" then
        objConnect.Open "Active Directory Provider"
    Else
        objConnect.Open "Active Directory Provider", strUserName, strPassword
    End If
    If Err.Number then
        Print "Error 0x" & CStr(Hex(Err.Number)) & " ocurred opening a provider."
        If Err.Description <> "" Then
            Print "Error description: " & Err.Description & "."
        End If
        Exit Sub
    End If

    Set objCommand.ActiveConnection = objConnect

    'Set the query string and other properties
    objCommand.CommandText  = strSearchPath & strCriteria & strProperties & strScope
    objCommand.Properties("Page Size") = 100000                    'reset search properties
    objCommand.Properties("Timeout") = 300000 'seconds
'    objCommand.Properties("SearchScope") = 2

    'After setting all the parameter now execute the search and display the results.
    intResult = intExecuteSearch(objRecordSet, objCommand, objOutputFile)

    If strOutputFile <> "" Then
        objOutputFile.Close
        If intResult > 0 Then
            Wscript.Echo "Results are saved in file " & strOutputFile & "."
        End If
    End If

End Sub

'********************************************************************
'*
'* Function intExecuteSearch()
'* Purpose: Performs an LDAP search based on given criteria
'* Input:   objRecordSet    a recordset to store the info returned
'*          objCommand      the query command object
'*          objOutputFile   an output file object
'* Output:  Results of the search are either printed on screen or saved in objOutputFile.
'*          intExecuteSearch is set to -1 if the search failed or the number of objects
'*          found if succeeded.
'*
'********************************************************************

Private Function intExecuteSearch(objRecordSet, objCommand, objOutputFile)

    ON ERROR RESUME NEXT

    Dim  intNumObjects, i, j , k, intUBound, strMessage

    intNumObjects = 0
    intUBound = 0
    intExecuteSearch = 0

    'Let the user know what is going on
    Print objCommand.CommandText

    'Execute the query
    Set objRecordSet = objCommand.Execute
    Print "Finished the query."
    If Err.Number then
        Print "Error 0x" & CStr(Hex(Err.Number)) & " ocurred during the query."
        If Err.Description <> "" Then
            Print "Error description: " & Err.Description & "."
        End If
        Err.Clear
        intExecuteSearch = -1        'failed
        Exit Function
    End If

    'Get the total number of objects found.
    objRecordSet.MoveLast
    intNumObjects = objRecordSet.RecordCount
    intExecuteSearch = intNumObjects    'Succeeded

    If intNumObjects Then                'If intNumObjects is not zero
        Wscript.Echo "Found " & intNumObjects & " objects."
        objRecordSet.MoveFirst
        k = 1
        While Not objRecordSet.EOF
            For i = 0 To objRecordSet.Fields.Count - 1
                intUBound = UBound(objRecordSet.Fields(i).Value)

                If Err.Number Then
                    'This means that it is a single valued property.
                    Err.Clear
                    strMessage = objRecordSet.Fields(i).Name & " " & k & " = " _
                        & objRecordSet.Fields(i).Value
                Else                            'It is a multivalued property.
                    If intUBound = 0 Then        'There is only one implemented
                        strMessage = objRecordSet.Fields(i).Name & " " & k & " = " _
                            & objRecordSet.Fields(i).Value(0)
                    Else                        'It is truely multivalued.
                        strMessage = objRecordSet.Fields(i).Name & " " & k
                        For j = 0 to intUBound
                            strMessage = strMessage & vbCRLF & "     " & j+1 & " " _
                                & objRecordSet.Fields(i).Value(j)
                        Next
                    End If
                End If
                WriteLine strMessage, objOutputFile
            Next
            objRecordSet.MoveNext
            k = k + 1
        Wend
    Else
        Wscript.Echo "No object satisfying the criteria has been found within " _
            & strADsPath & "."
    End If

End Function

'********************************************************************
'*
'* Sub WriteLine()
'* Purpose: Writes a text line either to a file or on screen.
'* Input:   strMessage  the string to print
'*          objFile     an output file object
'* Output:  strMessage is either displayed on screen or written to a file.
'*
'********************************************************************

Sub WriteLine(ByRef strMessage, ByRef objFile)

    If IsObject(objFile) then        'objFile should be a file object
        objFile.WriteLine strMessage
    Else
        Wscript.Echo  strMessage
    End If

End Sub

'********************************************************************
'*
'* Sub Print()
'* Purpose: Prints a message on screen if blnQuiet = False.
'* Input:   strMessage      the string to print
'* Output:  strMessage is printed on screen if blnQuiet = False.
'*
'********************************************************************

Sub Print(ByRef strMessage)
    If Not blnQuiet then
        Wscript.Echo  strMessage
    End If
End Sub

'********************************************************************
'*
'* Function FormatProvider
'* Purpose: Formats Provider so it is not case sensitive
'* Input:   Provider    a string
'* Output:  FormatProvider is the Provider with the correct Case
'*
'********************************************************************

Private Function FormatProvider(Provider)
    FormatProvider = ""
    I = 1
    Do Until Mid(Provider, I, 1) = ":"
        If I = Len(Provider) Then
            'This Provider is Probabaly not valid, but we'll let it pass anyways.
            FormatProvider = Provider
            Exit Function
        End If
        I = I + 1
    Loop

    Select Case LCase(Left(Provider, I - 1))
        Case "winnt"
            FormatProvider = "WinNT" & Right(Provider,Len(Provider) - (I - 1))
        Case "ldap"
            FormatProvider = "LDAP" & Right(Provider,Len(Provider) - (I - 1))			
    End Select


End Function


'********************************************************************
'*                                                                  *
'*                           End of File                            *
'*                                                                  *
'********************************************************************

'********************************************************************
'*
'* Procedures calling sequence: SEARCH.VBS
'*
'*    intParseCmdLine
'*    ShowUsage
'*    Search
'*        intExecuteSearch
'*            WriteLine
'*
'********************************************************************

'********************************************************************
