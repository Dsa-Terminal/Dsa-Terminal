
' clonegg.vbt start

' CloneSecurityPrincipal VBScript
'
' Clone all Global Groups in a domain 
'
' Copyright (C) 1999 Microsoft Corporation.

option explicit

const SCRIPT_FILENAME    = "clonegg.vbs"
const SCRIPT_SOURCE_NAME = "clonegg.vbt"      
const SCRIPT_DATE        = "Aug 17 2001"      
const SCRIPT_TIME        = "12:42:13"      












' clonepr.vbi start









' various manifest constants
const CLASS_USER         = 0
const CLASS_LOCAL_GROUP  = 1
const CLASS_GLOBAL_GROUP = 2
const CLASS_OTHER        = 3

' the elements of this array are indexed by the above constants
dim classNames(2)
classNames(CLASS_USER)         = "User" 
classNames(CLASS_LOCAL_GROUP)  = "Group"
classNames(CLASS_GLOBAL_GROUP) = "Group"

' from iads.h
const ADS_GROUP_TYPE_DOMAIN_LOCAL_GROUP     = &H4       
const ADS_GROUP_TYPE_GLOBAL_GROUP           = &H2
const ADS_GROUP_TYPE_UNIVERSAL_GROUP		= &H8
const ADS_GROUP_TYPE_SECURITY_ENABLED       = &H80000000
const ADS_NAME_INITTYPE_DOMAIN              = 1         
const ADS_NAME_INITTYPE_SERVER              = 2         
const ADS_NAME_TYPE_1779                    = 1         
const ADS_NAME_TYPE_NT4                     = 3         
const ADS_NAME_TYPE_SID_OR_SID_HISTORY_NAME = 12        
const ADS_PROPERTY_APPEND                   = 3         
const ADS_PROPERTY_DELETE                   = 4         
const ADS_PROPERTY_UPDATE                   = 2         

' from lmaccess.h
const UF_TEMP_DUPLICATE_ACCOUNT = &H0100
const UF_NORMAL_ACCOUNT         = &H0200

' from andyhar's adsi reskit
const ADS_SID_RAW                   = 0
const ADS_SID_HEXSTRING             = 1
const ADS_SID_SDDL                  = 4
const ADS_SID_WINNT_PATH            = 5
const ADS_SID_ACTIVE_DIRECTORY_PATH = 6

const E_ADS_UNKNOWN_OBJECT          = &H80005004
const E_ADS_ERROR_DS_NO_SUCH_OBJECT = &H80072030
const E_ADS_ERROR_DS_NAME_NOT_FOUND = &H80072116



' create the COM object implementing ICloneSecurityPrincipal
dim clonepr
set clonepr = CreateObject("DSUtils.ClonePrincipal")
if Err.Number then DumpErrAndQuit

' create the COM object implementing IADsNameTranslate
dim nameTranslate
set nameTranslate = CreateObject("NameTranslate")
if Err.Number then DumpErrAndQuit

' create the COM object implementing IADsPathname
dim adsPathname
set adsPathname = CreateObject("Pathname")
if Err.Number then DumpErrAndQuit

' create the COM object implementing IADsError
dim adsError
set adsError = CreateObject("DSUtils.ADsError")
if Err.Number then DumpErrAndQuit

' create the COM object implementing IADsSID
dim sid
set sid = CreateObject("DSUtils.ADsSID")
if Err.Number then DumpErrAndQuit



'
' functions and subroutines follow
'


