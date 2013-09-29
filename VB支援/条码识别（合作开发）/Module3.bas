Attribute VB_Name = "Module3"
Option Explicit


Public lSrcPix(300) As Long
Public lBarPix(300) As Long
Public pixI As Long
Public pixY As Long


Public lCodeID(13) As Long


'扫描条码
Public Function ScanBar(ByVal X1 As Long, ByVal Y1 As Long) As String
    Dim i As Long
    
    For i = 0 To UBound(lCodeID)
        lCodeID(i) = -1
    Next
    
    Call BarPix(X1, Y1, Form1.Picture1.Width / 15, Y1 + 30)
    
    i = 0
    Select Case CodeMode
    Case 103
        Do
            Call FixPix(0.9 - 0.02 * i, 0.4 + 0.1 * i)
            Call BarID_A
            
            ScanBar = BarChar_A
            
            i = i + 1
            If ScanBar <> "" Or i > 3 Then
                Exit Do
            End If
        Loop
        
        '测试用代码
'        For i = 1 To 12
'            If lCodeID(i) = -1 Then
'                Form1.Print BarCode(1 + 6 * i)
'                Form1.Print lBarPix(1 + 6 * i) & "," & lBarPix(2 + 6 * i) & "," & lBarPix(3 + 6 * i) & "," & lBarPix(4 + 6 * i) & "," & lBarPix(5 + 6 * i) & "," & lBarPix(6 + 6 * i)
'            Else
'                Form1.Print sCA(lCodeID(i))
'            End If
'        Next
'        Form1.Print "chk=" & IIf(lCodeID(13) = -1, BarCode(1 + 6 * 13), lCodeID(13))
'        If lCodeID(13) = -1 Then
'            i = 13
'            Form1.Print lBarPix(1 + 6 * i) & "," & lBarPix(2 + 6 * i) & "," & lBarPix(3 + 6 * i) & "," & lBarPix(4 + 6 * i) & "," & lBarPix(5 + 6 * i) & "," & lBarPix(6 + 6 * i)
'        End If
    Case 105
        Do
            Call FixPix(0.9 - 0.02 * i, 0.4 + 0.1 * i)
            Call BarID_C
            
            ScanBar = BarChar_C
            
            i = i + 1
            If ScanBar <> "" Or i > 3 Then
                Exit Do
            End If
        Loop
    End Select
End Function


'扫描给定区域条码的像素点
Public Sub BarPix(ByVal X1 As Long, ByVal Y1 As Long, ByVal X2 As Long, ByVal Y2 As Long)
    Dim lPre As Long, i As Long, x As Long, y As Long
    
    For i = 0 To UBound(lSrcPix)
        lSrcPix(i) = 0
    Next
    
    y = Y1
    Do Until y > Y2
        lPre = -1
        pixI = 0
        
        For x = X1 To X2
            If InColor(x, y, 50, 50, 50, 50) = True Then
                If lPre = 0 Then
                    pixI = pixI + 1
                End If
                
                lPre = 1
            Else
                If lPre = 1 Then
                    pixI = pixI + 1
                End If
                
                lPre = 0
            End If
            
            If pixI <= 6 * 14 Then
                lSrcPix(pixI) = lSrcPix(pixI) + 1
            Else
                Exit For
            End If
        Next

        y = y + 1
        If lSrcPix(1) > 55 Then
            Exit Do
        End If
    Loop
    
    pixY = y - Y1
End Sub


'修正像素点数据
Public Sub FixPix(ByVal sT As Single, ByVal sD As Single)
    Dim i As Long
    
    For i = 1 To pixI - 1
        If i Mod 2 = 0 Then
            lBarPix(i) = lSrcPix(i) * sT - pixY * sD
        Else
            lBarPix(i) = lSrcPix(i)
        End If
    Next
End Sub


'识别编码方式
Public Function CodeMode() As Long
    If lSrcPix(4) / lSrcPix(1) >= 1.35 Then
        CodeMode = 103
    Else
        CodeMode = 105
    End If
End Function
    

