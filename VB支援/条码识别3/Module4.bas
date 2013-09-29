Attribute VB_Name = "Module4"
Option Explicit


Public sFile(2000) As String
Public lFileNum As Long
Public lpFile As Long
Public lRE As Long
Public lOK As Long
Public lNO As Long


Public Sub EnumFiles(ByVal sPath As String)
    Dim fs As New FileSystemObject

    lFileNum = GetFile(fs.GetFolder(sPath))
    
    Set fs = Nothing
End Sub


Public Function GetFile(ByVal fldParent As Folder) As Long
    Dim fldSub As Folder, fSub As File
    Dim i As Long
    
    For Each fldSub In fldParent.SubFolders
        GetFile fldSub
    Next
    
    For Each fSub In fldParent.Files
        If LCase(Right(fSub.Name, 4)) = ".jpg" Then
            sFile(i) = fSub.Name
            i = i + 1
        End If
    Next
    
    GetFile = i
    
    Set fldSub = Nothing
    Set fSub = Nothing
End Function