sub CloneSecurityPrincipal(byref srcObject, byval srcSam, byval dstDom, byval dstDC, byval dstSam, byval dstDN)
   on error resume next

   ' verify that the source object is of a type that we support
   dim srcObjectClass
   srcObjectClass = ObjectClass(srcObject)

	select case srcObjectClass
		case CLASS_USER
			if srcObject.UserFlags and UF_TEMP_DUPLICATE_ACCOUNT then
				Echo "Source object is a temporary local user account, which is not supported."
	         wscript.quit(0)			
			end if 
      case CLASS_LOCAL_GROUP
      case CLASS_GLOBAL_GROUP
         ' do nothing
      case else
         ' not a supported object class
         Echo "Source object is of type " & srcObject.Class & ", which is not supported by this tool."
         wscript.quit(0)
   end select

   ' bind to the destination object

   ' we attempt to locate the destination object by it's sam account name, in
   ' order to determine if that name is already in use by a security principal
   ' in the destination domain.

   dim dstObjectSamPath
   dstObjectSamPath = "WinNT://" & dstDom & "/" & dstDC & "/" & dstSam

   dim dstObjectDNPath
   dstObjectDNPath = "LDAP://" & dstDC & "/" & dstDN

   dim dstObjectClass
   dim dstObject

   Err.Clear
   set dstObject = GetObject(dstObjectSamPath)
   dim errnum1
   errnum1 = Err.Number
   select case errnum1
      case E_ADS_UNKNOWN_OBJECT
         ' destination is not found

         Echo "Destination object " & dstSam & " not found (by SAM name) path used: " & dstObjectSamPath

         ' bind to the DN of the object, then
         Err.Clear
         set dstObject = GetObject(dstObjectDNPath)
         dim errnum2
         errnum2 = Err.Number
         select case errnum2
            case E_ADS_ERROR_DS_NO_SUCH_OBJECT
               Echo "Destination object " & dstDN & " not found (by DN) path used: " & dstObjectDNPath

               ' create the dstDN object of the same type as the source
               Err.Clear
               set dstObject = CreateDestinationDN(dstSam, dstDN, dstDC, srcObjectClass)

            case 0
               ' dstDN found

               Echo "Destination DN found"

               dstObjectClass = ObjectClass(dstObject)

               if dstObjectClass <> srcObjectClass then
                  Bail "Source and destination objects differ in class type."
               end if

               if UCase(dstObject.SamAccountName) <> UCase(dstSam) then
                  ' sam name of the object is not the same as the sam name
                  ' specified on the command line
                  Bail "SAM account name of " & dstDN & " is " & dstObject.SamAccountName & " not " & dstSam
               end if

            case else
               Echo "Error attempting to bind to " & dstObjectDNPath
               DumpErrAndQuit

         end select

      case 0
         ' dstSam found.  Find the DN of the object it refers to

         Echo "Destination SAM name found"

         nameTranslate.Init ADS_NAME_INITTYPE_SERVER, dstDC
         if Err.Number then DumpErrAndQuit

         nameTranslate.Set ADS_NAME_TYPE_NT4, dstDom & "\" & dstSam
         if Err.Number then DumpErrAndQuit

         dim foundDN
         foundDN = nameTranslate.Get(ADS_NAME_TYPE_1779)  ' aka full DN
         if Err.Number then DumpErrAndQuit

         Echo dstSam & " refers to " & foundDN

         if UCase(dstDN) <> UCase(foundDN) then
            ' sam name is in use by another object than the one the user
            ' indicated.
            Bail "SAM account name " & dstSam & " is in use by object " & foundDN & ", not " & dstDN
         end if

         ' at this point, we've verified that the sam name specified by the
         ' user matches the DN.  Now verify that the DN refers to an object
         ' of the same type as the source  

         set dstObject = GetObject("LDAP://" & dstDC & "/" & foundDN)
         if Err.Number then DumpErrAndQuit

         dstObjectClass = ObjectClass(dstObject)
         if dstObjectClass <> srcObjectClass then
            Bail "Source and destination objects differ in class type."
         end if

      case else
         Echo "Error attempting to bind to destination object " & dstObjectSamPath
         DumpErrAndQuit
   end select

   ' at this point, dstObject is bound to the object onto which we
   ' should clone the source object 

   ' copy the source object's properties
   Echo "Setting properties for target " & dstObject.Class & " " & dstObject.Name
   select case srcObjectClass
      case CLASS_USER

         ' copy the properties of the source user to the destination user
         clonepr.CopyDownlevelUserProperties srcSam, dstSam, 0
         if Err.Number then DumpErrAndQuit

         Echo "Downlevel properties set."

         ' fixup the destination user's group memberships

         FixupUserGroupMemberships srcObject, dstObject, dstDC
         if Err.Number then DumpErrAndQuit

         Echo "User's Group memberships restored."

         ' commit the changes
         dstObject.SetInfo
         if Err.Number then DumpErrAndQuit

         Echo "User changes commited."

      case CLASS_LOCAL_GROUP
         ' copy the source group's description
         if srcObject.Description <> "" then 
            dstObject.Put "Description", srcObject.Description
            dstObject.SetInfo
            if Err.Number then DumpErrAndQuit
         end if

         Echo "Local group description set."

         ' copy the source local group's membership
         CopyLocalGroupMembership srcObject, dstObject
         if Err.Number then DumpErrAndQuit

         Echo "Local group membership copied."

         ' commit the changes
         dstObject.SetInfo
         if Err.Number then DumpErrAndQuit

         Echo "Local group changes commited."

      case CLASS_GLOBAL_GROUP
         ' copy the source group's description
         if srcObject.Description <> "" then 
            dstObject.Put "Description", srcObject.Description
            dstObject.SetInfo
            if Err.Number then DumpErrAndQuit
         end if

         Echo "Global group description set."

         ' fixup the destination group's members
         FixupGlobalGroupMembers srcObject, dstObject, dstDC
         if Err.Number then DumpErrAndQuit

         Echo "Global group memberships restored."

         ' commit the change
         dstObject.SetInfo
         if Err.Number then DumpErrAndQuit

         Echo "Global group changes commited."

      case else
         ' why are we here?  what is my purpose in life?
         wscript "illegal code path"
         wscript.quit(0)

   end select

   ' Add the SID of the source principal to the sid history of the destination
   ' principal.
   Echo "Adding SID for source " & srcObject.Class & " " & srcObject.Name & " to SID history of target " & dstObject.Class & " " & dstObject.Name
   clonepr.AddSidHistory srcSam, dstSam, 0
   if Err.Number then DumpErrAndQuit

   Echo "SID history set successfully."

   ' all done
   Echo srcObject.Name & " cloned successfully."
