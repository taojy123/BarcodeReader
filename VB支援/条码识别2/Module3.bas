Attribute VB_Name = "Module3"
Option Explicit


Public lBarPix(300) As Long
Public pixI As Long

Public lCodeID(20, 13) As Long

'扫描条码
Public Function ScanBar(ByVal X1 As Long, ByVal Y1 As Long) As String
    Dim i As Long, n As Long, d(10) As Long, dI As Long
'   Dim s As String
    
    d(0) = 70
    d(1) = 60
    d(2) = 80
    d(3) = 50
    d(4) = 90
    d(5) = 75
    d(6) = 65
    d(7) = 85
    d(8) = 55
    d(9) = 95
    d(10) = 45
    
    For dI = 0 To UBound(d)
        For n = 0 To UBound(lCodeID, 1)
            Call BarPix(X1, Y1 + n, Form1.Picture1.Width / 15, d(dI))
            Call CodeValue(n)
            
'            s = ""
'            For i = 0 To 13
'                s = s & lCodeID(n, i) & ","
'            Next
'            s = s & "("
'            For i = 1 To 6
'                s = s & lBarPix(6 * 13 + i) & ","
'            Next
'            s = s & BarCode(1 + 6 * 13) & ")"
'            Form1.Print s
        Next
        ScanBar = BarChar
        If ScanBar <> "" Then
            'Form1.Print ScanBar
            Exit For
        End If
    Next
End Function

'扫描给定区域条码的像素点
Public Sub BarPix(ByVal X1 As Long, ByVal Y1 As Long, ByVal X2 As Long, ByVal d As Long)
    Dim isSame As Boolean, x As Long
    
    pixI = 0
    lBarPix(pixI) = 0
    
    For x = X1 To X2
        If isSame <> InColor(x, Y1, d, d, d, d) Then
            pixI = pixI + 1
            lBarPix(pixI) = 0
            
            isSame = Not isSame
        End If
        
        lBarPix(pixI) = lBarPix(pixI) + 1
    Next
End Sub

'得到条码ID值
Public Sub CodeValue(ByVal n As Long)
    Dim i As Long, sBarCode As String
                  
    For i = 0 To 13
        sBarCode = BarCode(1 + 6 * i)
        
        If sBarCode <> "" Then
            lCodeID(n, i) = CodeID(sBarCode)
        Else
            Exit For
        End If
    Next
End Sub

'根据像素数据得到编码
Public Function BarCode(ByVal n As Long) As String
    On Error Resume Next
    
    Dim i As Long, lPixSum As Long, sTmp(5) As Single, lTmp(5) As Long, lSum As Long, sDif As Single, tmpI As Long
    
    For i = 0 To 5
        If lBarPix(n + i) > 0 Then
            lPixSum = lPixSum + lBarPix(n + i)
        Else
            Exit Function
        End If
    Next
    
    For i = 0 To 5
        sTmp(i) = lBarPix(n + i) * 11 / lPixSum
        lTmp(i) = IIf(sTmp(i) < 1, 1, sTmp(i))
        lSum = lSum + lTmp(i)
    Next
    
    Select Case lSum
    Case 10
        For i = 0 To 5
            If lTmp(i) < sTmp(i) Then
                If sDif < sTmp(i) - lTmp(i) And lTmp(i) < 4 Then
                    sDif = sTmp(i) - lTmp(i)
                    tmpI = i
                End If
            End If
        Next
        tmpI = FixCode(sTmp, lTmp, tmpI, 1)
        lTmp(tmpI) = lTmp(tmpI) + 1
    Case 12
        For i = 0 To 5
            If lTmp(i) > sTmp(i) Then
                If sDif < lTmp(i) - sTmp(i) And lTmp(i) > 1 Then
                    sDif = lTmp(i) - sTmp(i)
                    tmpI = i
                End If
            End If
        Next
        tmpI = FixCode(sTmp, lTmp, tmpI, -1)
        lTmp(tmpI) = lTmp(tmpI) - 1
    End Select
    
    For i = 0 To 5
        BarCode = BarCode & lTmp(i)
    Next
End Function

'修正编码数据
Public Function FixCode(sArr() As Single, lArr() As Long, ByVal k As Long, ByVal d As Long) As Long
    Dim i As Long, n As Long, s As String

    For i = 0 To 5
        If sArr(k) = sArr(i) Then
            s = ""
            For n = 0 To 5
                s = s & (lArr(n) + IIf(n = i, d, 0))
            Next
            If CodeID(s) > -1 Then
                FixCode = i
                Exit Function
            End If
        End If
    Next
    
    FixCode = k
End Function

'根据编码得到ID值
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