Public Function BarCode(ByVal n As Long) As String
    On Error Resume Next
    
    Dim i As Long, lPixSum As Long, sTmp(5) As Single, lTmp(5) As Long, lSum As Long, sDif As Single, tmpI As Long
    
    For i = 0 To 5
        lPixSum = lPixSum + lBarPix(n + i)
    Next
    
    For i = 0 To 5
        sTmp(i) = lBarPix(n + i) * 11 / lPixSum
        lTmp(i) = sTmp(i)
        lSum = lSum + lTmp(i)
    Next
    
    Select Case lSum
    Case 10
        For i = 0 To 5
            If lTmp(i) < sTmp(i) Then
                If sDif < sTmp(i) - lTmp(i) Then
                    sDif = sTmp(i) - lTmp(i)
                    tmpI = i
                End If
            End If
        Next
        lTmp(tmpI) = lTmp(tmpI) + 1
    Case 12
        For i = 0 To 5
            If lTmp(i) > sTmp(i) Then
                If sDif < lTmp(i) - sTmp(i) Then
                    sDif = lTmp(i) - sTmp(i)
                    tmpI = i
                End If
            End If
        Next
        lTmp(tmpI) = lTmp(tmpI) - 1
    End Select
    
    For i = 0 To 5
        BarCode = BarCode & lTmp(i)
    Next
End Function


Public Function CodeID(ByVal sParam As String) As Long
    Dim i As Long
    
    For i = 0 To UBound(sBC)
        If sParam = sBC(i) Then
            CodeID = i
            Exit Function
        End If
    Next
    
    CodeID = -1
End Function


Public Sub BarID_A()
    Dim i As Long
    
    lCodeID(1) = 54
    lCodeID(2) = 41
    lCodeID(3) = 48
                    
    For i = 4 To 12
        If lCodeID(i) < 16 Or lCodeID(i) > 25 Then
            lCodeID(i) = CodeID(BarCode(1 + 6 * i))
        End If
    Next
    If lCodeID(i) = -1 Then
        lCodeID(i) = CodeID(BarCode(1 + 6 * i))
    End If
End Sub

Public Sub BarID_C()
    Dim i As Long
    
    For i = 1 To 7
        If lCodeID(i) = -1 Then
            lCodeID(i) = CodeID(BarCode(1 + 6 * i))
        End If
    Next
End Sub

Public Function BarChar_A() As String
    Dim i As Long, errI As Long, chkSum As Long
    
    chkSum = 103
    
    For i = 1 To 12
        If lCodeID(i) = -1 Then
            If errI = 0 Then
                errI = i
            Else
                Exit Function
            End If
        Else
            chkSum = chkSum + i * lCodeID(i)
        End If
    Next
    
    If errI = 0 Then
        'Form1.Print chkSum Mod 103
        
        If chkSum Mod 103 <> lCodeID(13) Then Exit Function
    Else
        For i = 16 To 25
            If (chkSum + errI * i) Mod 103 = lCodeID(13) Then
                lCodeID(errI) = i
                Exit For
            End If
        Next
        
        If lCodeID(errI) = -1 Then Exit Function
    End If
    
    For i = 1 To 12
        BarChar_A = BarChar_A & sCA(lCodeID(i))
    Next
End Function


Public Function BarChar_C() As String
    Dim i As Long, errI As Long, chkSum As Long
    
    chkSum = 105
    
    For i = 1 To 6
        If lCodeID(i) = -1 Then
            If errI = 0 Then
                errI = i
            Else
                Exit Function
            End If
        Else
            chkSum = chkSum + i * lCodeID(i)
        End If
    Next
    
    If errI = 0 Then
        If chkSum Mod 103 <> lCodeID(7) Then Exit Function
    Else
        For i = 0 To 99
            If (chkSum + errI * i) Mod 103 = lCodeID(7) Then
                lCodeID(errI) = i
                Exit For
            End If
        Next
        
        If lCodeID(errI) = -1 Then Exit Function
    End If
    
    For i = 1 To 6
        BarChar_C = BarChar_C & sCC(lCodeID(i))
    Next
End Function