end sub



' Create a DS security principal object, and return a bound reference to it.
' 
' samName - in, sam account name of object-to-be
'
' DN - in, full DN of the object to be created
'
' DC - in, name of domain controller on which the object is to be created
'
' objectClass - in, CLASS_ constant for the type of object to create

function CreateDestinationDN(byval samName, byval DN, byval DC, byval objectClass)
   on error resume next
   Echo "Creating " & DN

   ' determine the name of the container to place the new object by removing
   ' the leaf-most portion of the DN
   dim p
   p = InStr(1, DN, ",", 1)

   dim dstCN
   dstCN = Mid(DN, 1, p - 1)  ' - 1 to omit the comma

   dim ouDN, ouDNPath
   ouDN = Mid(DN, p + 1)   ' + 1 to skip the comma
   ouDNPath = "LDAP://" & DC & "/" & ouDN
      
   dim container, errnum3
   set container = GetObject(ouDNPath)
   select case Err.Number
      case E_ADS_ERROR_DS_NO_SUCH_OBJECT
         Bail "Container " & ouDN & " not found"
      case 0
         ' do nothing
      case else
         Echo "Error attempting to bind to " & ouDN
         DumpErrAndQuit
   end select

   dim dstObject
   set dstObject = container.Create(classNames(objectClass), dstCN)
   if Err.Number then
      Echo "Error attempting to create " & DN
      DumpErrAndQuit
   end if

   dstObject.Put "samAccountName", samName
   if Err.Number then
      Echo "Error attempting to set samAccountName for " & DN
      DumpErrAndQuit
   end if

   select case objectClass
      case CLASS_USER
         ' nothing more to add

      case CLASS_LOCAL_GROUP
         ' set group type to local
         dstObject.Put "groupType", ADS_GROUP_TYPE_DOMAIN_LOCAL_GROUP + ADS_GROUP_TYPE_SECURITY_ENABLED
         if Err.Number then
            Echo "Error attempting to set local group type for " & DN
            DumpErrAndQuit
         end if

      case CLASS_GLOBAL_GROUP
         ' set group type to global
         dstObject.Put "groupType", ADS_GROUP_TYPE_GLOBAL_GROUP + ADS_GROUP_TYPE_SECURITY_ENABLED
         if Err.Number then
            Echo "Error attempting to set global group type for " & DN
            DumpErrAndQuit
         end if

   end select

   dstObject.SetInfo
   if Err.Number then
      Echo "Error attempting to commit create of " & DN
      DumpErrAndQuit
   end if

   Echo "Created " & DN

   set CreateDestinationDN = dstObject