'得到条码字符串
Public Function BarChar() As String
    Dim i As Long, n As Long, lMode As Long, lLen As Long, isFix As Boolean
    Dim lID(20, 13) As Long, idI(13) As Long, lpID(13) As Long
    Dim aMost() As String, sBarChar As String, lChk As Long

    For i = 0 To UBound(lCodeID, 1)
        If lCodeID(i, 0) = 103 Or lCodeID(i, 0) = 105 Then
            lMode = lCodeID(i, 0)
            Exit For
        End If
    Next
    
    If lMode = 0 Then Exit Function
    
    lLen = IIf(lMode = 103, 13, 7)
    For i = 1 To lLen
        idI(i) = -1
        
        For n = 0 To UBound(lCodeID, 1)
            If i < lLen Then
                If lCodeID(n, i) >= IIf(lMode = 103, 16, 0) And lCodeID(n, i) <= IIf(lMode = 103, 25, 99) And inArray(lID(), i, idI(i), lCodeID(n, i)) = False Then
                    idI(i) = idI(i) + 1
                    lID(idI(i), i) = lCodeID(n, i)
                End If
            Else
                If lCodeID(n, i) >= 0 And lCodeID(n, i) <= 102 And inArray(lID(), i, idI(i), lCodeID(n, i)) = False Then
                    idI(i) = idI(i) + 1
                    lID(idI(i), i) = lCodeID(n, i)
                End If
            End If
        Next
    Next
    
    If idI(lLen) = -1 Then Exit Function

    If lMode = 103 Then
        lID(0, 1) = 54
        idI(1) = 0
        lID(0, 2) = 41
        idI(2) = 0
        lID(0, 3) = 48
        idI(3) = 0
    End If
    
    For i = 1 To lLen
        If idI(i) > 0 Then
            aMost = Split(inMost(lID, lCodeID, idI(i), UBound(lCodeID, 1), i), ",")
            idI(i) = UBound(aMost) - 1
            
            For n = 0 To idI(i)
                lID(n, i) = aMost(n)
            Next
        End If
    Next
    
    '测试代码-开始
'    Dim s As String
'    For i = 1 To lLen
'        For n = 0 To idI(i)
'            s = s & lID(n, i) & IIf(n = idI(i), "", ",")
'        Next
'        s = s & IIf(i = lLen, "", "/")
'    Next
'    Form1.Print s
    '测试代码-结束
    
    For i = 1 To lLen
        If idI(i) = -1 Then
'            If lMode = 103 And isFix = False Then
'                For n = 0 To 9
'                    lID(n, i) = 16 + n
'                Next
'                idI(i) = 9
'                isFix = True
'            Else
                Exit Function
'            End If
        End If
    Next
    

    
    BarChar = BarVaild(lID(), idI(), lpID(), 1, lMode, lLen - 1)
    
    If BarChar = "" And lMode = 103 And isFix = False Then
        For i = 1 To 12
            If idI(i) <> 0 Then Exit For
        Next
        If i > 12 Then
            lChk = 103
            For i = 1 To 12
                lChk = lChk + i * lID(0, i)
            Next
            lChk = lChk Mod 103
            For n = 0 To UBound(lCodeID, 1)
                If lChk = lCodeID(n, 13) Then
                    For i = 1 To 12
                        BarChar = BarChar & sCA(lID(0, i))
                    Next
                    Exit Function
                End If
            Next
        End If
        
'        i = inLeast(lID, lCodeID, UBound(lCodeID, 1))
'        For n = 0 To 9
'            lID(n, i) = 16 + n
'        Next
'        idI(i) = 9
'
'        BarChar = BarVaild(lID(), idI(), lpID(), 1, lMode, lLen - 1)
    End If
End Function

'递归算法遍历ID组合
Public Function BarVaild(lID() As Long, idI() As Long, lpID() As Long, i As Long, lChk As Long, lLen As Long) As String
    If i <= lLen Then
        For lpID(i) = 0 To idI(i)
            lChk = lChk + i * lID(lpID(i), i)
            
            BarVaild = BarVaild(lID(), idI(), lpID(), i + 1, lChk, lLen)
            lChk = lChk - i * lID(lpID(i), i)

            If BarVaild <> "" Then Exit Function
        Next
    Else
        If inArray(lID(), i, idI(i), lChk Mod 103) = True Then
            Dim j As Long
            For j = 1 To lLen
                BarVaild = BarVaild & IIf(lLen = 12, sCA(lID(lpID(j), j)), sCC(lID(lpID(j), j)))
            Next
        End If
    End If
End Function

'查检是否为重复ID
Public Function inArray(arr() As Long, ByVal k As Long, ByVal n As Long, ByVal ele As Long) As Boolean
    Dim i As Long
    
    For i = 0 To n
        If arr(i, k) = ele Then
            inArray = True
            
            Exit For
        End If
    Next
End Function

'出现次数最多的ID值
Public Function inMost(sArr() As Long, tArr() As Long, ByVal sI As Long, ByVal tI As Long, ByVal k As Long) As String
    Dim i As Long, n As Long, aI As Long, lNum As Long
    
    For i = 0 To sI
        aI = 0
        For n = 0 To tI
            If sArr(i, k) = tArr(n, k) Then
                aI = aI + 1
            End If
        Next
        
        If aI >= lNum Then
            inMost = IIf(lNum = aI, inMost, "") & sArr(i, k) & ","
            lNum = aI
        End If
    Next
End Function

'ID出现次数最少的位
Public Function inLeast(sArr() As Long, tArr() As Long, ByVal tI As Long) As Long
    Dim i As Long, n As Long, aI As Long, lNum As Long
    
    lNum = tI + 1
    For i = 4 To 12
        aI = 0
        For n = 0 To tI
            If sArr(0, i) = tArr(n, i) Then
                aI = aI + 1
            End If
        Next
        
        If aI <= lNum Then
            inLeast = i
            lNum = aI
        End If
    Next
End Function