end function



' for each group to which the source user object belongs, look for that
' group's sid in the sid histories of objects in the destination forest
' (domain?).  If found, add the destination user as a member of the located
' group.  Thus, when a user is cloned, the clone becomes a member of all the
' existing cloned groups corresponding to the original groups the
' orignal user belonged to.

sub FixupUserGroupMemberships(byref srcObject, byref dstObject, byval dstDC)
   on error resume next
   Echo "Fixing group memberships for " & dstObject.Class & " " & dstObject.Name

   nameTranslate.Init ADS_NAME_INITTYPE_SERVER, dstDC
   if Err.Number then DumpErrAndQuit

   dim group
   dim sidString
   for each group in srcObject.Groups
      if (ObjectClass(group) = CLASS_GLOBAL_GROUP) then
         Echo "  Found global group " & group.ADsPath

         sid.SetAs ADS_SID_WINNT_PATH, group.AdsPath & "," & group.Class
         if Err.Number then DumpErrAndQuit

         sidString = sid.GetAs(ADS_SID_SDDL)
         if Err.Number then DumpErrAndQuit

         if IsBuiltInSid(sidString) then
            Echo "  " & group.ADsPath & " is a built-in group"

            ' built-ins are present in every domain with the same sid.  So we
            ' can't search for the corresponding destination object by sid, or
            ' we may be multiple matches (if there is more than 1 domain in the
            ' destination forest, and the destination DC also happens to be
            ' a global catalog).  So, here we compose a sid-style LDAP path
            ' for the built-in destination object.

            sidString = "<sid=" & sid.GetAs(ADS_SID_HEXSTRING) & ">"
            if Err.Number then DumpErrAndQuit

            dim mypath
            mypath = "LDAP://" & dstDC & "/" & sidString

            dim mygroup
            set mygroup = GetObject(mypath)
            if Err.Number then DumpErrAndQuit

            if not IsUserMemberOfGroup(mygroup, dstObject) then
               Echo "  Adding " & dstObject.Name & " to group " & mygroup.Name
               mygroup.Add dstObject.AdsPath
            else
               Echo "  " & dstObject.Name & " is already member of " & mygroup.Name
            end if
            if Err.Number then DumpErrAndQuit 
         else

            ' find the DN of the object with that sid as its object sid or in
            ' its sid history (the sid history is where it will be, if the object
            ' is a clone).

            nameTranslate.Set ADS_NAME_TYPE_SID_OR_SID_HISTORY_NAME, sidString
            select case Err.Number
               case E_ADS_ERROR_DS_NAME_NOT_FOUND
                  ' do nothing: skip this member; it hasn't been cloned yet

                  Echo "  Skipping " & group.ADsPath & " -- not cloned yet"

               case 0
                  ' found!
                  dim foundDN
                  foundDN = ""
                  foundDN = nameTranslate.Get(ADS_NAME_TYPE_1779)  ' aka full DN

                  select case Err.Number
                     case E_ADS_ERROR_DS_NAME_NOT_FOUND
                        ' do nothing: skip this member; it hasn't been cloned yet
                     case 0
                        AddUserToGroup dstObject, foundDN, dstDC
                     case else
                        DumpErrAndQuit
                  end select

               case else
                  DumpErrAndQuit

            end select
         end if
      else
         Echo "  Skipping group " & group.AdsPath & " -- not global group"
      end if

      ' need to clear this so next iteration won't choke.
      Err.Clear
   next
end sub



' for each member of the source local group, obtain the member's SID and add
' that SID as a member of the destination local group.  If that SID does not
' refer to a security principal in the destination domain, then the SAM will
' create a Foreign Principal Object (FPO) to represent that SID.  then SAM
' will replace the reference to the SID in the group membership with the DN
' of the FPO.  An FPO acts like a proxy for the SID.

sub CopyLocalGroupMembership(byref srcObject, byref dstObject)
   on error resume next

   Echo "Copying local group membership"

   ' get the sids in string form of each of the members of the source
   ' group.  collect them in an array
   dim member
   dim sidString
   dim sidStringArray()
   dim i
   i = 0

   dim dn
   dn = dstObject.Get("distinguishedName")
   if Err.Number then DumpErrAndQuit

   Echo "  Getting destination group membership as SIDs"

   dim dstExistingMemberSIDs
   dstExistingMemberSIDs = clonepr.GetMembersSIDs(dn)
   if Err.Number then DumpErrAndQuit

   dim numExistingMembers
   numExistingMembers = 0
   dim x
   for each x in dstExistingMemberSIDs
     numExistingMembers = numExistingMembers + 1
   next

   for each member in srcObject.Members
      dim sidDeletedAccount
      if IsDeletedAccount(member.AdsPath, sidDeletedAccount) then
         Echo "  Considering deleted account: " & sidDeletedAccount
         sid.SetAs ADS_SID_SDDL, sidDeletedAccount
      else
         Echo "  Considering normal account: " & member.AdsPath
         sid.SetAs ADS_SID_WINNT_PATH, member.AdsPath & "," & member.Class
      end if
      if Err.Number then DumpErrAndQuit

      sidString = "<sid=" & sid.GetAs(ADS_SID_HEXSTRING) & ">"
      if Err.Number then DumpErrAndQuit

      if (0 = numExistingMembers) Or (not SidStringExists(sidString, dstExistingMemberSIDs)) then
         Echo "  Adding " & sidString
         redim preserve sidStringArray(i)
         sidStringArray(i) = sidString
         i = i + 1
      end if
   next

   ' use the array to update the destination group in one whack.
   if i then
      if 0 = numExistingMembers then 
        dstObject.PutEx ADS_PROPERTY_UPDATE, "member", sidStringArray
      else
        dstObject.PutEx ADS_PROPERTY_APPEND, "member", sidStringArray
      end if
      if Err.Number then DumpErrAndQuit

      dstObject.SetInfo
      if Err.Number then DumpErrAndQuit
   end if
end sub



function IsDeletedAccount(byref AdsPath, byref sidDeletedAccount)
  dim pos0, pos1
  pos0 = InStr(1, AdsPath, "://", 1)
  pos1 = InStr(pos0 + 3, AdsPath, "/", 1)

  if 0 = pos1 then
    IsDeletedAccount = True
    sidDeletedAccount = Mid(AdsPath, pos0 + 3)
  else
    IsDeletedAccount = False
  end if

end function



function SidStringExists(byref sidString, byref dstExistingMemberSIDs)
  dim sid
  sid = UCase(sidString)

  SidStringExists = False

  dim x
  For each x in dstExistingMemberSIDs
    if UCase(x) = sid then
       Echo "  Skipping existing sid " & x
       SidStringExists = True
       exit function
    end if
  next

end function



' for each member of the source global group, look for that member's sid in
' the sid histories of objects the destination forest (domain?).  If found,
' add that located object as a member of the destination group.  Thus,
' when a global group is cloned, the existing clones of all users that belong
' to the original group will belong to the cloned group.

sub FixupGlobalGroupMembers(byref srcObject, byref dstObject, byval dstDC)
   on error resume next
   Echo "Fixing group membership for " & dstObject.Class & " " & dstObject.Name

   nameTranslate.Init ADS_NAME_INITTYPE_SERVER, dstDC
   if Err.Number then DumpErrAndQuit

   dim member
   dim sidString
   for each member in srcObject.Members

      if member.UserFlags and UF_NORMAL_ACCOUNT then

         ' extract the sid of the account
         sid.SetAs ADS_SID_WINNT_PATH, member.AdsPath & "," & member.Class
         if Err.Number then DumpErrAndQuit

         sidString = sid.GetAs(ADS_SID_SDDL)
         if Err.Number then DumpErrAndQuit

         ' find the DN of the member with that sid as its object sid or in
         ' its sid history (the sid history is where it will be, if the member
         ' is a clone).
         nameTranslate.Set ADS_NAME_TYPE_SID_OR_SID_HISTORY_NAME, sidString
         select case Err.Number
            case E_ADS_ERROR_DS_NAME_NOT_FOUND
               ' do nothing: skip this member; it hasn't been cloned yet

            case 0
               ' found!
               dim foundDN
               foundDN = ""
               foundDN = nameTranslate.Get(ADS_NAME_TYPE_1779)  ' aka full DN

               select case Err.Number
                  case E_ADS_ERROR_DS_NAME_NOT_FOUND
                     ' do nothing: skip this member; it hasn't been cloned yet
                  case 0
                     ' add the dn to the members property of the dst object
                     dim path
                     path = "LDAP://" & dstDC & "/" & foundDN
                     Dim tempObj 
                     set tempObj = GetObject(path)
                     if Err.Number then DumpErrAndQuit
                     if NOT IsUserMemberOfGroup( dstObject, tempObj ) then
                        Echo "  adding " & foundDN & " to group " & dstObject.Name
                        dstObject.Add path
                     end if
                     if Err.Number then DumpErrAndQuit

                  case else
                     DumpErrAndQuit
               end select

            case else
               DumpErrAndQuit
         end select

         ' need to clear this so the next iteration doesn't choke
         Err.Clear

      else 

         ' skip computer, temp and trust accounts
         Echo "  Skipping non-user account " & member.Name
      end if
   next
end sub



' user - in, reference to user object, bound with LDAP provider.
' 
' groupDN - in, full DN of the group to which the user is to be added
' 
' dstDC - in, name of destination domain controller

sub AddUserToGroup(byref user, byval groupDN, byval dstDC)
   on error resume next

   dim path
   path = "LDAP://" & dstDC & "/" & groupDN

   dim group
   set group = GetObject(path)
   if Err.Number then DumpErrAndQuit

   if not IsUserMemberOfGroup(group,user) then 
      Echo "  Adding " & user.Name & " to group " & group.Name
      group.Add user.AdsPath
   else
      Echo "  " & user.Name & " is already member of " & group.Name
   end if
   if Err.Number then DumpErrAndQuit
end sub



function IsUserMemberOfGroup( byref group, byref user )
   if group.IsMember(user.AdsPath) then
        IsUserMemberOfGroup = True
        exit function
   end if 

   sid.SetAs ADS_SID_ACTIVE_DIRECTORY_PATH, group.AdsPath
   if Err.Number then DumpErrAndQuit

   dim sidString
    sidString = sid.GetAs(ADS_SID_SDDL)
    if Err.Number then DumpErrAndQuit
    if Len(sidString) > 9 then
        dim lastDash
        lastDash = InStrRev(sidString, "-", -1, 1)
        if lastDash then
           dim ridString
           ridString = Mid(sidString, lastDash + 1)
           if StrComp(ridString,user.PrimaryGroupId,1) = 0 then
                IsUserMemberOfGroup = True
                exit function
           end if
        end if 
    end if
    
    IsUserMemberOfGroup = False
end function
    


' based on the class of the object, return one of CLASS_USER,
' CLASS_LOCAL_GROUP, CLASS_GLOBAL_GROUP, CLASS_OTHER

function ObjectClass(object)
   dim cls
   cls = UCase(object.Class)

   if cls = "GROUP" then
      if (object.GroupType and ADS_GROUP_TYPE_DOMAIN_LOCAL_GROUP) then
         ' type is local group
         ObjectClass = CLASS_LOCAL_GROUP
         exit function
      else
         if ((object.GroupType and ADS_GROUP_TYPE_GLOBAL_GROUP) or (object.GroupType and ADS_GROUP_TYPE_UNIVERSAL_GROUP)) then
            ' type is global group
            ObjectClass = CLASS_GLOBAL_GROUP
            exit function
         end if
      end if
   else
      if cls = "USER" then
         ' type is user
         ObjectClass = CLASS_USER
         exit function
      end if
   end if

   ' type is not recognized
   ObjectClass = CLASS_OTHER
   exit function
end function



' returns non-zero if the stringized SID refers to a well-known rid, zero
' otherwise

function HasWellKnownRid(byval sidString)
   ' a SID refers to a well-known account if the first sub-authority (aka
   ' RID) is < 1000.  The first subauthority is the last portion of the
   ' stringized SID

   if Len(sidString) > 9 then
      dim lastDash
      lastDash = InStrRev(sidString, "-", -1, 1)
      if lastDash then
         dim ridString
         ridString = Mid(sidString, lastDash + 1)
         if CLng(ridString) < 1000 then
            HasWellKnownRid = True
            exit function
         end if
      end if
   end if

   HasWellKnownRid = False
end function



' returns non-zero if the stringized SID refers to a builtin sid, zero
' otherwise

function IsBuiltInSid(byval sidString)
   ' a SID  refers to builtin account or group if it has prefix S-1-5-32-

   if Len(sidString) > 9 then
         dim  prefixString
         prefixString = Mid(sidString, 1, 9)
         if StrComp( prefixString, "S-1-5-32-", 1 ) = 0  then
            IsBuiltInSid = true
            exit function
         end if
   end if

   IsBuiltInSid = False
end function



' searches for and returns the value of a command line argument of the form
' /argName:value from the supplied array.  erases the entry in the array so
' that only untouched entries remain.

function GetArgValue(argName, args())
    dim a
    dim v
    dim argNameLength
    dim x
    dim argCount
    dim fullArgName

    fullArgName = "/" & argName & ":"
    argCount = Ubound(args)

    ' Get the length of the argname we are looking for
    argNameLength = Len(fullArgName)
    GetArgValue = "" ' default to nothing
    
    for x = 0 To argCount 
        if Len(args(x)) >= argNameLength then

            a = Mid(args(x), 1, argNameLength)
            if UCase(a) = UCase(fullArgName) then

                ' erase it so we can look for unknown args later
                v = args(x)
                args(x) = ""

                if Len(v) > argNameLength then
                    GetArgValue = Mid(v, argNameLength + 1)
                    exit function
                else 
                    GetArgValue = ""
                    exit function
                end if
            end if
        end if
    next 
end function



' walks thru the array searching for any non-empty element.  if at least one
' is found, then return non-zero.  Otherwise return 0.

function CheckForBadArgs(byref args())
   dim i
   for i = 0 to UBound(args) 
      if Len(args(i)) > 0 then
         CheckForBadArgs = 1
         exit function
      end if
   next

   CheckForBadArgs = 0
end function



sub DumpErrAndQuit
   dim errnum
   errnum = Err.Number

   Echo "Error 0x" & CStr(Hex(errnum)) & " occurred."
   if len(Err.Description) then
      Echo "Error Description: " & Err.Description
   end if
   if len(Err.Source) then 
      Echo "Error Source     : " & Err.Source
   end if
   Echo "ADsError Description: "
   Echo adsError.GetErrorMsg(errnum)
   wscript.quit(0)
end sub



sub Bail(byref message)
   Echo "Error: " & message
   wscript.quit(0)
end sub



sub Echo(byref message)
   wscript.echo message
end sub



' clonepr.vbi end











' clonedom.vbi start









const ARG_COUNT = 5

sub Main
   if wscript.arguments.count <> ARG_COUNT then
      PrintUsageAndQuit
   end if

   ' copy the command-line arguments for parsing
   dim args()
   Redim args(0)
   args(0) = ""

   dim i
   for i = 0 to wscript.arguments.count - 1
       Redim Preserve args(i)
       args(i) = wscript.arguments.item(i)
   next

   ' command line parameters
   dim srcDC       ' source domain controller                     
   dim srcDom      ' source domain                                
   dim dstDC       ' destination controller                       
   dim dstDom      ' destination domain                           
   dim dstOU       ' destination OU for clones

   ' parse the saved command-line arguments, extracting the values
   srcDC   = GetArgValue("srcdc",   args)
   srcDom  = GetArgValue("srcdom",  args)
   dstDC   = GetArgValue("dstdc",   args)
   dstDom  = GetArgValue("dstdom",  args)
   dstOU   = GetArgValue("dstou",   args)

   ' ensure the user did not pass any unrecognized command-line arguments
   if CheckForBadArgs(args) then
       Echo "Unknown command-line arguments specified"
       PrintUsageAndQuit
   end if
   
   ' establish authenticate connections to the source and destination domain
   ' controllers
   on error resume next
   clonepr.Connect srcDC, srcDom, dstDC, dstDom
   if Err.Number then DumpErrAndQuit

   Echo "Connected to source and destination domain controllers"

   dim srcDomain
   set srcDomain = GetObject("WinNT://" & srcDom & "/" & srcDC & ",Computer")
   if Err.Number then DumpErrAndQuit

   ' for every security principal in the source domain, call
   ' ShouldCloneObject. if that function returns True, then clone the object.
   ' Otherwise ignore it.
   dim cloneCounter
   dim srcObject
   dim srcObjectClass
   cloneCounter = 0
   for each srcObject in srcDomain
      if ShouldCloneObject(srcObject) then
         Echo "Bound to source " & srcObject.Class & " " & srcObject.Name

         srcObjectClass = ObjectClass(srcObject)

         do 
            if srcObjectClass = CLASS_USER then
               if srcObject.UserFlags and UF_TEMP_DUPLICATE_ACCOUNT then
                  Echo "Skipping temporary local user account."
                  exit do
               end if
            end if 

            dim srcSam        ' source principal SAM name
            dim dstSam        ' destination principal SAM name
            dim dstDN         ' destination principal full DN

            srcSam = srcObject.Name
            dstSam = srcSam
            dstDN = adsPathname.GetEscapedElement(0, "CN=" & dstSam) & "," & dstOU

            CloneSecurityPrincipal srcObject, srcSam, dstDom, dstDC, dstSam, dstDN
            cloneCounter = cloneCounter + 1
         loop while 0

         Echo ""

      end if
   next

   Echo cloneCounter & " objects(s) cloned"
end sub



sub PrintUsageAndQuit
   Echo "Usage: cscript " & SCRIPT_FILENAME & " /srcdc:<dcname> /srcdom:<domain>"
   Echo "/dstdc:<dcname> /dstdom:<domain> /dstou:<ouname>"
   Echo ""
   Echo "Parameters:"
   Echo " /srcdc   - source domain controller NetBIOS computer name (without leading \\)"
   Echo ""
   Echo " /srcdom  - source domain NetBIOS name"
   Echo ""
   Echo " /dstdc   - destination domain controller NetBIOS computer name (without "
   Echo "            leading \\)"
   Echo "            This script must be run on the machine indicated here."
   Echo ""
   Echo " /dstdom  - destination domain DNS name"
   Echo ""
   Echo " /dstou   - destination OU for the clones"
   Echo ""
   Echo "Notes:"
   Echo ""
   Echo "If the destination principals do not exist, they will be created."
   Echo "In that case, the OU named by dstou must exist."
   Echo ""
   Echo "Currently logged-on user must be a member of the Administrators"
   Echo "group of both the source and destination domains."
   Echo ""
   Echo SCRIPT_DATE & " " & SCRIPT_TIME

   wscript.quit(0)
end sub



' clonedom.vbi end




Main
wscript.quit(0)



' returns True if the object is a global group and not WellKnown Group

function ShouldCloneObject(byref srcObject)
   on error resume next

   if ObjectClass(srcObject) = CLASS_GLOBAL_GROUP then

      sid.SetAs ADS_SID_WINNT_PATH, srcObject.AdsPath & "," & srcObject.Class
      if Err.Number then DumpErrAndQuit

      dim sidString
      sidString = sid.GetAs(ADS_SID_SDDL)
      if Err.Number then DumpErrAndQuit

'To Stop Cloning Well Known Sids Uncomment 4 lines below

     ' if HasWellKnownRid(sidString) then
     '    ShouldCloneObject = False
     '    exit function
     ' end if

      if IsBuiltInSid( sidString ) then
        Echo srcObject.Name & " is a builtin Account."
        Echo "BuiltIn Users and Groups cannot be cloned"
        ShouldCloneObject = False
        exit function
      end if
    
      ShouldCloneObject = True
      exit function
   end if

   ShouldCloneObject = False
end function



' clonegg.vbt end
